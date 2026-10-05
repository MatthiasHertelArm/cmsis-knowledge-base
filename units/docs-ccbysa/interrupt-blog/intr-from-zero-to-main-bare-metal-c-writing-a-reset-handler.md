---
id: "intr-from-zero-to-main-bare-metal-c-writing-a-reset-handler"
type: "concept"
domain: "debug"
title: "From Zero to main(): Bare metal C: Writing a Reset_Handler"
summary: "Unfortunately, the Reset_Handler is often an inscrutable mess of Assembly code. See the nRF52 SDK startup file for example."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-05-14-zero-to-main-1.md"
doc_source: "https://interrupt.memfault.com/blog/zero-to-main-1#writing-a-reset-handler"
license: "CC-BY-SA-4.0"
mode: "V"
---

Unfortunately, the Reset_Handler is often an inscrutable mess of Assembly code.
See the [nRF52 SDK
startup](https://github.com/NordicSemiconductor/nrfx/blob/293f553ed9551c1fdfd05eac48e75bbdeb4e7290/mdk/gcc_startup_nrf52.S#L217)
file for example.

Instead of going through this file line-by-line, let's see if we can write a
minimal Reset_Handler from first principles.

Here again, ARM's Technical Reference Manuals are useful. [Section 5.9.2 of the
Cortex-M3
TRM](https://developer.arm.com/docs/ddi0337/e/exceptions/resets/intended-boot-up-sequence)
contains the following table:



| Action | Description |
|---|---|
| Initialize variables | Any global/static variables must be setup. This includes initializing the BSS variable to 0, and copying initial values from ROM to RAM for non-constant variables. |
| [Setup stacks] | If more than one stack is be used, the other banked SPs must be initialized. The current SP can also be changed to Process from Main. |
| [Initialize any runtime] | Optionally make calls to C/C++ runtime init code to enable use of heap, floating point, or other features. This is normally done by __main` from the C/C++ library. |




So, our ResetHandler is responsible for initializing static and global
variables, and starting our program.
This mirrors what the C standards tells us:

> All objects with static storage duration shall be initialized (set to their
> initial values) before program startup. The manner and timing of such
> initialization are otherwise unspecified.

(Section 5.1.2, Execution environment)

In practice this means that given the following snippet:

```c
static uint32_t foo;
static uint32_t bar = 2;
```

Our `Reset_Handler` needs to make sure that the memory at `&foo` is 0x00000000, and the
memory at `&bar` is 0x00000002.

We cannot just go and initialize each variable one by one. Instead, we rely on
the compiler (technically, the linker) to put all those variables in the same
place so we can initialize them in one fell swoop.

For static variables that must be zeroed, the linker gives us `_sbss` and
`_ebss` as start and end addresses. We can therefore do:

```c
/* Clear the zero segment */
for (uint32_t *bss_ptr = &_sbss; bss_ptr < &_ebss;) {
    *bss_ptr++ = 0;
}
```

For static variables with an init value, the linker gives us:
* `_etext` as the address the init values are stored at
* `_sdata` as the address the static variables live at
* `_edata` as the end of the static variables memory

We then can do:
```c
uint32_t *init_values_ptr = &_etext;
uint32_t *data_ptr = &_sdata;
if (init_values_ptr != data_ptr) {
    for (; data_ptr < &_edata;) {
        *data_ptr++ = *init_values_ptr++;
    }
}
```

Putting it together, we can write our `Reset_Handler`

```c
void Reset_Handler(void)
{
    /* Copy init values from text to data */
    uint32_t *init_values_ptr = &_etext;
    uint32_t *data_ptr = &_sdata;

    if (init_values_ptr != data_ptr) {
        for (; data_ptr < &_edata;) {
            *data_ptr++ = *init_values_ptr++;
        }
    }

    /* Clear the zero segment */
    for (uint32_t *bss_ptr = &_sbss; bss_ptr < &_ebss;) {
        *bss_ptr++ = 0;
    }
}
```

We still need to start our program! That's achieved with a simple call to
`main()`.

```c
void Reset_Handler(void)
{
    /* Copy init values from text to data */
    uint32_t *init_values_ptr = &_etext;
    uint32_t *data_ptr = &_sdata;

    if (init_values_ptr != data_ptr) {
        for (; data_ptr < &_edata;) {
            *data_ptr++ = *init_values_ptr++;
        }
    }

    /* Clear the zero segment */
    for (uint32_t *bss_ptr = &_sbss; bss_ptr < &_ebss;) {
        *bss_ptr++ = 0;
    }

    /* Overwriting the default value of the NVMCTRL.CTRLB.MANW bit (errata reference 13134) */
    NVMCTRL->CTRLB.bit.MANW = 1;

    /* Branch to main function */
    main();

    /* Infinite loop */
    while (1);
}
```

You will note that we added two things:
1. An infinite loop after `main()`, so we do not run off into the weeds if the
   main function returns
2. Workaround for chip bugs which are best taken care of before our program
   starts. Sometimes these are wrapped in a `SystemInit` function called by the
   `Reset_Handler` before `main`. This is the approach [taken by
Nordic](https://github.com/NordicSemiconductor/nrfx/blob/6f54f689e9555ea18f9aca87caf44a3419e5dd7a/mdk/system_nrf52811.c#L60).

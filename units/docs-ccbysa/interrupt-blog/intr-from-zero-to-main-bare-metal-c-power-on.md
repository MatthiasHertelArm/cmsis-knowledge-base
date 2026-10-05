---
id: "intr-from-zero-to-main-bare-metal-c-power-on"
type: "concept"
domain: "debug"
title: "From Zero to main(): Bare metal C: Power on!"
summary: "So how did we get to main? All we can tell from observation is that we applied power to the board and our code started executing. There must be behavior intrinsic to the chip that defines how code is executed."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-05-14-zero-to-main-1.md"
doc_source: "https://interrupt.memfault.com/blog/zero-to-main-1#power-on"
license: "CC-BY-SA-4.0"
mode: "V"
---

So how did we get to main? All we can tell from observation is that we applied
power to the board and our code started executing. There must be behavior
intrinsic to the chip that defines how code is executed.

And indeed, there is! Digging into the [ARMv6-M Technical Reference
Manual](https://static.docs.arm.com/ddi0419/d/DDI0419D_armv6m_arm.pdf), which is
the underlying architecture manual for the Cortex-M0+, we can
find some pseudo-code that describes reset behavior:

```c
// B1.5.5 TakeReset()
// ============
TakeReset()
    VTOR = Zeros(32);
    for i = 0 to 12
        R[i] = bits(32) UNKNOWN;
    bits(32) vectortable = VTOR;
    CurrentMode = Mode_Thread;
    LR = bits(32) UNKNOWN; // Value must be initialised by software
    APSR = bits(32) UNKNOWN; // Flags UNPREDICTABLE from reset
    IPSR<5:0> = Zeros(6); // Exception number cleared at reset
    PRIMASK.PM = '0'; // Priority mask cleared at reset
    CONTROL.SPSEL = '0'; // Current stack is Main
    CONTROL.nPRIV = '0'; // Thread is privileged
    ResetSCSRegs(); // Catch-all function for System Control Space reset
    for i = 0 to 511 // All exceptions Inactive
        ExceptionActive[i] = '0';
    ClearEventRegister(); // See WFE instruction for more information
    SP_main = MemA[vectortable,4] AND 0xFFFFFFFC<31:0>;
    SP_process = ((bits(30) UNKNOWN):'00');
    start = MemA[vectortable+4,4]; // Load address of reset routine
    BLXWritePC(start); // Start execution of reset routine
```

In short, the chip does the following:

- Reset the vector table address to `0x00000000`
- Disable all interrupts
- Load the SP from address `0x00000000`
- Load the PC from address `0x00000004`

"Mystery solved!", you'll say. Our `main` function must be at address
`0x00000004`!

Let us check.

First, we dump our `bin` file to see what address `0x0000000` and `0x00000004` contain:

```terminal
francois-mba:zero-to-main francois$ xxd build/minimal/minimal.bin  | head
00000000: 0020 0020 c100 0000 b500 0000 bb00 0000  . . ............
00000010: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000020: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000030: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000040: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000050: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000060: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000070: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000080: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000090: 0000 0000 0000 0000 0000 0000 0000 0000  ................
```

If I'm reading this correctly, our initial SP is `0x20002000`, and our start
address pointer is `0x000000c1`.

Let's dump our symbols to see which one is at `0x000000c1`.

```terminal
francois-mba:minimal francois$ arm-none-eabi-objdump -t build/minimal.elf | sort
...
000000b4 g     F .text  00000006 NMI_Handler
000000ba g     F .text  00000006 HardFault_Handler
000000c0 g     F .text  00000088 Reset_Handler
00000148 l     F .text  0000005c system_pinmux_get_group_from_gpio_pin
000001a4 l     F .text  00000020 port_get_group_from_gpio_pin
000001c4 l     F .text  00000022 port_get_config_defaults
000001e6 l     F .text  0000004e port_pin_set_output_level
00000234 l     F .text  00000038 port_pin_toggle_output_level
0000026c l     F .text  00000040 set_output
000002ac g     F .text  0000002c main
...
```

That's odd! Our main function is found at `0x000002ac`. No symbol at `0x000000c1`, but a
`Reset_Handler` symbol at `0x000000c0`.

It turns out that the lowest bit of the PC is used to indicate thumb2
instructions, which is one of the two instruction sets supported by ARM
processors, so `Reset_Handler` is what we're looking for (for more details check
out section A4.1.1 in the ARMv6-M manual).

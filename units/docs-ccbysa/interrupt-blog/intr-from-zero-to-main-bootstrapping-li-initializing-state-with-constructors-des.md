---
id: "intr-from-zero-to-main-bootstrapping-li-initializing-state-with-constructors-des"
type: "concept"
domain: "debug"
title: "From Zero to main(): Bootstrapping libc with Newlib: Implementing Newlib / Initializing State with Constructors & Destructors"
summary: "Although we could perfectly well stop here, we can improve a bit over the above."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-12-bootstrapping-libc-with-newlib.md"
doc_source: "https://interrupt.memfault.com/blog/bootstrapping-libc-with-newlib#initializing-state-with-constructors-destructors"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Implementing Newlib_

Although we could perfectly well stop here, we can improve a bit over the above.

In our example, `printf` depends implicitly on `serial_init` being called. This
isn’t the end of the world, but it goes against the spirit of a standard library
function which should be usable anywhere in our program.

Instead, let’s see what we can do so that this works:

```c
int main() {
  printf("Hello, World\n");
}
```

Can you think of a solution?

If we want `printf` to work anywhere in our `main` function, then `serial_init`
must be run **before** main. What runs before main? We know from our previous
post that it is the `Reset_Handler`. A simple solution might therefore be:

```c
void Reset_Handler(void)
{
  /* ... */
  /* Hardware Initialization */
  serial_init();

  /* Branch to main function */
  main();

  /* Infinite loop */
  while (1);
}
```

The GNU compiler collection and Newlib offer an alternative solution:
constructors.

Constructors are functions which should be run before `main`. Conceptually, they
are similar to the constructors of statically allocated C++ objects.

A function is marked as a constructor using the attribute syntax:
`__attribute__((constructor))`. We can thus update `serial_init`:

```c
static void __attribute__((constructor)) serial_init(void) {
  struct usart_config usart_conf;

  usart_get_config_defaults(&usart_conf);
  usart_conf.mux_setting = USART_RX_3_TX_2_XCK_3;
  usart_conf.pinmux_pad0 = PINMUX_UNUSED;
  usart_conf.pinmux_pad1 = PINMUX_UNUSED;
  usart_conf.pinmux_pad2 = PINMUX_PB22D_SERCOM5_PAD2;
  usart_conf.pinmux_pad3 = PINMUX_PB23D_SERCOM5_PAD3;

  usart_serial_init(&stdio_uart_module, SERCOM5, &usart_conf);
  usart_enable(&stdio_uart_module);
}
```

But how do these constructors get invoked? We know that in firmware, we do not
get anything for free. This is where newlib comes in.

By default, GCC will put every constructor into an array in their own section of
flash. Newlib then offers a function, `__libc_init_array` which iterates over
the array and invokes every constructor. You can find out more about it by
reading [the source
code](https://github.com/bminor/newlib/blob/master/newlib/libc/misc/init.c).

All we need to do is call `__libc_init_array` prior to `main` in our
`Reset_Handler`, and we are good to go.

```c
void Reset_Handler(void)
{
  /* ... */
  /* Run constructors / initializers */
  __libc_init_array();

  /* Branch to main function */
  main();

  /* Infinite loop */
  while (1);
}
```

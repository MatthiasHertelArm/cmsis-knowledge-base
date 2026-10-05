---
id: "intr-firmware-testing-with-renode-and-g-example-firmware-overview"
type: "concept"
domain: "debug"
title: "Firmware Testing with Renode and GitHub Actions: Example Firmware Overview"
summary: "This post builds upon previous ideas and examples written on Interrupt. If you find yourself missing some context, the following posts would be useful:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-07-07-test-automation-renode.md"
doc_source: "https://interrupt.memfault.com/blog/test-automation-renode#example-firmware-overview"
license: "CC-BY-SA-4.0"
mode: "V"
---

This post builds upon previous ideas and examples written on Interrupt. If you
find yourself missing some context, the following posts would be useful:

- [Cortex-M MCU Emulation with
  Renode](https://interrupt.memfault.com/blog/intro-to-renode)
- [Building a Tiny CLI Shell for Tiny Firmware](https://interrupt.memfault.com/blog/firmware-shell)

Rather than the STM32Cube HAL, I used an open-source MCU HAL called `libopencm3`
with excellent support for the STM32. It is included as a submodule in the repo.

The primary way we'll control the firmware is through a CLI shell written
previously and linked above.

With the shell in place, this means that our main loop of the firmware is
simply:

```c
int main(void) {
    clock_setup();
    gpio_setup();
    usart_setup();

    printf("App STARTED\n");

    // Configure shell
    sShellImpl shell_impl = {
      .send_char = usart_putc,
    };
    shell_boot(&shell_impl);

    char c;
    while (1) {
        c = usart_getc();
        shell_receive_char(c);
    }

    return 0;
}
```

The supporting `*_setup()` calls and their implementations can be found in the
other `.c` files in
[`src/`](https://github.com/memfault/interrupt-renode-test-automation/tree/master/src).

We can build our example firmware by invoking Make.

```
$ make -j4
Building libopencm3
  GENHDR  include/libopencm3/stm32/f4/irq.json
  [...]
  AR      libopencm3_stm32f4.a
  LD    build/renode-example.elf
```

Now we have our `renode-example.elf` file which we can load into Renode.

```
$ ./start.sh
```

And then we see our firmware's shell in the UART window of Renode.



  


We can interact with it exactly as if it was connected to our computer over USB
serial! This would have made writing and testing the firmware for my [Tiny
Shell](https://interrupt.memfault.com/blog/firmware-shell) post **much** easier. I'm glad
I took the time now to learn Renode for the next time.

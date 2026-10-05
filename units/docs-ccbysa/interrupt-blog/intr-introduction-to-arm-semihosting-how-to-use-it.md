---
id: "intr-introduction-to-arm-semihosting-how-to-use-it"
type: "concept"
domain: "debug"
title: "Introduction to ARM Semihosting: How to Use It"
summary: "In this example, I run the program on an STM32 and use the arm-none-eabi toolchain along with openOCD gdbserver."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-02-16-arm-semihosting.md"
doc_source: "https://interrupt.memfault.com/blog/arm-semihosting#how-to-use-it"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this example, I run the program on an STM32 and use the `arm-none-eabi`
toolchain along with **openOCD** `gdbserver`. Other tools may be used instead
depending on your hardware, for more details on which debug interface to use, it
would be wise to read [this article](https://interrupt.memfault.com/blog/a-deep-dive-into-arm-cortex-m-debug-interfaces).

Once you are all set, we can start coding.

First, to enable semihosting, you need to link:
* `libc.a`, the standard C library (*newlib*[^3] for `arm-none-eabi-gcc`),
* and `librdimon.a`, a part of the *libgloss*[^4] library (for platform-specific
  code) to your project.

This is done by adding a few options to the ARM linker:
* removing `-nostartfiles` flag to allow linking standards libraries,
* adding `-lc -lrdimon` flags,
* and changing the *spec strings* file[^5] to `--specs=rdimon.specs` to use the
  semihosted version of the *syscalls*.

The last point essentially means that the system calls can be used when a
debugger is attached (note that the CPU may crash if a debugger is not present).

Now on the C code side, you need to call `initialise_monitor_handles()` before
starting a semihosting operation.

```c
#ifdef SEMIHOSTING
extern void initialise_monitor_handles(void);
#endif

int main(void) {
#ifdef SEMIHOSTING
  	initialise_monitor_handles();
#endif

  	// other tasks ...

#ifdef SEMIHOSTING
    printf("hello world!\n");
    printf("hello world!\n");
#endif

    // other tasks ...

  	return 0;
}
```

If you are using `crt0` initialization function, `initialise_monitor_handles()`
has already been called for you before `main()`.

Once you have done this, you can compile and program your microcontroller as
usual, however, once the microcontroller flashed it should be halted and not run
yet.

In my case, I launch *OpenOCD* `gdbserver` in one terminal, to flash, reset and
halt the CPU. And run `gdb` from another terminal to connect to the server, and
enable the semihosting in the server side[^6].

```shell
$ arm-none-eabi-gdb -ex "target extended-remote localhost:3333" -ex "monitor reset halt" -ex "monitor arm semihosting enable"
```

> If `initialise_monitor_handles()` is called before enabling the semihosting in
> the server, a `HardFault` may occur due to an unexpected debug event.

Once semihosting is enabled, you can run your program from `gdb`, and the
semihosting operation will be handled by the `gdbserver`.

Isn't it great? 😋

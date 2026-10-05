---
id: "intr-from-zero-to-main-bootstrapping-li-system-calls"
type: "concept"
domain: "debug"
title: "From Zero to main(): Bootstrapping libc with Newlib: Implementing Newlib / System Calls"
summary: "Not so fast! Let’s go back to our “Hello World” example:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-12-bootstrapping-libc-with-newlib.md"
doc_source: "https://interrupt.memfault.com/blog/bootstrapping-libc-with-newlib#system-calls"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Implementing Newlib_

Not so fast! Let’s go back to our “Hello World” example:

```c
int main() {
  printf("Hello World!\n");
  while(1) {}
}
```

Removing `-nostdlib` is not quite enough. Instead of `printf` being undefined,
we now see a whole mess of undefined symbols:

```shell
Linking build/minimal.elf
/usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/bin/ld: /usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/lib/thumb/v6-m/nofp/libg_nano.
a(lib_a-sbrkr.o): in function `_sbrk_r':
sbrkr.c:(.text._sbrk_r+0xc): undefined reference to `_sbrk'
/usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/bin/ld: /usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/lib/thumb/v6-m/nofp/libg_nano.
a(lib_a-writer.o): in function `_write_r':
writer.c:(.text._write_r+0x10): undefined reference to `_write'
/usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/bin/ld: /usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/lib/thumb/v6-m/nofp/libg_nano.
a(lib_a-closer.o): in function `_close_r':
closer.c:(.text._close_r+0xc): undefined reference to `_close'
/usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/bin/ld: /usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/lib/thumb/v6-m/nofp/libg_nano.
a(lib_a-lseekr.o): in function `_lseek_r':
lseekr.c:(.text._lseek_r+0x10): undefined reference to `_lseek'
/usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/bin/ld: /usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/lib/thumb/v6-m/nofp/libg_nano.
a(lib_a-readr.o): in function `_read_r':
readr.c:(.text._read_r+0x10): undefined reference to `_read'
/usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/bin/ld: /usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/lib/thumb/v6-m/nofp/libg_nano.
a(lib_a-fstatr.o): in function `_fstat_r':
fstatr.c:(.text._fstat_r+0xe): undefined reference to `_fstat'
/usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/bin/ld: /usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/lib/thumb/v6-m/nofp/libg_nano.
a(lib_a-isattyr.o): in function `_isatty_r':
isattyr.c:(.text._isatty_r+0xc): undefined reference to `_isatty'
collect2: error: ld returned 1 exit status
```

Specifically, the compiler is asking for `_fstat`, `_read`, `_lseek`, `_close`,
`_write`, and `_sbrk`.

The newlib documentation[^6] calls these functions “system calls”.  In short,
they are the handful of things newlib expects the underlying “operating system”.
The complete list of them is provided below:

```
_exit, close, environ, execve, fork, fstat, getpid, isatty, kill,
link, lseek, open, read, sbrk, stat, times, unlink, wait, write
```

You’ll notice that several of the syscalls relate to filesystem operation or
process control. These do not make much sense in a firmware context, so we’ll
often simply provide a stub that returns an error code.

Let’s look at the ones our “Hello, World” example requires.
#### fstat
`fstat`  returns the status of an open file.  The minimal version of this should
identify all files as character special devices. This forces one-byte-read at a
time.

```c
#include <sys/stat.h>
int fstat(int file, struct stat *st) {
  st->st_mode = S_IFCHR;
  return 0;
}
```

#### lseek

`lseek` repositions the file offset of the open file associated with the file
descriptor `fd` to the argument `offset` according to the directive `whence`.

Here we can simply return 0, which implies the file is empty.

```c
int lseek(int file, int offset, int whence) {
  return 0;
}
```

#### close

`close` closes a file descriptor `fd`.

Since no file should have gotten `open`-ed, we can just return an error on
close:

```c
int close(int fd) {
  return -1;
}
```

#### write

This is where things get interesting! `write` writes up to `count` bytes from
the buffer starting at `buf` to the file referred to by the file descriptor
`fd`.

Functions like `printf` rely on `write` to write bytes to `STDOUT`. In our case,
we will want those bytes to be written to serial instead.

On the SAMD21 chip we are using, writing bytes to serial is done using the
`usart_serial_putchar` function. We can use it to implement `write`:

```c
static struct usart_module stdio_uart_module;

int _write (int fd, char *buf, int count) {
  int written = 0;

  for (; count != 0; --count) {
    if (usart_serial_putchar(&stdio_uart_module, (uint8_t)*buf++)) {
      return -1;
    }
    ++written;
  }
  return written;
}
```

We’ll also need to initialize the USART peripheral prior to calling printf:

```c
static void serial_init(void) {
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

int main() {
  serial_init();

  printf("Hello, World!\n");
  while (1) {}
}
```

#### read

`read`  attempts to read up to `count` bytes from file descriptor `fd` into the
buffer at `buf`.

Similarly to `write`, we want `read` to read bytes from serial:

```c
int _read (int fd, char *buf, int count) {
  int read = 0;

  for (; count > 0; --count) {
    usart_serial_getchar(&stdio_uart_module, (uint8_t *)buf++);
    read++;
  }

  return read;
}
```

#### sbrk

`sbrk` increases the program’s data space by `increment` bytes. In other words,
it increases the size of the heap.

What does `printf` have to do with the heap, you will justly ask? It turns out
that newlib’s `printf` implementations allocates data on the heap and depends on
a working `malloc` implementation.

The source for `printf` is hard to follow, but you will find that indeed [it
calls
malloc](https://github.com/bminor/newlib/blob/6497fdfaf41d47e835fdefc78ecb0a934875d7cf/newlib/libc/stdio/vfprintf.c#L226)!

Here’s a simple implementation of `sbrk`:

```c
void *_sbrk(int incr) {
  static unsigned char *heap = HEAP_START;
  unsigned char *prev_heap = heap;
  heap += incr;
  return prev_heap;
}
```

More often than not, we want the heap to use all the RAM not used by anything
else. We therefore set `HEAP_START` to the first address not spoken for in our
linker script. In our [previous
post](https://interrupt.memfault.com/blog/how-to-write-linker-scripts-for-firmware#complete-linker-script),
we had added the `_end` variable in our linker script to that end.

We replace `HEAP_START` with `_end` and get:

```c
void *_sbrk(int incr) {
  static unsigned char *heap = NULL;
  unsigned char *prev_heap;

  if (heap == NULL) {
    heap = (unsigned char *)&_end;
  }
  prev_heap = heap;

  heap += incr;

  return prev_heap;
}
```

Putting it all together, we get the following `main.c` file:

```c
static struct usart_module stdio_uart_module;

// LIBC SYSCALLS
/////////////////////

extern int _end;

void *_sbrk(int incr) {
  static unsigned char *heap = NULL;
  unsigned char *prev_heap;

  if (heap == NULL) {
    heap = (unsigned char *)&_end;
  }
  prev_heap = heap;

  heap += incr;

  return prev_heap;
}

int _close(int file) {
  return -1;
}

int _fstat(int file, struct stat *st) {
  st->st_mode = S_IFCHR;

  return 0;
}

int _isatty(int file) {
  return 1;
}

int _lseek(int file, int ptr, int dir) {
  return 0;
}

void _exit(int status) {
  __asm("BKPT #0");
}

void _kill(int pid, int sig) {
  return;
}

int _getpid(void) {
  return -1;
}

int _write (int file, char * ptr, int len) {
  int written = 0;

  if ((file != 1) && (file != 2) && (file != 3)) {
    return -1;
  }

  for (; len != 0; --len) {
    if (usart_serial_putchar(&stdio_uart_module, (uint8_t)*ptr++)) {
      return -1;
    }
    ++written;
  }
  return written;
}

int _read (int file, char * ptr, int len) {
  int read = 0;

  if (file != 0) {
    return -1;
  }

  for (; len > 0; --len) {
    usart_serial_getchar(&stdio_uart_module, (uint8_t *)ptr++);
    read++;
  }
  return read;
}


// APP
////////////////////

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

int main() {
  serial_init();
  printf("Hello, World!\n");
}
```

This compiles fine, and can be run on our MCU. Hello, World!

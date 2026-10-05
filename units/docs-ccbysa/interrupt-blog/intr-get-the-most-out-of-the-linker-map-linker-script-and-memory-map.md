---
id: "intr-get-the-most-out-of-the-linker-map-linker-script-and-memory-map"
type: "concept"
domain: "debug"
title: "Get the most out of the linker map file: Digging into the map files / Linker script and memory map"
summary: "Following the memory configuration is the Linker script and memory map. That one is interesting as it gives detailed information about the symbols in your program."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-07-09-get-the-most-out-of-the-linker-map-file.md"
doc_source: "https://interrupt.memfault.com/blog/get-the-most-out-of-the-linker-map-file#linker-script-and-memory-map"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Digging into the map files_

Following the memory configuration is the **Linker script and memory map**. That one is interesting as it gives detailed information about the symbols in your program. In our case, it first indicates the `text` area size and its content (`text` is our compiled code, as opposed to `data` which is program data). Here, the interrupt vectors (under the section `.isr_vector`) are present at the beginning of the executable, defined in `gcc_startup_nrf52840.S`:

```
    Linker script and memory map

    .text           0x0000000000001000      0x8c8
     ***(.isr_vector)**
     .isr_vector    0x0000000000001000      0x200 _build/nrf52840_xxaa/**gcc_startup_nrf52840.S.o**
                    0x0000000000001000                __isr_vector
     *(.text*)
     .text          0x0000000000001200       0x40 /usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/thumb/v7e-m+fp/hard/crtbegin.o
     .text          0x0000000000001240       0x74 /usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/lib/thumb/v7e-m+fp/hard/crt0.o
                    0x0000000000001240                _mainCRTStartup
                    0x0000000000001240                _start
     .text          0x00000000000012b4       0x3c _build/nrf52840_xxaa/gcc_startup_nrf52840.S.o
                    0x00000000000012b4                Reset_Handler
                    0x00000000000012dc                NMI_Handler

    [...]

     .text.**bsp_board_led_invert**
                    0x00000000000012f0       **0x34** _build/nrf52840_xxaa/**boards.c.o**
                    0x00000000000012f0                bsp_board_led_invert
```

Those lines give us the address of each function and its size. Above, you can read the address of `bsp_board_led_invert`, coming from `boards.c.o` (compilation unit of `board.c` as you guessed) which has a size of 0x34 bytes in the `text` area. That way, we are able to locate each function used in the program.

My constant string `_delay_ms_str` is obviously included in the program as it is initialized. Read-only data are saved as `rodata` and kept in the `FLASH` region as specified in the [linker script](https://interrupt.memfault.com/blog/how-to-write-linker-scripts-for-firmware) (stored in Flash and not copied in RAM as it is constant). I can find it under that line:

```
    .rodata.main.str1.4
    	              0x00000000000017b8        0x4 _build/nrf52840_xxaa/main.c.o
```

I also noticed that the inclusion of `_ctype_` added 0x101 bytes of read-only data in the `text` area 😯.

```
    .rodata._ctype_
                    0x00000000000017c0      **0x101** /usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/lib/thumb/v7e-m+fp/hard/libc_nano.a(lib_a-ctype_.o)
                    0x00000000000017c0                **_ctype_**
```

As standard libraries are open-source ([link](https://sourceware.org/git/gitweb.cgi?p=newlib-cygwin.git;a=tree;f=newlib;hb=HEAD)), we can easily find out why it's taking that much space. I dived into the inner-working of `atoi` (`atoi_r` in its **reentrant** version, see below), which calls directly `strtol_r`:

```c
int
_DEFUN (_atoi_r, (s),
  struct _reent *ptr _AND
  _CONST char *s)
{
  return (int) _strtol_r (ptr, s, NULL, 10);
}
```

When it comes to `strtol_r`, it is actually more complex than only converting characters into an integer because if performs type checking, using `ctype`. The way `ctype` works is by using a table where the ASCII symbol types are stored into an array. Here are the main parts of `ctype`, annotated with my comments:

```c
// Flags indicating the symbol type
#define _U  01    // Uppercase letter
#define _L  02    // Lowercase letter
#define _N  04    // Numeric
#define _S  010
#define _P  020   // Ponctuation
#define _C  040   // Control characters
#define _X  0100  // Hexadecimal
#define _B  0200

// ASCII table types
#define _CTYPE_DATA_0_127 \
  _C, _C, _C, _C, _C, _C, _C, _C, \
  _C, _C|_S, _C|_S, _C|_S,  _C|_S,  _C|_S,  _C, _C, \
  _C, _C, _C, _C, _C, _C, _C, _C, \
  _C, _C, _C, _C, _C, _C, _C, _C, \
  _S|_B,  _P, _P, _P, _P, _P, _P, _P, \
  _P, _P, _P, _P, _P, _P, _P, _P, \
  _N, _N, _N, _N, _N, _N, _N, _N, \
  _N, _N, _P, _P, _P, _P, _P, _P, \
  _P, _U|_X,  _U|_X,  _U|_X,  _U|_X,  _U|_X,  _U|_X,  _U, \
  _U, _U, _U, _U, _U, _U, _U, _U, \
  _U, _U, _U, _U, _U, _U, _U, _U, \
  _U, _U, _U, _P, _P, _P, _P, _P, \
  _P, _L|_X,  _L|_X,  _L|_X,  _L|_X,  _L|_X,  _L|_X,  _L, \
  _L, _L, _L, _L, _L, _L, _L, _L, \
  _L, _L, _L, _L, _L, _L, _L, _L, \
  _L, _L, _L, _P, _P, _P, _P, _C

// _ctype_ structure takes 257 (0x101) bytes, as seen on the map file (.rodata._ctype_)
_CONST char _ctype_[1 + 256] = {
  0,
  _CTYPE_DATA_0_127,
  _CTYPE_DATA_128_255
};
```

Interestingly, the addition of `atoi` not only increased our code size (the `text` area), but also our data size (the `data` area). With the diff file, I can easily discover data that was before discarded by the linker:

```
    .data._impure_ptr
    								0x0000000000000000        0x4 /usr/local/Cellar/arm-none-eabi-gcc/8-2018-q4-major/gcc/bin/../lib/gcc/arm-none-eabi/8.2.1/../../../../arm-none-eabi/lib/thumb/v7e-m+fp/hard/libc_nano.a(lib_a-impure.o)
```

Now you may have noticed the function names finishing by `_r`, when calling `strtol_r` for example. That suffix indicates reentrancy. Documentation about reentrancy can be found [in newlib source code](https://sourceware.org/git/gitweb.cgi?p=newlib-cygwin.git;a=blob_plain;f=newlib/libc/reent/reent.tex;hb=HEAD). To sum-up, reentrant functions can be called even when the same function is already in execution in another process, without intervening the execution. From the documentation:

```tex
Each function which uses the global reentrancy structure uses the global
variable _impure_ptr, which points to a reentrancy structure.
```

In our case, we need that new global variable to call the reentrant function: `atoi_r`.

One last piece of information to keep in mind: initialized variables have to be kept in Flash but they appear in `RAM` in the map file because they are copied into RAM before entering the `main` function. Here, symbols `__data_start__` and `__data_end__` keep track of the area used in RAM to keep initialized variables. Those values are stored in Flash starting at `0x00000000000018d0`:

```
    .data           0x0000000020000008       0x70 load address 0x00000000000018d0
                    0x0000000020000008                __data_start__ = .
    [...]
                    0x0000000020000078                __data_end__ = .
```

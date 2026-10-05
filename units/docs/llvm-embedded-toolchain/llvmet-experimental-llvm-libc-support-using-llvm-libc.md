---
id: "llvmet-experimental-llvm-libc-support-using-llvm-libc"
type: "concept"
domain: "project"
title: "Experimental LLVM libc support: Using LLVM libc"
summary: "To compile a program with this LLVM libc, you must provide the following command line options, in addition to --target, -march or -mcpu, and the input and output files:"
status: "draft"
collection: "llvm-embedded-toolchain"
source: "ARM-software/LLVM-embedded-toolchain-for-Arm@c9dff0a:docs/llvmlibc.md"
doc_source: "https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/blob/c9dff0a/docs/llvmlibc.md#using-llvm-libc"
license: "Apache-2.0"
mode: "V"
---

To compile a program with this LLVM libc, you must provide the
following command line options, in addition to `--target`, `-march` or
`-mcpu`, and the input and output files:

* `--config=llvmlibc.cfg` if you are using LLVM libc as an overlay
  package (but you do not need this if you have built the whole
  toolchain with only LLVM libc)

* `-lcrt0` to include a library defining the `_start` symbol (or else
  provide that symbol yourself)

* `-lsemihost` to include a library that implements porting functions
  in LLVM's libc in terms of the Arm semihosting API (or else provide
  an alternative implementation of those functions yourself)

* `-Wl,--defsym=__stack=0x`_nnnnnn_ to define the starting value of
  your stack pointer. Alternatively, use a linker script that defines
  the symbol `__stack` in addition to whatever other memory layout you
  want.

* `-Wl,__llvm_libc_heap_limit=0x`_nnnnnn_ if you are using the heap.
  The heap start defined by the value of the symbol `_end` which will
  be defined by the linker if no linker script is used. Alternatively
  use a linker script that defines the symbols `_end` and
  `__llvm_libc_heap_limit` in addition to whatever other memory layout
  you want.

* LLVM libc does not define errno. If you are using a function that
  sets errno then you must implement the function `int *__llvm_libc_errno()`
  that returns the address of your definition of errno.

For example:

```
clang --config=llvmlibc.cfg --target=arm-none-eabi -march=armv7m -o hello hello.c -lsemihost -lcrt0 -Wl,--defsym=__stack=0x200000
```

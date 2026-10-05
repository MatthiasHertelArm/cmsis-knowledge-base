---
id: "intr-better-firmware-with-llvm-clang-setting-up-your-project-to-compile-with"
type: "concept"
domain: "debug"
title: "Better Firmware with LLVM/Clang: Setting up your project to compile with GCC & Clang"
summary: "Now that we have seen a small sampling of what we can do with LLVM/Clang, let's walk through the steps involved to update a GCC based project to compile with it!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-20-arm-cortexm-with-llvm-clang.md"
doc_source: "https://interrupt.memfault.com/blog/arm-cortexm-with-llvm-clang#setting-up-your-project-to-compile-with-gcc-clang"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that we have seen a small sampling of what we can do with LLVM/Clang, let's walk through the
steps involved to update a GCC based project to compile with it!

Fortunately, the LLVM/Clang project has made every effort to support GNU GCC assembly,
attributes, compiler flags & GNU linker script syntax, so a majority of the code in your project
should already be compatible and the migration effort should be quite minimal.

### Make Build System Compiler Aware

There will be a few system updates we will want to make depending on the compiler we are using. For example, Clang has a number of flags that GCC does not support so we will only want to enable those when Clang is in use.

Here is a template of what a makefile supporting both Clang and GCC targets can look like:

```bash
# Set things up to use the arm-none-eabi-gcc that is on
# our path by default but allow things to be easily overridden, i.e:
#
# COMPILER=<PATH_TO_OTHER_GCC_VERSION>/arm-none-eabi-gcc make
# COMPILER=clang make
COMPILER ?= arm-none-eabi-gcc
CC = $(COMPILER)

# [ ... ]

ifneq '' '$(findstring clang,$(CC_VERSION_INFO))'
$(info ===Clang Compiler Detected===)

COMPILER_SPECIFIC_CFLAGS +=
COMPILER_SPECIFIC_LDFLAGS +=

endif


ifneq '' '$(findstring gcc,$(CC_VERSION_INFO))'
$(info ===GCC Compiler Detected===)

COMPILER_SPECIFIC_CFLAGS +=
COMPILER_SPECIFIC_LDFLAGS +=

endif

CFLAGS += $(COMPILER_SPECIFIC_CFLAGS)
LDFLAGS += $(COMPILER_SPECIFIC_LDFLAGS)
```

### Create a "compiler.h" header

You'll probably encounter some code in your project that is compatible with GCC but not Clang. For
any project supporting multiple compilers you will find a "compiler.h" style header that wraps
compiler specifics behind a common macro. For example, for Clang you need to use a different
attribute to disable optimizations on a function.

```c
//! @file example_project/compiler.h

#if defined(__clang__)

#define EXAMPLE_PROJ_NO_OPT __attribute__((optnone))

#elif defined(__GNUC__)

#define EXAMPLE_PROJ_NO_OPT __attribute__((optimize("O0")))

#else
#  error "Unsupported Compiler"
#endif
```

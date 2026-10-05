---
id: "intr-better-firmware-with-llvm-clang-cross-compiling-with-clang"
type: "concept"
domain: "debug"
title: "Better Firmware with LLVM/Clang: Cross Compiling With Clang"
summary: "Unlike GCC, a default build of Clang is multi-target capable. To cross compile all you have to do is specify the appropriate --target argument into Clang."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-20-arm-cortexm-with-llvm-clang.md"
doc_source: "https://interrupt.memfault.com/blog/arm-cortexm-with-llvm-clang#cross-compiling-with-clang"
license: "CC-BY-SA-4.0"
mode: "V"
---

Unlike GCC, a default build of Clang is multi-target capable. To cross compile all you have to do
is specify the appropriate `--target` argument into Clang. If no `--target` is specified it falls
back to its default behavior of targeting the native host architecture.

You can dump a list of the architectures supported by running `llc --version`:

```bash
$ llc --version
LLVM (http://llvm.org/):
  LLVM version 10.0.0
  Optimized build.
  Default target: x86_64-apple-darwin18.5.0
  Host CPU: skylake

  Registered Targets:
    aarch64    - AArch64 (little endian)
    aarch64_32 - AArch64 (little endian ILP32)
    aarch64_be - AArch64 (big endian)
    amdgcn     - AMD GCN GPUs
    arm        - ARM
[ ... ]
```

#### The Clang Target Triple

The value passed to `--target` itself is a bit complicated. The good thing is for ARM Cortex-M, you
can always pass the same value: `--target=arm-none-eabi`.

> Feel free to skip to the [next section](#update-clang-baremetal) if you aren't interested in
> learning more about the `--target` argument internals.

##### Clang Target Triple Internals

The makeup of a `--target` value is actually:

`<arch><sub>-<vendor>-<sys>-<abi>`

A rough breakdown of what is expected for ARM targets is:

- `arch`: One of the "registered targets" that was output from `llc --version` so for ARM it is `arm`.
- `sub` : When left blank the value is inferred from other flags specified as part of the
  compilation. For ARM Cortex-M, `v6m`, `v7m`, `v7em`, `v8m`, etc are all be legal values.
- `vendor`: For ARM this can be left blank or you can specify `unknown` explicitly.
- `sys`: For embedded targets this will be `none`. If you are compiling code targeting an OS, the
  name of the OS will be used. For example, `linux` or `darwin`.
- `abi`: For Embedded ARM this will always be `eabi` ("embedded-application binary interface")

If you stick with the `--target=arm-none-eabi` option suggested, the architecture will be resolved from the GCC compiler flags. (i.e Notably `-mcpu` or `-march`)

Confusingly, unspecified or invalid fields will be filled in or replaced under the hood by the
LLVM toolchain. This can make it hard to determine if you have specified a legal target or not:

```bash
$ clang --target=armv7notrealsub-none-eabi --print-target-triple
armv7notrealsub-none-unknown-eabi
```

If you want to sanity check that the target being targeted is correct, the most reliable way I
have found to do this is by compiling an empty file and emitting LLVM Intermediate Representation (IR). The "target triple" line will inform
you what architecture code is actually being generated for:

##### Checking Target Triple By Dumping LLVM IR

```bash
$ touch test.c
$ clang --target=armv7notrealsub-none-eabi -emit-llvm -S test.c
$ cat test.ll | grep "target triple"
  target triple = "armv4t-none-unknown-eabi"
```

{:#update-clang-baremetal}

### Updating Clang to cross-compile a "bare-metal" target

#### ARM Cortex-M "bare-metal" targets

When you compile an application to run on an operating system (i.e `darwin` or `linux` instead of `none`),
the C standard libraries will be picked up automatically for you. Code not targeting an OS is
often referred to as running on a "bare-metal" environment. With LLVM/Clang you
are responsible for providing locations of the standard libraries in this scenario, which is comprised of:

- The C standard library[^2] -- `libc.a`
- Mathematical Functions of C standard library -- Often, this is exported in a separate library, `libm.a`.
- Compiler Built-Ins -- Most compilers include a set of built-in functions. The compiler will
  opportunistically replace parts of your code with builtins for better performance or to save code
  space. With GNU GCC these builtins are exposed via `libgcc.a`[^3]. With clang they are exposed
  via `libclang_rt.builtins.*.a`. There is no formal specification for what builtins need to be
  implemented but Clang makes every effort to match the exact subset required by GCC.

Fortunately, for ARM Cortex-M development, the official GNU Arm toolchain[^1] bundles pre-compiled
variants of [Newlib's libc and libm](https://interrupt.memfault.com/blog/bootstrapping-libc-with-newlib).

When you compile a project with the GNU Arm toolchain, `libc.a` & `libm.a` from the pre-compiled
Newlib as well as GCC's `libgcc.a` will be linked into your project automatically.

I would suggest instead using the compiler flag `--nostdlib` to disable this behavior. This will force you
to manually specify these targets (by adding `-lc`, `-lm`, & `-lgcc` to your LDFLAGS). It makes it
more explicit when library dependencies are pulled into your project and easier to experiment with
swapping in alternative versions of the standard library.

#### Adding standard libraries to Clang "bare-metal" compilation

Clang does not bundle a C standard library for "bare-metal" ARM Cortex-M targets, so the
recommendation in this scenario is to use the libraries included with the GNU Arm toolchain.

GCC and Clang expose some useful compiler arguments to make this straightforward to accomplish. Notably, with
Clang we can use `--sysroot` to change the default search path Clang uses for standard includes.

In our Makefile we can use the following `arm-none-eabi-gcc` compiler commands to programmatically
build the paths we need to provide to Clang.

- `-print-sysroot` for the path to pass to Clangs `--sysroot` option
- `-print-multi-directory` this will display where libc.a and libm.a within the gcc toolchain are located relative to `$SYS_ROOT/lib`
- `-print-libgcc-file-name` will dump the complete path to GCC builtin functions (`libgcc.a`)

##### Makefile Modifications

Putting it all together and updating the Makefile we started above we have:

```bash
# Note: These arguments will be used by clang to select
# the specific architecture target when we use the
# invoke Clang with --target=arm-none-eabi
ARCH_CFLAGS += \
  -mthumb -mcpu=cortex-m4 \
  -mfloat-abi=hard -mfpu=fpv4-sp-d16 \

# [ ... ]

ifneq '' '$(findstring clang,$(CC_VERSION_INFO))'
$(info ===Clang Compiler Detected===)

# Default assumes a GNU Arm toolchain is on your path
# but an explicit path can also be provided by doing
# ARM_GNU_CC=<PATH_TO_GCC> make
ARM_CORTEXM_SYSROOT = \
  $(shell $(ARM_GNU_CC) $(ARCH_CFLAGS) -print-sysroot 2>&1)

# The directory where Newlib's libc.a & libm.a reside
# for the specific target architecture
ARM_CORTEXM_MULTI_DIR = \
  $(shell $(ARM_GNU_CC) $(ARCH_CFLAGS) -print-multi-directory 2>&1)

# Pick up builtins needed for compilation
ARM_CORTEXM_BUILTINS ?= \
$(shell $(ARM_GNU_CC) $(ARCH_CFLAGS) -print-libgcc-file-name 2>&1)

COMPILER_SPECIFIC_CFLAGS += \
  --target=arm-none-eabi \
  --sysroot=$(ARM_CORTEXM_SYSROOT)

COMPILER_SPECIFIC_LDFLAGS += \
  -L$(ARM_CORTEXM_SYSROOT)/lib/$(ARM_CORTEXM_MULTI_DIR) \
  $(ARM_CORTEXM_BUILTINS)
endif
```

### Use Clang's `-Oz` instead of `-Os`

For embedded projects, the quality of a compiler is often evaluated by how small of a binary it can
create. With GCC, the smallest code is emitted when compiling with the `-Os` option. With Clang,
you will want to use `-Oz` instead which enables additional space optimizations beyond those
enabled by Clang's version of `-Os`.

```bash
ifneq '' '$(findstring clang,$(CC_VERSION_INFO))'
$(info ===Clang Compiler Detected===)
# [ ... ]

COMPILER_SPECIFIC_CFLAGS += \
...
  -0z
endif

ifneq '' '$(findstring gcc,$(CC_VERSION_INFO))'
$(info ===GCC Compiler Detected===)

COMPILER_SPECIFIC_CFLAGS += \
  -Os
endif
```

### Compiling libclang_rt.builtins\*.a for ARM Cortex-M

If you are interested in taking the road less traveled, it _is_ possible to compile LLVMs builtin
library for ARM Cortex-M though I would not recommend it.

> At this point we can compile our project with either GCC and Clang! [Skip ahead](#using-gcc-and-clang)
> to the next section to try that out instead!

You can even find some documentation
about the endeavor [here](https://llvm.org/docs/HowToCrossCompileBuiltinsOnArm.html).

Disclaimers: At the time of writing this article,

- Some of the official documentation, such as the instructions for "Alternative using a cmake cache" no
  longer work.
- It does not appear possible to compile a builtin targeting the Cortex-M hard float ABI (i.e
  `armv7em` target).
- It does not appear possible to compile `libclang_rt` for ARM Cortex-M on OSX. You need to use
  Docker or be running on Linux natively.

#### Setting up environment for libclang_rt build

```bash
$ export ARM_SYSROOT=$(arm-none-eabi-gcc -print-sysroot)

# This needs to be a complete ARM target triple to pick up
# architecture specific optimizations
#   Cortex M0, M0+: armv6m-none-eabi
#   Cortex M3: armv7m-none-eabi
#   Cortex M4, M7: armv7em-none-eabi
#   Cortex M33: armv8m-none-eabi
# Let's target Cortex M3 as an example:
$ export NONE_EABI_TARGET=armv7m-none-eabi

$ export LLVM_BIN_PATH=$(dirname $(which clang))

# Only Soft Float ABI seems to work
$ export NONE_EABI_TARGET_FLAGS="-mthumb -mfloat-abi=soft -mfpu=none"
```

#### Configuring and Compiling libclang_rt for baremetal

Once you have set up the env you will need to checkout the compiler-rt project and compiler:

```bash
$ git clone https://github.com/llvm/llvm-project.git llvm-project
$ cd llvm-project/compiler-rt
$ mkdir build
$ cd build

$ cmake -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release \
-DCMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY \
-DCOMPILER_RT_OS_DIR="baremetal" \
-DCOMPILER_RT_BUILD_BUILTINS=ON \
-DCOMPILER_RT_BUILD_SANITIZERS=OFF \
-DCOMPILER_RT_BUILD_XRAY=OFF \
-DCOMPILER_RT_BUILD_LIBFUZZER=OFF \
-DCOMPILER_RT_BUILD_PROFILE=OFF \
-DCMAKE_C_COMPILER=${LLVM_BIN_PATH}/clang \
-DCMAKE_C_COMPILER_TARGET=${NONE_EABI_TARGET} \
-DCMAKE_ASM_COMPILER_TARGET=${NONE_EABI_TARGET} \
-DCMAKE_AR=${LLVM_BIN_PATH}/llvm-ar \
-DCMAKE_NM=${LLVM_BIN_PATH}/llvm-nm \
-DCMAKE_LINKER=${LLVM_BIN_PATH}/ld.lld \
-DCMAKE_RANLIB=${LLVM_BIN_PATH}/llvm-ranlib \
-DCOMPILER_RT_BAREMETAL_BUILD=ON \
-DCOMPILER_RT_DEFAULT_TARGET_ONLY=ON \
-DLLVM_CONFIG_PATH=${LLVM_BIN_PATH}/llvm-config \
-DCMAKE_C_FLAGS= ${NONE_EABI_TARGET_FLAGS} \
-DCMAKE_ASM_FLAGS=${NONE_EABI_TARGET_FLAGS} \
-DCOMPILER_RT_INCLUDE_TESTS=OFF \
-DCMAKE_SYSROOT=${ARM_SYSROOT} ..

$ make
...
[100%] Built target clang_rt.builtins-armv7m
Scanning dependencies of target builtins
[100%] Built target builtins
Scanning dependencies of target compiler-rt-headers
[100%] Built target compiler-rt-headers
Scanning dependencies of target compiler-rt
[100%] Built target compiler-rt
```

At the end of the build, the Clang `libgcc.a` equivalent will be emitted to `./lib/baremetal/libclang_rt.builtins-armv7m.a`

You can swap `libgcc` with the generated `libclang_rt`in our example project by overrding
`ARM_CORTEXM_BUILTINS` when invoking make:

##### Swapping libgcc with libclang_rt.builtins-armv7m

```bash
$ cd interrupt/examples/freertos-example-llvm/
$ make clean
$ ARM_CORTEXM_BUILTINS=\
  <PATH_TO>/lib/baremetal/libclang_rt.builtins-armv7m.a make
```

{: #using-gcc-and-clang}

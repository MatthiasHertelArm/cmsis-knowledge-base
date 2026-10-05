---
id: "intr-better-firmware-with-llvm-clang-overview-of-scan-build"
type: "concept"
domain: "debug"
title: "Better Firmware with LLVM/Clang: Static Analysis With Clang and scan-build / Overview of scan-build"
summary: "Part of: Static Analysis With Clang and scan-build"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-20-arm-cortexm-with-llvm-clang.md"
doc_source: "https://interrupt.memfault.com/blog/arm-cortexm-with-llvm-clang#overview-of-scan-build"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Static Analysis With Clang and scan-build_

`scan-build` is a static analyzer included as part of the LLVM toolchain. It works by intercepting calls to `gcc` or `clang` and making a static analysis pass.

`scan-build` works by overriding the `CC` and `CXX` used by `CMake` and `Make`. If you aren't doing anything tricky in your project, invoking the tool is as simple as:

```bash
$ scan-build make
$ scan-build cmake ..
```

`scan-build` has a number of "Checkers"[^7] enabled by default. You can view them by running `scan-build --help`:

```bash
$ scan-build --help
CONTROLLING CHECKERS:

 A default group of checkers are always run unless explicitly disabled.
 Checkers may be enabled/disabled using the following options:

 -enable-checker [checker name]
 -disable-checker [checker name]
[...]
AVAILABLE CHECKERS:

 + core.CallAndMessage           Check for logical errors for function calls and Objective-C message expressions (e.g., uninitialized arguments, null function pointers)
 + core.DivideZero               Check for division by zero
 + core.DynamicTypePropagation   Generate dynamic type information
 + core.NonNullParamChecker      Check for null pointers passed as arguments to a function whose arguments are references or marked with the 'nonnull' attribute
 + core.NullDereference          Check for dereferences of null pointers
 + core.StackAddressEscape       Check that addresses to stack memory do not escape the function
 + core.UndefinedBinaryOperatorResult Check for undefined results of binary operators
[...]
NOTE: "+" indicates that an analysis is enabled by default.
```

The default set is a good starting point, and you can easily enable non-default ones or
disable individual defaults. You can even implement your own custom pugins but these topics are outside the scope of this article.

Let's run scan-build on our example project. We'll see it finds a few interesting potential issues that neither Clang or GCC noticed during compilation.

Results will be emitted directly to the console but you can also browse them using the `scan-view`
command bundled with LLVM. `scan-view` will open an html representation of all the issues
discovered. From this view, you can easily filter by issue type and dig into the specifics of an analysis pass.

I've included [the full output for the example project here](https://interrupt.memfault.com/misc/llvm_scan_build_report) but here's an
example of the type of information you will see:

#### Report Overview



#### Report Analysis Example



#### Running scan-build

```bash
$ cd interrupt/examples/freertos-example-llvm/
$ make clean
$ scan-build make
scan-build: Using 'bin/clang-10' for static analysis
[...]
Linking library
Generated build/nrf52.elf
scan-build: 8 bugs found.
scan-build: Run 'scan-view /var/folders/dm/b0yt' to examine bug reports.
```

`scan-build` uses `gcc` by default on some platforms.
If this happens, you may see error messages related to unrecognized command line options and the `===GCC Compiler Detected===` message.
Set the compiler for `scan-build` to clang with the `--use-cc` and `--use-c++` options:
```bash
$ scan-build --use-cc=clang --use-c++=clang make
```

#### core.NullDereference Checker

```c
int example_operate_on_pointer(uint8_t *pointer) {
  int result = 0;
  if (pointer == NULL) {
    result = -1;
  }
  result += *pointer;
  return result;
}
```

```bash
src/builtin_scanbuild_examples.c:13:13:
  warning: Dereference of null pointer (loaded from variable 'pointer')
  result += *pointer;
```

> NOTE: The NullDereference Checker only looks for null pointer accesses _after_ there has already been a nullability check. This helps prevent the generation of false positives for functions that never get passed a NULL pointer.

#### core.DivideZero Checker

```c
int example_divide_by_zero(int denominator) {
  int rv = 5;
  if (denominator == 0) {
    rv = 1 / denominator;
  }
  return rv;
}
```

```bash
src/builtin_scanbuild_examples.c:20:11: warning: Division by zero
  rv = 1 / denominator;
```

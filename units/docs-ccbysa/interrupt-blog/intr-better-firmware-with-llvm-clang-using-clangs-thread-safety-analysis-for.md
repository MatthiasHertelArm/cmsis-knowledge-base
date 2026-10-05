---
id: "intr-better-firmware-with-llvm-clang-using-clangs-thread-safety-analysis-for"
type: "concept"
domain: "debug"
title: "Better Firmware with LLVM/Clang: Static Analysis With Clang and scan-build / Using Clangs Thread Safety Analysis for RTOS Mutexes"
summary: "Part of: Static Analysis With Clang and scan-build"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-20-arm-cortexm-with-llvm-clang.md"
doc_source: "https://interrupt.memfault.com/blog/arm-cortexm-with-llvm-clang#using-clangs-thread-safety-analysis-for-rtos-mutexes"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Static Analysis With Clang and scan-build_

Clang also supports a Thread Safety Analyzer which can catch deadlocks and race
conditions that arise when writing multi-threaded applications (or using multiple tasks in a RTOS). The checkers are enabled at
compile time by using the `-Wthread-safety` compiler flag so there is zero runtime overhead!

The analyzer was contributed and is maintained by Google and is used "extensively in Google's
internal code base".[^8] There is pretty good documentation about
how to leverage the feature for C++. However, the analyzers can be used for C code as well via compiler attributes.
It's pretty common in an embedded system with an RTOS to have mutexes for subsystems such as
an accelerometer or flash driver. In our example project we have:

```c
//! @file mutex.h
void flash_lock(void);
void flash_unlock(void);

void accel_lock(void);
void accel_unlock(void);
```

To use the analyzer we need to annotate where locks are given and released. We can also
flag if certain functions require a lock. We can wrap all of these behind macros in `compiler.h`:

#### Macros helpers for utilizing -Wthread-safety in C

```c
//! The Thread Safety Analyzers need an identifier to track things by
//! When using C++, this capability attribute can be bound to a Class.
//! For C, we'll just create a dummy variable that is not referenced
//! by actual code so it gets optimized away during compilation.
typedef int __attribute__((capability("mutex")))
  _ClangThreadSafetyLockReference;
#define INTERNAL_EXAMPLE_PROJ_DECLARE_LOCK_TRACKER(name) \
  extern _ClangThreadSafetyLockReference _##name

//! Flags a function that acquires a resource. In our example
//! we'll want to apply this attribute to flash_lock() and
//! accel_lock().
#define EXAMPLE_PROJ_FUNC_ACQUIRES_LOCK(name) \
  INTERNAL_EXAMPLE_PROJ_DECLARE_LOCK_TRACKER(name); \
  __attribute__((acquire_capability(_##name)))

//! Flags a function that releases a resource. For our example,
//! the accel_unlock() and flash_unlock() functions need this.
#define EXAMPLE_PROJ_FUNC_RELEASES_LOCK(name) \
  __attribute__((release_capability(_##name)))

//! Flags a function as requiring a lock be held by the time
//! it is invoked. For example, an "accel_read()" function.
#define EXAMPLE_PROJ_FUNC_REQUIRES_LOCK_HELD(name) \
  __attribute__((requires_capability(_##name)))

//! Disables thread safety checks for a function
//! This is required for the *_lock and *_unlock functions
//! in our example to prevent False positives.
#define EXAMPLE_PROJ_FUNC_DISABLE_LOCK_CHECKS \
  __attribute__((no_thread_safety_analysis))
```

Let's update our code to take advantage of the annotations:

```c
#pragma once

//! @file mutex.h
#include "example_project/compiler.h"

// ...

EXAMPLE_PROJ_FUNC_ACQUIRES_LOCK(flash)
void flash_lock(void);

EXAMPLE_PROJ_FUNC_RELEASES_LOCK(flash)
void flash_unlock(void);

EXAMPLE_PROJ_FUNC_ACQUIRES_LOCK(accel)
void accel_lock(void);

EXAMPLE_PROJ_FUNC_RELEASES_LOCK(accel)
void accel_unlock(void);

EXAMPLE_PROJ_FUNC_REQUIRES_LOCK_HELD(accel)
extern void example_func_requires_accel(void);
```

Now let's try out a few examples:

```c
void example_flash_lock_bug(void) {
  flash_lock();

  int rv = do_some_work_while_holding_locks();
  if (rv == -1) {
    return;
  }
  flash_unlock();
}
```

```bash
$ cd interrupt/examples/freertos-example-llvm/
$ make clean
$ CLI_CFLAG_OVERRIDES=-Wthread-safety COMPILER=clang make
[...]
src/mutex_examples.c:14:1:
  error: mutex '_flash' is not held on every path through here
      [-Werror,-Wthread-safety-analysis]
}
^
src/mutex_examples.c:7:3: note: mutex acquired here
  flash_lock();
```

```c
void example_accel_lock_bug(void) {
  example_func_requires_accel();
}
```

```bash
$ cd interrupt/examples/freertos-example-llvm/
$ make clean
$ CLI_CFLAG_OVERRIDES=-Wthread-safety COMPILER=clang make
[...]
src/mutex_examples.c:17:3:
  error: calling function 'example_func_requires_accel' requires holding
      mutex '_accel' exclusively [-Werror,-Wthread-safety-analysis]
  example_func_requires_accel();
```

Pretty neat, right?!

Some additional checkers can be enabled via annotations as well to enforce certain locks are acquired
before/after others. Take a look at the official documentation for more ideas![^8].

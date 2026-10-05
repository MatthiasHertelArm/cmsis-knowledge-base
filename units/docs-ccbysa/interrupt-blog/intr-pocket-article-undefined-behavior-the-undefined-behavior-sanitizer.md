---
id: "intr-pocket-article-undefined-behavior-the-undefined-behavior-sanitizer"
type: "concept"
domain: "debug"
title: "Pocket article: Undefined Behavior Sanitizer Trap on Error: The Undefined Behavior Sanitizer"
summary: "Undefined Behavior Sanitizer (UBSan) is part of a set of tools that perform runtime checks on C family software. You can read more here:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-06-22-ubsan-trap.md"
doc_source: "https://interrupt.memfault.com/blog/ubsan-trap#the-undefined-behavior-sanitizer"
license: "CC-BY-SA-4.0"
mode: "V"
---

Undefined Behavior Sanitizer (UBSan) is part of a set of tools that perform
runtime checks on C family software. You can read more here:

[https://releases.llvm.org/15.0.0/tools/clang/docs/UndefinedBehaviorSanitizer.html](https://releases.llvm.org/15.0.0/tools/clang/docs/UndefinedBehaviorSanitizer.html)

[https://developers.redhat.com/blog/2014/10/16/gcc-undefined-behavior-sanitizer-ubsan](https://developers.redhat.com/blog/2014/10/16/gcc-undefined-behavior-sanitizer-ubsan)

The other sanitizers in the family include
[AddressSanitizer](https://releases.llvm.org/15.0.0/tools/clang/docs/AddressSanitizer.html),
[LeakSanitizer](https://releases.llvm.org/15.0.0/tools/clang/docs/LeakSanitizer.html), and others.

> Note: **_AddressSanitizer_** is a very powerful tool for detecting memory
> out-of-bounds errors, and I highly recommend enabling it in your unit tests. It
> is worthy of a dedicated post so we won't go into too much detail here, other
> than it needs to be carefully integrated with the host platform- it works best
> on Linux (though it is available on some other platforms)

UBSan can catch several types of undefined behavior, for example:

- **array bounds checking**
- **integer / floating point overflows** (note that these are undefined per the
  C spec, but are usually deterministic for a particular compiler + arch +
  lib... however, changing optimization level might change how the UB is
  expressed!)
- **alignment when dereferencing**; it's possible to trick a compiler when
  dereferencing type-punned objects and in other scenarios, this traps those
  operations, though they may also end up in fault handler anyway depending on
  your architecture
- **loading an out-of-range enum**

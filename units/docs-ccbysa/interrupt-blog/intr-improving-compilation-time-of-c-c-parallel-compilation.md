---
id: "intr-improving-compilation-time-of-c-c-parallel-compilation"
type: "concept"
domain: "debug"
title: "Improving Compilation Time of C/C++ Projects: Steps Towards Faster Builds / Parallel Compilation"
summary: "The first and easiest thing to do to speed up builds is ensure you are building with multiple threads. Make, IAR, and Keil all support parallel compilation, so ensure you and the entire team have enabled this."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-02-11-improving-compilation-times-c-cpp-projects.md"
doc_source: "https://interrupt.memfault.com/blog/improving-compilation-times-c-cpp-projects#parallel-compilation"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Steps Towards Faster Builds_

The first and easiest thing to do to speed up builds is ensure you are building
with multiple threads. Make, IAR, and Keil all support parallel compilation, so
ensure you and the entire team have enabled this.

Below are some times recorded compiling the example project with GCC and
different thread counts.

(figure: comparison of compiler build times with GCC threads)

With Make, it is as simple as invoking Make with the argument `-jN`, where `N`
is the number of desired threads to use. If you or your team members
occasionally forget to pass in this parameter, I suggest wrapping the command
[using
Invoke](https://interrupt.memfault.com/blog/building-a-cli-for-firmware-projects#adding-parallel-builds).

If you are calling Make from a Makefile (a.k.a. recursive Make[^15]), verify
that you are using `$(MAKE)` instead of `make` when using it in a rule, as
follows:

```make
# GOOD
somerule:
	$(MAKE) -C subdir

# BAD
somerule:
	make -C subdir
```

If you passed in `-j4 --output-sync=recurse` as arguments to your initial Make
call, they will also be passed through to future `$(MAKE)` calls. In the second
`# BAD` example above, they will not be propagated and Make will run `somerule:`
in a single thread.

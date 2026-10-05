---
id: "intr-improving-compilation-time-of-c-c-profiling-the-build-system"
type: "concept"
domain: "debug"
title: "Improving Compilation Time of C/C++ Projects: Profiling the Build System"
summary: "I've now provided a few ways for you to speed up the compilation of files, but how do you go about profiling the rest of the build system rules? I have some good news and bad news."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-02-11-improving-compilation-times-c-cpp-projects.md"
doc_source: "https://interrupt.memfault.com/blog/improving-compilation-times-c-cpp-projects#profiling-the-build-system"
license: "CC-BY-SA-4.0"
mode: "V"
---

I've now provided a few ways for you to speed up the compilation of files, but
how do you go about profiling the rest of the build system rules? I have some
good news and bad news.

The good news is that most modern build systems have a way to show the execution
trace of the entire build, broken down by each rule. This is a great way to find
out how long each file takes to build and also to find where the bottle necks
are during parallel builds.

The bad news is that if you are using Make, there isn't a great way to do
profiling. My ultimate suggestion would be to just not use Make and opt for
something more modern. Bazel and CMake are good options. However, continue
reading if you want a couple of hacks for profiling build steps with Make.

### Profiling Individual Make Build Commands

The easiest way to add timing information to compilation steps is to prepend the
`time` command to the desired rules. For instance, if we wanted to profile each
call to `$(CC)`, we could do something like

```make
CC = time arm-none-eabi-gcc
```

or

```make
%.o : %.c
	time $(CC) $(CFLAGS) -c -o $@ $<

```

> NOTE: When using parallel builds in Make, the logging output can get
> scrambled. My advice is to ensure you are using a newer version of GNU Make
> and the `--output-sync=recurse` command line option[^13].

### Profiling Every Make Build Rule

If you want to profile every build rule in your Makefile, a
[clever approach](http://alangrow.com/blog/profiling-every-command-in-a-makefile)
is to override the `SHELL` Make variable with a timing script.

It produces a lot of noise, but it may help you discover slow steps in the
build.

{:.no_toc}

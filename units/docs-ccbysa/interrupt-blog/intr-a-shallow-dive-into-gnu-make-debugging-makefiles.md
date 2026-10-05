---
id: "intr-a-shallow-dive-into-gnu-make-debugging-makefiles"
type: "concept"
domain: "debug"
title: "A Shallow Dive into GNU Make: Debugging Makefiles"
summary: "I typically use the Make equivalent of printf, the $(info/warning/error) functions, for small problems, for example when checking conditional paths that aren't working:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-03-gnu-make-guidelines.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-make-guidelines#debugging-makefiles"
license: "CC-BY-SA-4.0"
mode: "V"
---

I typically use the Make equivalent of `printf`, the `$(info/warning/error)`
functions, for **small problems**, for example when checking conditional paths that
aren't working:

```makefile
ifeq ($(CC),clang)
$(error whoops, clang not supported!)
endif
```

For **debugging** why a rule is running when it shouldn't (or vice versa), you can
use the `--debug` options:
[https://www.gnu.org/software/make/manual/html_node/Options-Summary.html](https://www.gnu.org/software/make/manual/html_node/Options-Summary.html)

I recommend redirecting stdout to a file when using this option, it can produce
a lot of output.

### Profiling

For **profiling** a make invocation (e.g. for attempting to improve compilation
times), this tool can be useful:

[https://github.com/rocky/remake](https://github.com/rocky/remake)

Check out the tips here for compilation-related performance improvements:

[https://interrupt.memfault.com/blog/improving-compilation-times-c-cpp-projects](https://interrupt.memfault.com/blog/improving-compilation-times-c-cpp-projects)

### Using a Verbose Flag

If your project includes a lot of compiler flags (search paths, lots of warning
flags, etc.), then you may want to simplify the output of Make rules. It can be
useful to have a toggle to easily see the full output, for example:

```makefile
ifeq ($(V),1)
Q :=
else
Q := @
endif

%.o: %.c
	# prefix the compilation command with the $(Q) variable
	# use echo to print a simple "Compiling x.c" to show progress
	@echo Compiling $(notdir @^)
	$(Q) $(CC) -c $^ -o $@
```

To enable printing out the full compilation commands, set the `V` environment
variable like so:

```bash
$ V=1 make
```

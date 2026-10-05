---
id: "intr-a-shallow-dive-into-gnu-make-prerequisites"
type: "concept"
domain: "debug"
title: "A Shallow Dive into GNU Make: Anatomy of a Makefile / Prerequisites"
summary: "As seen above, these are targets that Make will check before running a rule. They can be files or other targets."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-03-gnu-make-guidelines.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-make-guidelines#prerequisites"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Anatomy of a Makefile_

As seen above, these are targets that Make will check before running a rule. They
can be files or other targets.

If any prerequisite is newer (modified-time) than the target, Make will run the
target rule.

In C projects, you might have a rule that converts a C file to an object file,
and you want the object file to rebuild if the C file changes:

```makefile
foo.o: foo.c
	# use automatic variables for the input and output file names
	$(CC) $^ -c $@
```

#### Automatic Prerequisites

A very important consideration for C language projects is to trigger
recompilation if an `#include` header files change for a C file. This is done
with the `-M` compiler flag for gcc/clang, which will output a `.d` file you
will then import with the Make `include` directive.

The `.d` file will contain the necessary prerequisites for the `.c` file so any
header change causes a rebuild. See more details here:

[https://www.gnu.org/software/make/manual/html_node/Automatic-Prerequisites.html](https://www.gnu.org/software/make/manual/html_node/Automatic-Prerequisites.html)
[http://make.mad-scientist.net/papers/advanced-auto-dependency-generation/](http://make.mad-scientist.net/papers/advanced-auto-dependency-generation/)

The basic form might be:

```makefile
# these are the compiler flags for emitting the dependency tracking file. Note
# the usage of the '$<' automatic variable
DEPFLAGS = -MMD -MP -MF $<.d

test.o: test.c
    $(CC) $(DEPFLAGS) $< -c $@

# bring in the prerequisites by including all the .d files. prefix the line with
# '-' to prevent an error if any of the files do not exist
-include $(wildcard *.d)
```

#### Order-Only Prerequisites

These prerequisites will only be built if they don't exist; if they are newer
than the target, they will not trigger a target re-build.

A typical use is to create a directory for output files; emitting files to a
directory will update its `mtime` attribute, but we don't want that to trigger a
rebuild.

```makefile
OUTPUT_DIR = build

# output the .o to the build directory, which we add as an order-only
# prerequisite- anything right of the | pipe is considered order-only
$(OUTPUT_DIR)/test.o: test.c | $(OUTPUT_DIR)
	$(CC) -c $^ -o $@

# rule to make the directory
$(OUTPUT_DIR):
	mkdir -p $@
```

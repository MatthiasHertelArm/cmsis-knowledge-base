---
id: "intr-a-shallow-dive-into-gnu-make-targets-goals"
type: "concept"
domain: "debug"
title: "A Shallow Dive into GNU Make: Anatomy of a Makefile / Targets (Goals)"
summary: "Targets are the left hand side in the rule syntax:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-03-gnu-make-guidelines.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-make-guidelines#targets-goals"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Anatomy of a Makefile_

Targets are the left hand side in the rule syntax:

```makefile
target: prerequisite
	recipe
```

Targets almost always name **files**. This is because Make uses last-modified
time to track if a target is newer or older than its prerequisites and whether
it needs to be rebuilt!

When invoking Make, you can specify which target(s) you want to build as the
`goal`s by specifying it as a positional argument:

```bash
# make the 'test.txt' and 'all.zip' targets
make test.txt all.zip
```

If you don't specify a goal in the command, Make uses the first target specified
in the makefile, called the "default goal" (you can also
[override](https://www.gnu.org/software/make/manual/html_node/Goals.html) the
default goal if you need to).

#### Phony Targets

Sometimes it's useful to have meta-targets like `all`, `clean`, `test`, etc. In these cases, you don't want Make to check for a file named `all`/`clean` etc.

Make provides the `.PHONY` target syntax to mark a target as not pointing to a
file:

```makefile
# Say our project builds a program and a library 'foo' and 'foo.a'; if we want
# to build both by default we might make an 'all' rule that builds both
.PHONY: all

all: foo foo.a
```

If you have multiple phony targets, a good pattern might be to append each to
`.PHONY` where it's defined:

```makefile
# the 'all' rule that builds and tests. Note that it's listed first to make it
# the default rule
.PHONY: all
all: build test

# compile foo.c into a program 'foo'
foo: foo.c
	$(CC) foo.c -o foo

# compile foo-lib.c into a library 'foo.a'
foo.a: foo-lib.c
	# compile the object file
	$(CC) foo-lib.c -c foo-lib.o
	# use ar to create a static library containing our object file. using the
	# '$@' variable here to specify the rule target 'foo.a'
	$(AR) rcs $@ foo-lib.o

# a phony rule that builds our project; just contains a prerequisite of the
# library + program
.PHONY: build
build: foo foo.a

# a phony rule that runs our test harness. has the 'build' target as a
# prerequisite! Make will make sure (pardon the pun) the build rule executes
# first
.PHONY: test
test: build
	./run-tests.sh
```

> **NOTE!!! `.PHONY` targets are ALWAYS considered out-of-date, so Make will
ALWAYS run the recipe for those targets (and therefore any target that has a
`.PHONY` prerequisite!). Use with caution!!**

#### Implicit Rules

Implicit rules are provided by Make. I find using them to be confusing since
there's so much behavior happening behind the scenes. You will occasionally
encounter them in the wild, so be aware.

Here's a quick example:

```makefile
# this will compile 'test.c' with the default $(CC), $(CFLAGS), into the program
# 'test'. it will handle prerequisite tracking on test.c
test: test.o
```

Full list of implicit rules here:

[https://www.gnu.org/software/make/manual/html_node/Catalogue-of-Rules.html](https://www.gnu.org/software/make/manual/html_node/Catalogue-of-Rules.html)

#### Pattern Rules

Pattern rules let you write a generic rule that applies to multiple targets via
pattern-matching:

```makefile
# Note the use of the '$<' automatic variable, specifying the first
# prerequisite, which is the .c file
%.o: %.c
	$(CC) -c $< -o $@
```

The rule will then be used to make any target matching the pattern, which above
would be any file matching `%.o`, e.g. `foo.o`, `bar.o`.

If you use those `.o` files mentioned above to build a program:

```makefile
OBJ_FILES = foo.o bar.o

# Use CC to link foo.o + bar.o into 'program'. Note the use of the '$^'
# automatic variable, specifying ALL the prerequisites (all the OBJ_FILES)
# should be part of the link command
program: $(OBJ_FILES)
    $(CC) -o $@ $^
```

---
id: "intr-a-shallow-dive-into-gnu-make-variables"
type: "concept"
domain: "debug"
title: "A Shallow Dive into GNU Make: Anatomy of a Makefile / Variables"
summary: "Variables are used with the syntax $(FOO), where FOO is the variable name."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-03-gnu-make-guidelines.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-make-guidelines#variables"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Anatomy of a Makefile_

Variables are used with the syntax `$(FOO)`, where `FOO` is the variable name.

Variables contain purely strings as Make does not have other data types. Appending to a variable will add a space and the new content:

```makefile
FOO = one
FOO += two
# FOO is now "one two"

FOO = one
FOO = $(FOO)two
# FOO is now "onetwo"
```

#### Variable Assignment

In GNU Make syntax, variables are assigned with two "**flavors**":

1. *recursive expansion*: `variable = expression`
   The expression on the right hand side is assigned verbatim to the variable-
   this behaves much like a macro in C/C++, where the expression is evaluated
   when the variable is used:
   ```makefile
   FOO = 1
   BAR = $(FOO)
   FOO = 2
   # prints BAR=2
   $(info BAR=$(BAR))
   ```
2. *simple expansion*: `variable := expression`
   This assigns the *result* of an expression to a variable; the expression is
   expanded at the time of assignment:
   ```makefile
   FOO = 1
   BAR := $(FOO)
   FOO = 2
   # prints BAR=1
   $(info BAR=$(BAR))
   ```

> Note: the `$(info ...)` function is being used above to print expressions and
can be handy when debugging makefiles!*`

Variables which are not explicitly,
[implicitly](https://www.gnu.org/software/make/manual/html_node/Implicit-Variables.html),
nor
[automatically](https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html)
set will evaluate to an empty string.

#### Environment Variables

Environment variables are carried into the Make execution environment. Consider
the following makefile for example:

```makefile
$(info YOLO variable = $(YOLO))
```

If we set the variable `YOLO` in the shell command when running `make`, we'll set the value:

```bash
$ YOLO="hello there!" make
YOLO variable = hello there!
make: *** No targets.  Stop.
```

> Note: Make prints the "No targets" error because our makefile had no targets
listed!

If you use the `?=` assignment syntax, Make will only assign that value if the
variable doesn't already have a value:

Makefile:

```makefile
# default CC to gcc
CC ?= gcc
```

We can then override `$(CC)` in that makefile:

```bash
$ CC=clang make
```

Another common pattern is to allow inserting additional flags. In the makefile,
we would append to the variable instead of directly assigning to it.

```makefile
CFLAGS += -Wall
```

This permits passing extra flags in from the environment:

```bash
$ CFLAGS='-Werror=conversion -Werror=double-promotion' make
```

This can be very useful!

#### Overriding Variables

A special category of variable usage is called **overriding variables**. Using
this command-line option will override the value set **ANYWHERE ELSE** in the
environment or Makefile!

Makefile:

```makefile
# the value passed in the make command will override
# any value set elsewhere
YOLO = "not overridden"
$(info $(YOLO))
```

Command:

```bash
# setting "YOLO" to different values in the environment + makefile + overriding
# variable, yields the overriding value
$ YOLO="environment set" make YOLO='overridden!!'
overridden!!
make: *** No targets.  Stop.
```

Overriding variables can be confusing, and should be used with caution!

#### Target-Specific Variables

These variables are only available in the recipe context. They also apply to any prerequisite recipe!

```makefile
# set the -g value to CFLAGS
# applies to the prog.o/foo.o/bar.o recipes too!
prog : CFLAGS = -g
prog : prog.o foo.o bar.o
	echo $(CFLAGS) # will print '-g'
```

#### Implicit Variables

These are pre-defined by Make (unless overridden with any other variable type of
the same name). Some common examples:

- `$(CC)` - the C compiler (`gcc`)
- `$(AR)` - archive program (`ar`)
- `$(CFLAGS)` - flags for the C compiler

Full list here:

[https://www.gnu.org/software/make/manual/html_node/Implicit-Variables.html](https://www.gnu.org/software/make/manual/html_node/Implicit-Variables.html)

#### Automatic Variables

These are special variables always set by Make and available in recipe context.
They can be useful to prevent duplicated names (Don't Repeat Yourself).

A few common automatic variables:

```makefile
# $@ : the target name, here it would be "test.txt"
test.txt:
	echo HEYO > $@

# $^ : name of all the prerequisites
all.zip: foo.txt test.txt
	# run the gzip command with all the prerequisites "$^", outputting to the
	# name of the target, "$@"
	gzip -c $^ > $@
```

See more at:
[https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html](https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html)

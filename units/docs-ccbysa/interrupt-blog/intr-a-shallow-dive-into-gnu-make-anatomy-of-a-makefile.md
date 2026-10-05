---
id: "intr-a-shallow-dive-into-gnu-make-anatomy-of-a-makefile"
type: "concept"
domain: "debug"
title: "A Shallow Dive into GNU Make: Anatomy of a Makefile"
summary: "A Makefile contains rules used to produce targets. Some basic components of a Makefile are shown below:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-03-gnu-make-guidelines.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-make-guidelines#anatomy-of-a-makefile"
license: "CC-BY-SA-4.0"
mode: "V"
---

A Makefile contains **rules** used to produce **targets**. Some basic components of a Makefile are shown below:

```makefile
# Comments are prefixed with the '#' symbol

# A variable assignment
FOO = "hello there!"

# A rule creating target "test", with "test.c" as a prerequisite
test: test.c
	# The contents of a rule is called the "recipe", and is
	# typically composed of one or more shell commands.
	# It must be indented from the target name (historically with
	# tabs, spaces are permitted)

	# Using the variable "FOO"
	echo $(FOO)

	# Calling the C compiler using a predefined variable naming
	# the default C compiler, '$(CC)'
	$(CC) test.c -o test
```

Let's take a look at each part of the example above.

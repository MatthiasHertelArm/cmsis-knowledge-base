---
id: "intr-a-shallow-dive-into-gnu-make-recipe"
type: "concept"
domain: "debug"
title: "A Shallow Dive into GNU Make: Anatomy of a Makefile / Recipe"
summary: "The \"recipe\" is the list of shell commands to be executed to create the target. They are passed into a sub-shell (/bin/sh by default)."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-03-gnu-make-guidelines.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-make-guidelines#recipe"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Anatomy of a Makefile_

The "recipe" is the list of shell commands to be executed to create the target. They are
passed into a sub-shell (`/bin/sh` by default). The rule is considered
successful if the target is updated after the recipe runs (but is not an error
if this doesn't happen).

```makefile
foo.txt:
	# a simple recipe
	echo HEYO > $@
```

If any line of the recipe returns a non-zero exit code, Make will terminate and
print an error message. You can tell Make to ignore non-zero exit codes by
prefixing with the `-` character:

```makefile
.PHONY: clean
clean:
	# we don't care if rm fails
	-rm -r ./build
```

Prefixing a recipe line with `@` will disable echoing that line before
executing:

```makefile
clean:
	@# this recipe will just print 'About to clean everything!'
	@# prefixing the shell comment lines '#' here also prevents them from
	@# appearing during execution
	@echo About to clean everything!
```

Make will expand variable/function expressions in the recipe context before
running them, but will otherwise not process it. If you want to access shell
variables, escape them with `$`:

```makefile
USER = linus

print-user:
	# print out the shell variable $USER
	echo $$USER

	# print out the make variable USER
	echo $(USER)
```

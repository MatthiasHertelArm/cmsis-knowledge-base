---
id: "intr-a-shallow-dive-into-gnu-make-advanced-topics"
type: "concept"
domain: "debug"
title: "A Shallow Dive into GNU Make: Advanced Topics"
summary: "These features are less frequently encountered, but provide some powerful functionality that can enable sophisticated behavior in your build."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-03-gnu-make-guidelines.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-make-guidelines#advanced-topics"
license: "CC-BY-SA-4.0"
mode: "V"
---

These features are less frequently encountered, but provide some powerful
functionality that can enable sophisticated behavior in your build.

### Functions

Make functions are called with the syntax:

```makefile
$(function-name arguments)
```

where `arguments` is a comma-delimited list of arguments.

#### Built-in Functions

There are several functions provided by Make. The most common ones I use are for text
manipulation:
[https://www.gnu.org/software/make/manual/html_node/Text-Functions.html](https://www.gnu.org/software/make/manual/html_node/Text-Functions.html)
[https://www.gnu.org/software/make/manual/html_node/File-Name-Functions.html](https://www.gnu.org/software/make/manual/html_node/File-Name-Functions.html)

For example:

```makefile
FILES=$(wildcard *.c)

# you can combine function calls; here we strip the suffix off of $(FILES) with
# the $(basename) function, then add the .o suffix
O_FILES=$(addsuffix .o,$(basename $(FILES)))

# note that the GNU Make Manual suggests an alternate form for this particular
# operation:
O_FILES=$(FILES:.c=.o)
```

#### User-Defined Functions

You can define your own functions as well:

```makefile
reverse = $(2) $(1)

foo = $(call reverse,a,b)
```

A more complicated but quite useful example:

```makefile
# recursive wildcard (use it instead of $(shell find . -name '*.c'))
# taken from https://stackoverflow.com/a/18258352
rwildcard=$(foreach d,$(wildcard $1*),$(call rwildcard,$d/,$2) $(filter $(subst *,%,$2),$d))

C_FILES = $(call rwildcard,.,*.c)
```

#### Shell Function

You can have Make call a shell expression and capture the result:

```makefile
TODAYS_DATE=$(shell date --iso-8601)
```

I'm cautious when using this feature, though; it adds a dependency on whatever
programs you use, so if you're calling more exotic programs, make sure your
build environment is controlled (e.g. in a container or with
[Conda](https://interrupt.memfault.com/blog/conda-developer-environments)).

### Conditionals

Make has syntax for conditional expressions:

```makefile
FOO=yolo
ifeq ($(FOO),yolo)
$(info foo is yolo!)
else
$(info foo is not yolo :( )
endif

# testing if a variable is set; unset variables are empty
ifneq ($(FOO),)  # checking if FOO is blank
$(info FOO is unset)
endif
```

The "complex conditional" syntax is just the `if-elseif-else` combination:

```makefile
# "complex conditional"
ifeq ($(FOO),yolo)
$(info foo is yolo)
else ifeq ($(FOO), heyo)
$(info foo is heyo)
else
$(info foo is not yolo or heyo :( )
endif
```

### `include` Directive

You can import other Makefile contents using the `include` directive:

`sources.mk`:

```makefile
SOURCE_FILES := \
  bar.c \
  foo.c \

```

`Makefile`:

```makefile
include sources.mk

OBJECT_FILES = $(SOURCE_FILES:.c=.o)

%.o: %.c
	$(CC) -c $^ -o $@
```

### Sub-make

Invoking Make from a Makefile should be done with the `$(MAKE)` variable:

```makefile
somelib.a:
	$(MAKE) -C path/to/somelib/directory
```

This is often used when building external libraries. It's also used heavily in Kconfig builds (e.g. when building the Linux kernel).

Note that this approach has some pitfalls:

- Recursive invocation can result in slow builds.
- Tracking prerequisites can be tricky; often you will see `.PHONY` used.

More details on the disadvantages here:

[http://aegis.sourceforge.net/auug97.pdf](http://aegis.sourceforge.net/auug97.pdf)

### Metaprogramming with `eval`

`Make`'s `eval` directive allows us to generate Make syntax at runtime:

```makefile
# generate rules for xml->json in some weird world
FILES = $(wildcard inputfile/*.xml)

# create a user-defined function that generates rules
define GENERATE_RULE =
$(eval
# prereq rule for creating output directory
$(1)_OUT_DIR = $(dir $(1))/$(1)_out
$(1)_OUT_DIR:
	mkdir -p $@

# rule that calls a script on the input file and produces $@ target
$(1)_OUT_DIR/$(1).json: $(1) | $(1)_OUT_DIR
	./convert-xml-to-json.sh $(1) $@
)

# add the target to the all rule
all: $(1)_OUT_DIR/$(1).json
endef
```

```makefile
# produce the rules
.PHONY: all
all:

$(foreach file,$(FILES),$(call GENERATE_RULE,$(file)))
```

Note that approaches using this feature of Make can be quite confusing, adding
helpful comments explaining what the intent is can be useful for your future
self!

### VPATH

`VPATH` is a special Make variable that contains a list of directories Make
should search when looking for prerequisites and targets.

It can be used to emit object files or other derived files into a `./build`
directory, instead of cluttering up the `src` directory:

```makefile
# This makefile should be invoked from the temporary build directory, eg:
# $ mkdir -p build && cd ./build && make -f ../Makefile

# Derive the directory containing this Makefile
MAKEFILE_DIR = $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

# now inform Make we should look for prerequisites from the root directory as
# well as the cwd
VPATH += $(MAKEFILE_DIR)

SRC_FILES = $(wildcard $(MAKEFILE_DIR)/src/*.c)

# Set the obj file paths to be relative to the cwd
OBJ_FILES = $(subst $(MAKEFILE_DIR)/,,$(SRC_FILES:.c=.o))

# now we can continue as if Make was running from the root directory, and not a
# subdirectory

# $(OBJ_FILES) will be built by the pattern rule below
foo.a: $(OBJ_FILES)
	$(AR) rcs $@ $(OBJ_FILES)

# pattern rule; since we added ROOT_DIR to VPATH, Make can find prerequisites
# like `src/test.c` when running from the build directory!
%.o: %.c
	# create the directory tree for the output file 👍
	echo $@
	mkdir -p $(dir $@)
	# compile
	$(CC) -c $^ -o $@
```

I recommend avoiding use of `VPATH`. It's usually simpler to achieve the same
out-of-tree behavior by outputting the generated files in a build directory
without needing `VPATH`.

### `touch`

You may see the `touch` command used to track rules that seem difficult to
otherwise track; for example, when unpacking a toolchain:

```makefile
# our tools are stored in tools.tar.gz, and downloaded from a server
TOOLS_ARCHIVE = tools.tar.gz
TOOLS_URL = https://httpbin.org/get

# the rule to download the tools using wget
$(TOOLS_ARCHIVE):
	wget $(TOOLS_URL) -O $(TOOLS_ARCHIVE)

# rule to unpack them
tools-unpacked.dummy: $(TOOLS_ARCHIVE)
	# running this command results in a directory.. but how do we know it
	# completed, without a file to track?
	tar xzvf $^
	# use the touch command to record completion in a dummy file
	touch $@
```
I recommend avoiding the use of `touch`. However there are some cases where it
might be unavoidable.

---
id: "intr-from-zero-to-main-bootstrapping-li-implementing-our-own-c-standard-library"
type: "concept"
domain: "debug"
title: "From Zero to main(): Bootstrapping libc with Newlib: Implementing our own C standard library"
summary: "In some cases, you may want to take different tradeoffs than the ones taken by the implementers of Newlib. Perhaps you are willing to sacrifice some functionality for code space, or are willing to trade performance for security."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-12-bootstrapping-libc-with-newlib.md"
doc_source: "https://interrupt.memfault.com/blog/bootstrapping-libc-with-newlib#implementing-our-own-c-standard-library"
license: "CC-BY-SA-4.0"
mode: "V"
---

In some cases, you may want to take different tradeoffs than the ones taken by
the implementers of Newlib. Perhaps you are willing to sacrifice some
functionality for code space, or are willing to trade performance for security.
In most cases it is easier to replace a few functions, though you may end up
with a fully custom C library.

### Replacing a function

Because Newlib is a static library with a separate object file for every
function, all you need to do to replace a function is define it in your program.
The linker won’t go looking for it in static libraries if it finds it in your
code.

For example, we may want to replace Newlib’s `printf` implementation, either
because it is too large or because it depends on dynamic memory management.
Using Marco Paland’s excellent alternative[^7] is as simple as a Makefile change.

We first clone it in our firmware’s folder under `lib/printf`, and update our
Makefile to reflect the change:

```makefile
PROJECT := with-libc
BUILD_DIR ?= build

INCLUDES = \
  ... \
  lib/printf

SRCS = \
  ... \
  lib/printf/printf.c \
	startup_samd21.c \
	$(PROJECT).c

include ../common-standalone.mk
```

### Full replacement

In some cases, you may want to do away with Newlib altogether. Perhaps you don’t
want any dynamic memory allocation, in which case you could use Embedded
Artistry’s solid alternative[^8]. Another good reason to replace the version of
Newlib provided by your toolchain is to use your own build of it because you
would like to use different compile-time flags.

Once we have copied the static lib (`.a`) for our selected libc, we disable
Newlib with `-nostdlib` and explicitly link in our substitute library. You can
find the resulting Makefile below:

```makefile
PROJECT := with-libc
BUILD_DIR ?= build

CFLAGS += -nostdlib
LDFLAGS += -L../lib/embeddedartistry_libc -lc

INCLUDES = \
	$(ASF_PATH)/sam0/drivers/sercom \
	$(ASF_PATH)/sam0/drivers/sercom/usart \
	$(ASF_PATH)/common/services/serial \
	$(ASF_PATH)/common/services/serial/sam0_usart

SRCS = \
	$(ASF_PATH)/sam0/drivers/sercom/usart/usart.c \
	$(ASF_PATH)/sam0/drivers/sercom/sercom.c \
	startup_samd21.c \
	$(PROJECT).c

include ../common-standalone.mk
```

> Note that the `__libc_init_array` functionality is not found in every standard
> C library. You will either need to avoid using it, or bring in Newlib’s
> implementation.

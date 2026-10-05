---
id: "intr-improving-compilation-time-of-c-c-precompiled-headers"
type: "concept"
domain: "debug"
title: "Improving Compilation Time of C/C++ Projects: Steps Towards Faster Builds / Precompiled headers"
summary: "After cleaning up all of the header dependency issues that you can find, there may still be some headers that you can't avoid including everywhere, and they are slowing down your build."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-02-11-improving-compilation-times-c-cpp-projects.md"
doc_source: "https://interrupt.memfault.com/blog/improving-compilation-times-c-cpp-projects#precompiled-headers"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Steps Towards Faster Builds_

> NOTE: This is a GCC/Clang-only feature.

After cleaning up all of the header dependency issues that you can find, there
may still be some headers that you can't avoid including everywhere, and they
are slowing down your build. The good news is that there is a way to pre-compile
your headers with GCC[^12].

Pre-compiling a header means that the compiler will only need to compile a
header _once_, and whenever it is included by other files, it will reuse the
built object. It compiles the header into an intermediate file with the
extension `.h.gch`. If the location of these files is added as an include path
when compiling (before the real headers), GCC will use the precompiled versions
instead.

#### Implementing Precompiled Headers

Let's go over the easiest way to do this in GCC, one that doesn't require you to
re-architect your project.

First, create a header file `precompiled.h` and place it in your source tree.
Add a rule to compile this header, just as you would with a `.c` file. It should
be built before building the `.c` or `.cpp` files. Then include this header
using the CFLAG argument `-include <>` when compiling the `.c` and `.cpp` files.
With Make, this looks something like:

```make
PRECOMPILED_H := "precompiled.h"
PRECOMPILED_H_OBJ := $(PRECOMPILED_H).gch

%.h.gch: $(PRECOMPILED_H)
	$(CC) $(CFLAGS) -c -o $@ $<
%.o : %.c | $(PRECOMPILED_H_OBJ)
	$(CC) $(CFLAGS) -include $(PRECOMPILED_H) -c -o $@ $<
```

Time to try it out. Let's go back to our `extra.c` file we had defined above.

```c
// extra.c

#include "stm32f4xx.h"

char *extra(void) {
  return "extra";
}
```

Recall that the inclusion of the `stm32f4xx.h` header caused the build
[time to slow down by \~150 ms](#large-files--slow-builds) for this file.

If we create a `precompiled.h` file with the contents below

```c
// precompiled.h

#include "stm32f4xx.h"

// Add other large headers
```

and compile our `extra.c` file with this included, we go back to our 50 ms
compile time!

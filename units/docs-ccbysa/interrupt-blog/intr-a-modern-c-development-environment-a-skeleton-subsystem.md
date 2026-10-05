---
id: "intr-a-modern-c-development-environment-a-skeleton-subsystem"
type: "concept"
domain: "debug"
title: "A Modern C Development Environment: A skeleton subsystem"
summary: "For this article, we'll create a single .c and .h pair, built using cmake, with a single random number generator function, as follows:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-08-09-a-modern-c-dev-env.md"
doc_source: "https://interrupt.memfault.com/blog/a-modern-c-dev-env#a-skeleton-subsystem"
license: "CC-BY-SA-4.0"
mode: "V"
---

For this article, we'll create a single `.c` and `.h` pair, built using [cmake](https://cmake.org/), with a single random number generator function, as follows:

```bash
$ tree --charset=utf-8 --dirsfirst
.
├── include
│   └── dummy
│       └── dummy.h
├── src
│   └── dummy.c
├── CMakeLists.txt
├── builder.Dockerfile
└── makefile <- this is just our makefile containing the docker commands
```

```c
#include "dummy/dummy.h"
uint8_t dummy_random(void)
{
    return 4U; // determined by fair dice roll.
}
```

I'll spare you the details, the `CMakeLists.txt` simply defines a library named "Dummy" and adds the corresponding files to the library. Have a look at the [example project on GitHub](https://github.com/lmapii/cproject) and its [`CMakeLists.txt`](https://github.com/lmapii/cproject/blob/main/CMakeLists.txt) file. What's important is: This already builds within our development container and `vscode`! Open the integrated terminal in your remote instance and execute `cmake` as follows.

```bash
$ cmake -B build
-- The C compiler identification is GNU 10.2.1
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Configuring done
-- Generating done
-- Build files have been written to: /workspaces/cproject/build
$ cmake --build build
Scanning dependencies of target Dummy
[ 50%] Building C object CMakeFiles/Dummy.dir/src/dummy.c.o
[100%] Linking C static library libDummy.a
[100%] Built target Dummy
```

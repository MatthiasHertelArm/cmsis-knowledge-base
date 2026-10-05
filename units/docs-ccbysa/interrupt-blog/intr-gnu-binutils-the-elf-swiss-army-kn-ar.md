---
id: "intr-gnu-binutils-the-elf-swiss-army-kn-ar"
type: "concept"
domain: "debug"
title: "GNU Binutils: the ELF Swiss Army Knife: GNU Binutil Command Examples / ar"
summary: "ar can be used for building and inspecting static libraries. Large projects will often build subcomponents into static libraries or wind up including a .a provided by a vendor."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-04-08-gnu-binutils.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-binutils#ar"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: GNU Binutil Command Examples_

`ar` can be used for building and inspecting static libraries. Large projects will often build
subcomponents into static libraries or wind up including a `.a` provided by a vendor.

The most typical invocation of `ar` you will see in a project is something like:

```bash
arm-none-eabi-ar rcs mylib.a file1.o file2.o file3.o
```

where:

- `r` - tells `ar` to add the .o files to the archive
- `c` - turns off warnings if a new archive had to be created
- `s` - adds an index section to the archive for faster linking

#### Common Confusion Point

Let's build a simple static library from the following code:

```c
// library.h
#pragma once
void my_library_function(void);
```

```c
// main.c
#include "library.h"

int main (int argc, char *argv[]) {
  my_library_function();
}
```

```c
// lib_v1.c
#include <stdio.h>

#include "library.h"

void my_library_function(void) {
  printf("%s  %s:%d: Version 1\n", __func__, __FILE__, __LINE__);
}
```

To create the static library, `mylib.a`, we run the following:

```bash
$ gcc -c -o lib_v1.o lib_v1.c
$ ar rcs mylib.a lib_v1.o
$ gcc main.c mylib.a
```

Running the application, we see:

```bash
$ ./a.out
my_library_function  lib_v1.c:6: Version 1
```

Now lets "refactor" the code and move our `my_library_function()` to a new file, `lib_v2.c`,
archive it into `mylib.a` and rebuild our final application:

```bash
$ cp lib_v1.c lib_v2.c
$ gcc -c -o lib_v2.o lib_v2.c
$ ar rcs mylib.a lib_v2.o
$ gcc main.c mylib.a
```

##### Pop Quiz: What do you expect to see print?

- A: `my_library_function lib_v1.c:6: Version 1`
- B: `my_library_function lib_v2.c:6: Version 1`

Let's try it out and find out:

```bash
$ ./a.out
my_library_function  lib_v1.c:6: Version 1
```

Interesting, we are seeing the print message from our original implementation which was in
`lib_v1.c` but not the new one from `lib_v2.c`.

We can use the `t` option of `ar` to display the contents of the archive:

```bash
ar t mylib.a
lib_v1.o
lib_v2.o
```

Aha, `lib_v1.o` is still in the archive. We can delete it using the `d` option and recompile:

```bash
$ ar d  mylib.a lib_v1.o
$ gcc main.c mylib.a
```

Now when we run `./a.out`, we see the print message from `lib_v2.c` as we would expect.

```bash
$ ./a.out
my_library_function  lib_v2.c:6: Version 1
```

#### Recreate static libraries to avoid using out-of-date objects

The behavior we observed above is because `ar`, unlike other Binutil commands, _appends_ to a
pre-existing file if it exists. With embedded software, since creating a new archive is very fast,
I recommend just deleting any pre-existing archive when a new one gets generated. For example, we
achieve this in the Make rule below by adding `rm -f $@` before the `ar` invocation:

```bash
$(MYLIB_TARGET): $(MYLIB_OBJ_FILES)
    @echo "Generating $@"
    rm -f $@
    arm-none-eabi-ar rcs $@ $(MYLIB_OBJ_FILES)
```

This way you are guaranteed to not have stale object files in your archive even if you don't do a
full rebuild.

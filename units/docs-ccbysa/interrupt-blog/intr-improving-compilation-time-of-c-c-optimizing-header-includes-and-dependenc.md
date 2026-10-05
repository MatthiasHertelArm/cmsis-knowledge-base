---
id: "intr-improving-compilation-time-of-c-c-optimizing-header-includes-and-dependenc"
type: "concept"
domain: "debug"
title: "Improving Compilation Time of C/C++ Projects: Steps Towards Faster Builds / Optimizing Header Includes and Dependencies"
summary: "This (large) section goes into how to clean up and optimize dependencies between your source files and headers."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-02-11-improving-compilation-times-c-cpp-projects.md"
doc_source: "https://interrupt.memfault.com/blog/improving-compilation-times-c-cpp-projects#optimizing-header-includes-and-dependencies"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Steps Towards Faster Builds_

This (large) section goes into how to clean up and optimize dependencies between
your source files and headers.

#### Large Files = Slow Builds

Generally speaking, the larger the input file into the compiler is, the longer
it will take to compile. If the compiler is fed a file of 10 lines, it might
take 10 ms to compile, but with 5000 lines, it might take 100 ms.

One step that happens before a file is compiled is "preprocessing". A
preprocessor takes all `#include "file.h"` essentially copy-pastes the contents
into each source file, and does this recursively. This means that a `.c` file as
small as the following could wind up being 5000+ lines of code for the compiler!

```c
// extra.c

#include "stm32f4xx.h"

char *extra(void) {
  return "extra";
}
```

We can check the contents of the preprocessed (post-processed) file by calling
`gcc` with the `-E` flag.

```
$ arm-none-eabi-gcc -E -g -Os ... -c src/extra.c > preprocessed.txt
$ cat preprocessed.txt | wc -l
    5397
```

It turns out that the header file `stm32f4xx.h` and all of its transitively
included header files amass into a file of 5398 lines. To put some build numbers
to this result, let's test compiling this small file with and without the
`stm32f4xx.h` header.

```
# Header included
$ time arm-none-eabi-gcc ... -c -o obj/extra.o ./src/extra.c
0.17s user 0.03s system 96% cpu 0.206 total

# Header excluded
$ time arm-none-eabi-gcc ... -c -o obj/extra.o ./src/extra.c
0.03s user 0.02s system 90% cpu 0.053 total
```

This shows that, just by including a single header in our otherwise 3 line `.c`
file, the file went from being built in 50 ms to 200 ms. In the next section
we'll see how easy it is to slow down every compilation due to an accidental or
large included header file.

#### Preventing Dependencies is _hard_

It's incredibly easy to accidentally add a nasty header dependency chain into
your code base. Take for example the file `FreeRTOSConfig.h` in the Amazon AWS
FreeRTOS nRF52840 port,
[linked here](https://github.com/aws/amazon-freertos/blob/e6d2e075e1dfa6729ab818a1b80cdb983b688492/vendors/nordic/boards/nrf52840-dk/aws_demos/config_files/FreeRTOSConfig.h).

That configuration file should have _no external dependencies_. It's also a file
that you should be free to import anywhere and everywhere, as it's small and
self contained, consisting only of macros. However, in this particular nRF52840
port, the `FreeRTOSConfig.h` file has a few extra seemingly innocent imports.

Check out the dependency graph below for the file `FreeRTOSConfig.h` mentioned
above:



  


You can see that, while the `FreeRTOSConfig.h` header should have little to no
dependencies, it ultimately includes 30 other header files along with it.

If we take the FreeRTOS linked list implementation file `FreeRTOS/list.c` and
compile it, it will now include all of those headers mentioned above, which
include the vendor and hardware specific files. A file that should take no more
than 50 ms to compile now takes roughly 500 ms on my machine!

To investigate for yourself which headers are recursively included for a single
`.c` file, you can use GCC's `-MMD` flag to print out intermediate `.d` files
for us during the compilation. These files are usually used as an input to Make
for auto dependency generation[^7], but we can also look at them by hand.

I've published the
[AWS FreeRTOS nRF52830 list.d file](https://gist.github.com/tyhoff/a7028c60f8e0db1a548d3f236967109f)
in a Github Gist.

Next time, before including that extra header file, especially to another header
file, think twice.

#### Find Large Files and Dependency Chains Quickly

To find the largest files after preprocessing, you can pass the CFLAG argument
`-save-temps` to GCC, which will save these intermediate files as `.i` files (it
will also save the result of the assembler as `.s` files). This allows you to
get a rough idea of the largest files that the compiler sees.

My one-liner for this step is to find all `.i` files, run them through `wc -l`
to print out the number of lines, then `sort -r` to sort in descending order.

```
$ find . -name "*.i" | xargs wc -l | sort -rn
   11445 ./stm32f4xx_hal_i2c.i
   11272 ./api_msg.i
   10307 ./api_lib.i
   10206 ./stm32f4xx_hal_tim.i
   10102 ./memp.i
   ...
```

We can also count the number of lines in each `.d` file. This gives us a rough
idea of the `.c` files which include the largest number of header files.

```
$ find . -name "*.d" | xargs wc -l | sort -rn
     110 ./dep/memp.d
     105 ./dep/timeouts.d
     105 ./dep/init.d
      99 ./dep/netif.d
      99 ./dep/api_msg.d
      ...
```

#### Exploring Header Dependency Graphs

Rather than just thinking twice before adding a header file, there are tools
(albeit not great ones) you can use to explore dependency graphs. I won't
explain them here as I have found
[this post by Gernot Klingler on the topic](http://gernotklingler.com/blog/open-source-tools-examine-and-adjust-include-dependencies/)
to be a really good resource on the topic.

The primary way I dig into dependency issues is by investigating GCC's `.d`
files that it produces and look for repeated trees of includes. If you find that
every file in your firmware includes FreeRTOS or standard peripheral headers,
there are probably issues to fix.

One tool I would be wary of using or investing time in is Include What You
Use[^6] \(or IWYU\). I have found that the egregious dependency issues, the ones
that slow down your build by minutes, can usually be fixed by resolving just a
few includes or headers. When running IWYU, it will complain about every file
and will likely hide the root issues. I suggest investigating the `.d` files or
one of the other Graphiz style tools mentioned in the post linked above.

#### Fixing Header Dependency Issues

Speeding up the build by resolving header dependency chains is mostly a
guess-and-check process. You have to try something, do a clean rebuild, and then
compare times or lines of code. I've committed a number of these fixes to
previous projects I've worked on, and I have some tips to share.

1. Don't include headers in your header files (`.h`) that should have been
   included in your `.c` or `.cpp` files.
2. For headers that are included frequently and/or include many other headers,
   consider using forward declarations[^11]. For instance, let's look at the
   following header file.

   ```c
   // settings_file.h

   // Very Large Header File!
   #include "filesystem.h"

   bool settings_file_open(File *file);
   ```

   We are including `filesystem.h` _only_ to have an opaque pointer to a `File`
   defined, but we are paying the price by including such a large file. Since we
   don't need the full internal definition of `File`, we can instead use a
   forward declaration.

   ```c
   // settings_file.h

   typedef struct File File;

   bool settings_file_open(File *file);
   ```

   If you find yourself needing to forward declare this more than once, I
   suggest creating a header file `filesystem_types.h` which contains these
   declarations. Now other files can include this new `_types.h` header instead.

   ```c
   // filesystem_types.h

   typedef struct File File;

   // Other forward declarations
   ```

3. Use [include guards](https://en.wikipedia.org/wiki/Include_guard). I suggest
   using `#pragma once` since it is less error prone and is quite portable[^14].
   The standard C way works too.
4. Wrap third party library code in an abstraction layer so its internal types
   and headers do not leak where they do not belong. Vendors are not in the
   business of clean and quick compiling code, and you shouldn't be at the mercy
   of their bad habits.

On a previous project, the most significant patch I made related to header
dependencies resulted in a compilation speedup of 30%. Before the change, almost
every file in our firmware project had incidentally included the entire set of
our vendor's peripheral library header files, which are usually huge. Each `.c`
file was accidentally including more than 600 headers.

The fix was to create a couple of `..._types.h` files which contained forward
declarations to help break the dependencies between our code and vendor code.

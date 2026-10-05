---
id: "intr-dealing-with-large-symbol-files-compress-debug-info-with-dwz"
type: "concept"
domain: "debug"
title: "Dealing with Large Symbol Files: Compress Debug Info with `dwz`"
summary: "The dwz tool available here (and from many package managers) performs some nice optimizations of DWARF info (the fundamental format of the debug info data)."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-03-30-dealing-with-large-symbol-files.md"
doc_source: "https://interrupt.memfault.com/blog/dealing-with-large-symbol-files#compress-debug-info-with-dwz"
license: "CC-BY-SA-4.0"
mode: "V"
---

The `dwz` tool available [here](https://sourceware.org/dwz/) (and from many
package managers) performs some nice optimizations of DWARF info (the
fundamental format of the debug info data). You can read some more details in
the man page, either by downloading the source and loading it:

```bash
❯ man -l dwz.1
```

Or from one of the many online copies, for example
[Debian Linux](https://manpages.debian.org/testing/dwz/dwz.1.en.html).

Running it on our test binary:

```bash
❯ dwz hello.debug -o hello.debug.dwz
❯ ls -l hello.debug*
-rwxrwxr-x 1 noah noah 42336 Mar  2 12:30 hello.debug
-rwxrwxr-x 1 noah noah 26144 Mar  2 14:11 hello.debug.compressed
-rwxrwxr-x 1 noah noah 42304 Mar  2 14:22 hello.debug.dwz
-rwxrwxr-x 1 noah noah 14568 Mar  2 14:07 hello.debug.stripped
```

Ok, that didn't really improve much 😕 it's possible the debug info for such a
small program is already pretty optimized, or maybe `dwz` doesn't bother
optimizing below a threshold (I haven't checked).

Let's try it again on a large binary, the `cmake` program compiled with
`CMAKE_BUILD_TYPE=Debug`:

```bash
# use dwz to optimize the debug information in 'bin/cmake'
❯ dwz bin/cmake -o cmake.dwz
# use objcopy to compress debug info in the result
❯ objcopy --compress-debug-sections cmake.dwz cmake.dwz.compressed
# and for completeness, also compress debug info in the original cmake file
❯ objcopy --compress-debug-sections bin/cmake cmake.compressed
# let's take a look at file sizes now
❯ ls -lh bin/cmake cmake.dwz cmake.dwz.compressed cmake.compressed
-rwxrwxr-x 1 noah noah 179M Mar  2 14:46 bin/cmake
-rwxrwxr-x 1 noah noah  88M Mar  2 15:45 cmake.compressed
-rwxrwxr-x 1 noah noah 129M Mar  2 14:47 cmake.dwz
-rwxrwxr-x 1 noah noah  70M Mar  2 14:48 cmake.dwz.compressed
```

To summarize:

| Strategy                            | File Size | Size Compared to Base |
| ----------------------------------- | --------- | --------------------- |
| base                                | 179MB     | 100%                  |
| `dwz`                               | 129MB     | 72%                   |
| `--compress-debug-sections`         | 88MB      | 49%                   |
| `dwz` + `--compress-debug-sections` | 70MB      | 39%                   |

I also tested on another large C++ program, and the savings were very
impressive:

```bash
❯ ls -lh program.*
-rwxrwxr-x 1 noah noah 146M Mar  2 16:51 program
-rw-rw-r-- 1 noah noah  66M Mar  2 16:52 program.compressed
-rwxrwxr-x 1 noah noah  37M Mar  2 16:53 program.dwz
-rwxrwxr-x 1 noah noah  16M Mar  2 16:53 program.dwz.compressed
```

146MB for the original binary, down to 16M for the `dwz` and compressed one, or
11% of the original!

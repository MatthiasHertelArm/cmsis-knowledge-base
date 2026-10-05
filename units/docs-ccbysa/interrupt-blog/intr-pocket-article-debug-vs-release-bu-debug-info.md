---
id: "intr-pocket-article-debug-vs-release-bu-debug-info"
type: "concept"
domain: "debug"
title: "Pocket article: Debug vs. Release Builds Considered Harmful: Debug info"
summary: "Debug info (\"debugging information\") is metadata that's included in the output symbol file (typically project.elf/project.out/project.axf, but almost always it's an ELF file)."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-04-25-debug-vs-release-builds.md"
doc_source: "https://interrupt.memfault.com/blog/debug-vs-release-builds#debug-info"
license: "CC-BY-SA-4.0"
mode: "V"
---

Debug info ("debugging information") is metadata that's included in the output
symbol file (typically `project.elf`/`project.out`/`project.axf`, but almost
always it's an ELF file).

This debugging information is placed into the symbol file in "non-loadable"
sections, which means:

- When flashing the symbol file to a device, the debug info is not loaded (it's
  completely ignored)
- When converting the symbol file to a `.bin` or `.hex` format for factory
  programming, the debug info is omitted

Since enabling debug info has no impact on the final loaded executable, the only
downsides to enabling it are:

- _Slightly_ longer build times (can be ~10%, but difficult to measure, and
  negligible if you're using [build caching](https://interrupt.memfault.com/blog/improving-compilation-times-c-cpp-projects)!)
- Much larger symbol file size (can go from approximately the on-target size of
  the program, to many megabytes). This is generally not a problem, except for
  some C++ projects, where the type information can grow dramatically (for
  example, building the Chrome browser with debug info enabled can
  [exceed 4GiB](https://randomascii.wordpress.com/2023/03/08/when-debug-symbols-get-large/)
  ❗)

A quick example demonstrating that compiling with debug info has **zero**
impact on the final program:

```bash
# a simple hello world program
❯ echo > hello.c <<EOF
#include <stdio.h>
int main(void) {
  printf("hello!\n");
  return 0;
}
EOF

# Compile with debug info disabled
❯ gcc -o hello-no-debug hello.c

# Compile it again with debug info enabled
❯ gcc -ggdb3 -o hello-with-debug hello.c

# Run the 'strip' tool to remove all data not part of the program contents.
# Note that we're also removing the (non-loaded) gnu build ID section, because
# the gnu build ID is computed over the program contents AND debug information;
# 'strip' doesn't remove it by default.
# See https://interrupt.memfault.com/blog/reproducible-firmware-builds for
# details!
❯ strip --remove-section=.note.gnu.build-id hello-no-debug hello-with-debug

# compare the two files; they're bit-for-bit identical
❯ diff hello-no-debug hello-with-debug && echo 'identical!'
identical!
```

**Summary: debug info should always be enabled!**

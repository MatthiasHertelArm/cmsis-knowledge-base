---
id: "intr-pocket-article-debugging-ccache-mi-common-problems"
type: "concept"
domain: "debug"
title: "Pocket article: Debugging ccache misses: Common Problems"
summary: "It can be pretty handy to have the build timestamp inserted into the final binary. The downside is this precludes fully reproducible builds 😕."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-10-04-ccache-debugging.md"
doc_source: "https://interrupt.memfault.com/blog/ccache-debugging#common-problems"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Using `__TIME__` / `__DATE__`

It can be pretty handy to have the build timestamp inserted into the final
binary. The downside is this precludes fully reproducible builds 😕.

However, if it's desirable to use these macros in the program, try to isolate
them to a single compilation unit, for example:

```c
// build_time.h

const char *get_build_time(void);
const char *get_build_date(void);
```

```c
// build_time.c
#include "build_time.h"

const char *get_build_time(void) {
  return __TIME__;
}
const char *get_build_date(void) {
  return __DATE__;
}
```

Now instead of a cache miss everywhere that macro is used, there's just a single
miss when compiling `build_time.c` 🥲

If it's undesirable to remove the `__TIME__` etc macros from a library or other
third party code being compiled, but the result is not important, an escape
hatch is to use one of the `ccache` Configuration Options to ignore the macros
when checking for a cache hit:

```bash
❯ CCACHE_SLOPPINESS=time_macros
```

### Generated header files

If a generated header file is used very widely in a build, it can cause a lot of
`ccache` misses. Either rework the system to avoid propagating a generated
header, or take advantage of the `ccache` Configuration Option escape hatch
(note that this one is a little more risky):

```bash
❯ CCACHE_SLOPPINESS=include_file_ctime,include_file_mtime
```

See
<https://ccache.dev/manual/4.6.3.html#_handling_of_newly_created_header_files>

### Build system injected command line options

In the example used in this article, the build system (Makefile) is passing a
random value when compiling `main.c`, which causes a cache miss on every build!

This problem is very situation-specific, but often requires some changes to the
project or build system infrastructure to deal with; in this case, the Makefile
was modified to permit overriding the offending variable when running:

```bash
# override the BUILD_UUID to be a fixed value, for reproducible builds
❯ BUILD_UUID=00000000-0000-0000-0000-000000000000 make
```

Other build systems may permit similar control over dynamic values- it can be
tricky to track them down, so the `ccache` debug log is very helpful here!

### Compiler mtime changes

This problem is pretty niche, but can occur when the compiler itself is freshly
installed, but is the same exact compiler as was used when the cache was last
populated.

For example, if a build is running inside a Docker container, and the GCC
compiler is freshly installed on every build, `ccache` will consider the
compiler to be different.

There are various ways to deal with the problem; probably the most obvious is to
keep the compiler install static, for example by including it inside the Docker
image rather than installing on each build:

```bash
# check the mtime, modified time, for the gcc compiler inside the 'gcc:latest'
# Docker image
❯ docker run --rm -i -t gcc bash -c 'stat $(which gcc)'
  File: /usr/local/bin/gcc
  Size: 1280424         Blocks: 2504       IO Block: 4096   regular file
Device: 2bh/43d Inode: 10651076    Links: 3
Access: (0755/-rwxr-xr-x)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2022-09-13 21:48:19.000000000 +0000
Modify: 2022-09-13 21:48:19.000000000 +0000
Change: 2022-09-30 19:17:16.755951197 +0000
 Birth: 2022-09-30 19:17:16.583945061 +0000
```

If that's not practical, luckily `ccache` has an option for dealing with this
scenario:

```bash
# have ccache use a hash of the compiler itself, instead of mtime of the
# compiler program
❯ CCACHE_COMPILERCHECK=content
```

More details here:

<https://ccache.dev/manual/4.6.3.html#config_compiler_check>

### `__has_include` False Hit

There's a known limitation with `ccache` when using `__has_include` to
optionally include header files- `ccache` is not able to track if the presence
of the optional file changes, and will fetch from the cache as usual. From the
[manual](https://ccache.dev/manual/4.9.1.html#_the_direct_mode):

> There is a catch with the direct mode: header files that were used by the
> compiler are recorded, but header files that were not used, but would have
> been used if they existed, are not. So, when ccache checks if a result can be
> taken from the cache, it currently can’t check if the existence of a new
> header file should invalidate the result. In practice, the direct mode is safe
> to use in the absolute majority of cases.

The workaround I recommend is to set the `CCACHE_NODIRECT=true` setting, which
forces the preprocessor to run before checking for a cache hit.

Since preprocessor invocation should typically be very fast, I just leave this
setting on globally on my development machine (in the relevant shell rc file),
and you can also set it in CI, for example for GitHub actions:

```yaml
env:
  # disable ccache Direct Mode for all jobs
  CCACHE_NODIRECT: true
```









{:.no_toc}

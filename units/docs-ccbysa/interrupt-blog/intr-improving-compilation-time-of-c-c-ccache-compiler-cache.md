---
id: "intr-improving-compilation-time-of-c-c-ccache-compiler-cache"
type: "concept"
domain: "debug"
title: "Improving Compilation Time of C/C++ Projects: Steps Towards Faster Builds / ccache - Compiler Cache"
summary: "ccache[^1] is a compiler cache that speeds up recompilation."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-02-11-improving-compilation-times-c-cpp-projects.md"
doc_source: "https://interrupt.memfault.com/blog/improving-compilation-times-c-cpp-projects#ccache-compiler-cache"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Steps Towards Faster Builds_

> NOTE: This is trivial to set up when using GCC + Make. It might be more
> difficult or impossible with other build systems or compilers.

ccache[^1] is a compiler cache that speeds up recompilation. It compares the
input files and compilation flags to any previous inputs it has previously
compiled, and if there is a match, it will pull the compiled object file from
its cache and provide that instead of recompiling the input. It is useful when
switching branches often and in CI systems where subsequent builds are very
similar. It's not uncommon to see 10x speedups for large projects.

(figure: comparison of compile build times with ccache)

Some people question whether ccache is safe to use in production due to the risk
of an accidental cache hit. The ccache homepage
[covers this topic](https://ccache.dev/).

#### Using ccache

You can use ccache by prefixing the compiler when compiling individual files.

```
$ ccache arm-none-eabi-gcc <args>
```

ccache can be installed in the following ways for each operating system:

- macOS - [Brew](https://formulae.brew.sh/formula/ccache) or
  [Conda](https://anaconda.org/conda-forge/ccache)
- Linux - [Apt](https://launchpad.net/ubuntu/bionic/+package/ccache) or
  [Conda](https://anaconda.org/conda-forge/ccache)
- Windows -
  [Github nagayasu-shinya/ccache-win64](https://github.com/nagayasu-shinya/ccache-win64)

I suggest against the commonly suggested way of symlinking your compilers to the
`ccache` binary and instead to set up your build system in the following way:

```make
ARM_CC    ?= arm-none-eabi-gcc
CC_PREFIX ?= ccache
CC        ?= $(CC_PREFIX) $(ARM_CC)

%.o : %.c
	$(CC) $(CFLAGS) -c -o $@ $<
```

With this setup, your environment remains simple and developers only need to
install ccache with no further setup.

You can easily check whether ccache is set up properly using the following steps
and verifying there are "cache hits".

```
# This initial build with populate the cache
$ make
...

# Clear ccache stats
$ ccache --zero-stats

# Run the build again (most artifacts should be cached)
$ make clean && make
...

# Ensure ccache had some hits
$ ccache --show-stats
cache directory                     /Users/tyler/.ccache
primary config                      /Users/tyler/.ccache/ccache.conf
secondary config      (readonly)    /usr/local/Cellar/ccache/3.7.3/etc/ccache.conf
stats updated                       Mon Feb 10 23:24:26 2020
stats zeroed                        Mon Feb 10 23:24:18 2020
cache hit (direct)                     0
cache hit (preprocessed)              75
cache miss                             0
cache hit rate                    100.00 %
called for link                        4
can't use precompiled header           1
cleanups performed                     0
files in cache                      8521
cache size                         197.0 MB
max cache size                       5.0 GB
```

As you can see above, I had a 100% cache hit rate on a rebuild!

> If you have a substantially large project, I've heard good things about
> icecc[^2] and sccache[^3], but these are generally for projects with thousands
> of large files and many developers.

---
id: "intr-pocket-article-debugging-ccache-mi-diagnosing-cache-misses"
type: "concept"
domain: "debug"
title: "Pocket article: Debugging ccache misses: Diagnosing cache misses"
summary: "The first step in dealing with ccache misses is identifying the cause of the misses. There's three levels of debug techniques I use here:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-10-04-ccache-debugging.md"
doc_source: "https://interrupt.memfault.com/blog/ccache-debugging#diagnosing-cache-misses"
license: "CC-BY-SA-4.0"
mode: "V"
---

The first step in dealing with `ccache` misses is identifying the cause of the
misses. There's three levels of debug techniques I use here:

### 1. Measure total cache misses

> Note: the example program and Makefile used in this article can be found in
> GitHub here:
> <https://github.com/memfault/interrupt/tree/master/example/ccache-debugging>

`ccache` keeps track of cache hits + misses, which can be viewed by running
`ccache -s` (or `ccache -sv` for more verbose output). When measuring cache
misses, first run `ccache -z` to zero out the stats, then run the build being
measured, then run `ccache -sv` to see the cache hit rate:

```bash
❯ ccache -sv
Summary:
  Cache directory:    /home/noah/.cache/ccache
  Primary config:     /home/noah/.config/ccache/ccache.conf
  Secondary config:   /usr/local/etc/ccache.conf
  Stats updated:      Fri Sep 30 14:30:03 2022
  Hits:                  550 /  998 (55.11 %)
    Direct:              550 /  998 (55.11 %)
    Preprocessed:          0 /  448 (0.00 %)
  Misses:                448
    Direct:              448
    Preprocessed:        448
  Uncacheable:             2
Primary storage:
  Hits:                 1100 / 1996 (55.11 %)
  Misses:                896
  Cache size (GB):      4.64 / 5.00 (92.80 %)
  Files:              127188
  Cleanups:                1
Uncacheable:
  Called for linking:      2
```

In the above example, the hit rate is about 55%, which is pretty poor. It's nice
to have zero cache misses when possible! But often there's a few compilation
steps that use dynamic content and aren't practical to cache- in a large build,
having a few non-cached compilations is usually not too critical.

### 2. Identify objects that are missing the cache

The `ccache` manual does a good job of describing this process in the section
here:

<https://ccache.dev/manual/4.6.3.html#_cache_debugging>

The workflow I use is something like this:

```bash
# run the build command, outputting the ccache debug data into a folder named
# "ccache-debug-1":
❯ CCACHE_DEBUG=1 CCACHE_DEBUGDIR=ccache-debug-1 make
# clean the build
❯ make clean
# run the build command again, outputting ccache debug data into a different
# folder, "ccache-debug-2"
❯ CCACHE_DEBUG=1 CCACHE_DEBUGDIR=ccache-debug-2 make
```

Now there's 2 sets of ccache debug data. Then I run this command to remove some
of the extra output to make it easier to debug (this is just one technique;
using a diff tool with filename filters would be another way):

```bash
# remove all but the *.ccache-input-text ccache debug files
❯ find . \( -name '*.ccache-input-[cdp]' -o -name '*.ccache-log' \) -exec rm {} \;
```

Then I use a directory diff tool, of which there are a lot of options-
personally I use `meld`:

```bash
❯ meld ccache-debug-1 ccache-debug-2
```





Using `diff`, the output looks like this:

```diff
❯ diff -dur ccache-debug-1 ccache-debug-2
diff --color -dur ccache-debug-1/home/noah/dev/memfault/interrupt/example/ccache-debugging/main.o.ccache-input-text ccache-debug-2/home/noah/dev/memfault/interrupt/example/ccache-debugging/main.o.ccache-input-text
--- ccache-debug-1/home/noah/dev/memfault/interrupt/example/ccache-debugging/main.o.ccache-input-text   2022-09-30 14:48:11.301685115 -0400
+++ ccache-debug-2/home/noah/dev/memfault/interrupt/example/ccache-debugging/main.o.ccache-input-text   2022-09-30 14:48:15.333828955 -0400
@@ -15,7 +15,7 @@
 ### manifest version
 2
 ### arg
--DBUILD_UUID="0fb1039e-3cb7-4761-a3a1-7cb0d87c48ad"
+-DBUILD_UUID="ba796adf-7946-41e9-a295-919c0a785d94"
 ### inputfile
 main.c
 ### sourcecode
@@ -1022,8 +1022,8 @@
 int main(int argc, char **argv) {
   (void)argc, (void)argv;

-  printf("%s\n", "0fb1039e-3cb7-4761-a3a1-7cb0d87c48ad");
-  printf("%s : %s\n", "Sep 30 2022", "14:48:11");
+  printf("%s\n", "ba796adf-7946-41e9-a295-919c0a785d94");
+  printf("%s : %s\n", "Sep 30 2022", "14:48:15");

   return 0;
 }
```

From this, we can see that there's a compiler argument, `-DBUILD_UUID`, that
changed from the first build to the second, and caused the cache miss.

We can also see there's a timestamp that changed from the first build to the
second.

### 3. Detailed examination of the ccache debug log

`ccache` in debug mode will spit out a detailed debug log. If the simple diff
technique above doesn't uncover the issue, digging through the log of a miss
should show the problem, though it's a bit more tedious.

To find `ccache` debug log files with cache misses, I use the following
`ripgrep` command:

```bash
❯ rg --no-ignore 'Result: .*_miss'
ccache-debug-1/home/noah/dev/memfault/interrupt/example/ccache-debugging/main.o.ccache-log
65:[2022-09-30T14:58:02.545438 137617] Result: cache_miss
66:[2022-09-30T14:58:02.545440 137617] Result: direct_cache_miss
67:[2022-09-30T14:58:02.545441 137617] Result: preprocessed_cache_miss
68:[2022-09-30T14:58:02.545443 137617] Result: primary_storage_miss
```

Opening up that log file, we can see some interesting entries below:

```log
[2022-09-30T14:58:02.527849 137617] Command line: ccache cc -DBUILD_UUID="00000000-0000-0000-0000-000000000000" -c main.c -o main.o
[2022-09-30T14:58:02.527854 137617] Hostname: thinkpad-x13
[2022-09-30T14:58:02.527856 137617] Working directory: /home/noah/dev/memfault/interrupt/example/ccache-debugging
[2022-09-30T14:58:02.527857 137617] Compiler type: gcc
[2022-09-30T14:58:02.527878 137617] Source file: main.c
[2022-09-30T14:58:02.527880 137617] Object file: main.o
[2022-09-30T14:58:02.528061 137617] Trying direct lookup
[2022-09-30T14:58:02.528074 137617] Found __DATE__ in main.c
[2022-09-30T14:58:02.528076 137617] Found __TIME__ in main.c
[2022-09-30T14:58:02.528078 137617] Disabling direct mode
[2022-09-30T14:58:02.528112 137617] Running preprocessor
[2022-09-30T14:58:02.528115 137617] Executing /usr/bin/cc -DBUILD_UUID="00000000-0000-0000-0000-000000000000" -E main.c
[2022-09-30T14:58:02.533521 137617] Include file generated_header.h too new
[2022-09-30T14:58:02.533552 137617] Got result key from preprocessor
[2022-09-30T14:58:02.533576 137617] No 33a3eri78s7c31pfvspaj5g3e4o9g2q78 in primary storage
[2022-09-30T14:58:02.533581 137617] Running real compiler
[2022-09-30T14:58:02.533600 137617] Executing /usr/bin/cc -DBUILD_UUID="00000000-0000-0000-0000-000000000000" -c -fdiagnostics-color -o main.o main.c
[2022-09-30T14:58:02.545265 137617] Using default compression level 1
[2022-09-30T14:58:02.545320 137617] Storing result file main.o
[2022-09-30T14:58:02.545324 137617] Storing embedded file #0 .o (1736 bytes) from main.o
[2022-09-30T14:58:02.545417 137617] Stored 33a3eri78s7c31pfvspaj5g3e4o9g2q78 in primary storage (/home/noah/.cache/ccache/3/3/a3eri78s7c31pfvspaj5g3e4o9g2q78R)
[2022-09-30T14:58:02.545438 137617] Result: cache_miss
[2022-09-30T14:58:02.545440 137617] Result: direct_cache_miss
[2022-09-30T14:58:02.545441 137617] Result: preprocessed_cache_miss
[2022-09-30T14:58:02.545443 137617] Result: primary_storage_miss
```

Some notable log messages:

1. `Found __DATE__ in main.c` : this disables "direct" cache mode
2. `Include file generated_header.h too new` : this also disables "direct" mode

Dealing with those problems (see below for the strategies) and re-running
results in a successful cache hit 🎉, with this debug log entry:

```log
5:04:39.975549 141290] Command line: ccache cc -DBUILD_UUID="00000000-0000-0000-0000-000000000000" -c main.c -o main.o
[2022-09-30T15:04:39.975554 141290] Hostname: thinkpad-x13
[2022-09-30T15:04:39.975555 141290] Working directory: /home/noah/dev/memfault/interrupt/example/ccache-debugging
[2022-09-30T15:04:39.975557 141290] Compiler type: gcc
[2022-09-30T15:04:39.975580 141290] Source file: main.c
[2022-09-30T15:04:39.975582 141290] Object file: main.o
[2022-09-30T15:04:39.975661 141290] Trying direct lookup
[2022-09-30T15:04:39.975692 141290] Retrieved 9727fqbvqefb749v8pop2k8o8a9tbsf78 from primary storage (/home/noah/.cache/ccache/9/7/27fqbvqefb749v8pop2k8o8a9tbsf78M)
[2022-09-30T15:04:39.975700 141290] Looking for result key in /home/noah/.cache/ccache/9/7/27fqbvqefb749v8pop2k8o8a9tbsf78M
[2022-09-30T15:04:39.976110 141290] Got result key from manifest
[2022-09-30T15:04:39.976128 141290] Retrieved 0425ht0hb4kn2n7ubfv5stesqrgc4m3e4 from primary storage (/home/noah/.cache/ccache/0/4/25ht0hb4kn2n7ubfv5stesqrgc4m3e4R)
[2022-09-30T15:04:39.976136 141290] Reading result /home/noah/.cache/ccache/0/4/25ht0hb4kn2n7ubfv5stesqrgc4m3e4R
[2022-09-30T15:04:39.976295 141290] Reading embedded entry #0 .o (1736 bytes)
[2022-09-30T15:04:39.976298 141290] Writing to main.o
[2022-09-30T15:04:39.976326 141290] Succeeded getting cached result
[2022-09-30T15:04:39.976330 141290] Result: direct_cache_hit
[2022-09-30T15:04:39.976332 141290] Result: primary_storage_hit
```

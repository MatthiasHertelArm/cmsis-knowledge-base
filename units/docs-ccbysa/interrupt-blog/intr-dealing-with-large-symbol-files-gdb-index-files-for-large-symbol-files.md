---
id: "intr-dealing-with-large-symbol-files-gdb-index-files-for-large-symbol-files"
type: "concept"
domain: "debug"
title: "Dealing with Large Symbol Files: GDB Index Files for Large Symbol Files"
summary: "Something you may notice when manipulating large binaries in GDB: lots of operations are slowwww, including the initial load. Fortunately, there's an easy way to speed this up: pre-generate the GDB index."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-03-30-dealing-with-large-symbol-files.md"
doc_source: "https://interrupt.memfault.com/blog/dealing-with-large-symbol-files#gdb-index-files-for-large-symbol-files"
license: "CC-BY-SA-4.0"
mode: "V"
---

Something you may notice when manipulating large binaries in GDB: lots of
operations are slowwww, including the initial load. Fortunately, there's an easy
way to speed this up: pre-generate the GDB index.

For the cmake executable, this works like so:

```bash
❯ cp bin/cmake bin/cmake.gdbindex
❯ gdb-add-index bin/cmake.gdbindex
# let's take a look at file sizes:
❯ ls -lh bin/cmake*
-rwxrwxr-x 1 noah noah 179M Mar  2 14:46 bin/cmake
-rwxrwxr-x 1 noah noah 203M Mar  2 17:44 bin/cmake.gdbindex
# 😓 ouch, that added a lot to the file size
```

Now benchmarking the speed at which gdb can load the files:

```bash
❯ hyperfine 'gdb -batch -ex quit bin/cmake' 'gdb -batch -ex quit bin/cmake.gdbindex'
Benchmark 1: gdb -batch -ex quit bin/cmake
  Time (mean ± σ):      4.105 s ±  0.045 s    [User: 4.814 s, System: 0.146 s]
  Range (min … max):    4.040 s …  4.193 s    10 runs

Benchmark 2: gdb -batch -ex quit bin/cmake.gdbindex
  Time (mean ± σ):      1.046 s ±  0.023 s    [User: 1.847 s, System: 0.128 s]
  Range (min … max):    1.013 s …  1.079 s    10 runs

Summary
  'gdb -batch -ex quit bin/cmake.gdbindex' ran
    3.93 ± 0.09 times faster than 'gdb -batch -ex quit bin/cmake'
```

😮 impressive speed up! It's somewhat of a niche operation to optimize for, but
since it's part of the edit-compile-test loop, it could be worth doing.

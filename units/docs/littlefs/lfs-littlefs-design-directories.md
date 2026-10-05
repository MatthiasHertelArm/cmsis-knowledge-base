---
id: "lfs-littlefs-design-directories"
type: "concept"
domain: "project"
title: "littlefs DESIGN: Directories"
summary: "Now we just need directories to store our files. As mentioned above we want a strict binding of directories and metadata pairs, but there are a few complications we need to sort out."
status: "draft"
collection: "littlefs"
source: "littlefs-project/littlefs@6cb4e86:DESIGN.md"
doc_source: "https://github.com/littlefs-project/littlefs/blob/6cb4e86/DESIGN.md#directories"
license: "BSD-3-Clause"
mode: "V"
---

Now we just need directories to store our files. As mentioned above we want
a strict binding of directories and metadata pairs, but there are a few
complications we need to sort out.

On their own, each directory is a linked-list of metadata pairs. This lets us
store an unlimited number of files in each directory, and we don't need to
worry about the runtime complexity of unbounded logs. We can store other
directory pointers in our metadata pairs, which gives us a directory tree, much
like what you find on other filesystems.

```
            .--------.
           .| root   |
           ||        |
           ||        |
           |'--------'
           '---|--|-'
            .-'    '-------------------------.
           v                                  v
      .--------.        .--------.        .--------.
     .| dir A  |------->| dir A  |       .| dir B  |
     ||        |       ||        |       ||        |
     ||        |       ||        |       ||        |
     |'--------'       |'--------'       |'--------'
     '---|--|-'        '----|---'        '---|--|-'
      .-'    '-.            |             .-'    '-.
     v          v           v            v          v
.--------.  .--------.  .--------.  .--------.  .--------.
| file C |  | file D |  | file E |  | file F |  | file G |
|        |  |        |  |        |  |        |  |        |
|        |  |        |  |        |  |        |  |        |
'--------'  '--------'  '--------'  '--------'  '--------'
```

The main complication is, once again, traversal with a constant amount of
[RAM]. The directory tree is a tree, and the unfortunate fact is you can't
traverse a tree with constant RAM.

Fortunately, the elements of our tree are metadata pairs, so unlike CTZ
skip-lists, we're not limited to strict COW operations. One thing we can do is
thread a linked-list through our tree, explicitly enabling cheap traversal
over the entire filesystem.

```
            .--------.
           .| root   |-.
           ||        | |
   .-------||        |-'
   |       |'--------'
   |       '---|--|-'
   |        .-'    '-------------------------.
   |       v                                  v
   |  .--------.        .--------.        .--------.
   '->| dir A  |------->| dir A  |------->| dir B  |
     ||        |       ||        |       ||        |
     ||        |       ||        |       ||        |
     |'--------'       |'--------'       |'--------'
     '---|--|-'        '----|---'        '---|--|-'
      .-'    '-.            |             .-'    '-.
     v          v           v            v          v
.--------.  .--------.  .--------.  .--------.  .--------.
| file C |  | file D |  | file E |  | file F |  | file G |
|        |  |        |  |        |  |        |  |        |
|        |  |        |  |        |  |        |  |        |
'--------'  '--------'  '--------'  '--------'  '--------'
```

Unfortunately, not sticking to pure COW operations creates some problems. Now,
whenever we want to manipulate the directory tree, multiple pointers need to be
updated. If you're familiar with designing atomic data structures this should
set off a bunch of red flags.

To work around this, our threaded linked-list has a bit of leeway. Instead of
only containing metadata pairs found in our filesystem, it is allowed to
contain metadata pairs that have no parent because of a power loss. These are
called orphaned metadata pairs.

With the possibility of orphans, we can build power loss resilient operations
that maintain a filesystem tree threaded with a linked-list for traversal.

Adding a directory to our tree:

```
         .--------.
        .| root   |-.
        ||        | |
.-------||        |-'
|       |'--------'
|       '---|--|-'
|        .-'    '-.
|       v          v
|  .--------.  .--------.
'->| dir A  |->| dir C  |
  ||        | ||        |
  ||        | ||        |
  |'--------' |'--------'
  '--------'  '--------'

allocate dir B
=>
         .--------.
        .| root   |-.
        ||        | |
.-------||        |-'
|       |'--------'
|       '---|--|-'
|        .-'    '-.
|       v          v
|  .--------.    .--------.
'->| dir A  |--->| dir C  |
  ||        | .->|        |
  ||        | | ||        |
  |'--------' | |'--------'
  '--------'  | '--------'
              |
   .--------. |
  .| dir B  |-'
  ||        |
  ||        |
  |'--------'
  '--------'

insert dir B into threaded linked-list, creating an orphan
=>
         .--------.
        .| root   |-.
        ||        | |
.-------||        |-'
|       |'--------'
|       '---|--|-'
|        .-'    '-------------.
|       v                      v
|  .--------.  .--------.  .--------.
'->| dir A  |->| dir B  |->| dir C  |
  ||        | || orphan!| ||        |
  ||        | ||        | ||        |
  |'--------' |'--------' |'--------'
  '--------'  '--------'  '--------'

add dir B to parent directory
=>
               .--------.
              .| root   |-.
              ||        | |
.-------------||        |-'
|             |'--------'
|             '--|-|-|-'
|        .------'  |  '-------.
|       v          v           v
|  .--------.  .--------.  .--------.
'->| dir A  |->| dir B  |->| dir C  |
  ||        | ||        | ||        |
  ||        | ||        | ||        |
  |'--------' |'--------' |'--------'
  '--------'  '--------'  '--------'
```

Removing a directory:

```
               .--------.
              .| root   |-.
              ||        | |
.-------------||        |-'
|             |'--------'
|             '--|-|-|-'
|        .------'  |  '-------.
|       v          v           v
|  .--------.  .--------.  .--------.
'->| dir A  |->| dir B  |->| dir C  |
  ||        | ||        | ||        |
  ||        | ||        | ||        |
  |'--------' |'--------' |'--------'
  '--------'  '--------'  '--------'

remove dir B from parent directory, creating an orphan
=>
         .--------.
        .| root   |-.
        ||        | |
.-------||        |-'
|       |'--------'
|       '---|--|-'
|        .-'    '-------------.
|       v                      v
|  .--------.  .--------.  .--------.
'->| dir A  |->| dir B  |->| dir C  |
  ||        | || orphan!| ||        |
  ||        | ||        | ||        |
  |'--------' |'--------' |'--------'
  '--------'  '--------'  '--------'

remove dir B from threaded linked-list, returning dir B to free blocks
=>
         .--------.
        .| root   |-.
        ||        | |
.-------||        |-'
|       |'--------'
|       '---|--|-'
|        .-'    '-.
|       v          v
|  .--------.  .--------.
'->| dir A  |->| dir C  |
  ||        | ||        |
  ||        | ||        |
  |'--------' |'--------'
  '--------'  '--------'
```

In addition to normal directory tree operations, we can use orphans to evict
blocks in a metadata pair when the block goes bad or exceeds its allocated
erases. If we lose power while evicting a metadata block we may end up with
a situation where the filesystem references the replacement block while the
threaded linked-list still contains the evicted block. We call this a
half-orphan.

```
               .--------.
              .| root   |-.
              ||        | |
.-------------||        |-'
|             |'--------'
|             '--|-|-|-'
|        .------'  |  '-------.
|       v          v           v
|  .--------.  .--------.  .--------.
'->| dir A  |->| dir B  |->| dir C  |
  ||        | ||        | ||        |
  ||        | ||        | ||        |
  |'--------' |'--------' |'--------'
  '--------'  '--------'  '--------'

try to write to dir B
=>
                  .--------.
                 .| root   |-.
                 ||        | |
.----------------||        |-'
|                |'--------'
|                '-|-||-|-'
|        .--------'  ||  '-----.
|       v            |v         v
|  .--------.     .--------.  .--------.
'->| dir A  |---->| dir B  |->| dir C  |
  ||        |-.   |        | ||        |
  ||        | |   |        | ||        |
  |'--------' |   '--------' |'--------'
  '--------'  |      v       '--------'
              |  .--------.
              '->| dir B  |
                 | bad    |
                 | block! |
                 '--------'

oh no! bad block detected, allocate replacement
=>
                  .--------.
                 .| root   |-.
                 ||        | |
.----------------||        |-'
|                |'--------'
|                '-|-||-|-'
|        .--------'  ||  '-------.
|       v            |v           v
|  .--------.     .--------.    .--------.
'->| dir A  |---->| dir B  |--->| dir C  |
  ||        |-.   |        | .->|        |
  ||        | |   |        | | ||        |
  |'--------' |   '--------' | |'--------'
  '--------'  |      v       | '--------'
              |  .--------.  |
              '->| dir B  |  |
                 | bad    |  |
                 | block! |  |
                 '--------'  |
                             |
                 .--------.  |
                 | dir B  |--'
                 |        |
                 |        |
                 '--------'

insert replacement in threaded linked-list, creating a half-orphan
=>
                  .--------.
                 .| root   |-.
                 ||        | |
.----------------||        |-'
|                |'--------'
|                '-|-||-|-'
|        .--------'  ||  '-------.
|       v            |v           v
|  .--------.     .--------.    .--------.
'->| dir A  |---->| dir B  |--->| dir C  |
  ||        |-.   |        | .->|        |
  ||        | |   |        | | ||        |
  |'--------' |   '--------' | |'--------'
  '--------'  |      v       | '--------'
              |  .--------.  |
              |  | dir B  |  |
              |  | bad    |  |
              |  | block! |  |
              |  '--------'  |
              |              |
              |  .--------.  |
              '->| dir B  |--'
                 | half   |
                 | orphan!|
                 '--------'

fix reference in parent directory
=>
               .--------.
              .| root   |-.
              ||        | |
.-------------||        |-'
|             |'--------'
|             '--|-|-|-'
|        .------'  |  '-------.
|       v          v           v
|  .--------.  .--------.  .--------.
'->| dir A  |->| dir B  |->| dir C  |
  ||        | ||        | ||        |
  ||        | ||        | ||        |
  |'--------' |'--------' |'--------'
  '--------'  '--------'  '--------'
```

Finding orphans and half-orphans is expensive, requiring a _O(n²)_
comparison of every metadata pair with every directory entry. But the tradeoff
is a power resilient filesystem that works with only a bounded amount of RAM.
Fortunately, we only need to check for orphans on the first allocation after
boot, and a read-only littlefs can ignore the threaded linked-list entirely.

If we only had some sort of global state, then we could also store a flag and
avoid searching for orphans unless we knew we were specifically interrupted
while manipulating the directory tree (foreshadowing!).

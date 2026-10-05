---
id: "lfs-littlefs-readme-design"
type: "concept"
domain: "project"
title: "littlefs README: Design"
summary: "At a high level, littlefs is a block based filesystem that uses small logs to store metadata and larger copy-on-write (COW) structures to store file data."
status: "draft"
collection: "littlefs"
source: "littlefs-project/littlefs@6cb4e86:README.md"
doc_source: "https://github.com/littlefs-project/littlefs/blob/6cb4e86/README.md#design"
license: "BSD-3-Clause"
mode: "V"
---

At a high level, littlefs is a block based filesystem that uses small logs to
store metadata and larger copy-on-write (COW) structures to store file data.

In littlefs, these ingredients form a sort of two-layered cake, with the small
logs (called metadata pairs) providing fast updates to metadata anywhere on
storage, while the COW structures store file data compactly and without any
wear amplification cost.

Both of these data structures are built out of blocks, which are fed by a
common block allocator. By limiting the number of erases allowed on a block
per allocation, the allocator provides dynamic wear leveling over the entire
filesystem.

```
                    root
                   .--------.--------.
                   | A'| B'|         |
                   |   |   |->       |
                   |   |   |         |
                   '--------'--------'
                .----'   '--------------.
       A       v                 B       v
      .--------.--------.       .--------.--------.
      | C'| D'|         |       | E'|new|         |
      |   |   |->       |       |   | E'|->       |
      |   |   |         |       |   |   |         |
      '--------'--------'       '--------'--------'
      .-'   '--.                  |   '------------------.
     v          v              .-'                        v
.--------.  .--------.        v                       .--------.
|   C    |  |   D    |   .--------.       write       | new E  |
|        |  |        |   |   E    |        ==>        |        |
|        |  |        |   |        |                   |        |
'--------'  '--------'   |        |                   '--------'
                         '--------'                   .-'    |
                         .-'    '-.    .-------------|------'
                        v          v  v              v
                   .--------.  .--------.       .--------.
                   |   F    |  |   G    |       | new F  |
                   |        |  |        |       |        |
                   |        |  |        |       |        |
                   '--------'  '--------'       '--------'
```

More details on how littlefs works can be found in [DESIGN.md](https://github.com/littlefs-project/littlefs/blob/6cb4e86/DESIGN.md) and
[SPEC.md](https://github.com/littlefs-project/littlefs/blob/6cb4e86/SPEC.md).

- [DESIGN.md](https://github.com/littlefs-project/littlefs/blob/6cb4e86/DESIGN.md) - A fully detailed dive into how littlefs works.
  I would suggest reading it as the tradeoffs at work are quite interesting.

- [SPEC.md](https://github.com/littlefs-project/littlefs/blob/6cb4e86/SPEC.md) - The on-disk specification of littlefs with all the
  nitty-gritty details. May be useful for tooling development.

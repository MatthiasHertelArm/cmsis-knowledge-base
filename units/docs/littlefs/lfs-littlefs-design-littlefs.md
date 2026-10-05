---
id: "lfs-littlefs-design-littlefs"
type: "concept"
domain: "project"
title: "littlefs DESIGN: littlefs"
summary: "If we look at existing filesystems, there are two interesting design patterns that stand out, but each have their own set of problems. Logging, which provides independent atomicity, has poor runtime performance."
status: "draft"
collection: "littlefs"
source: "littlefs-project/littlefs@6cb4e86:DESIGN.md"
doc_source: "https://github.com/littlefs-project/littlefs/blob/6cb4e86/DESIGN.md#littlefs"
license: "BSD-3-Clause"
mode: "V"
---

So what does littlefs do?

If we look at existing filesystems, there are two interesting design patterns
that stand out, but each have their own set of problems. Logging, which
provides independent atomicity, has poor runtime performance. And COW data
structures, which perform well, push the atomicity problem upwards.

Can we work around these limitations?

Consider logging. It has either a _O(n²)_ runtime or _O(n)_ RAM cost. We
can't avoid these costs, _but_ if we put an upper bound on the size we can at
least prevent the theoretical cost from becoming problem. This relies on the
super secret computer science hack where you can pretend any algorithmic
complexity is _O(1)_ by bounding the input.

In the case of COW data structures, we can try twisting the definition a bit.
Let's say that our COW structure doesn't copy after a single write, but instead
copies after _n_ writes. This doesn't change most COW properties (assuming you
can write atomically!), but what it does do is prevent the upward motion of
wear. This sort of copy-on-bounded-writes (CObW) still focuses wear, but at
each level we divide the propagation of wear by _n_. With a sufficiently
large _n_ (> branching factor) wear propagation is no longer a problem.

See where this is going? Separate, logging and COW are imperfect solutions and
have weaknesses that limit their usefulness. But if we merge the two they can
mutually solve each other's limitations.

This is the idea behind littlefs. At the sub-block level, littlefs is built
out of small, two block logs that provide atomic updates to metadata anywhere
on the filesystem. At the super-block level, littlefs is a CObW tree of blocks
that can be evicted on demand.

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

There are still some minor issues. Small logs can be expensive in terms of
storage, in the worst case a small log costs 4x the size of the original data.
CObW structures require an efficient block allocator since allocation occurs
every _n_ writes. And there is still the challenge of keeping the RAM usage
constant.

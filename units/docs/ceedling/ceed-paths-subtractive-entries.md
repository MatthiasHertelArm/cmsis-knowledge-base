---
id: "ceed-paths-subtractive-entries"
type: "concept"
domain: "test"
title: "`:paths`: Subtractive entries"
summary: "Globs are super duper helpful when you have many paths to list. But, what if a single glob gets you 20 nested paths, but you actually want to exclude 2 of those paths?"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/paths.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/paths/#subtractive-entries"
license: "MIT"
mode: "V"
---

Globs are super duper helpful when you have many paths to list. But, what if a
single glob gets you 20 nested paths, but you actually want to exclude 2 of
those paths?

Must you revert to listing all 18 paths individually? No, my friend, we've got
you. Behold, subtractive paths.

Put simply, with an optional preceding decorator `-:`, you can instruct Ceedling
to remove certain directory paths from a collection after it builds that
collection.

By default, paths are additive. For pretty alignment in your YAML, you may also
use `+:`, but strictly speaking, it’s not necessary.

Subtractive paths may be simple paths or globs just like any other path entry.

!!! note "Subtractive paths resolve after all mixins merge"
    The resolution of subtractive paths happens after your full paths lists are
    assembled. So, if you use `:paths` entries in Mixins to build up your
    project configuration, subtractive paths will only be processed after the
    final mixin is merged. That is, you can merge in additive and subtractive
    paths with Mixins to your heart’s content. The subtractive paths are not
    removed until all Mixins have been merged.

[GCC]: https://gcc.gnu.org
[inline-ruby-string-expansion]: ../project-file.md#inline-ruby-string-expansion

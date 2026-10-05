---
id: "ceed-files-subtractive-files-entries"
type: "concept"
domain: "test"
title: "`:files`: Subtractive `:files` entries"
summary: "Tailoring a file collection includes adding to it but also subtracting from it."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/files.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/files/#subtractive-files-entries"
license: "MIT"
mode: "V"
---

Tailoring a file collection includes adding to it but also subtracting from it.

Put simply, with an optional preceding decorator `-:`, you can instruct Ceedling
to remove certain file paths from a collection after it builds that collection.

By default, paths are additive. For pretty alignment in your YAML, you may also
use `+:`, but strictly speaking, it’s not necessary.

Subtractive paths may be simple paths or globs just like any other path entry.

See the [example section](#advanced-tailoring).


[globs-tutorial]: http://ruby.about.com/od/beginningruby/a/dir2.htm
[ruby-globs]: https://ruby-doc.org/core-3.0.0/Dir.html#method-c-glob
[inline-ruby-string-expansion]: ../project-file.md#inline-ruby-string-expansion

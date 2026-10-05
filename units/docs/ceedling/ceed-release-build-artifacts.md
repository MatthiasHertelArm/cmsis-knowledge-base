---
id: "ceed-release-build-artifacts"
type: "concept"
domain: "test"
title: "`:release_build`: `:artifacts`"
summary: "By default, Ceedling copies to the <build path>/artifacts/release directory the output of the release linker and (optionally) a map file. Many toolchains produce other important output files as well."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/release-build.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/release-build/#artifacts"
license: "MIT"
mode: "V"
---

By default, Ceedling copies to the _<build path>/artifacts/release_
directory the output of the release linker and (optionally) a map
file. Many toolchains produce other important output files as well.
Adding a file path to this list will cause Ceedling to copy that file
to the artifacts directory.

The artifacts directory is helpful for organizing important build
output files and provides a central place for tools such as Continuous
Integration servers to point to build output. Selectively copying
files prevents incidental build cruft from needlessly appearing in the
artifacts directory.

Note that [inline Ruby string expansion][inline-ruby-string-expansion]
is available in artifact paths.

**Default**: `[]` (empty)

[inline-ruby-string-expansion]: ../project-file.md#inline-ruby-string-expansion

---
id: "ceed-dependencies-artifacts"
type: "concept"
domain: "test"
title: "Dependencies: Artifacts"
summary: "These are the outputs of the build process. There are there types of artifacts. Any dependency may have none or some of these. Calling out these files tells Ceedling that they are important."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/dependencies.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/dependencies/#artifacts"
license: "MIT"
mode: "V"
---

These are the outputs of the build process. There are there types of artifacts. Any dependency
may have none or some of these. Calling out these files tells Ceedling that they are important.
Your dependency’s build process may produce many other files... but these are the files that
Ceedling understands it needs to act on.

### `static_libraries`

Specifying one or more static libraries will tell Ceedling where it should find static libraries
output by your build process. These libraries are automatically added to the list of dependencies
and will be linked with the rest of your code to produce the final release.

If any of these libraries don't exist, Ceedling will trigger your build process in order for it
to produce them.

### `dynamic_libraries`

Specifying one or more dynamic libraries will tell Ceedling where it should find dynamic libraries
output by your build process. These libraries are automatically copied to the same folder as your
final release binary.

If any of these libraries don't exist, Ceedling will trigger your build process in order for it
to produce them.

### `includes`

Often when libraries are built, the same process will output a collection of includes so that
your release code knows how to interact with that library. It’s the public API for that library.
By specifying the directories that will contain these includes (don't specify the files themselves,
Ceedling only needs the directories), Ceedling is able to automatically add these to its internal
include list. This allows these files to be used while building your release code, as well we making
them mockable during unit testing.

### `source`

It’s possible that your external dependency will just produce additional C files as its output.
In this case, Ceedling is able to automatically add these to its internal source list. This allows
these files to be used while building your release code.

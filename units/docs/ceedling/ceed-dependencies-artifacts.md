---
id: "ceed-dependencies-artifacts"
type: "concept"
domain: "test"
title: "Dependencies: Artifacts"
summary: "Artifacts are the outputs of the build process, listed under :artifacts. A dependency may have any of them or none. Your dependency’s build process may produce many other files, but these are the ones Ceedling acts on."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/dependencies.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/dependencies/#artifacts"
license: "MIT"
mode: "V"
---

Artifacts are the outputs of the build process, listed under `:artifacts`. A dependency
may have any of them or none. Your dependency’s build process may produce many other
files, but these are the ones Ceedling acts on.

### `static_libraries`

Static libraries Ceedling links into your test and release builds. If one does not
exist, Ceedling fetches and builds the dependency to produce it.

### `dynamic_libraries`

Dynamic libraries Ceedling links into your test and release builds. If one does not
exist, Ceedling fetches and builds the dependency to produce it. `dependencies:deploy`
copies them to the [`:deploy` path](#working-paths), by default beside your release
executable, where it loads them at run time.

### `executables`

Programs a dependency builds, such as a code generator, a flashing utility, or a tool
your release ships alongside it. Ceedling never links them. A release build, or
`dependencies:make`, fetches and builds the dependency when one does not exist, while
test builds do not wait on them. `dependencies:deploy` copies them, with any dynamic
libraries, to the [`:deploy` path](#working-paths).

On Windows, list each executable with its `.exe` extension.

### `includes`

The public headers a dependency provides. Ceedling adds their directories to its search
paths, so your code can include them and your tests can mock them. An entry may be:

- a header file, such as `include/wolfssl.h`, which adds that file’s directory;
- a directory, such as `include`;
- a glob, such as `include/**`, which adds every directory it finds.

### `source`

Directories of C files a dependency produces, such as generated code. Ceedling adds the
directories to its search paths and their C files to your release build.

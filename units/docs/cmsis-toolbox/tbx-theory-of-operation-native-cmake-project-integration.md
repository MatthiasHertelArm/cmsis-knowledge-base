---
id: "tbx-theory-of-operation-native-cmake-project-integration"
type: "concept"
domain: "project"
title: "Theory of Operation: Native CMake Project Integration"
summary: "CMSIS-Toolbox 2.15 can orchestrate a native CMake project directly from a cmake: project entry."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-operation.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/#native-cmake-project-integration"
license: "Apache-2.0"
mode: "V"
---

CMSIS-Toolbox 2.15 can orchestrate a native CMake project directly from a [`cmake:` project entry](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/YML-Input-Format.md#cmake-build). Such an entry creates a synthetic project context and generated `*.cbuild.yml` metadata, but bypasses processing that is specific to `*.cproject.yml` files, such as CMSIS component, translation-control, and linker-script generation.

For each selected native CMake context, `cbuild` uses the specified source directory and generator, appends the entries under `configure:` to the CMake configure operation, and builds the optional `target:`. If `target:` is omitted, the native CMake project's default target is built. The normal clean and rebuild operations apply to these contexts. To generate a compilation database, add `-DCMAKE_EXPORT_COMPILE_COMMANDS=ON` under `configure:`.

Files declared under `images:` are treated as outputs of the native build. They are copied into the generated context information and, when selected by a `target-set:`, into `*.cbuild-run.yml` for programming and debugging. The optional `device:` identifies the processor that executes those images in a multi-processor target.

This direct project integration differs from the following mechanism, which invokes CMake only as a custom build step.

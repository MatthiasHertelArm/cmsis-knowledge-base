---
id: "devt-pack-generation-tool-how-it-works"
type: "concept"
domain: "pack"
title: "Pack Generation Tool: How it Works"
summary: "The contents of a component are retrieved from the input manifest file and from the CMake targets associated with it. If several CMake targets are listed, the build information (source files, include paths and defines) will be merged."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packgen/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/packgen/README.md#how-it-works"
license: "Apache-2.0"
mode: "V"
---

The contents of a `component` are retrieved from the input manifest file and
from the CMake targets associated with it. If several CMake targets are listed,
the build information (source files, include paths and defines) will be merged.
The build information of other components or CMake targets listed as
`dependencies` will be filtered out.

External dependencies of a component can be added to the `conditions` list.
When an internal component is listed as dependency, a `require` condition is
automatically inserted. For checking the correctness of external dependencies
the path of external PDSC files (absolute or relative to the working directory)
can be specified with the command line option `--include`.

Files that are not among the build information such as config files can still
join a component by adding them to the `files` list.

After changing CMakeLists and/or other included CMake files, use the tool
option `--regenerate` to rerun the CMake generation step. When changing only
the input YAML file there is no need to regenerate CMake targets.

Multiple sets of CMake options are supported and shall be inserted in the
manifest file in the top level `build` mapping. The set(s) of options to be
considered in the generation of a given component shall be inserted in the
`build` field under the `components` mapping, while the `operation` to be
applied to them can be chosen as `intersection` or `difference`.

The `manifest.yml` file shall be placed alongside the entry point `CMakeLists.txt`.
The command line option `--source` shall be used to indicate the root (top-level)
source folder when the `CMakeLists.txt` and `manifest.yml` are not located at the
root folder. Paths inside the `manifest.yml` file shall be relative to the root folder.

The contents of include paths to be recursively copied into the pack can be
filtered by setting allowed file extensions in the `extensions` tag, the
default are `.h` and `.hpp`. These extensions are also used for handling file
categories of source files coming from CMake targets.

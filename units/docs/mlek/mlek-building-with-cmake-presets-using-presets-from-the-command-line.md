---
id: "mlek-building-with-cmake-presets-using-presets-from-the-command-line"
type: "concept"
domain: "edge-ai"
title: "Building with CMake Presets: Using presets from the command line"
summary: "Presets can be also used from a command-line:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/cmake_presets.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/cmake_presets.md#using-presets-from-the-command-line"
license: "Apache-2.0"
mode: "V"
---

Presets can be also used from a command-line:
```commandline
cmake --preset <config-name>
cmake --build --preset <config-name>
```
where config-name is one of:
```commandline
native
mps3-300-gcc
mps3-300-llvm
mps3-300-armclang
mps3-310-gcc
mps3-310-llvm
mps3-310-armclang
mps4-315-gcc
mps4-315-llvm
mps4-315-armclang
mps4-320-gcc
mps4-320-llvm
mps4-320-armclang
```
This will automatically configure and build the evaluation-kit into a corresponding folder.
You can still pass in build flags as usual, for example:
```commandline
cmake --preset mps3-300-gcc -DUSE_CASE_BUILD=inference_runner
cmake --build --preset mps3-300-gcc
```

---
id: "ethu-arm-cmsis-ethos-u-continuous-integration-ci"
type: "concept"
domain: "edge-ai"
title: "Arm CMSIS Ethos-U: Continuous Integration (CI)"
summary: "The Test Ethos-U workflow pins Arm GNU Toolchain 14.2.1 in vcpkg-configuration.json. TensorFlow Lite Micro 1.26.5 is built as C++17 with exceptions and RTTI disabled, matching the compiler settings supplied by the TensorFlow Lite Micro pack."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/README.md#continuous-integration-ci"
license: "Apache-2.0"
mode: "V"
---

| CI workflow | Description |
|---|---|
| [`pack`](https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/./.github/workflows/pack.yml) | Generates the documentation and software pack for pull requests, pushes to `main`, and published releases. |
| [`gh-pages`](https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/./.github/workflows/gh-pages.yml) | Deploys the generated content from the `gh-pages` branch to GitHub Pages. |
| [`test-ethos-u`](https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/./.github/workflows/test-ethos-u.yml) | Builds and runs the Ethos-U55, Ethos-U65, and Ethos-U85 integration tests with Arm Compiler 6 and GCC. |

The Test Ethos-U workflow pins Arm GNU Toolchain 14.2.1 in
[`vcpkg-configuration.json`](https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/./examples/Test-Ethos-U/vcpkg-configuration.json).
TensorFlow Lite Micro 1.26.5 is built as C++17 with exceptions and RTTI disabled,
matching the compiler settings supplied by the TensorFlow Lite Micro pack. Newer
GCC versions diagnose the pack's private class-specific `operator delete` when
exceptions are enabled.

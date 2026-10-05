---
id: "ethint-cmsis-ethos-u-integration-example-command-line-build"
type: "concept"
domain: "edge-ai"
title: "CMSIS Ethos-U integration example: Command-line build"
summary: "With the tools on PATH and the required packs available, build the U85 AppKit-E8 application with:"
status: "draft"
collection: "cmsis-ethos-integration"
source: "Arm-Examples/CMSIS-Ethos-Integration@529e966:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/529e966/README.md#command-line-build"
license: "Apache-2.0"
mode: "V"
---

With the tools on `PATH` and the required packs available, build the U85
AppKit-E8 application with:

```sh
cbuild Test-Ethos-U85.csolution.yml --active AppKit-E8-U85@J-Link --toolchain GCC --packs
```

`--packs` downloads missing public packs. For a different target or compiler,
select it with `--active` or `--toolchain` respectively. The
[Build workflow](https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/529e966/.github/workflows/Build.yml) checks the U55 and U85 solutions
with both AC6 and GCC.

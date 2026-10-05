---
id: "csx-simple-trustzone-application-generate-the-project-binaries"
type: "concept"
domain: "project"
title: "Simple TrustZone Application: Generate the project binaries"
summary: "The solution provides Debug and Release target sets. Select the required set with the --active option:"
status: "draft"
collection: "csolution-examples"
source: "Open-CMSIS-Pack/csolution-examples@02f71b2:SimpleTrustZone/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/SimpleTrustZone/README.md#generate-the-project-binaries"
license: "Apache-2.0"
mode: "V"
---

The solution provides `Debug` and `Release` target sets. Select the required set with the `--active` option:

```txt
> cbuild SimpleTZ.csolution.yml --packs --active AVH@Debug --toolchain AC6
> cbuild SimpleTZ.csolution.yml --packs --active AVH@Release --toolchain AC6
```

Replace `AC6` with `GCC` to build a target set with the GCC compiler.

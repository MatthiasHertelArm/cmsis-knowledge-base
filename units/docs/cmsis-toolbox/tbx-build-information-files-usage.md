---
id: "tbx-build-information-files-usage"
type: "concept"
domain: "project"
title: "Build Information Files: Run and Debug Management / Usage"
summary: "The .cbuild-run.yml file provides all information about the application project for run and debug. It can be used with tools such as pyOCD as shown below."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-CBuild-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-CBuild-Format/#usage"
license: "Apache-2.0"
mode: "V"
---

_Part of: Run and Debug Management_

The `*.cbuild-run.yml` file provides all information about the application project for run and debug. It can be used with tools such as pyOCD as shown below.

Start gdbserver for debug connection:

```bash
>pyocd gdbserver --cbuild-run out\MyProject+TargetHW.cbuild-run.yml
```

Program flash with application images:

```bash
>pyocd load --cbuild-run out\MyProject+TargetHW.cbuild-run.yml
```

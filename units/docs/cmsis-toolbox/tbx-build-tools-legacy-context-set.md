---
id: "tbx-build-tools-legacy-context-set"
type: "concept"
domain: "project"
title: "Build Tools: Command Examples / Legacy Context Set"
summary: "The option --context-set saves selected --context options in SimpleTZ.cbuild-set.yml or reuses that selection. Refer to file structure of .cbuild-set.yml for details."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#legacy-context-set"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Examples_

!!! Note
    Use a [`target-set:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/build-overview.md#working-with-target-set) and `--active` for new projects. Context sets are retained for legacy projects.

The option `--context-set` saves selected `--context` options in `SimpleTZ.cbuild-set.yml` or reuses that selection. Refer to [file structure of `*.cbuild-set.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/YML-CBuild-Format.md#cbuild-setyml) for details.

```shell
cbuild SimpleTZ.csolution.yml -S -c CM33_s.Release -c CM33_ns.Debug
```

Read the previously stored `--context` setup from the file `SimpleTZ.cbuild-set.yml`.

```shell
cbuild SimpleTZ.csolution.yml -S
```

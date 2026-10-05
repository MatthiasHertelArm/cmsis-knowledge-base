---
id: "tbx-build-tools-list-debug-adapters"
type: "concept"
domain: "project"
title: "Build Tools: Command Examples / List Debug Adapters"
summary: "List the debug adapters registered with the CMSIS-Toolbox. The names in the default output are the values accepted by debugger: name:. Use --verbose to show aliases that are also accepted, and --filter to restrict the list."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#list-debug-adapters"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Examples_

List the debug adapters registered with the CMSIS-Toolbox. The names in the default output are the values accepted by [`debugger: name:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/YML-Input-Format.md#debugger). Use `--verbose` to show aliases that are also accepted, and `--filter` to restrict the list.

```shell
csolution list debuggers
csolution list debuggers --filter pyOCD --verbose
```

Example output:

```text
CMSIS-DAP@pyOCD
  CMSIS-DAP
  DAP-Link
ST-Link@pyOCD
  ST-LINK
```

---
id: "tbx-csolution-project-structure-plm-of-software-packs"
type: "concept"
domain: "project"
title: "CSolution Project Structure: Directory Structure / PLM of Software Packs"
summary: "Software packs evolve over time (bug fixes, new features, dependency and component updates). Checking the installed vs."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#plm-of-software-packs"
license: "Apache-2.0"
mode: "V"
---

_Part of: Directory Structure_

Software packs evolve over time (bug fixes, new features, dependency and component updates). Checking the installed vs. available software pack versions helps you decide when to upgrade (or stay pinned) to keep builds reproducible and to avoid unexpected behavior changes caused by a pack update.

Use these steps to update packs and configuration files:

1. **Update available pack information:** `cpackget update-index` updates the public index and cached PDSC metadata. With `--sparse`, only the index is updated.
2. **Install required packs:** `cpackget add` installs the requested pack and its dependencies. During an automatic index update, only the PDSC metadata required for these packs is refreshed. This does not change a project's resolved versions or RTE files.
3. **Review available project updates:** `csolution check pack-updates` reports newer versions and optionally their release notes. It does not modify the project.
4. **Resolve project pack versions:** `csolution` records exact versions in `*.cbuild-pack.yml`. Existing entries keep the project reproducible; changing a `pack:` requirement or deliberately removing a `resolved-pack:` entry allows that pack to be resolved again.
5. **Update configuration files:** `csolution update-rte` updates the configuration-management files in the RTE directory. Alternatively, use `cbuild --update-rte` to request the same update before building. A normal `cbuild` invocation leaves RTE configuration files unchanged. User-edited configuration files are not overwritten; changed pack files are provided separately for review and merging.

In the example below, `csolution check pack-updates` reports that `Keil::MDK-Middleware` can be updated from `8.1.0` to `8.2.0` (shown as `8.1.0 -> 8.2.0`). Using the option `--verbose` prints the relevant release notes. The option `--filter "USB"` narrows the output to USB-related entries.

**Example:**

```shell
>csolution check pack-updates SDS.csolution.yml --verbose --filter "USB"
Keil::MDK-Middleware@8.1.0 -> 8.2.0
  Release notes for v8.2.0:
      Network Component Version 8.2.0
      - fixed conversion from Unix time to HTTP-date format
      - added netHandleError system error handler to the user API
      - improved BSD socket control with enhanced setsockopt and getsockopt functions
      - modified File System interface functions to be weakly linked, allowing user overrides
      FileSystem Component Version 8.0.2 (unchanged)
      USB Component Version 8.0.1
      - USB Device: updated USB transfer handling to use only buffers from USB data buffers memory section
      - USB Device: improved USB MSC compliance
```

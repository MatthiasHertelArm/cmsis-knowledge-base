---
id: "tbx-csolution-project-structure-software-components"
type: "concept"
domain: "project"
title: "CSolution Project Structure: Directory Structure / Software Components"
summary: "Software components are re-usable library or source files that do not require modification in the user application. Optionally, configurable source and header files are provided to allow the setting of parameters for the software component."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#software-components"
license: "Apache-2.0"
mode: "V"
---

_Part of: Directory Structure_

[Software components](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/CreateApplications.md#software-components) are re-usable library or source files that do not require modification in the user application.
Optionally, configurable source and header files are provided to allow the setting of parameters for the software component.

- Configurable source and header files are copied to the project using the directory structure explained above.
- Libraries, source, and header files that are not configurable (and need no modification) are stored in the directory
  of the software component (typically part of CMSIS_Pack_ROOT) and get included directly from this location into the
  project.
- An include path to the header files of the software component is added to the C/C++ Compiler control string.

!!! Notes
    - The command `cbuild setup <solution>.csolution.yml --update-rte` prepares the build information and updates the files in the `./RTE` directory.
    - The `csolution` command `update-rte` only updates the configuration files in the `RTE` directory.
    - A normal `cbuild` invocation does not change RTE configuration files. Add `--update-rte` when an update is required.
    - Using the option `--verbose` outputs additional version details.

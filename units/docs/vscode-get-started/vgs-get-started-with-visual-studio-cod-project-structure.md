---
id: "vgs-get-started-with-visual-studio-cod-project-structure"
type: "concept"
domain: "project"
title: "Get started with Visual Studio Code: Project structure"
summary: "The project is written in CSolution Project Format:"
status: "draft"
collection: "vscode-get-started"
source: "Open-CMSIS-Pack/vscode-get-started@675c86f:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-get-started/blob/675c86f/README.md#project-structure"
license: "Apache-2.0"
mode: "V"
---

The project is written in
[`CSolution Project Format`](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/):

- The [`get_started.csolution.yml`](https://github.com/Open-CMSIS-Pack/vscode-get-started/blob/675c86f/./get_started.csolution.yml) file lists and defines the required packs, target and
  build types, as welll as projects.
- The [`hello/hello.cproject.yml`](https://github.com/Open-CMSIS-Pack/vscode-get-started/blob/675c86f/./hello/hello.cproject.yml) file defines components and source files.
- The [`vcpkg-configuration.json`](https://github.com/Open-CMSIS-Pack/vscode-get-started/blob/675c86f/./vcpkg-configuration.json) file orchestrates the installation of all required tools
  locally or [in the cloud](#run-in-github-codespaces).

### Toolchain settings

The example is using the
[Arm Compiler for Embedded](https://developer.arm.com/dev2/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded) as
the build toolchain. It is prepared to run on the
[Arm GNU Toolchain](https://developer.arm.com/dev2/Tools%20and%20Software/GNU%20Toolchain) and the
[Arm Toolchain for Embedded](https://developer.arm.com/dev2/Tools%20and%20Software/Arm%20Toolchain%20for%20Embedded) as
well. If you want to use one of these, do the following:

- Add the compiler in the `vcpkg-configuration.json` file.
- Change the `compiler:` setting at the end of the `get_started.csolution.yml` file.

---
id: "cact-arm-software-cmsis-actions-action-vcpkg"
type: "concept"
domain: "devops"
title: "ARM-software/cmsis-actions: Action: vcpkg"
summary: "This action installs a development environment with the tools described in the file vcpkg-configuration.json. The tools are downloaded from the Arm Tools Artifactory. Refer to CMSIS-Toolbox - Installation - vcpkg - Setup using CLI installation guide for more information."
status: "draft"
collection: "cmsis-actions"
source: "ARM-software/cmsis-actions@f248cd4:README.md"
doc_source: "https://github.com/ARM-software/cmsis-actions/blob/f248cd4/README.md#action-vcpkg"
license: "Apache-2.0"
mode: "V"
---

This action installs a development environment with the tools described in the file `vcpkg-configuration.json`.
The tools are downloaded from the [Arm Tools Artifactory](https://artifacts.tools.arm.com).
Refer to [CMSIS-Toolbox - Installation - vcpkg - Setup using CLI  installation guide](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/blob/main/docs/installation.md#vcpkg---setup-using-cli)
for more information.

```yaml
- name: Setup vcpkg environment
  uses: ARM-software/cmsis-actions/vcpkg@v1
  with:
    config: "./vcpkg-configuration.json"
    vcpkg-downloads: "${{ github.workspace }}/.vcpkg/downloads"
    cache: "-"
```

inputs              | default value                              | description
--------------------|--------------------------------------------|--------------
`config:`           | "./vcpkg-configuration.json"               | Path and filename of the vcpkg configuration file.
`vcpkg-downloads:`  | "${{ github.workspace }}/.vcpkg/downloads" | Download folder for vcpkg tool artifacts
`cache:`            | "-" (no cache used)                        | [Create a cache with a key](https://github.com/actions/cache?tab=readme-ov-file#creating-a-cache-key) to store tool artifacts.

The activated environment is preserved into `$GITHUB_PATH` and `$GITHUB_ENV` so that it can be used by subsequent steps. The cache is based on
[actions/cache](https://github.com/actions/cache) and improves workflow execution time.

### Usage examples vcpkg

- [github.com/Arm-Examples/AVH_CI_Template](https://github.com/Arm-Examples/AVH_CI_Template/blob/main/.github/workflows/basic.yml) uses `vcpkg` to install the required tools.

- [https://github.com/ARM-software/CMSIS-FreeRTOS](https://github.com/ARM-software/CMSIS-FreeRTOS/blob/main/.github/workflows/cmsis_rv2.yaml)
  uses `vcpkg` with a cache. As there are multiple test executions, the workflow execution speed is improved.

---
id: "tbx-create-applications-update-software-packs"
type: "concept"
domain: "project"
title: "Create Applications: Update Software Packs"
summary: "An update of a software pack can be performed with these steps:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/CreateApplications.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/CreateApplications/#update-software-packs"
license: "Apache-2.0"
mode: "V"
---

An update of a software pack can be performed with these steps:

- Download new software packs as needed using `cpackget`.
- Use `csolution update-rte` with the option `--load latest` to select the latest pack versions and update the RTE configuration files.

```bash
csolution update-rte Hello.csolution.yml --load latest
```

- List potentially outdated configuration files using the command `csolution list configs`.

```bash
csolution list configs Hello.csolution.yml --active <target-type>[@<target-set>]
../RTE/CMSIS/RTX_Config.c@5.1.1 (update@5.2.0) from ARM::CMSIS:RTOS2:Keil RTX5&Source@5.8.0
../RTE/Device/SSE-300-MPS3/startup_SSE300MPS3.c@1.1.1 (up to date) from ARM::Device:Startup&C Startup@2.0.0
../RTE/Device/SSE-300-MPS3/system_SSE300MPS3.c@1.1.1 (up to date) from ARM::Device:Startup&C Startup@2.0.0
```

!!! Note
    The text `update@version` indicates that a new configuration file is available. Use a merge utility to identify and merge configuration settings from a previous version. Refer to [PLM of configuration files](https://open-cmsis-pack.github.io/cmsis-toolbox/CreateApplications/build-overview.md#plm-of-configuration-files) for more information.

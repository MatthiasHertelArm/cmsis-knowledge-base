---
id: "czep-zephyr-integration-with-cmsis-tool-command-line-build"
type: "concept"
domain: "project"
title: "Zephyr Integration with CMSIS-Toolbox: Command-line build"
summary: "Install CMSIS-Toolbox, the GCC compiler, and the Zephyr workspace described above. Ensure that the Zephyr virtual environment is active, then run for example:"
status: "draft"
collection: "cmsis-zephyr"
source: "Arm-Examples/CMSIS-Zephyr@ef8713c:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Zephyr/blob/ef8713c/README.md#command-line-build"
license: "Apache-2.0"
mode: "V"
---

Install [CMSIS-Toolbox](https://open-cmsis-pack.github.io/cmsis-toolbox/installation/), the GCC compiler, and the
[Zephyr workspace described above](#zephyr-installation). Ensure that the Zephyr virtual environment is active, then
run for example:

```bash
cbuild zephyr.csolution.yml --packs --active NUCLEO-H563ZI
```

The command uses the same common project information as VS Code and invokes West to build the selected Zephyr application. Refer to [West Build System Integration](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#west-build-system-integration) for details.

> [!CAUTION]
> If you see errors during `west build` (for example during `generating a build system`), the `west` installation or `PATH` is likely incorrect. Check [Settings](https://code.visualstudio.com/docs/configure/settings) - **Cmsis-Csolution:** Environment Variables.
> Verify that the values match the paths in [Configure VS Code](#configure-vs-code).
<!-- -->
> [!TIP]
> For more information, see the [Keil Studio documentation - Work with Zephyr applications](https://mdk-packs.github.io/vscode-cmsis-solution-docs/zephyr.html).

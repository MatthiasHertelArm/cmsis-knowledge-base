---
id: "czep-zephyr-integration-with-cmsis-tool-cmsis-toolbox-integration"
type: "concept"
domain: "project"
title: "Zephyr Integration with CMSIS-Toolbox: CMSIS-Toolbox Integration"
summary: "Zephyr and west remain responsible for configuring and building the Zephyr application. The zephyr.csolution.yml file adds common project information for the selectable application configurations and their target hardware."
status: "draft"
collection: "cmsis-zephyr"
source: "Arm-Examples/CMSIS-Zephyr@ef8713c:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Zephyr/blob/ef8713c/README.md#cmsis-toolbox-integration"
license: "Apache-2.0"
mode: "V"
---

Zephyr and `west` remain responsible for configuring and building the Zephyr application. The [`zephyr.csolution.yml`](https://github.com/Arm-Examples/CMSIS-Zephyr/blob/ef8713c/./zephyr.csolution.yml) file adds [common project information](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/#common-project-information-for-the-development-workflow) for the selectable application configurations and their target hardware.

CMSIS-Toolbox uses the same common project information in VS Code, command-line, and CI/DevOps workflows. CMSIS-Packs provide device and board data that complements the Zephyr build information with programming, run, and debug configuration, peripheral views, and trace configuration. Generated files such as `compile_commands.json` and `*.cbuild-run.yml` connect smart editor features, static code analysis and test tools, target deployment, and trace to the application development workflow without replacing Zephyr or `west`.

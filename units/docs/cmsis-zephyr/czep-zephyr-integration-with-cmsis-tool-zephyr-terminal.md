---
id: "czep-zephyr-integration-with-cmsis-tool-zephyr-terminal"
type: "concept"
domain: "project"
title: "Zephyr Integration with CMSIS-Toolbox: Zephyr Terminal"
summary: "Keil Studio includes a built-in Zephyr Terminal for running west commands in the IDE. When you open it, it configures the working directory and Zephyr environment for the selected project."
status: "draft"
collection: "cmsis-zephyr"
source: "Arm-Examples/CMSIS-Zephyr@ef8713c:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Zephyr/blob/ef8713c/README.md#zephyr-terminal"
license: "Apache-2.0"
mode: "V"
---

(figure: ZephyrTerminal)

Keil Studio includes a built-in **Zephyr Terminal** for running `west` commands in the IDE. When you open it, it configures the working directory and Zephyr environment for the selected project.

**Example `west` commands:**

```bash
# Build the project
west build

# Open GUI configuration
west build -t guiconfig

# Generate RAM report
west build -t ram_report
```

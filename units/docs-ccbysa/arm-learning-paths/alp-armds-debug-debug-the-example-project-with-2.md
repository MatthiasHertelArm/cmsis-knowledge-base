---
id: "alp-armds-debug-debug-the-example-project-with-2"
type: "concept"
domain: "project"
title: "Get started with Arm Development Studio: Debug the example: Debug the example project with MPS2+"
summary: "The project contains startup_Cortex-M3_AC6_MPS2.launch within the project folder."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/armds/debug.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/armds/debug/#debug-the-example-project-with-mps2"
license: "CC-BY-SA-4.0"
mode: "V"
---

The project contains `startup_Cortex-M3_AC6_MPS2.launch` within the project folder.

1. Double-click on the `.launch` file to inspect. Observe settings in various panes, defining the MPS2+ configuration to connect to, the image to be loaded, and other connection options.

2. From the `Target Connection` pulldown, select the debug adapter used to connect to the target. `CMSIS-DAP` is an on-board debug adapter that connects via USB, and so no additional hardware is needed.

3. Click `Browse` to identify your debug adapter, then click `Apply` to save.

4. Click `Debug` to start the debug session.

**Note:**
Subsequent debug sessions can be launched directly from the `Debug Control` pane.

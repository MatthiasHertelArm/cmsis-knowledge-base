---
id: "alp-context-switch-cortex-m-example-run-the-example-project"
type: "concept"
domain: "rtos"
title: "Learn about context switching on Arm Cortex-M processors: Example Arm DS project to demonstrate context switching operations: Run the example project"
summary: "The built executable from previous step can run on an Armv8-M FVP model supplied with Arm Development Studio. A ready to use launch configuration file rtos_context_switch.launch is provided with the example project."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/context-switch-cortex-m/example.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/context-switch-cortex-m/example/#run-the-example-project"
license: "CC-BY-SA-4.0"
mode: "V"
---

The built executable from previous step can run on an Armv8-M FVP model supplied with Arm Development Studio. A ready to use launch configuration file `rtos_context_switch.launch` is provided with the example project.

Follow the steps below to run the executable using this configuration:
1.	Select Run - Debug Configurations....
2.	Select `rtos_context_switch` from the list of Generic Arm C/C++ Application configurations.
3.	Click on Debug to start debugging. The executable image will be downloaded to the target Armv8-M FVP model and the program counter is set to main.
4.	Run the executable (press F8). Text output appears in the target console view.

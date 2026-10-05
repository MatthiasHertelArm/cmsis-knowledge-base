---
id: "alp-new-debug-targets-armds-dstream-create-a-platform-configuratio"
type: "concept"
domain: "debug"
title: "Add new debug targets to Arm Development Studio: Debug connection with Arm DSTREAM: Create a Platform Configuration for your Hardware"
summary: "Arm Development Studio is supplied with out-of-the-box configurations for many development boards. This step could be skipped as the MPS2+ platform is provided, but this example is to illustrate how to create a configuration for any board."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/new_debug_targets_armds/dstream.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/new_debug_targets_armds/dstream/#create-a-platform-configuration-for-your-hardware"
license: "CC-BY-SA-4.0"
mode: "V"
---

Arm Development Studio is supplied with out-of-the-box configurations for many development boards. This step could be skipped as the MPS2+ platform is provided, but this example is to illustrate how to create a configuration for any board.

If not done previously, select `File` > `New` > `Other` > `Configuration Database` > `Configuration Database`, and give it a meaningful name. This is where the debugger stores all user-made configurations.

Then select `File` > `New` > `Other` > `Configuration Database` > `Platform Configuration`, which will be the actual configuration to create. When prompted, select the above `Configuration Database`.

You may then be prompted to ask how to generate such a configuration. Select Automatic, and click Next. Browse for your DSTREAM unit, which should be connected to your target hardware. The unit will interrogate the target and determine which Arm processors are present. Save the configuration with an appropriate name.

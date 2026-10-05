---
id: "alp-new-debug-targets-armds-fastmodels-create-a-model-configuration-f"
type: "concept"
domain: "debug"
title: "Add new debug targets to Arm Development Studio: Debug connection to Arm Fast Models: Create a Model Configuration for your Virtual Platform"
summary: "In the Arm Development Studio IDE menu, select File > New > Other > Configuration Database > Configuration Database, and give it a meaningful name. This creates a project folder where the debugger stores all user-made configurations."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/new_debug_targets_armds/fastmodels.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/new_debug_targets_armds/fastmodels/#create-a-model-configuration-for-your-virtual-platform"
license: "CC-BY-SA-4.0"
mode: "V"
---

In the `Arm Development Studio IDE` menu, select `File` > `New` > `Other` > `Configuration Database` > `Configuration Database`, and give it a meaningful name. This creates a project folder where the debugger stores all user-made configurations.

Then select `File` > `New` > `Other` > `Configuration Database` > `Model Configuration`, which will be the actual configuration to create. When prompted, select the above `Configuration Database` to store in. Click `Next`.

You will be prompted to ask which debug interface to use, `Iris` or `CADI`. `Iris` is the default and recommended interface. Click `Next`.

You are then prompted to either launch the model, or browse for an already running model. Select `Launch and connect to specific model`.

Browse for the Fast Model executable. The debugger will append necessary command options to enable debug. This is the most straight forward option, and recommended for first time users.

A `.mdf` file will be created. Specify an appropriate manufacturer and platform name for identification, and click `Import`.

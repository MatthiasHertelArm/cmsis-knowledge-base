---
id: "alp-new-debug-targets-armds-fastmodels-create-a-new-debug-connection"
type: "concept"
domain: "debug"
title: "Add new debug targets to Arm Development Studio: Debug connection to Arm Fast Models: Create a new Debug Connection for your Virtual Platform"
summary: "Select File > New > Model Connection, and give it a meaningful name. It is recommended to associate with the specific project (startup_Cortex-M3_AC6)."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/new_debug_targets_armds/fastmodels.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/new_debug_targets_armds/fastmodels/#create-a-new-debug-connection-for-your-virtual-platform"
license: "CC-BY-SA-4.0"
mode: "V"
---

Select `File` > `New` > `Model Connection`, and give it a meaningful name. It is recommended to associate with the specific project (`startup_Cortex-M3_AC6`).

Select the model configuration you created above (the text filter can assist if many targets defined), and click `Finish`.

You can again select to launch a new instance of the model or connect to an already running model. Select `Launch a new model`.

### Load image

Navigate to the `Files` tab, and browse (within Workspace) to the `startup_Cortex-M3_AC6.axf` pre-built image. Then, in the `Debugger` tab, select `Debug from entry point`.

If connecting to an already running model with a loaded image (`-a <image>`), select `Load symbols from file` from the `Files` tab. In this scenario, in the `Debugger` tab, select `Connect Only`.

Click `Debug` to connect to the virtual platform, and commence your debug session.

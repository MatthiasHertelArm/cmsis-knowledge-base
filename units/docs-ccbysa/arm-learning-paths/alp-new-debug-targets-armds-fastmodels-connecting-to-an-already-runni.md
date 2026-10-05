---
id: "alp-new-debug-targets-armds-fastmodels-connecting-to-an-already-runni"
type: "concept"
domain: "debug"
title: "Add new debug targets to Arm Development Studio: Debug connection to Arm Fast Models: Connecting to an already running model"
summary: "When creating the model configuration, you can select to browse for a model running on local or remote hosts. As these models are not being launched by the debugger, additional command options are needed."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/new_debug_targets_armds/fastmodels.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/new_debug_targets_armds/fastmodels/#connecting-to-an-already-running-model"
license: "CC-BY-SA-4.0"
mode: "V"
---

When creating the `model configuration`, you can select to browse for a model running on local or remote hosts. As these models are not being launched by the debugger, additional command options are needed.

### Browse for model running on local host

If this is selected, you must previously have launched the model with `-I` option to start the Iris server in the model.

If no port number (`--port-number`) is specified, recommend adding `-p` to output the port number used.

### Browse for model running on remote host

If this is selected (where the virtual platform is running on a different machine on the network), you must previously have launched the model with `-I -A` options to start the Iris server in the model and allow remote access.

If no port number (`--port-number`) is specified, recommend adding `-p` to output the port number used. You will be prompted for the server address (the machine running the virtual platform) and port number.

### Debug Connection

In the `Connections` tab, select `Connect to already running model`. Specify the `Connection Address` as `localhost:<port>` or `hostname:<port>` as appropriate.

If the model has an image loaded (`-a <image>`), select `Load symbols from file` from the `Files` tab. In this scenario, in the `Debugger` tab, you must select `Connect Only`.

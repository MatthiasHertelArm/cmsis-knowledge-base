---
id: "alp-new-debug-targets-armds-dstream-create-a-debug-configuration-f"
type: "concept"
domain: "debug"
title: "Add new debug targets to Arm Development Studio: Debug connection with Arm DSTREAM: Create a Debug Configuration for your Platform"
summary: "Now that the debugger is aware of your platform, you can now create a debug configuration to describe how the debugger will connect to that platform."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/new_debug_targets_armds/dstream.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/new_debug_targets_armds/dstream/#create-a-debug-configuration-for-your-platform"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that the debugger is aware of your platform, you can now create a debug configuration to describe how the debugger will connect to that platform.

To start, select `File` > `New` > `Hardware Connection`, and give it a meaningful name. It is recommended to associate the connection with a specific project (`startup_Cortex-M3_AC6`) when available.

Select the `Platform Configuration` you created (the text filter can assist if many targets defined), and click Finish.

Ensure `DSTREAM family` is selected from the Target Connection pulldown, and Browse for your DSTREAM unit. The debugger will recognize the type of DSTREAM unit connected. Use the `DTSL Options` Edit button to specify additional settings (such as which processor(s) to trace).

To load an image, navigate to the `Files` tab, and browse to the appropriate ELF image. Then, in the `Debugger` tab, select `Debug from entry point`.

If the target is already running with an image you can also load the debug symbols from the `Files` tab. In that scenario, in the `Debugger` tab, select `Connect Only`.

Click `Debug` to connect to the platform, and commence your debug session.

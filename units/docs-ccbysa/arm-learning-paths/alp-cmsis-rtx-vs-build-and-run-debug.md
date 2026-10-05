---
id: "alp-cmsis-rtx-vs-build-and-run-debug"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil Studio (VS Code): Build and run the application: Debug"
summary: "To start debugging, click the Debug icon, or enter the Run and Debug extension view."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx_vs/build_and_run.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx_vs/build_and_run/#debug"
license: "CC-BY-SA-4.0"
mode: "V"
---

To start debugging, click the `Debug` icon, or enter the `Run and Debug` extension view.

Choose the debug connection you configured earlier to launch the FVP (Fixed Virtual Platform).

Use the debugging controls to step through your code.

Once the OS is initialized, you'll see the output from the threads displayed in the `Debug Console`.

```
[model] hello from thread 1
[model] hello from thread 2
[model] hello from thread 3
[model] hello from thread 1
[model] hello from thread 2
...
```
To end the debug session, click `Stop` or press `Ctrl`+`F5`.

**Note:**
For a more feature-rich debugging environment, consider using the `Arm Keil μVision IDE`.

For more details, see [Build an RTX5 RTOS application with Keil μVision](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx/).

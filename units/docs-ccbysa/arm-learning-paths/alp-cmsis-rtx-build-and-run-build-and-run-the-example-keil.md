---
id: "alp-cmsis-rtx-build-and-run-build-and-run-the-example-keil"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil μVision: Build and run the application: Build and run the example (Keil MDK)"
summary: "Save all files, and click build (F7) the example."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx/build_and_run.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx/build_and_run/#build-and-run-the-example-keil-mdk"
license: "CC-BY-SA-4.0"
mode: "V"
---

Save all files, and click `build` (`F7`) the example.

Click `Debug` (`Ctrl+F5`) to launch the FVP, and put the IDE into debug mode.
* Use the menu (`View` > `Watch Windows` > `RTX RTOS`) to observe the RTOS features.
* Use the menu (`View` > `Serial Windows` > `Debug (printf)`) to observe the printf output.

Click `Run` (`F5`) to start the application, and after a short time, click `Stop`.

Observe in the `RTX RTOS` view that the threads have been created. Two other threads, `osRtxIdleThread` and `osRtxTimerThread` will also be created.

(figure: Screenshot of the RTX RTOS view in Keil μVision showing the list of created threads including thread_1, thread_2, osRtxIdleThread, and osRtxTimerThread with their status and priority information#center)

However no output is seen in the `printf viewer`. This is because semihosting isn't supported. You'll learn how to address this in the next section.

Exit the debug session (`Ctrl+F5`).

---
id: "alp-cmsis-rtx-build-and-run-build-and-run-the-example-arm"
type: "concept"
domain: "rtos"
title: "Build an RTX5 RTOS application with Keil μVision: Build and run the application: Build and run the example (Arm Development Studio)"
summary: "Save all files, then right-click on the project, and select Build Project."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsis_rtx/build_and_run.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsis_rtx/build_and_run/#build-and-run-the-example-arm-development-studio"
license: "CC-BY-SA-4.0"
mode: "V"
---

Save all files, then right-click on the project, and select `Build Project`.

A `.axf` file will be generated in the `Configuration Name` folder.

You must now create a `Debug Configuration`:
  * Navigate the menu to `File` > `New` > `Model Connection`.
  * Create a Debug connection, and associate it with your project.
  * Select the `MPS2_Cortex-M4` from the selection of FVPs Installed with Arm DS.
  * In the Debug configuration view:
    * In `Files` tab, browse for your `.axf` image.
	* In `Debugger` tab, select `Debug from symbol (main)`
	* In `OS Awareness` tab, select `Keil CMSIS-RTOS RTX` from the pull-down.
	* Click `Apply` to save all settings, then click `Debug`.
	  * Subsequent debug sessions can be invoked directly from the `Debug Control` pane.

When debugging, use the `OS Data` view to observe RTOS information. Open from the `Window` > `Show View` menu. Use the pull down to select different categories.

(figure: Screenshot of the OS Data view showing RTOS thread information including task names, states, and stack usage#center)

For thread aware debug, right-click on the debug connection in the `Debug Control` view, and select `Display threads`.

(figure: Screenshot of the Debug Control view with the context menu showing the Display threads option for thread-aware debugging#center)

You'll see the printf() output in `Target Console` pane.
```
hello from thread 1
hello from thread 2
hello from thread 3
hello from thread 1
hello from thread 2
...
```

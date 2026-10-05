---
id: "alp-coverage-mdk-mdk-set-up-debug-with-fvp"
type: "concept"
domain: "debug"
title: "Get started with Keil MDK Code Coverage: Set up Code Coverage: Set up debug with FVP"
summary: "By default, this project uses the legacy simulator provided with MDK, which does not support code coverage."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/coverage_mdk/mdk.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/coverage_mdk/mdk/#set-up-debug-with-fvp"
license: "CC-BY-SA-4.0"
mode: "V"
---

By default, this project uses the legacy simulator provided with MDK, which does not support code coverage.

To run on the FVP, open Options for Target (figure: Options for Target Icon), navigate to the `Debug` pane, and select `Models Cortex-M Debugger` from the `Use:` pull-down.

Click `Settings`, and under `Command`, browse to one of the supplied FVPs in the `Keil_v5/ARM/avh-fvp/bin/models` folder of your MDK installation (for example, `FVP_MPS2_Cortex-M3_MDK.exe`).

**Older MDK versions:**
Depending on the version of MDK you have installed the path to FVP executable may differ.

MDK versions before 5.37: Keil_v5/ARM/FVP

MDK versions 5.38, 5.39: Keil_v5/ARM/VHT

MDK version 5.40 or later: Keil_v5/ARM/avh-fvp/bin/models


Specify a `Coverage File`, and enable `Load` and `Store` for that file. Because of the way the data is created, code coverage can't be updated in real-time.

**Real hardware:**
If you're using real hardware, no coverage file is needed. The data generates directly from the hardware, and the coverage updates in real-time.


Click `OK` to save settings, then start a debug session (`Ctrl+F5`).

If not already open, navigate to `View` > `Analysis Windows` > `Code Coverage` to enable that view.

Run the application for a few seconds, going through several iterations of the LEDs turning on and off. Observe that the Code Coverage data doesn't update (with FVP). Close the debug session and start a new one to load the coverage data. The code coverage data now displays in the `Code Coverage` window.

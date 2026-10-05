---
id: "aig-fm-fvp-fm-verify-installation"
type: "concept"
domain: "project"
title: "Arm Fast Models: Verify installation"
summary: "To verify everything is working OK, you can build one of the many example projects provided. - Launch the System Canvas IDE from your desktop, or from a terminal:"
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/fm_fvp/fm.md"
doc_source: "https://learn.arm.com/install-guides/fm_fvp/fm/#verify-installation"
license: "CC-BY-SA-4.0"
mode: "V"
---

To verify everything is working OK, you can build one of the many example projects provided.
 - Launch the `System Canvas` IDE from your desktop, or from a terminal:
 ```command
 sgcanvas &
 ```
 - From the menu, select `File` > `Load Project`, and browse to the `FastModelsPortfolio_<version>\examples` folder.
 - Select any example (such as `\LISA\FVP_MPS2\Build_Cortex-M3\FVP_MPS2_Cortex-M3.sgproj`).
 - Ensure an appropriate Project Configuration is selected from the pulldown in the upper toolbar (such as `Win64_Release-VC19`).
 - Click `Build` in the upper toolbar to build the virtual platform.
 - Once built, click `Run` and select `ISIM system`.
 - Click `OK` to launch the virtual platform.

The FVP will launch, and output text in the terminal similar to:
```output
telnetterminal0: Listening for serial connection on port 5000
telnetterminal1: Listening for serial connection on port 5001
telnetterminal2: Listening for serial connection on port 5002
```
A visualization of the FVP will also be displayed.

Terminate the FVP with `Ctrl+C`.

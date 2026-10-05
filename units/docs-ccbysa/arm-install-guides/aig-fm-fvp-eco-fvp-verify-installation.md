---
id: "aig-fm-fvp-eco-fvp-verify-installation"
type: "concept"
domain: "project"
title: "Arm Ecosystem FVPs and Architecture Envelope Models: Verify installation"
summary: "Arm Ecosystem FVPs and AEMs are not license managed."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/fm_fvp/eco_fvp.md"
doc_source: "https://learn.arm.com/install-guides/fm_fvp/eco_fvp/#verify-installation"
license: "CC-BY-SA-4.0"
mode: "V"
---

Arm Ecosystem FVPs and AEMs are not license managed.

To verify everything is working OK, run the installed FVP executable, located in the `models/<build_environment>` folder of the installed directory. No additional command options are needed for this step.

For example:
```command
./FVP_Corstone-1000
```
The FVP will launch, and output text in a terminal similar to:
```output
host_terminal_0: Listening for serial connection on port 5000
host_terminal_1: Listening for serial connection on port 5001
secenc_terminal: Listening for serial connection on port 5002
extsys_terminal: Listening for serial connection on port 5003
```
A visualization of the FVP will also be displayed.

Terminate the FVP with `Ctrl+C`.

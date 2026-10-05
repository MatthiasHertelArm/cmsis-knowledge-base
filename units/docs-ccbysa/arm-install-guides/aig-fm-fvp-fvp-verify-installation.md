---
id: "aig-fm-fvp-fvp-verify-installation"
type: "concept"
domain: "project"
title: "Fixed Virtual Platforms (FVP): Verify installation"
summary: "To verify everything is working OK, navigate to the install directory, and launch any of the supplied FVP executables. No additional command options are needed."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/fm_fvp/fvp.md"
doc_source: "https://learn.arm.com/install-guides/fm_fvp/fvp/#verify-installation"
license: "CC-BY-SA-4.0"
mode: "V"
---

To verify everything is working OK, navigate to the install directory, and launch any of the supplied FVP executables. No additional command options are needed.

For example:
```command
./FVP_MPS2/FVP_MPS2_Cortex-M3
```
The FVP will launch, and output text in a terminal similar to:
```output
telnetterminal0: Listening for serial connection on port 5000
telnetterminal1: Listening for serial connection on port 5001
telnetterminal2: Listening for serial connection on port 5002
```
A visualization of the FVP will also be displayed.

Terminate the FVP with `Ctrl+C`.

**Note:**
You might run into an enablement issue related to the stack:
```
cannot enable executable stack as shared object requires: Invalid argument
```
This stems from the status of the the exec flag, a security feature which helps prevent certain types of buffer overflow attacks. FVPs use just-in-time compilation and require an executable stack to function properly. 

You can a workaround this error using `execstack` on each of the runtime binaries in the error trace.
```
execstack -c <binary>
```

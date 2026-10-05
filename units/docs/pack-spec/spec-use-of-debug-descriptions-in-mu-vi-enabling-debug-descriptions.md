---
id: "spec-use-of-debug-descriptions-in-mu-vi-enabling-debug-descriptions"
type: "concept"
domain: "pack"
title: "Use of debug descriptions in &mu;Vision: Enabling debug descriptions"
summary: "By default &mu;Vision enables the use of the debug descriptions if such are specified for the target. It is possible to manually disable the use of the debug descriptions for a specific project target in Options for Target..."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_dbg_setup_tutorial.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/dbg_sqns_uvision.html"
license: "Apache-2.0"
mode: "V"
---

By default &mu;Vision enables the use of the debug descriptions if such are specified for the target. It is possible to manually disable the use of the debug descriptions for a specific project target in **Options for Target...** dialog - **Debug** tab - **Settings** button - **Pack** tab. If the item "Enable" is unchecked the debugger will ignore all device descriptions specified in the DFP:



When the use of debug descriptions is enabled various debugger configuration options can becomed locked as specified in the DFP. Section dbg_sqns_uvision_config explains the debugger parameters that can be configured with the debug descriptions.

Disabling the use of debug descriptions can be useful to verify the default debugger behavior on the device.

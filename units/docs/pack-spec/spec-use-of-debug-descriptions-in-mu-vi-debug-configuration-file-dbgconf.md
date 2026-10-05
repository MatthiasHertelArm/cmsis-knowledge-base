---
id: "spec-use-of-debug-descriptions-in-mu-vi-debug-configuration-file-dbgconf"
type: "concept"
domain: "pack"
title: "Use of debug descriptions in &mu;Vision: Debug configuration file (*.dbgconf)"
summary: "If the .pdsc file specifies for the target <debugvars> with the configfile attribute then &mu;Vision automatically creates an instance of debug configuration file for each target in the project by copying the .dbgconf from the specified location in …"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_dbg_setup_tutorial.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/dbg_sqns_uvision.html"
license: "Apache-2.0"
mode: "V"
---

If the .pdsc file specifies for the target `<debugvars>` with the `configfile` attribute then &mu;Vision automatically creates an instance of debug configuration file for each target in the project by copying the *.dbgconf from the specified location in the pack to the `DebugConfig` directory in the application project.



Clicking "Edit" button will open the debug configuration file in &mu;Vision for editing.  If the .dbgconf file is written with the Configuration Wizard annotations the graphical view is available in &mu;Vision providing users with the intuitive configuration interface. For example:

---
id: "spec-use-of-debug-descriptions-in-mu-vi-debug-connect-reset-configuration"
type: "concept"
domain: "pack"
title: "Use of debug descriptions in &mu;Vision: Debug connect & reset configuration"
summary: "μVision debugger provides options to enable and configure debug connect and reset operations. Based on these settings decisions in the debug flow are made as shown in usage_of_sequences."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_dbg_setup_tutorial.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/dbg_sqns_uvision.html"
license: "Apache-2.0"
mode: "V"
---

μVision debugger provides options to enable and configure debug connect and reset operations. Based on these settings decisions in the debug flow are made as shown in usage_of_sequences. Available configuration options depend on the debug adapters, but the approach is similar in most cases. Examples below explain the options available for ULINK and CMSIS-DAP adapters.

Use **Options for Target...** dialog - **Debug** tab - **Settings** button and then in **Connect:** dropdown menu select the option for debugger operation when establishing connection to the target.

Figure below shows how the options "with Pre-reset" and "under Reset" map to the corresponding operations in the connect flow described in usage_of_sequences.



Detailed explanation for available options are can be found in the documentation of corresponding debug adapter. For example for ULINKpro **Connect & Reset Options**

dbg_sqns_uvision_dbg_setting_reset explains the **Reset** dropdown menu in the same area and its mapping to the reset types used in usage_of_sequences.

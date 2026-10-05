---
id: "spec-use-of-debug-descriptions-in-mu-vi-logging-debug-sequences"
type: "concept"
domain: "pack"
title: "Use of debug descriptions in &mu;Vision: Logging debug sequences"
summary: "&mu;Vision can save information about executed debug sequences into a log file. This can be useful when implementing debug sequences or analyzing debugger behavior."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_dbg_setup_tutorial.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/dbg_sqns_uvision.html"
license: "Apache-2.0"
mode: "V"
---

&mu;Vision can save information about executed debug sequences into a log file. This can be useful when implementing debug sequences or analyzing debugger behavior.

The logging can be enabled via **Options for Target...** dialog - **Debug** tab - **Settings** button - **Pack** tab as shown on the figure below. The path and file name cannot be modified.



Note that the log file stores only debug sequences specified in the .pdsc file. The non-overwritten predefined debug sequences do not appear in the log but still get executed by the debugger.


### Debug access log


Detailed information about the debugger operation can be obtained in the debug access log.

It can be enabled in **Options for Target...** dialog - **Debug** tab - **Settings** button as shown on figure below. The file is stored in the project root folder as `<c>` \`<DebugAdapter>`_DebugLog_\`<sequenceNr>`.log</c> file. For example: `ULINKplus_DebugLog_0000.log.`

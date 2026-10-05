---
id: "spec-debug-description-usage-of-debug-access-sequences"
type: "concept"
domain: "pack"
title: "Debug Description: Usage of debug access sequences"
summary: "Predefined Debug Access Sequences are used in the following context: - Connect Debugger to Device is executed when debugging or flash programming with the target starts. - Reset Device is executed to reset the target."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/debug_description.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html"
license: "Apache-2.0"
mode: "V"
---

Predefined Debug Access Sequences are used in the following context:
 - **Connect Debugger to Device** is executed when debugging or flash programming with the target starts.
 - **Reset Device** is executed to reset the target.
 - **Verify Code** is executed to verify the content after flash programming.
 - **Disconnect Debugger** is executed when debugging or flash programming with the target stops.

The following diagrams show how the Debug Access Sequences are executed by a development tool.

**Connect Debugger to Device** is executed when debugging or flash programming with the target starts.



**Reset Device** is executed to reset the target.

The debugger decides whether the CPU is expected to halt after reset. If a halt is expected,
**ResetCatchSet** is called before and **ResetCatchClear** after the reset. Otherwise,
neither sequence is called and the CPU continues to run.

The debugger passes the same decision to the reset sequence in **__connection** bit 18
(set for halt, clear for run).
This indicator allows the reset sequence to coordinate the halt with custom reset or boot hardware,
or to halt the CPU itself; it does not control the reset catch configuration.



**Verify Code** is executed to verify the content after flash programming.



**Disconnect Debugger** is executed when debugging or flash programming with the target stops.

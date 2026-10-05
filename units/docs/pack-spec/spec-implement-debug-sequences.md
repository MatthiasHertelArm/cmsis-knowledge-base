---
id: "spec-implement-debug-sequences"
type: "concept"
domain: "pack"
title: "Implement debug sequences"
summary: "Most Cortex-M devices rely on Arm Debug Interface (ADI) that specifies standard interface for accessing debug functionality on the processor."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_dbg_setup_tutorial.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/dbg_debug_sqns.html"
license: "Apache-2.0"
mode: "V"
---

Most Cortex-M devices rely on Arm Debug Interface (ADI) that specifies standard interface for accessing debug functionality on the processor. However due to implementation-specific variations it can still be challenging for debug tool vendors to provide reliable debugging experience for complex devices. Device vendors can use debug access sequences to customize the debugger behavior for a particular device.

Section usage_of_sequences provides working example flows that can be implemented in a debugger. By overwriting the predefined debug sequences it is possible to customize the debugger operation for a specific device. The syntax and available functions are described in details in  writing_sequences. This chapter explains the common cases that can be covered using debug sequences:
 - dbg_sqns_dbgconf
 - dbg_sqns_errors
 - dbg_sqns_trace
 - dbg_sqns_reset
 - dbg_sqns_boot
 - dbg_sqns_multicore

The examples provided are quite generic demonstrating the concept to follow when addressing a specific scenario. However actual implementation shall always take device specific behavior into account.

---
id: "spec-implement-debug-sequences-ignore-access-errors"
type: "concept"
domain: "pack"
title: "Implement debug sequences: Ignore access errors"
summary: "In some cases the debug access errors need to be ignored to support device-specific implemenation."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_dbg_setup_tutorial.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/dbg_debug_sqns.html"
license: "Apache-2.0"
mode: "V"
---

In some cases the debug access errors need to be ignored to support device-specific implemenation. For that the predefined debug access sequence can be overwritten by duplicating the original code with the error handling disabled in required places using predefined debug access variable __errorcontrol.

Below is an example for an NXP IMXRT1051 family:

```
<sequence name="ResetSystem">
  <block>
    // System Control Space (SCS) offset as defined in Armv6-M/Armv7-M.
    __var SCS_Addr   = 0xE000E000;
    __var AIRCR_Addr = SCS_Addr + 0xD0C;
    __var DHCSR_Addr = SCS_Addr + 0xDF0;

    __errorcontrol = 0x1;     // Skip errors, write to AIRCR.SYSRESETREQ may not be able to finish with OK response
    // Execute SYSRESETREQ via AIRCR
    Write32(AIRCR_Addr, 0x05FA0004);
    __errorcontrol = 0x0;     // Honor errors again

    DAP_Delay(20000);         // Delay of 20ms to let reset finish. Otherwise access to DHCSR can fail with too fast debug units.
  </block>

  //Reset Recovery: Wait for DHCSR.S_RESET_ST bit to clear on read
  <control while="(Read32(DHCSR_Addr) &amp; 0x02000000)" timeout="500000"/>
</sequence>

```

In this implementation the standard system reset via AIRCR temporarily disables the DAP resulting in an access error. That could cause a debugger to disconnect. To overcome this the error handling is disabled before register write (___errorcontrol = 0x1;_) and then enabled after it again. Additionally a delay is introduced (_DAP_Delay(20000);_) to allow reset to complete. The rest of the code is same as in the default resetSystem implementation.

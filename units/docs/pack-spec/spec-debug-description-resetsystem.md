---
id: "spec-debug-description-resetsystem"
type: "concept"
domain: "pack"
title: "Debug Description: Predefined debug access sequences / ResetSystem"
summary: "Part of: Predefined debug access sequences"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/debug_description.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html"
license: "Apache-2.0"
mode: "V"
---

_Part of: Predefined debug access sequences_

Default implementation for **ResetSystem** debug access sequence that executes a system-wide  reset via software mechanisms. Detailed description is provided in the table above.

```
  <sequence name="ResetSystem">
  
    <block>
      // System Control Space (SCS) offset as defined in Armv6-M/Armv7-M.

      __var SCS_Addr   = 0xE000E000;
      __var AIRCR_Addr = SCS_Addr + 0xD0C;
      __var DHCSR_Addr = SCS_Addr + 0xDF0;
    
      // Execute SYSRESETREQ via AIRCR
      Write32(AIRCR_Addr, 0x05FA0004);

      // Delay for 100ms
      DAP_Delay(100000);
    </block>

    <!-- Reset Recovery: Wait for DHCSR.S_RESET_ST bit to clear on read -->
    <control while="(Read32(DHCSR_Addr) &amp; 0x02000000)" timeout="500000"/>
    
  </sequence>
```

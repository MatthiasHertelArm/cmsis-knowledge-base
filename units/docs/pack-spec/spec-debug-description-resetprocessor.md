---
id: "spec-debug-description-resetprocessor"
type: "concept"
domain: "pack"
title: "Debug Description: Predefined debug access sequences / ResetProcessor"
summary: "Part of: Predefined debug access sequences"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/debug_description.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html"
license: "Apache-2.0"
mode: "V"
---

_Part of: Predefined debug access sequences_

Default implementation for **ResetProcessor** debug access sequence that executes a local processor reset via software mechanisms. Detailed description is provided in the table above.

**Note:** This predefined debug access sequence is empty for Armv6-M and Armv8-M based processors.

```
  <sequence name="ResetProcessor">
  
    <block>
      // System Control Space (SCS) offset as defined in Armv7-M.

      __var SCS_Addr   = 0xE000E000;
      __var AIRCR_Addr = SCS_Addr + 0xD0C;
      __var DHCSR_Addr = SCS_Addr + 0xDF0;
    
      // Execute VECTRESET via AIRCR
      Write32(AIRCR_Addr, 0x05FA0001);
    </block>
    
    <!-- Reset Recovery: Wait for DHCSR.S_RESET_ST bit to clear on read -->
    <control while="(Read32(DHCSR_Addr) &amp; 0x02000000)" timeout="500000"/>

  </sequence>
```

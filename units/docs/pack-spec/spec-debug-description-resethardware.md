---
id: "spec-debug-description-resethardware"
type: "concept"
domain: "pack"
title: "Debug Description: Predefined debug access sequences / ResetHardware"
summary: "Part of: Predefined debug access sequences"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/debug_description.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html"
license: "Apache-2.0"
mode: "V"
---

_Part of: Predefined debug access sequences_

Default implementation for **ResetHardware** debug access sequence that executes a system-wide  reset via dedicated debugger reset line. Detailed description is provided  in the table above.

```
  <sequence name="ResetHardware">
    
    <block>
      __var nReset      = 0x80;
      __var canReadPins = 0;
    
      // De-assert nRESET line
      canReadPins = (DAP_SWJ_Pins(0x00, nReset, 0) != 0xFFFFFFFF);
    </block>
    
    <!-- Keep reset active for 50 ms -->
    <control while="1" timeout="50000"/>

    <control if="canReadPins">
    
      <!-- Assert nRESET line and wait max. 1s for recovery -->
      <control while="(DAP_SWJ_Pins(nReset, nReset, 0) &amp; nReset) == 0" timeout="1000000"/>
      
    </control>
    
    <control if="!canReadPins">
    
      <block>
        // Assert nRESET line
        DAP_SWJ_Pins(nReset, nReset, 0);
      </block>
      
      <!-- Wait 100ms for recovery if nRESET not readable -->
      <control while="1" timeout="100000"/>
      
    </control>
    
  </sequence>
```

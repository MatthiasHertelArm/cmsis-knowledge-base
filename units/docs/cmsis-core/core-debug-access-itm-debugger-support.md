---
id: "core-debug-access-itm-debugger-support"
type: "concept"
domain: "core"
title: "Debug Access: ITM Debugger Support"
summary: "A debugger may support a Debug (printf) Viewer window to display data."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_debug.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_debug.txt"
license: "Apache-2.0"
mode: "V"
---

A debugger may support a **Debug (printf) Viewer** window to display data.

**Direction: Microcontroller --> Debugger:**
- Characters received via ITM communication channel 0 are written in a printf-style to the 
**Debug (printf) Viewer** window.
    
**Direction: Debugger --> Microcontroller:**
- Check if ITM_RxBuffer variable is available (only performed once).
- Read the character from the **Debug (printf) Viewer** window.
- If ITM_RxBuffer is empty, write character to ITM_RxBuffer.

**Note:**
The current solution does not use a buffer mechanism for transmitting the characters.

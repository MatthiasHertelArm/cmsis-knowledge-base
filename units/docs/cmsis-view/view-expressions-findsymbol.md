---
id: "view-expressions-findsymbol"
type: "concept"
domain: "trace"
title: "Expressions: __FindSymbol"
summary: "Get address value of a symbol in the user application program."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

Get address value of a symbol in the user application program.

```
int32_t __FindSymbol (symbol_name)
```
- `symbol_name`:       Reference to a symbol (examples: "main", "os_active_TCB", "tasks.c/xSchedulerRunning").
Returns: 
          `address value`  Address of the symbol.

The function searches for a symbol and returns the address value of the symbol in the user application.

**Note:** If the symbol cannot be found, then an error in the \cviewer is displayed.

 rework
**Example:**

**C source file**
```
uint32_t tstack[200/4];      // 200 bytes stack space

void StackTest (void) {
  uint32_t  i;
  
  memset (tstack, 0x8A, sizeof (tstack));
  tstack[0] = 0xE25A2EA5;
  for (i=(200/4)-1; i >= 10; i--)  {
    tstack[i] = i;
  }
}
```

***.SCVD file**
```
<?xml version="1.0" encoding="utf-8"?>
<component_viewer schemaVersion="0.1" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="Component_Viewer.xsd">
  <component name="MyExample" version="1.0.0"/>    <!-- name and version of the component  -->
 
  <objects>
    <object name="MyProgram">
      <var  name="StackStart"  type="int32_t" value="0"  />
      <var  name="StackSize"   type="int32_t" value="0"  />
      <var  name="StackUsage"  type="int32_t" value="0"  />
 
      <calc>
        StackStart = __FindSymbol ("tstack");
        StackSize  = __size_of ("tstack") * 4;
        StackUsage = __CalcMemUsed (StackStart, StackSize, 0x8A8A8A8A, 0xE25A2EA5);
      </calc>
   
      <out name="MyProgram">
        <item alert="(StackUsage >> 31)"    
              property="tstack @%x[StackStart] size=%x[StackSize]"
              value="Usage %x[StackUsage &amp; 0xFFFFF] %d[(StackUsage>>20) &amp; 0xFF]%%" />
      </out>
    </object>
  </objects>
</component_viewer>
```

**Output**
"

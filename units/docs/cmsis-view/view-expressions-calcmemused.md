---
id: "view-expressions-calcmemused"
type: "concept"
domain: "trace"
title: "Expressions: __CalcMemUsed"
summary: "Provide memory usage information for stack area in user application program."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

Provide memory usage information for stack area in user application program.

```
uint32_t __CalcMemUsed 	(uint32_t StackAddress, uint32_t StackSize, uint32_t FillPattern, uint32_t MagicValue) 	
```
- `StackAddress`:    Start address of memory area
- `StackSize`:       Size of memory area in Bytes
- `FillPattern`:     Initial value of memory area, used to identify memory usage
- `MagicValue`:      Initial value at start address of memory area, used to identify memory (stack) overflow

Returns:  A packed 32-bit integer value that indicates memory usage in bytes, in percent, and memory overflow:
            - Bit `0..19`     Used memory in Bytes (how many bytes of **\b** FillPattern are overwritten) 
            - Bit `20..28`    Used memory in percent  (how many percent of **\b** FillPattern are overwritten) 
            - Bit `31`        Memory overflow (**\b** MagicValue is overwritten)


The function provides information about the memory usage of a stack area and is typically applied to calculate the utilization of RTOS thread stacks.
It assumes that the memory has been filled with a pattern value. Optionally there might be a value (called magic value) at the start of the memory 
that is used to detect stack overflows.

**Example 1**

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


**Example 2**

Typical usage with an RTOS thread control block.

```
<component_viewer...>
 
  <typedefs>
    <!-- Task/Thread Control Block, debugger reads 52 bytes -->
    <typedef name="Thread_CB" info="RTOS Task Control Block" size="52">
      :
      <member name="Stack"          type="uint32_t"       offset="44"  info="Pointer to Task Stack memory block"/>
      :
  <!-- Helper variables for Stack-usage calculation -->
       <var  name="StackSize"        type="uint32_t"    />
       <var  name="StkUse"           type="uint32_t"    />
       <var  name="BytesUsed"        type="uint32_t"    />
       <var  name="Percentage"       type="uint32_t"    />
       <var  name="StkOverflow"      type="int32_t"     />
       <var  name="ShowStackInfo"    type="int32_t"     />
     </typedef>
  </typedefs>
 
  </objects>
    <object name="Threads">
       <readlist name="TCB"    type="*Thread_CB"  symbol="os_TCB" based="1" count="10" init="1" />
 
  <!-- Stack Usage Calculation when watermark check is enabled (ShowStackInfo) -->
        <calc cond="TCB[i].ShowStackInfo && ((i != (TCB._count - 1)) && ((stackinfo >> 28) & 0x01))" >
          StkUse               = __CalcMemUsed (TCB[i].Stack, TCB[i].StackSize, 0xCCCCCCCC, 0xE25A2EA5);
          TCB[i].StkOverflow   = (StkUse & 0x80000000) ? 1 : 0;
          TCB[i].StkUse       &= ~0x80000000;
          TCB[i].BytesUsed     = (StkUse & 0xFFFFF);
          TCB[i].Percentage    = (StkUse >> 20) & 0xFF;
        </calc>
     </object>
  </objects>
</component_viewer>
```

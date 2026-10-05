---
id: "view-elemhead-component-viewer-var"
type: "concept"
domain: "trace"
title: "\\elemhead{component_viewer/.../.../var}"
summary: "\\elemhead{component_viewer/.../.../var}"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

**Note:** 
Define variables that are used locally for temporary calculations.
A redefinition of a \elem{var} element using the same **name** is not permitted and creates an error.



| Parent Element | Element Chain |  |  |
|---|---|---|---|
| `<typedef>` | elem_typedef |  |  |
| `<object>` | elem_object |  |  |
| \refelem{elem_list,list} | elem_list |  |  |
| Attributes | Description | Type | Use |
| name | Name of variable. The name can be used in scvd_expression. | xs:string | optional |
| value | Expression that specifies the initial value. | xs:string | optional |
| type | scalar_data_type or pointer to complex_data_type to access chained lists. | xs:string | optional |
| info | Descriptive text with additional information (comment). | xs:string | optional |



**Example:**
```
<component_viewer schemaVersion="0.1" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="Component_Viewer.xsd">
     
  <typedefs>
    <typedef name="DefVars">
      <member name="stack_frame"   type="uint8_t"       offset="37"          info="Stack frame: 0=Basic, 1=Extended, (2=VFP/D16 stacked, 4=NEON/D32 stacked)"/>
      <member name="SP"            type="uint32_t"      offset="40"          info="Current task Stack pointer (R13)"/>
      <member name="Stack"         type="uint32_t"      offset="44"          info="Pointer to Task Stack memory block"/>

      <!-- calculated offset -->
      <member name="Entry"         type="uint32_t"       offset="40 + 8"     info="Thread Entry Address"/>
    </typedef>
  <typedefs>
  
  <objects>
    <object name="VarExamples">
      <!-- indirected read example -->
      <var  name="adr_os_idle_TCB"  type="uint32_t"    value="__FindSymbol (&quot;os_idle_TCB&quot;)"     info="find symbol 'os_idle_TCB', result is the address"/>
      <!-- or -->
      <var  name="adr_os_idle_TCB"  type="uint32_t"    value="__FindSymbol ('os_idle_TCB')" />

      <var  name="array"            type="uint8_t"     size="10"  />
      <var  name="free_space"       type="uint64_t"    value="0x1D9988000" />
    <object>
  
    <object name="ListVars">
      <list name="i" start="0" limit="10" >
        <var  name="j"              type="uint8_t"     value="5"  />
        <calc>
          j += j+i;
        </calc>
      </list>
       
    </object>
  <objects>
   
</component_viewer>
```

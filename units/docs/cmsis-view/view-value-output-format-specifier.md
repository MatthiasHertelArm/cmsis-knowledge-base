---
id: "view-value-output-format-specifier"
type: "concept"
domain: "trace"
title: "Value output: Examples / \\%%  format specifier"
summary: "The following example show how to output a percentage sign."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

_Part of: Examples_

The following example show how to output a percentage sign. 

**C source file**
```
  volatile char string[10] = "MyTest";
  unsigned short wString[15] = L"USB_MSC1";
```

***.SCVD file**
```
<?xml version="1.0" encoding="utf-8"?>
<component_viewer schemaVersion="0.1" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="Component_Viewer.xsd">
  <component name="MyExample" version="1.0.0"/>
 
  <objects>
    <object name="MyProgram">
      <read name="string_val"  type="int8_t"   symbol="string"  size="10"   />
      <read name="wstring_val" type="int16_t"  symbol="wString" size="15"   />
 
      <out name="MyProgram">
        <item property="string %%t"     value="%t[string_val]" /> 
        <item property="string %%t"     value="Status=%t[i_value==0 ? &quot;Free&quot; : &quot;Busy&quot;]" /> 
        <item property="wString %%U"    value="%U[wstring_val]" /> 
      </out>
    </object>
  </objects>
 
</component_viewer>
```

**Output**

The example shows the **%**-sign output in the **Property** column.

" "Output of \% format specifier"

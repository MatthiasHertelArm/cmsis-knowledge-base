---
id: "view-value-output-e-format-specifier"
type: "concept"
domain: "trace"
title: "Value output: Examples / \\%E format specifier"
summary: "The following example shows how to output integer values as symbolic enumerator value."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

_Part of: Examples_

The following example shows how to output integer values as symbolic enumerator value.

**C source file**
```
// <!-- \%E Format Specifier -->	  
enum color { red=1, yellow=2, green=3, };
 
enum color light1;
enum color light2 = yellow;
```

***.SCVD File**
```
<?xml version="1.0" encoding="utf-8"?>
<component_viewer schemaVersion="0.1" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="Component_Viewer.xsd">
  <component name="MyExample" version="1.0.0"/>    <!-- name and version of the component  -->
  
<!-- \%E Format Specifier -->	  
  <typedefs>
    <typedef name="Color"    size="4"      info="enum color">
      <member name="val"     type="uint32_t"   offset="0">
        <enum name="red (alert)"         value="1"     info="alert color"     />
        <enum name="yellow (attention)"  value="2"     info="attention color" />
        <enum name="green (working)"     value="3"     info="working color"   />
      </member>
    </typedef>
  </typedefs>
 
  <objects>
    <object name="MyProgram">
      <!-- \%E Format Specifier -->	  
      <read name="light1"      type="Color"   symbol="light1"       />
      <read name="light2"      type="Color"   symbol="light2"       />
   
      <out name="MyProgram">
        <!-- \%E Format Specifier -->	  
        <item property="Enum format %%E"  value="light1=%E[light1.val] | light2=%E[light2.val]" />
      </out>
    </object>
  </objects>
   
</component_viewer>
```


**Output**
" "Output of \%E format specifiers"

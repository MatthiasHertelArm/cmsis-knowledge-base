---
id: "view-value-output-n-format-specifier"
type: "concept"
domain: "trace"
title: "Value output: Examples / \\%N format specifier"
summary: "The following example show how to output an name string from the target application using the \\%N format specifier."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

_Part of: Examples_

The following example show how to output an name string from the target application using the \%N format specifier.

**C source file**
```
volatile char *name = "MyName";
```

***.SCVD file**
```
<?xml version="1.0" encoding="utf-8"?>
<component_viewer schemaVersion="0.1" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="Component_Viewer.xsd">
  <component name="MyExample" version="1.0.0"/>    <!-- name and version of the component  -->
  
  <objects>
    <object name="MyProgram">
      <read name="name_val"  type="uint32_t"   symbol="name"   />
 
      <out name="MyProgram">
        <item property="name %%N"     value="%N[name_val]" /> 
      </out>
    </object>
  </objects>
   
</component_viewer>
```

 picture incorrect

**Output**
" "Output of \%N format specifier"

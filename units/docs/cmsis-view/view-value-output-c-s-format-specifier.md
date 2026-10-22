---
id: "view-value-output-c-s-format-specifier"
type: "concept"
domain: "trace"
title: "Value output: Examples / \\%C, \\%S format specifier"
summary: "The following example show how to output an address value as symbol that is part of the user application using: - \\%C as symbolic name with file context. - \\%S as symbolic name."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

_Part of: Examples_

The following example show how to output an address value as symbol that is part of the user application using:
 - **\%C** as symbolic name with file context.
 - **\%S** as symbolic name.

**C source file**
```
// <!-- \%C, \%S Format Specifier -->  
static void myFunction (void)  {
   ;
}
 	
typedef  void (*function_t) (void);
function_t myFunction_p = myFunction;
 
int32_t * pival=&sival;
```

***.SCVD file**
```
<?xml version="1.0" encoding="utf-8"?>
<component_viewer schemaVersion="0.1" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="Component_Viewer.xsd">
  <component name="MyExample" version="1.0.0"/>    <!-- name and version of the component  -->
  
  <objects>
    <object name="MyProgram">
      <!-- \%C, \%S Format Specifier -->	  
      <read name="p_func"      type="uint32_t" symbol="myFunction_p"        />
      <read name="p_ival"      type="uint32_t" symbol="pival"               />
  
      <out name="MyProgram">
        <!-- \%C, \%S Format Specifier -->	  
        <item property="Pointer format %%S"   value="myFunction_p=%S[p_func] | pival=%S[p_ival]" />
        <item property="Pointer format %%C"   value="myFunction_p=%C[p_func] | pival=%C[p_ival]" />
      </out>
    </object>
  </objects>
   
</component_viewer>
```

**Output**
" "Output of \%C, %S format specifiers"

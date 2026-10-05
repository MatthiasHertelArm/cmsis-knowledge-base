---
id: "spec-package-eccn-element"
type: "concept"
domain: "pack"
title: "/package/ECCN element"
summary: "A pack may be bound to export control: if so, the pack should provide the related Export Control Classification Numbers (ECCN) for both the United States and the European Union."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pdsc_format.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_ECCN.html"
license: "Apache-2.0"
mode: "V"
---

A pack may be bound to export control: if so, the pack should provide the related Export Control Classification Numbers (ECCN)
for both the United States and the European Union.

This section describes the Export Control Classification Numbers (ECCN)
for the content of the pack for both the US and the EU.
(For more information, please refer to the Commerce Control List (CCL) index)

**Example:**
```
<package>
  ...
  <ECCN>
    <ECCN-EU>NEC</ECCN-EU>
    <ECCN-US>5D992.c</ECCN-US>
  </ECCN>
  ...
</package>
```


 



  | 
    Parent Element | 
    Element Chain | 
  

  | 
    package | 
    element_package | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    ECCN-EU | 
    Defines the Export Control Classification Number for the European Union (EU) | 
    ECCNEUCodeEnum | 
    1..1 | 
  

  | 
    ECCN-US | 
    Defines the Export Control Classification Number for the United States (US) | 
    ECCNUSCodeEnum | 
    1..1 |

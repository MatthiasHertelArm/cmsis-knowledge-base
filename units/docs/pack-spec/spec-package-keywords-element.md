---
id: "spec-package-keywords-element"
type: "concept"
domain: "pack"
title: "/package/keywords element"
summary: "Is the group element for wrapping keywords, which can be used to find a Pack. Keywords can be exported to web pages to provide information for search engines, such as Google."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pdsc_format.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_keywords.html"
license: "Apache-2.0"
mode: "V"
---

Is the group element for wrapping keywords, which can be used to find a Pack.
Keywords can be exported to web pages to provide information for search engines, such as Google.

**Example:**
```
<package>
  ...
  <keywords>
    <keyword>ARM</keyword>
    <keyword>Cortex-M</keyword>
    <keyword>TCP/IP Stack</keyword>
  </keywords>
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
    keyword | 
    Element that encloses one keyword. Enter a keyword between the opening and closing tag of this element. | 
    xs:string | 
    1..1 |

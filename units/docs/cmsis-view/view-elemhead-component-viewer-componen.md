---
id: "view-elemhead-component-viewer-componen"
type: "concept"
domain: "trace"
title: "\\elemhead{component_viewer/component}"
summary: "Define the name of component that is described in this SCVD file. This element specifies also the version of the SCVD file."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

Define the name of component that is described in this SCVD file.  This element specifies also the version of the SCVD file.



  | 
    Parent Element | 
    Element Chain | 
  

  | 
    `<component_viewer>` | 
    elem_component_viewer | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    name | 
    Alphanumeric string identifying the component. Used as menu entry to open viewers. | 
    xs:string | 
    required | 
  

  | 
    version | 
    Alphanumeric string identifying the version of the component description. | 
    xs:string | 
    optional | 
  



**Example:**
```
<component_viewer schemaVersion="0.1" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="Component_Viewer.xsd">
 
  <component name="RTOS" version="1.21.23"/>    <!-- name and version of the component  -->
  ...
</component_viewer>
```

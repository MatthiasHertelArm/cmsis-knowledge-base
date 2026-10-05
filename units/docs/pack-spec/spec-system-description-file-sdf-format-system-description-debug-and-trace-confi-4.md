---
id: "spec-system-description-file-sdf-format-system-description-debug-and-trace-confi-4"
type: "concept"
domain: "pack"
title: "System Description File (*.SDF) Format: /system_description/debug_and_trace_config/trace/trace_capture"
summary: "Describes settings for the trace capture device."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/sdf_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/sdf_pg.html"
license: "Apache-2.0"
mode: "V"
---

Describes settings for the trace capture device.



  | 
    Parents | 
    Element Chain | 
  

  | 
    trace | 
    /system_description/debug_and_trace_config/trace | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    sdf_element_config_item | 
    Describes a configuration item attribute/value pair | 
    complexType | 
    0..* |   
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    type | 
    Trace capture type: for example parallel or HSSTP. | 
    xs:string | 
    required | 
  



\delim

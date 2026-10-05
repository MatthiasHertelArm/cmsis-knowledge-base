---
id: "spec-system-description-file-sdf-format-system-description-platform"
type: "concept"
domain: "pack"
title: "System Description File (*.SDF) Format: /system_description/platform"
summary: "Describes the platform configuration (scanchain, topology and cluster arrangement)."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/sdf_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/sdf_pg.html"
license: "Apache-2.0"
mode: "V"
---

Describes the platform configuration (scanchain, topology and cluster arrangement).



  | 
    Parents | 
    Element Chain | 
  

  | 
    system_description | 
    /system_description | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    sdf_element_scanchain | 
    Lists all DAPs/Devices in the order that they appear on the scanchain (Note - order is reverse to DAP references in PDSC files). The first device in the scanchain is one closest to target's TDI pin. | 
    complexType | 
    0..* |   
  

  | 
    sdf_element_topology | 
    Describes the system topology | 
    complexType | 
    0..1 |   
  

  | 
    sdf_element_clusters | 
    Describes the cluster arrangement | 
    complexType | 
    0..1 |   
  



\delim

---
id: "spec-technical-background-central-api-definition"
type: "concept"
domain: "pack"
title: "Technical background: Central API definition"
summary: "The CMSIS-Pack system allows a central API definition that shares header file information and documentation of an API interface."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_creation.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/cp_Packs.html"
license: "Apache-2.0"
mode: "V"
---

The CMSIS-Pack system allows a central API definition that shares header file information and documentation of an
API interface.



This single API interface definition ensures consistency when it is used across multiple implementations that consume the
interface. The API interface definition can be distributed separately or as part of the software component that consumes this
interface. 

An example is the **CMSIS-Driver** pack that contains various hardware interface drivers that all compatible with the
CMSIS-Driver APIs (that are published in the CMSIS Pack).

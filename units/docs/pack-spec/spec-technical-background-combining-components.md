---
id: "spec-technical-background-combining-components"
type: "concept"
domain: "pack"
title: "Technical background: Combining components"
summary: "When using software components, you can use the conditions to automatically resolve dependencies on other components. Use this to combine components for a project in a certain way, while combining them differently for another project."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_creation.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/cp_Packs.html"
license: "Apache-2.0"
mode: "V"
---

When using software components, you can use the conditions to automatically resolve dependencies on other components. Use
this to combine components for a project in a certain way, while combining them differently for another project. In the
following example, a network stack transfers data via Ethernet. The network stack requires a MAC and PHY to do this. The
selected device from silicon vendor A that contains an on-chip MAC, thus only requiring a PHY to be selected:

 "Example with internal MAC"

You can copy the project, select a different device from silicon vendor B for example and let the run-time environment
manager do the exchange of the components. As the new devices do not have an on-chip MAC, you need to select a different
component to fulfill the requirement for the network stack:

 "Example with external MAC and PHY"

This reduces the development time drastically, as the developer does not need to care for the correct dependency between
software components, but can concentrate on the implementation of his own application code.

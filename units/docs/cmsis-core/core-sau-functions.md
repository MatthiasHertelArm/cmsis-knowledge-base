---
id: "core-sau-functions"
type: "concept"
domain: "core"
title: "SAU Functions"
summary: "Secure Attribution Unit (SAU) functions related to TrustZone for Armv8-M."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_trustzone.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_trustzone.txt"
license: "Apache-2.0"
mode: "V"
---

Secure Attribution Unit (SAU) functions related to TrustZone for Armv8-M.

The Secure Attribution Unit (SAU) functions SAU 

**Note:**
A SAU is always present if the security extension is available.
The functionality differs if the SAU contains SAU regions.
If SAU regions are available is configured with the macro __SAUREGION_PRESENT (see core_config_sect).

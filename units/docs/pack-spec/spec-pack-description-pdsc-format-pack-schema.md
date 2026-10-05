---
id: "spec-pack-description-pdsc-format-pack-schema"
type: "concept"
domain: "pack"
title: "Pack Description (*.pdsc) Format: Pack Schema"
summary: "The XML schema file PACK.xsd defines the sections used in a .pdsc file. The current PACK.xsd can be found in the ARM.CMSIS pack in the directory .\\\\CMSIS\\\\Utilities."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pdsc_format.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/packFormat.html"
license: "Apache-2.0"
mode: "V"
---

The XML schema file **PACK.xsd** defines the sections used in a ***.pdsc** file. The current **PACK.xsd** can be
found in the ARM.CMSIS pack in the directory .\\CMSIS\\Utilities.

The packFormat is structured using grouping elements and contains the following top level elements:
 - 
: describes package related information like vendor, package name, description, version. Is the root element.
 - `<description>`: brief description of the software pack with optional link to Markdown overview documentation.
 - `<ECCN>`: section listing Export Control Classification Numbers (ECCN) for EU and US.
 - `<keywords>`: lists keywords to search for packages. Can be used for search engines.
 - environments: Grouping element for environments information. Each inner environment element may be used to provide tool-specific information pertaining to the package as a whole.
 - `<repository>`: specifies the HTTPS URL and repository type of a public repository where the pack originates from.
 - `<dominate>`: the pack contains one or more device, API, or component that overrules other packs with identical items.
 - `<releases>`: lists release versions with descriptions.
 - `<changelogs>`: lists changelog files associated with components and apis within the pack.
 - `<licenseSets>`: lists license files associated with the pack and contained components and apis.
 - `<requirements>`: lists required packs, compiler, programming language standards and their version or version range.
 - `<taxonomy>`: lists description elements that define component classes and component group names.
 - element_part-taxonomy "
": lists description elements that define part classes and part group names.
 - `<apis>`: describes Application Programming Interfaces (API) Specifications contained in the software pack.
 - `<generators>`: specifies the tools that have been used to generate the PDSC file.
 - `<devices>`: lists the devices supported by this software pack. It specifies the device attributes and
   files like flash programming algorithms, CMSIS device header files, CMSIS System View Descriptions, etc.
 - `<boards>`: lists the development boards supported by the software pack.
 - 
: lists the parts (devices other than the MCUs) supported by the software pack.
 - `<conditions>`: defines dependencies to devices, processors, components, and tools that are used within the software pack.
   It allows making components and files conditional.
 - `<components>`: lists the software components contained in the software pack.
 - `<examples>`: specifies example projects contained in the pack.
 - `<csolution>`: lists pack content that relates to *csolution projects* that are managed using the CMSIS-Toolbox.

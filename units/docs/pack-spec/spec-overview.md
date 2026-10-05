---
id: "spec-overview"
type: "concept"
domain: "pack"
title: "Overview"
summary: "The complete file collection along with the PDSC file is shipped in ZIP-format (renamed to .pack)."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/General.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/Overview.html"
license: "Apache-2.0"
mode: "V"
---

**Open-CMSIS-Pack** describes a delivery mechanism for software components, device parameters, and evaluation board
support. The XML-based package description (PDSC) file describes the content of a software pack (file collection) that
includes:
 -  Source code, header files, and software libraries
 -  Documentation and source code templates
 -  Device parameters along with startup code and programming algorithms
 -  Example projects

The complete file collection along with the PDSC file is shipped in ZIP-format (renamed to *.pack). The PDSC file is designed
for software development environments and describes the user and device relevant context for the files supplied within such
a pack file. This information can also be used for display on web sites (refer to createPackPublish).

The CMSIS-Pack system solves several problems:

- It provides meta-data of files that relate to a software component. All files that belong to a software component can be
  identified and information about the original provider is preserved.
- It enables consistent software component upgrade and identifies incompatible configuration files that may be part of the
  user application.
- Software component providers can specify the interfaces and relationship to other software components.
- The meta-data of a software component can include dependency information for toolchains, devices, and processors which
  simplifies the integration into application programs.

After installing a software pack, all included software components are available to the development
tools. Software components are a collection of source modules, header and configuration files as well as
libraries. Packs containing software components can also include examples and user code templates.

The pack_revisionHistory lists the main changes between versions.

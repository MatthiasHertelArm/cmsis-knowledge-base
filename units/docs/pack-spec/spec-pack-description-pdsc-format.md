---
id: "spec-pack-description-pdsc-format"
type: "concept"
domain: "pack"
title: "Pack Description (*.pdsc) Format"
summary: "The Pack Description (.pdsc) Format uses standard XML annotations and is defined in the schema file PACK.xsd. Software components are distributed through Software Packs."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pdsc_format.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/packFormat.html"
license: "Apache-2.0"
mode: "V"
---

[TOC]

The **Pack Description (*.pdsc) Format**  uses standard XML annotations and is defined in the schema file **PACK.xsd**.
Software components are distributed through **Software Packs**.
A software pack is a zip file containing a single **Pack Description** file that describes
dependencies to devices, processors, tool chains, or other software components.

A descriptive text of the software pack along the text information for devices, components, and examples is part of each
a **Pack Description** (*.pdsc) file. In addition, information is provided which facilitates downloading, updating, and versioning of
of a software pack. The *.pdsc file contains also the complete version history of the software pack
with a brief list of the most significant changes.

---
id: "view-xml-elements"
type: "concept"
domain: "trace"
title: "XML elements"
summary: "The top level elements of an SCVD file are: - <component_viewer> — the root element enclosing all other elements - <component> — defines the component for which the viewer is created - <typedefs> — definitions for data types …"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

The top level elements of an SCVD file are:
 - `<component_viewer>` — the root element enclosing all other elements
 - `<component>` — defines the component for which the viewer is created
 - `<typedefs>` — definitions for data types and structures of the software component.
 - `<objects>` — defines the data collection and the output for software component objects.
 - `<events>` — defines the output for events (system and thread information).

The overall XML structure of an SCVD file is shown below.

 "Example of an SCVD File"

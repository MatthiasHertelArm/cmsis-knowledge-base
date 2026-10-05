---
id: "view-xml-elements"
type: "concept"
domain: "trace"
title: "XML elements"
summary: "The top level elements of an SCVD file are: - <componentviewer> &mdash; the root element enclosing all other elements - <component> &mdash; defines the component for which the viewer is created - <typedefs> &mdash; definitions for data types …"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

The top level elements of an SCVD file are:
 - `<component_viewer>` &mdash; the root element enclosing all other elements
 - `<component>` &mdash; defines the component for which the viewer is created
 - `<typedefs>` &mdash; definitions for data types and structures of the software component.
 - `<objects>` &mdash; defines the data collection and the output for software component objects.
 - `<events>` &mdash; defines the output for events (system and thread information).

The overall XML structure of an SCVD file is shown below.

 "Example of an SCVD File"

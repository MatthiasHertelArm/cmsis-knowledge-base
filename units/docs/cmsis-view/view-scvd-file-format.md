---
id: "view-scvd-file-format"
type: "concept"
domain: "trace"
title: "SCVD file format"
summary: "The SCVD (Software Component View Description) files are formatted in XML and based on the schema file Component_Viewer.xsd."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

The SCVD (Software Component View Description) files are formatted in XML and based on the schema file **Component_Viewer.xsd**.

The SCVD file format is described in the following sections:

 - xml_elements : specifies the structure and top level elements of an SCVD file.
 - Symbol_Access : explains how to refer to application symbols when reading program variables.
 - data_type : lists available scalar data types used in XML elements and explains how complex data types are defined.
 - scvd_expression : describes supported expressions for making calculations in an SCVD file.
 - builtin_function : lists built-in functions that can be used for  calculating stack memory usage, accessing CPU registers or application program symbols.
 - value_output : shows how to format output data for display in the \cviewer or \erecorder.

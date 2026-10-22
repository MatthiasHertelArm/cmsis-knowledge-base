---
id: "view-data-types-complex-data-types"
type: "concept"
domain: "trace"
title: "Data types: Complex Data Types"
summary: "Complex data types are defined using a <typedef> element and can be used in <read>, <readlist>, and <var> elements."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

Complex data types are defined using a `<typedef>` element and
can be used in `<read>`, `<readlist>`, and `<var>` elements.

`<var>` and `<read>` define a single variable or array based on a data type. 

`<readlist>` defines a list of variables or arrays.
The first instance of \`<readlist name="var">` will define 'var', 
the following use of \`<readlist name="var">` will use the definition.

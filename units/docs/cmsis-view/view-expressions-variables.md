---
id: "view-expressions-variables"
type: "concept"
domain: "trace"
title: "Expressions: Variables"
summary: "The SCVD interpreter has the following ways to define local variables that can be used in expressions: - Element <var> in the <typedef> section defines variables which are used in context with typedef, typically for temporary calculations."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

The SCVD interpreter has the following ways to define local variables that can be used in expressions:
  - Element `<var>` in the `<typedef>` section defines variables which are used in context with typedef, typically for temporary calculations.  
    These are automatically generated with `<read>` and `<readlist>`.
  - Element `<var>` in the `<objects>` section defines scalar or array variables.

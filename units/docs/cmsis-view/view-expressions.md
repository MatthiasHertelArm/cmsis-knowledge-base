---
id: "view-expressions"
type: "concept"
domain: "trace"
title: "Expressions"
summary: "The SCVD interpreter has built-in evaluation for expressions that are used in various XML elements and attributes."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

The SCVD interpreter has built-in evaluation for expressions that are used in various XML elements and attributes.
An expression is a combination of operands and expr_operator that evaluate to a resulting value
where the type of the result is derived from the expression.

An operand may be a numeric constant, a variable, a
built-in function,  a predefined variable, or an expression. Operators are
used to combine and compare operands.

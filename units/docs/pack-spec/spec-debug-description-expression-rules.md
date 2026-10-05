---
id: "spec-debug-description-expression-rules"
type: "concept"
domain: "pack"
title: "Debug Description: Writing debug access sequences / Expression rules"
summary: "Part of: Writing debug access sequences"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/debug_description.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html"
license: "Apache-2.0"
mode: "V"
---

_Part of: Writing debug access sequences_

Expressions are used in various places to describe one of the following:
- A value as assigned in a debug access statement.
- A condition to use in the **if** attribute of a **control** element.
- A condition to use in the **while** attribute of a **control** element.
- A parameter to a debug access function as described below.

An expression may consist of the following:
- Constant numbers in decimal and hexadecimal representation (prefix `0x`).
- Arithmetic operators such as `+`, `-`, `*`, `/`, and `%`.
- Bit-arithmetic operators such as `&`, `|`, `~`, `^`, `>>`, and `<<`.
- Comparison-operators such as `==`, `!=`, `<`, `>`, `<=`, and `>=`.
- Logic operators such as `!`, `&&`, `||`, and `==`.
- Conditional expression operations like: \code (x < y) ? a : b \endcode
- Precedence of sub-expressions is indicated by brackets (`(`, `)`). C-like precedence applies 
  if brackets are omitted.
- References to debug access variables for evaluating debug settings.
- Calls to debug access functions.

**Note:**
- All values used in expressions resolve to 64-bit unsigned integer values.
- All logic-operations and comparisons resolve to the value `1` if true, to `0` otherwise.
- XML prohibits the use of the characters `&`, `<`, and `>`. Use the corresponding
  XML entity names instead: `&amp;amp;`, `&amp;lt;`, and `&amp;gt;`.

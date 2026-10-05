---
id: "tfm-fixing-implicit-casting-for-c-enum-strategies-to-fix"
type: "concept"
domain: "security"
title: "Fixing implicit casting for C enumeration values: Strategies to fix"
summary: "0. Replace the enumerated type with an integer type and replace the enumeration constant with preprocessor constants. 1. Whenever possible, try to use matching types to avoid implicit casting."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/software/enum_implicit_casting.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/enum_implicit_casting.html#strategies-to-fix"
license: "BSD-3-Clause"
mode: "V"
---

0. Replace the enumerated type with an integer type and replace the enumeration
   constant with preprocessor constants.
1. Whenever possible, try to use matching types to avoid implicit casting.
   It happens, for example, for arithmetic operations, function calls and
   function returns. This strategy always have the lowest performance impact.
2. When using an enumeration constant in an arithmetic operation with another
   type, verify that the constant can fit in the other type and cast it.
3. When converting an integer to an enumeration type, use a conversion function
   to check if the integer matches an enumeration constant. To not impact
   performance too much, this function should be an inline function. If it does
   not match, use (or add) the error constant or return an error value.
4. When converting an enumeration type to an integer, use a conversion function
   to check that the integer type can contain the enumeration value.

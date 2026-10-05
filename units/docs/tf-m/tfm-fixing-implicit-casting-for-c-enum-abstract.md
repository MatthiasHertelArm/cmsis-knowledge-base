---
id: "tfm-fixing-implicit-casting-for-c-enum-abstract"
type: "concept"
domain: "security"
title: "Fixing implicit casting for C enumeration values: Abstract"
summary: "C enumerations provide a nice way to increase readability by creating new enumerated types but the developer should take extra care when mixing enumeration and integer values."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/software/enum_implicit_casting.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/enum_implicit_casting.html#abstract"
license: "BSD-3-Clause"
mode: "V"
---

C enumerations provide a nice way to increase readability by creating new
enumerated types but the developer should take extra care when mixing
enumeration and integer values.
This document investigates C enumerations safety and proposes strategies on how
to fix the implicit casting of the enumeration values of TF-M with other types.

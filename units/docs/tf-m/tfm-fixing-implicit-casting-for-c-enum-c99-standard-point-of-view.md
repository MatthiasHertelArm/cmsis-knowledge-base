---
id: "tfm-fixing-implicit-casting-for-c-enum-c99-standard-point-of-view"
type: "concept"
domain: "security"
title: "Fixing implicit casting for C enumeration values: C99 Standard point of view"
summary: "In TF-M many implicit casts are done between integer types (uint32_t, int32_t, size_t, etc), enumerated types (enum foobar) and enumeration constants (FOOBAR_ENUM_1)."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/software/enum_implicit_casting.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/enum_implicit_casting.html#c99-standard-point-of-view"
license: "BSD-3-Clause"
mode: "V"
---

In TF-M many implicit casts are done between integer types (`uint32_t`,
`int32_t`, `size_t`, etc), enumerated types (`enum foobar`) and
enumeration constants (`FOOBAR_ENUM_1`).

According to the C99 standard [1]_:

    **§6.2.5, 16**:
    An enumeration comprises a set of named integer constant values. Each
    distinct enumeration constitutes a different numerated type.

    **§6.7.2.2, 2**:
    The expression that defines the value of an enumeration constant shall be an
    integer constant expression that has a value representable as an int.

    **§6.7.2.2, 3**:
    The identifiers in an enumerator list are declared as constants that have
    type int and may appear wherever such are permitted.

    **§6.7.2.2, 4**:
    Each enumerated type shall be compatible with char, a signed integer type,
    or an unsigned integer type. The choice of type is implementation-defined,
    but shall be capable of representing the values of all the members of the
    enumeration.

From these four quotes from the C99 standard [1]_, the following conclusions can
be made:

* an enumeration defines a new type and should be treated as such
* the enumeration constants must only contains value representable as an `int`
* the enumeration constants have type `int`
* the actual type of the enumeration can be between `char`, signed and
  unsigned `int`. The compiler chooses the type it wants among those that can
  represent all declared constants of the enumeration.

Example::
```
enum french_cities {
    MARSEILLE,
    PARIS,
    LILLE,
    LYON
};
```
In that example, `MARSEILLE`, `PARIS`, `LILLE` and `LYON` are
enumeration constants of type `int` and `enum french_cities` is a enumerated
type which can be of actual type `char`, `unsigned int` or `int`
(the compiler chooses!).

For these reasons, doing an implicit cast between an enumeration and another
type is the same as doing an implicit cast between two different types. From a
defensive programming point of view, it should be checked that the destination
type can represent the values from the origin type. In this specific case it
means four things for enumerations:

* it is always safe to assign an enumeration constant to an int, but might be
  better to cast to show intent.
* when casting an enumeration constant to another type, it should be checked
  that the constant can fit into the destination type.
* when casting from an integer type (`uint32_t`, `int32_t`, etc) to an
  enumeration type, it should be checked that the integer's value is one of the
  enumeration constants. The comparison needs to be done on the biggest type of
  the two so that no information is lost. C integer promotion should
  automatically do that for the programmer (check §6.3.1.8, 1 for the rules).
* when casting from an enumeration type to an integer type, it should be checked
  that the enumeration type value fits into the integer type. The value of a
  variable which has the type of an enumeration type is not limited to the
  enumeration constants of the type. An enumeration constant will always fit
  into an `int`.

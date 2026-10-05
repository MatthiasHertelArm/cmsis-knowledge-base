---
id: "abi-procedure-call-standard-for-the-ar-data-types-and-alignment"
type: "concept"
domain: "core"
title: "Procedure Call Standard for the Arm® Architecture: Data Types and Alignment"
summary: "The following table shows the fundamental data types (Machine Types) of the machine. A NULL pointer is always represented by all-bits-zero."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:aapcs32/aapcs32.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/aapcs32/aapcs32.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Fundamental Data Types


The following table shows the fundamental data types (Machine Types) of
the machine.  A NULL pointer is always represented by all-bits-zero.


+----------------+----------------------+-----------+----------------+------------------------------------------------------------+
| Type Class     | Machine Type         | Byte size | Byte alignment | Note                                                       |
+================+======================+===========+================+============================================================+
| Integral       | Unsigned byte        | 1         | 1              | Character                                                  |
|                +----------------------+-----------+----------------+                                                            |
|                | Signed byte          | 1         | 1              |                                                            |
|                +----------------------+-----------+----------------+------------------------------------------------------------+
|                | Unsigned half-word   | 2         | 2              |                                                            |
|                +----------------------+-----------+----------------+                                                            |
|                | Signed half-word     | 2         | 2              |                                                            |
|                +----------------------+-----------+----------------+------------------------------------------------------------+
|                | Unsigned word        | 4         | 4              |                                                            |
|                +----------------------+-----------+----------------+                                                            |
|                | Signed word          | 4         | 4              |                                                            |
|                +----------------------+-----------+----------------+------------------------------------------------------------+
|                | Unsigned double-word | 8         | 8              |                                                            |
|                +----------------------+-----------+----------------+                                                            |
|                | Signed double-word   | 8         | 8              |                                                            |
+----------------+----------------------+-----------+----------------+------------------------------------------------------------+
| Floating       | Half precision       | 2         | 2              | See Half-precision Floating Point.                      |
| Point          +----------------------+-----------+----------------+------------------------------------------------------------+
|                | Single precision     | 4         | 4              | The encoding of floating point numbers is described in     |
|                | (IEEE 754)           |           |                | [ARMARM_] chapter C2, :title-reference:`VFP Programmer's   |
|                +----------------------+-----------+----------------+ Model`, §2.1.1                                             |
|                | Double precision     | 8         | 8              | `Single-precision format`, and            |
|                | (IEEE 754)           |           |                | §2.1.2  `Double-precision format`.        |
+----------------+----------------------+-----------+----------------+------------------------------------------------------------+
| Containerized  | 64-bit vector        | 8         | 8              | See Containerized Vectors.                              |
| vector         +----------------------+-----------+----------------+                                                            |
|                | 128-bit vector       | 16        | 8              |                                                            |
+----------------+----------------------+-----------+----------------+------------------------------------------------------------+
| Pointer        | Data pointer         | 4         | 4              | Pointer arithmetic should be unsigned.                     |
|                +----------------------+-----------+----------------+                                                            |
|                | Code pointer         | 4         | 4              | Bit 0 of a code pointer indicates the target instruction   |
|                |                      |           |                | set type (0 Arm, 1 Thumb).                                 |
+----------------+----------------------+-----------+----------------+------------------------------------------------------------+

#### Half-precision Floating Point


Optional extensions to the Arm architecture provide hardware support
for half-precision values. Three formats are currently supported:

1 - half-precision format specified in IEEE754-2008

2 - Arm Alternative format, which provides additional range but has no NaNs or
Infinities.

3 - Brain floating-point format, which provides a dynamic range similar to the
32-bit floating-point format, but with less precision.

The first two formats are mutually exclusive. The base standard of the AAPCS
specifies use of the IEEE754-2008 variant, and a procedure call variant that
uses the Arm Alternative format is permitted.



#### Containerized Vectors


The content of a containerized vector is opaque to most of the procedure
call standard: the only defined aspect of its layout is the mapping between
the memory format (the way a fundamental type is stored in memory) and
different classes of register at a procedure call interface. If a language
binding defines data types that map directly onto the containerized vectors
it will define how this mapping is performed.


### Endianness and Byte Ordering


From a software perspective, memory is an array of bytes, each of which is
addressable.

This ABI supports two views of memory implemented by the underlying
hardware.

*  In a little-endian view of memory the least significant byte of a data
   object is at the lowest byte address the data object occupies in memory.

*  In a big-endian view of memory the least significant byte of a data
   object is at the highest byte address the data object occupies in memory.

The least significant bit in an object is always designated as **bit 0**.

The mapping of a word-sized data object to memory is shown in
the diagrams below. All objects are pure-endian, so
the mappings may be scaled accordingly for larger or smaller objects
[#aapcs32-f3]_.


### Composite Types


A **Composite Type** is a collection of one or more Fundamental Data
Types that are handled as a single entity at the procedure call level. A
Composite Type can be any of:

*  An **aggregate**, where the members are laid out sequentially in
   memory

*  A **union**, where each of the members has the same address

*  An **array**, which is a repeated sequence of some other type (its
   base type).

The definitions are recursive; that is, each of the types may contain a
Composite Type as a member.

*  The **member alignment** of an element of a composite type is the
   alignment of that member after the application of any language alignment
   modifiers to that member

*  The **natural alignment** of a composite type is the maximum of
   each of the member alignments of the 'top-level' members of the composite
   type i.e. before any alignment adjustment of the entire composite is
   applied


#### Aggregates


*  The alignment of an aggregate shall be the alignment of its most-aligned
   component.

*  The size of an aggregate shall be the smallest multiple of its alignment
   that is sufficient to hold all of its members when they are laid out
   according to these rules.


#### Unions


*  The alignment of a union shall be the alignment of its most-aligned
   component.

*  The size of a union shall be the smallest multiple of its alignment that
   is sufficient to hold its largest member.


#### Arrays


*  The alignment of an array shall be the alignment of its base type.

*  The size of an array shall be the size of the base type multiplied by the
   number of elements in the array.

.. _Bit-fields (data types):


#### Bit-fields


A member of an aggregate that is a Fundamental Data Type may be subdivided
into bit-fields; if there are unused portions of such a member that are
sufficient to start the following member at its natural alignment then the
following member may use the unallocated portion.  For the purposes of
calculating the alignment of the aggregate the type of the member shall be
the Fundamental Data Type upon which the bit-field is based. [#aapcs32-f4]_
The layout of bit-fields within an aggregate is defined by the appropriate
language binding (see Arm C and C++ Language Mappings).


#### Homogeneous Aggregates


A Homogeneous Aggregate is a Composite Type where all of the Fundamental
Data Types that compose the type are the same.  The test for homogeneity is
applied after data layout is completed and without regard to access control
or other source language restrictions.

An aggregate consisting of containerized vector types is treated as
homogeneous if all the members are of the same size, even if the internal
format of the containerized members are different.  For example, a structure
containing a vector of 8 bytes and a vector of 4 half-words satisfies the
requirements for a homogeneous aggregate.

A Homogeneous Aggregate has a Base Type, which is the Fundamental Data Type
of each **Element**.  The overall size is the size of the Base Type
multiplied by the number of Elements; its alignment will be the alignment of
the Base Type.

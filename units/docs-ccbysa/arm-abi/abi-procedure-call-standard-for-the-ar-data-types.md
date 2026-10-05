---
id: "abi-procedure-call-standard-for-the-ar-data-types"
type: "concept"
domain: "core"
title: "Procedure Call Standard for the Arm® Architecture: Arm C and C++ Language Mappings / Data Types"
summary: "Part of: Arm C and C++ Language Mappings"
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:aapcs32/aapcs32.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/aapcs32/aapcs32.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Arm C and C++ Language Mappings_

#### Arithmetic Types


The mapping of C arithmetic types to Fundamental Data Types is shown in
the following table.

.. _Mapping of C & C++ built-in data types:


+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| C/C++ Type                     | Machine Type                            | Notes                                                                  |
+================================+=========================================+========================================================================+
| `char`                       | unsigned byte                           | `LDRB` is unsigned                                                   |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `unsigned char`              | unsigned byte                           |                                                                        |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `signed char`                | signed byte                             |                                                                        |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `[signed] short`             | signed halfword                         |                                                                        |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `unsigned short`             | unsigned halfword                       |                                                                        |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `[signed] int`               | signed word                             |                                                                        |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `unsigned int`               | unsigned word                           |                                                                        |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `[signed] long`              | signed word                             |                                                                        |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `unsigned long`              | unsigned word                           |                                                                        |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `[signed] long long`         | signed double-word                      | C99 Only                                                               |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `unsigned long long`         | unsigned double-word                    | C99 Only                                                               |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `__fp16`                     | half precision (IEEE754-2008 or Arm     | Arm extension documented in [ACLE_].                                   |
|                                | Alternative)                            | In a variadic function call this will be passed as a double-precision  |
|                                |                                         | value.                                                                 |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `__bf16`                     | half precision Brain floating-point     | Arm extension documented in [ACLE_].                                   |
|                                | format                                  |                                                                        |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `float`                      | single precision (IEEE 754)             |                                                                        |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `double`                     | double precision (IEEE 754)             |                                                                        |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `long double`                | double precision (IEEE 754)             |                                                                        |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `float _Imaginary`           | single precision (IEEE 754)             | C99 Only                                                               |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `double _Imaginary`          | double precision (IEEE 754)             | C99 Only                                                               |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
|   `long double _Imaginary`   | double precision (IEEE 754)             | C99 Only                                                               |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `float _Complex`             |      2 single precision (IEEE 754)      | C99 Only.  Layout is                                                   |
|                                |                                         |                                                                        |
|                                |                                         | .. code-block:: c                                                      |
|                                |                                         |                                                                        |
|                                |                                         |    struct { float re;                                                  |
|                                |                                         |             float im; };                                               |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `double _Complex`            |      2 double precision (IEEE 754)      | C99 Only.  Layout is                                                   |
|                                |                                         |                                                                        |
|                                |                                         | .. code-block:: c                                                      |
|                                |                                         |                                                                        |
|                                |                                         |    struct { double re;                                                 |
|                                |                                         |             double im; };                                              |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `long double _Complex`       |      2 double precision (IEEE 754)      | C99 Only.  Layout is                                                   |
|                                |                                         |                                                                        |
|                                |                                         | .. code-block:: c                                                      |
|                                |                                         |                                                                        |
|                                |                                         |    struct { long double re;                                            |
|                                |                                         |             long double im; };                                         |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `_Bool/bool`                 | unsigned byte                           | C99/C++ Only.  False has value 0 and True has value 1.                 |
|                                |                                         |                                                                        |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `wchar_t`                    | see text                                | built-in in C++, typedef in C, type is platform specific               |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `_BitInt(N <= 64)`           | Smallest of the signed Fundamental      | C2x Only.  Significant bits are allocated from least significant end of|
|                                | Integral Data Types where               | the Machine Type.  Non-significant bits within the Machine Type are    |
|                                | byte-size*8 >= N.                       | sign-extended.                                                         |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `unsigned _BitInt(N <= 64)`  | Smallest of the unsigned Fundamental    | C2x Only.  Significant bits are allocated from least significant end of|
|                                | Integral Data Types where               | the Machine Type.  Non-significant bits within the Machine Type are    |
|                                | byte-size*8 >= N.                       | zero-extended.                                                         |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `_BitInt(N > 64)`            | Allocated as if `unsigned int64_t[M]` | C2x Only.  Significant bits are allocated from least significant end of|
|                                | array where M*64 >= N.                  | the Machine Type.  The lower addressed double-word contains the least  |
|                                | Last element contains sign bit.         | significant bits of the type on a little-endian view and the most      |
|                                |                                         | significant bits of the type in a big-endian view.  Non-significant    |
|                                |                                         | bits within the last double-word are sign-extended.                    |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
| `unsigned _Bitint(N > 64)`   | Allocated as if `unsigned int64_t[M]` | C2x Only.  Significant bits are allocated from least significant end of|
|                                | where M*64 >= N.                        | the Machine Type.  The lower addressed double-word contains the least  |
|                                |                                         | significant bits of the type on a little-endian view and the most      |
|                                |                                         | significant bits of the type in a big-endian view.  Non-significant    |
|                                |                                         | bits within the last double-word are zero-extended.                    |
+--------------------------------+-----------------------------------------+------------------------------------------------------------------------+
The preferred type of `wchar_t` is `unsigned int`.  However, a virtual
platform may elect to use `unsigned short` instead.  A platform standard
must document its choice.


#### Pointer Types


The container types for pointer types are shown in the following table.  A
C++ reference type is implemented as a pointer to the type.


+---------------+--------------+----------------------------+
| Pointer Type  | Machine Type | Notes                      |
+===============+==============+============================+
| `T*`        | data pointer | any data type `T`        |
+---------------+--------------+----------------------------+
| `T (*F)()`  | code pointer | any function type `F`    |
+---------------+--------------+----------------------------+
| `T&`        | data pointer | C++ reference              |
+---------------+--------------+----------------------------+

#### Enumerated Types


This ABI delegates a choice of representation of enumerated types to a
platform ABI (whether defined by a standard or by custom and practice) or to
an interface contract if there is no defined platform ABI.

The two permitted ABI variants are:

*  An enumerated type normally occupies a word (`int` or ``unsigned
   int``). If a word cannot represent all of its enumerated values the type
   occupies a double word (`long long` or `unsigned long long`).

*  The type of the storage container for an enumerated type is the smallest
   integer type that can contain all of its enumerated values.

When both the signed and unsigned versions of an integer type can represent
all values, this ABI recommends that the unsigned type should be preferred
(in line with common practice).

The definition of enumerated types in the C and C++ language standards does
not define a binary interface and leaves open the following questions.

*  Does the container for an enumerated type have a fixed size (as expected
   in most OS environments) or is the size no larger than needed to hold the
   values of the enumeration (as expected by most embedded users)?

*  What happens when a (strictly, non-conforming) enumerated value (e.g.
   MAXINT+1) overflows a fixed-size (e.g. `int`) container?

*  Is a value of enumerated type (after any conversion required by C/C++)
   signed or unsigned?

In relation to the last question the C and C++ language standards state:

*  `[C]` Each enumerated type shall be compatible with an integer
   type. The choice of type is implementation-defined, but :emphasis:`shall
   be capable of representing the values of all the members of the
   enumeration`.

*  `[C++]` An enumerated type is `not` an integral type but
   ... An rvalue of...  enumeration type (7.2) can be converted to an rvalue
   of the first of the following types that can represent all the values of
   its underlying type: `int`, `unsigned int`, `long`, or
   `unsigned long`.

Under this ABI, these statements allow a header file that describes the
interface to a portable binary package to force its clients, in a portable,
strictly-conforming manner, to adopt a 32-bit signed (`int`/`long`)
representation of values of enumerated type (by defining a negative
enumerator, a positive one, and ensuring the range of enumerators spans more
than 16 bits but not more than 32).

Otherwise, a common interpretation of the binary representation must be
established by appealing to a platform ABI or a separate interface contract.


#### Additional Types


Both C and C++ require that a system provide additional type definitions
that are defined in terms of the base types.  Normally these types are
defined by inclusion of the appropriate header file.  However, in C++ the
underlying type of `size_t` can be exposed without the use of any header
files simply by using `::operator new()`, and the definition of
`va_list` has implications for the internal implementation in the compiler.
An AAPCS conforming object must use the definitions shown in the following table.


+-------------------+-----------------------+---------------------------------------------------------+
| Typedef           | Base type             | Notes                                                   |
+-------------------+-----------------------+---------------------------------------------------------+
| `size_t`        | `unsigned int`      | For consistent C++ mangling of `::operator new()`     |
+-------------------+-----------------------+---------------------------------------------------------+
| `va_list`       | .. code-block:: c     | A `va_list` may address any object in a parameter     |
|                   |                       | list.  Consequently, the first object addressed may     |
|                   |    struct __va_list { | only have word alignment (all objects are at least word |
|                   |      void *__ap;      | aligned), but any double-word aligned object will       |
|                   |    }                  | appear at the correct double-word alignment in memory.  |
|                   |                       | In C++, `__va_list` is in namespace `std`.          |
+-------------------+-----------------------+---------------------------------------------------------+

#### Volatile Data Types


A data type declaration may be qualified with the `volatile` type
qualifier.  The compiler may not remove any access to a volatile data type
unless it can prove that the code containing the access will never be
executed; however, a compiler may ignore a volatile qualification of an
automatic variable whose address is never taken unless the function calls
`setjmp()`.  A volatile qualification on a structure or union shall be
interpreted as applying the qualification recursively to each of the
fundamental data types of which it is composed.  Access to a
volatile-qualified fundamental data type must always be made by accessing
the whole type.

The behavior of assigning to or from an entire structure or union that
contains volatile-qualified members is undefined.  Likewise, the behavior is
undefined if a cast is used to change either the qualification or the size
of the type.

Not all Arm architectures provide for access to types of all widths; for
example, prior to Arm Architecture 4 there were no instructions to access a
16-bit quantity, and similar issues apply to accessing 64-bit quantities.
Further, the memory system underlying the processor may have a restricted
bus width to some or all of memory.  The only guarantee applying to volatile
types in these circumstances are that each byte of the type shall be
accessed exactly once for each access mandated above, and that any bytes
containing volatile data that lie outside the type shall not be accessed.
Nevertheless, if the compiler has an instruction available that will access
the type exactly it should use it in preference to smaller or larger
accesses.


#### Structure, Union and Class Layout


Structures and unions are laid out according to the Fundamental Data Types
of which they are composed (see Composite Types).  All members are
laid out in declaration order.  Additional rules applying to C++ non-POD
class layout are described in CPPABI32_ and GCPPABI_.

.. _Bit-fields (C mappings):


#### Bit-fields


A bit-field may have any integral type (including enumerated and bool
types).

A sequence of bit-fields is laid out in the order declared using the rules
below.

For each bit-field, the type of its container is:

*  Its declared type if its size is no larger than the size of its declared
   type.

*  The largest integral type no larger than its size if its size is larger
   than the size of its declared type (see Over-sized bit-fields).

The container type contributes to the alignment of the containing aggregate
in the same way a plain (not bit-field) member of that type would, without
exception for zero-sized or anonymous bit-fields.


**Note:** The C++ standard states that an anonymous bit-field is not a member, so it is unclear whether or not an anonymous bit-field of non-zero size should contribute to an aggregate’s alignment. Under this ABI it does.

The content of each bit-field is contained by exactly one instance of its
container type.

Initially, we define the layout of fields that are no bigger than their
container types.


##### Bit-fields no larger than their container


Let `F` be a bit-field whose address we wish to determine. We define
the container address, `CA(F)`, to be the byte address


CA(F) = &(container(F));
This address will always be at the natural alignment of the container type,
that is


CA(F) % sizeof(container(F)) == 0.
The bit-offset of `F` within the container, `K(F)`, is defined in
an endian-dependent manner:

*  For big-endian data types `K(F)` is the offset from the most
   significant bit of the container to the most significant bit of the
   bit-field.

*  For little-endian data types `K(F)` is the offset from the least
   significant bit of the container to the least significant bit of the
   bit-field.

A bit-field can be extracted by loading its container, shifting and masking
by amounts that depend on the byte order, `K(F)`, the container size,
and the field width, then sign extending if needed.

The bit-address of `F`, `BA(F)`, can now be defined as


BA(F) = CA(F) * 8 + K(F)
For a bit address `BA` falling in a container of width `C` and
alignment `A` (≤ `C`) (both expressed in bits), define the
unallocated container bits (`UCB`) to be


UCB(BA, C, A) = C - (BA % A)
We further define the truncation function


TRUNCATE(X,Y) = Y * floor(X/Y)
That is, the largest integral multiple of `Y` that is no larger than
`X`.

We can now define the next container bit address (`NCBA`) which will be
used when there is insufficient space in the current container to hold the next
bit-field as


NCBA(BA, A) = TRUNCATE(BA + A - 1, A)
At each stage in the laying out of a sequence of bit-fields there is:

*  A current bit address (`CBA`)

*  A container size, `C`, and alignment, `A`, determined by the
   type of the field about to be laid out (8, 16, 32, ...)

*  A field width, `W` (≤ `C`).

For each bit-field, `F`, in declaration order the layout is determined
by

1. If the field width, `W`, is zero, set `CBA = NCBA(CBA, A)`

2. If `W > UCB(CBA, C, A)`, set `CBA = NCBA(CBA, A)`

3. Assign `BA(F) = CBA`

4. Set `CBA = CBA + W`.


**Note:** The AAPCS does not allow exported interfaces to contain packed structures or bit-fields.  However a scheme for laying out packed bit-fields can be achieved by reducing the alignment, `A`, in the above rules to below that of the natural container type.  ARMCC uses an alignment of `A=8` in these cases, but GCC uses an alignment of `A=1`.


##### Bit-field extraction expressions


To access a field, `F`, of width `W` and container width `C`
at the bit-address `BA(F)`:

*  Load the (naturally aligned) container at byte address
   `TRUNCATE(BA(F), C) / 8` into a register `R` (or two registers if
   the container is 64-bits)

*  Set `Q = MAX(32, C)`

*  Little-endian, set `R = (R << ((Q - W) - (BA MOD C))) >> (Q - W)`.

*  Big-endian, set `R = (R << (BA MOD C)) >> (Q - W)`.

The long long bit-fields use shifting operations on 64-bit quantities; it may
often be the case that these expressions can be simplified to use operations on
a single 32-bit quantity (but see `Volatile bit-fields – preserving number and
width of container accesses`_).


##### Over-sized bit-fields


C++ permits the width specification of a bit-field to exceed the container
size and the rules for allocation are given in [GCPPABI_].  Using the
notation described above, the allocation of an over-sized bit-field of width
`W`, for a container of width `C` and alignment `A` is
achieved by:

*  Selecting a new container width `C'` which is the width of the
   fundamental integer data type with the largest size less than or equal to
   `W`.  The alignment of this container will be `A'`.  Note that
   `C' ≥ C` and `A' ≥ A`.

*  If `C' > UCB(CBA, C', A')` setting `CBA = NCBA(CBA, A')`.
   This ensures that the bit-field will be placed at the start of the next
   container type.

*  Allocating a normal (undersized) bit-field using the values (`C`,
   `C'`, `A'`)  for (`W`, `C`, `A`).

*  Setting `CBA = CBA + W - C`.


**Note:** Although standard C++ does not have a `long long` data type, this is a common extension to the language.  To avoid the presence of this type changing the layout of oversized bit-fields the above rules are described in terms of the fundamental machine types (Fundamental Data Types) where a 64-bit integer data type always exists.

An oversized bit-field can be accessed simply by accessing its container
type.


##### Combining bit-field and non-bit-field members


A bit-field container may overlap a non-bit-field member.  For the purposes
of determining the layout of bit-field members the `CBA` will be the
address of the first unallocated bit after the preceding non-bit-field type.


**Note:** Any tail-padding added to a structure that immediately precedes a bit-field member is part of the structure and must be taken into account when determining the `CBA`.

When a non-bit-field member follows a bit-field it is placed at the lowest
acceptable address following the allocated bit-field.


**Note:** When laying out fundamental data types it is possible to consider them all to be bit-fields with a width equal to the container size.  The rules in Bit-fields no larger than their container can then be applied to determine the precise address within a structure.


##### Volatile bit-fields – preserving number and width of container accesses


When a volatile bit-field is read, and its container does not overlap with any
non-bit-field member or any zero length bit-field member, its container must be
read exactly once using the access width appropriate to the type of the
container.

When a volatile bit-field is written, and its container does not overlap with
any non-bit-field member or any zero length bit-field member, its container
must be read exactly once and written exactly once using the access width
appropriate to the type of the container. The two accesses are not atomic.


**Note:** This ABI does not place any restrictions on the access widths of bit-fields where the container overlaps with a non-bit-field member or where the container overlaps with any zero length bit-field placed between two other bit-fields. This is because the C/C++ memory model defines these as being separate memory locations, which can be accessed by two threads simultaneously. For this reason, compilers must be permitted to use a narrower memory access width (including splitting the access into multiple instructions) to avoid writing to a different memory location. For example, in `struct S { int a:24; char b; };` a write to `a` must not also write to the location occupied by `b`, this requires at least two memory accesses in all current Arm architectures. In the same way, in `struct S { int a:24; int:0; int b:8; };`, writes to `a` or `b` must not overwrite each other.

Multiple accesses to the same volatile bit-field, or to additional volatile
bit-fields within the same container may not be merged.  For example, an
increment of a volatile bit-field must always be implemented as two reads
and a write.


**Note:** Note the volatile access rules apply even when the width and alignment of the bit-field imply that the access could be achieved more efficiently using a narrower type.  For a write operation the read must always occur even if the entire contents of the container will be replaced.

If the containers of two volatile bit-fields overlap then access to one
bit-field will cause an access to the other.  For example, in ``struct S
{volatile int a:8; volatile char b:2};` an access to `a`` will also
cause an access to `b`, but not vice-versa.

If the container of a non-volatile bit-field overlaps a volatile bit-field
then it is undefined whether access to the non-volatile field will cause the
volatile field to be accessed.

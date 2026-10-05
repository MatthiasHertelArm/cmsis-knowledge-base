---
id: "abi-procedure-call-standard-for-the-ar-appendix-support-for-advanced-simd-exten"
type: "concept"
domain: "core"
title: "Procedure Call Standard for the Arm® Architecture: APPENDIX: Support for Advanced SIMD Extensions and MVE"
summary: "The Advanced SIMD and M-profile Vector Extension to the Arm architecture add support for processing short vectors."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:aapcs32/aapcs32.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/aapcs32/aapcs32.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Introduction


The Advanced SIMD and M-profile Vector Extension to the Arm architecture add
support for processing short vectors. Because the C and C++ languages do not
provide standard types to represent these vectors, access to them is provided
by a vendor extension. The status of this appendix is normative in respect of
public binary interfaces, i.e. the calling convention and name mangling of
functions which use these types. In other respects it is informative.


### SIMD vector data types


Access to the SIMD vector data types is obtained by including either of the two
following header files: `arm_neon.h`, `arm_mve.h`. These headers
provide the following features:

*  They provide a set of user-level type names that map onto short vector
   types

*  They provide prototypes for intrinsic functions that map onto the Advanced
   SIMD and M-profile Vector Extension(MVE) intruction sets respectively.


**Note:** The intrinsic functions are beyond the scope of this specification. Details of the usage of the user-level types (e.g. initialization, and automatic conversions) are also beyond the scope of this specification. For further details see [ACLE_].


**Note:** The user-level types are listed in Advanced SIMD Extension only vector data types using 64-bit containerized vectors and SIMD vector data types using 128-bit containerized vectors. The types have 64-bit alignment and map directly onto the containerized vector fundamental data types. The memory format of the containerized vector is defined as loading the specified registers from an array of the Base Type using the Fill Operation and then storing that value to memory using a single `VSTM` of the loaded 64-bit (D) registers. MVE only allows 128-bit vector types and it uses unsigned integer vectors to represent polynomials. The tables also list equivalent structure types to be used for name mangling. Whether these types are actually defined by an implementation is unspecified.


+------------------+-----------------------------------+----------+-------------------+---------------------------+
| User type name   | Equivalent type name for mangling | Elements | Base type         | Fill operation            |
+==================+===================================+==========+===================+===========================+
| `int8x8_t`     | `struct __simd64_int8_t`        | 8        | signed byte       | `VLD1.8  {Dn}, [Rn]`    |
+------------------+-----------------------------------+----------+-------------------+---------------------------+
| `int16x4_t`    | `struct __simd64_int16_t`       | 4        | signed half word  | `VLD1.16 {Dn}, [Rn]`    |
+------------------+-----------------------------------+----------+-------------------+---------------------------+
| `int32x2_t`    | `struct __simd64_int32_t`       | 2        | signed word       | `VLD1.32 {Dn}, [Rn]`    |
+------------------+-----------------------------------+----------+-------------------+---------------------------+
| `int64x1_t`    | `struct __simd64_int64_t`       | 1        | signed            | `VLD1.64 {Dn}, [Rn]`    |
|                  |                                   |          | double word       |                           |
+------------------+-----------------------------------+----------+-------------------+---------------------------+
| `uint8x8_t`    | `struct __simd64_uint8_t`       | 8        | unsigned byte     | `VLD1.8  {Dn}, [Rn]`    |
+------------------+-----------------------------------+----------+-------------------+---------------------------+
| `uint16x4_t`   | `struct __simd64_uint16_t`      | 4        | unsigned          | `VLD1.16 {Dn}, [Rn]`    |
|                  |                                   |          | half word         |                           |
+------------------+-----------------------------------+----------+-------------------+---------------------------+
| `uint32x2_t`   | `struct __simd64_uint32_t`      | 2        | unsigned word     | `VLD1.32 {Dn}, [Rn]`    |
+------------------+-----------------------------------+----------+-------------------+---------------------------+
| `uint64x1_t`   | `struct __simd64_uint64_t`      | 1        | unsigned          | `VLD1.64 {Dn}, [Rn]`    |
|                  |                                   |          | double word       |                           |
+------------------+-----------------------------------+----------+-------------------+---------------------------+
| `float16x4_t`  | `struct __simd64_float16_t`     | 4        | half precision    | `VLD1.16 {Dn}, [Rn]`    |
|                  |                                   |          | float             |                           |
+------------------+-----------------------------------+----------+-------------------+---------------------------+
| `float32x2_t`  | `struct __simd64_float32_t`     | 2        | single precision  | `VLD1.32 {Dn}, [Rn]`    |
|                  |                                   |          | float             |                           |
+------------------+-----------------------------------+----------+-------------------+---------------------------+
| `poly8x8_t`    | `struct __simd64_poly8_t`       | 8        | 8-bit polynomial  | `VLD1.8  {Dn}, [Rn]`    |
|                  |                                   |          | over GF(2)        |                           |
+------------------+-----------------------------------+----------+-------------------+---------------------------+
| `poly16x4_t`   | `struct __simd64_poly16_t`      | 4        | 16-bit polynomial | `VLD1.16 {Dn}, [Rn]`    |
|                  |                                   |          | over GF(2)        |                           |
+------------------+-----------------------------------+----------+-------------------+---------------------------+

+------------------+-----------------------------------+----------+-------------------+---------------------------+
| User type name   | Equivalent type name for mangling | Elements | Base type         | Fill operation            |
+==================+===================================+==========+===================+===========================+
| `int8x16_t`    | `struct __simd128_int8_t`       | 16       | signed byte       | `VLD1.8  {Qn}, [Rn]`    |
+------------------+-----------------------------------+----------+-------------------+---------------------------+
| `int16x8_t`    | `struct __simd128_int16_t`      | 8        | signed half word  | `VLD1.16 {Qn}, [Rn]`    |
+------------------+-----------------------------------+----------+-------------------+---------------------------+
| `int32x4_t`    | `struct __simd128_int32_t`      | 4        | signed word       | `VLD1.32 {Qn}, [Rn]`    |
+------------------+-----------------------------------+----------+-------------------+---------------------------+
| `int64x2_t`    | `struct __simd128_int64_t`      | 2        | signed            | `VLD1.64 {Qn}, [Rn]`    |
|                  |                                   |          | double word       |                           |
+------------------+-----------------------------------+----------+-------------------+---------------------------+
| `uint8x16_t`   | `struct __simd128_uint8_t`      | 16       | unsigned byte     | `VLD1.8  {Qn}, [Rn]`    |
+------------------+-----------------------------------+----------+-------------------+---------------------------+
| `uint16x8_t`   | `struct __simd128_uint16_t`     | 8        | unsigned          | `VLD1.16 {Qn}, [Rn]`    |
|                  |                                   |          | half word         |                           |
+------------------+-----------------------------------+----------+-------------------+---------------------------+
| `uint32x4_t`   | `struct __simd128_uint32_t`     | 4        | unsigned word     | `VLD1.32 {Qn}, [Rn]`    |
+------------------+-----------------------------------+----------+-------------------+---------------------------+
| `uint64x2_t`   | `struct __simd128_uint64_t`     | 2        | unsigned          | `VLD1.64 {Qn}, [Rn]`    |
|                  |                                   |          | double word       |                           |
+------------------+-----------------------------------+----------+-------------------+---------------------------+
| `float32x4_t`  | `struct __simd128_float32_t`    | 4        | single precision  | `VLD1.32 {Qn}, [Rn]`    |
|                  |                                   |          | float             |                           |
+------------------+-----------------------------------+----------+-------------------+---------------------------+
| `poly8x16_t`   | `struct __simd128_poly8_t`      | 16       | 8-bit polynomial  | `VLD1.8  {Qn}, [Rn]`    |
|                  |                                   |          | over GF(2)        |                           |
+------------------+-----------------------------------+----------+-------------------+---------------------------+
| `poly16x8_t`   | `struct __simd128_poly16_t`     | 8        | 16-bit polynomial | `VLD1.16 {Qn}, [Rn]`    |
|                  |                                   |          | over GF(2)        |                           |
+------------------+-----------------------------------+----------+-------------------+---------------------------+
| `poly64x2_t`   | `struct __simd128_poly64_t`     | 2        | 64-bit polynomial | `VLD1.64 {Qn}, [Rn]`    |
|                  |                                   |          | over GF(2)        |                           |
+------------------+-----------------------------------+----------+-------------------+---------------------------+

#### C++ Mangling


For C++ the mangled name for parameters is as though the equivalent type name
was used.  For example,

```C++

void f(int8x8_t)
```
is mangled as


_Z1f15__simd64_int8_t
.. [#aapcs32-f1]
   This definition of conformance gives maximum freedom to implementers. For
   example, if it is known that both sides of an externally visible
   interface will be compiled by the same compiler, and that the interface
   will not be publicly visible, the AAPCS permits the use of private
   arrangements across the interface such as using additional argument
   registers or passing data in non-standard formats. Stack invariants must,
   nevertheless, be preserved because an AAPCS-conforming routine elsewhere
   in the call chain might otherwise fail. Rules for use of IP must be
   obeyed or a static linker might generate a non-functioning executable
   program.

   Conformance at a publicly visible interface does not depend on what
   happens behind that interface. Thus, for example, a tree of non-public,
   non-conforming calls can conform because the root of the tree offers a
   publicly visible, conforming interface and the other constraints are
   satisfied.

.. [#aapcs32-f2]
   **Data elements** include: parameters to routines named in the
   interface, static data named in the interface, and all data addressed by
   pointer values passed across the interface.

.. [#aapcs32-f3]
   The underlying hardware may not directly support a pure-endian view of data
   objects that are not naturally aligned.

.. [#aapcs32-f4]
   The intent is to permit the C construct `struct {int a:8; char b[7];}`
   to have size 8 and alignment 4.

.. [#aapcs32-f5]
   Although not mandated by this standard, compilers usually formulate the
   address of a static datum by loading the offset of the datum from SB, and
   adding SB to it. Usually, the offset is a 32-bit value loaded PC-relative
   from a literal pool. Usually, the literal value is subject to
   R_ARM_SBREL32-type relocation at static link time. The offset of a datum
   from SB is clearly a property of the layout of an executable, which is fixed
   at static link time. It does not depend on where the data is loaded, which
   is captured by the value of SB at run time.

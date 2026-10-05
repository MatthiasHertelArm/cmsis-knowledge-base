---
id: "abi-procedure-call-standard-for-the-ar-the-standard-variants"
type: "concept"
domain: "core"
title: "Procedure Call Standard for the Arm® Architecture: The Standard Variants"
summary: "This section applies only to non-variadic functions. For a variadic function the base standard is always used both for argument passing and result return."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:aapcs32/aapcs32.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/aapcs32/aapcs32.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

This section applies only to non-variadic functions.  For a variadic
function the base standard is always used both for argument passing and
result return.


### VFP and SIMD vector Register Arguments


This variant alters the manner in which floating-point values are passed
between a subroutine and its caller and allows significantly better
performance when a VFP co-processor, the Advanced SIMD Extension or the
M-profile Vector Extension is present.


#### Mapping between registers and memory format


Values passed across a procedure call interface in VFP registers are laid
out as follows:

*  A half precision floating point type is passed as if it were loaded from
   its memory format into the least significant 16 bits of a single
   precision register.

*  A single precision floating point type is passed as if it were loaded
   from its memory format into a single precision register with `VLDR`.

*  A double precision floating point type is passed as if it were loaded
   from its memory format into a double precision register with `VLDR`.

*  A 64-bit containerized vector type is passed as if it were loaded from
   its memory format into a 64-bit vector register (D\ `n`) with
   `VLDR`.

*  A 128-bit containerized vector type is passed as if it were loaded from
   its memory format into a 128-bit vector register (Q\ `n`) with
   a single `VLDM` of the two component 64-bit vector registers (for
   example, `VLDM r0,{d2,d3}` would load q1).


#### Procedure Calling


The set of call saved registers is the same as for the base standard
(VFP register usage conventions).


##### VFP co-processor register candidates


For the VFP the following argument types are VFP CPRCs.

*  A half-precision floating-point type.

*  A single-precision floating-point type.

*  A double-precision floating-point type.

*  A 64-bit or 128-bit containerized vector type.

*  A Homogeneous Aggregate with a Base Type of a single- or double-precision
   floating-point type with one to four Elements.

*  A Homogeneous Aggregate with a Base Type of 64-bit containerized vectors
   with one to four Elements.

*  A Homogeneous Aggregate with a Base Type of 128-bit containerized vectors
   with one to four Elements.


**Note:** There are no VFP CPRCs in a variadic procedure.

.. _Result return (VFP variant):


##### Result return


Any result whose type would satisfy the conditions for a VFP CPRC is
returned in the appropriate number of consecutive VFP registers starting
with the lowest numbered register (s0, d0, q0).

All other types are returned as for the base standard.

.. _Parameter passing (VFP variant):


##### Parameter passing


There is one VFP co-processor register class using registers s0-s15 (d0-d7) for
passing arguments.

The following co-processor rules are defined for the VFP:


+---------+-------------------------------------------------------------+
| A.2.vfp | The floating point argument registers are marked as         |
|         | unallocated.                                                |
+---------+-------------------------------------------------------------+
| B.3.vfp | Nothing to do.                                              |
+---------+-------------------------------------------------------------+
| C.1.vfp | If the argument is a VFP CPRC and there are sufficient      |
|         | consecutive VFP registers of the appropriate type           |
|         | unallocated then the argument is allocated to the           |
|         | lowest-numbered sequence of such registers.                 |
+---------+-------------------------------------------------------------+
| C.2.vfp |  If the argument is a VFP CPRC then any VFP registers that  |
|         |  are unallocated are marked as unavailable.  The NSAA is    |
|         |  rounded up to the next multiple of 4 if the natural        |
|         |  alignment of the argument is ≤ 4 or the next multiple of 8 |
|         |  if its natural alignment is ≥ 8 and the argument is copied |
|         |  to the stack at the adjusted NSAA.  The NSAA is further    |
|         |  incremented by the size of the argument.  The argument has |
|         |  now been allocated.                                        |
+---------+-------------------------------------------------------------+
Note that the rules require the ‘back-filling’ of unused co-processor
registers that are skipped by the alignment constraints of earlier
arguments.  The back-filling continues only so long as no VFP CPRC has been
allocated to a slot on the stack.


### Arm Alternative Format Half-precision Floating Point values


Code may be compiled to use the Arm Alternative format Half-precision values.
The rules for passing and returning values will either use the Base Standard
rules or the VFP and SIMD vector register rules.


### Read-Write Position Independence (RWPI)


Code compiled or assembled for execution environments that require
read-write position independence (for example, the single address-space
DLL-like model) use a static base to address writable data.  Core register
r9 is renamed as SB and used to hold the static base address: consequently
this register may not be used for holding other values at any time
[#aapcs32-f5]_.


### Variant Compatibility


The variants described in The Standard Variants can produce code that is
incompatible with the base standard.  Nevertheless, there still exist
subsets of code that may be compatible across more than one variant.  This
section describes the theoretical levels of compatibility between the
variants; however, whether a toolchain must accept compatible objects
compiled to different base standards, or correctly reject incompatible
objects, is implementation defined.


#### VFP and Base Standard Compatibility


Code compiled for the VFP calling standard is compatible with the base
standard (and vice-versa) if no floating-point or containerized vector
arguments or results are used, or if the only routines that pass or return
such values are variadic routines.


#### RWPI and Base Standard Compatibility


Code compiled for the base standard is compatible with the RWPI calling
standard if it makes no use of register r9.  However, a platform ABI may
restrict further the subset of code that is usefully compatible.


#### VFP and RWPI Standard Compatibility


The VFP calling variant and RWPI addressing variant may be combined to
create a third major variant.  The appropriate combination of the rules
described above will determine whether code is compatible.


#### Half-precision Format Compatibility


The set of values that can be represented in Arm Alternative format differs from
the set that can be represented in IEEE754-2008 format rendering code built to
use either format incompatible with code that uses the other.
However, most code will make no use of either format and will
therefore be compatible with both variants.

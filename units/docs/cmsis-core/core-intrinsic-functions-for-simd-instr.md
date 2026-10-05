---
id: "core-intrinsic-functions-for-simd-instr"
type: "concept"
domain: "core"
title: "Intrinsic Functions for SIMD Instructions"
summary: "Access to dedicated SIMD instructions available on Armv7E-M (Cortex-M4/M7), Armv8-M Mainline (Cortex-M33/M35P), and Armv8.1-M (Cortex-M55/M85)."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/ref_cm4_simd.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/ref_cm4_simd.txt"
license: "Apache-2.0"
mode: "V"
---

Access to dedicated SIMD instructions available on Armv7E-M (Cortex-M4/M7), Armv8-M Mainline
           (Cortex-M33/M35P), and Armv8.1-M (Cortex-M55/M85).



**Single Instruction Multiple Data (SIMD)** extensions are provided **only for Cortex-M4 and Cortex-M7 cores**
to simplify development of application software. SIMD extensions increase the processing capability
without materially increasing the power consumption. The SIMD extensions are completely transparent
to the operating system (OS), allowing existing OS ports to be used.

**SIMD Features:**

 - Simultaneous computation of 2x16-bit or 4x8-bit operands
 - Fractional arithmetic
 - User definable saturation modes (arbitrary word-width)
 - Dual 16x16 multiply-add/subtract 32x32 fractional MAC
 - Simultaneous 8/16-bit select operations
 - Performance up to 3.2 GOPS at 800MHz
 - Performance is achieved with a "near zero" increase in power consumption on a typical implementation

**Examples:**

**Addition:** Add two values using SIMD function

```
uint32_t add_halfwords(uint32_t val1, uint32_t val2)
{
  return __SADD16(val1, val2);
}
```



**Subtraction:** Subtract two values using SIMD function

```
uint32_t sub_halfwords(uint32_t val1, uint32_t val2)
{
  return __SSUB16(val1, val2);
}
```


**Multiplication:** Performing a multiplication using SIMD function

```
uint32_t dual_mul_add_products(uint32_t val1, uint32_t val2)
{
  return __SMUAD(val1, val2);
}
```

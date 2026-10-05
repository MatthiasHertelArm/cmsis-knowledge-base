---
id: "helium-introduction-cmsis-dsp-additions-replacement"
type: "concept"
domain: "optimization"
title: "Introduction: Audiomark Front-end optimization / CMSIS-DSP additions replacement"
summary: "Part of: Audiomark Front-end optimization"
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:Performance_analysis/ml-dsp-front-end-optimization-with-helium.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/Performance_analysis/ml-dsp-front-end-optimization-with-helium.md#cmsis-dsp-additions-replacement"
license: "Apache-2.0"
mode: "V"
---

_Part of: Audiomark Front-end optimization_

For DSP applications cases like Audiomark ANR/AEC, adding CMSIS-DSP
functions requires a visual source code analysis of the different loops.
Unfortunately, there is no automated procedure allowing to map some of
the suitable DSP operations to CMSIS-DSP API.

Identification and replacement of commonly DSP operations with CMSIS-DSP
operators requires a little bit of experience. It can be assumed that
ARM DSP library, which is heavily used by numerous partners, does not
have any evident miss in its offering, any standard operation will be
present and will have Helium support. As for CMSIS-NN, the library is
actively maintained by ARM, and it is recommended to stay close to
recent releases to get the most exhaustive covering.

Obvious substitutions can be deduced from DSP functions names or source
code documentation highlighting the purpose of the DSP kernel.

Here are few examples taken from Audiomark ANR and AEC

Power spectrum operation:
```C
static inline void power_spectrum(const spx_word16_t *X, spx_word32_t *ps, int N)
{
   int i, j;
   ps[0]=MULT16_16(X[0],X[0]);
   for (i=1,j=1;i<N-1;i+=2,j++)
   {
      ps[j] =  MULT16_16(X[i],X[i]) + MULT16_16(X[i+1],X[i+1]);
   }
   ps[j]=MULT16_16(X[i],X[i]);
}

```

The purpose of this **power_spectrum** routine is to compute the
magnitude squared of the elements of a complex data vector (PS\[i\] =
X\[i\]^2 + Y\[i\]^2)

The LibSpeexDSP basic operators can be derived in fixed or floating
point depending on compile options. Their semantics are tainted with a
fixed-point usage which can be confusing initially.

As mentioned above, the libSpeexDSP FFT sample order implies specific
handling of the first and last sample (DC / FO)

The core loop of this function can be mapped to
**arm_cmplx_mag_squared_f32**.

<https://arm-software.github.io/CMSIS-DSP/latest/group__cmplx__mag__squared.html>

Sample 0 specific operation needs to be handled.

```C
void power_spectrum(const spx_word16_t * X, spx_word32_t * ps, int N)
{
    ps[0] = MULT16_16(X[0], X[0]);
    arm_cmplx_mag_squared_f32(&X[1], ps + 1, N - 1);
}

```

Another example is the recurring call to **mdf_inner_prod** in the AEC
to compute the average energy held in a buffer.

```C
static inline spx_word32_t mdf_inner_prod(const spx_word16_t *x, const spx_word16_t *y, int len)
{
   spx_word32_t sum=0;
   len >>= 1;
   while(len--)
   {
      spx_word32_t part=0;
      part = MAC16_16(part,*x++,*y++);
      part = MAC16_16(part,*x++,*y++);
      // HINT: If you had a 40-bit accumulator, you could shift only at the end
      sum = ADD32(sum,SHR32(part,6));
   }
   return sum;
}

```

This routine can be replaced with **arm_power_f32** if both x and y
inputs are equals or **arm_dot_prod_f32**

- <https://arm-software.github.io/CMSIS-DSP/latest/group__power.html>
- <https://arm-software.github.io/CMSIS-DSP/latest/group__BasicDotProd.html>

Few other obvious substitutions can be found by inspecting loops content
which implement inline vector operations. For example, in ANR, there are
several windowing operations running operations using following
structure:

```C
    for (i=0;i<2*N;i++)
      st->frame[i] = MULT16_16_Q15(st->frame[i], st->window[i]);

```

Such loop can be replaced with **arm_mult_f32** for the floating-point
variant.

Next sample is about ANR computed gain application:

```C
   /* Apply computed gain */
   for (i=1;i<N;i++)
   {
      st->ft[2*i-1] = MULT16_16_P15(st->gain2[i],st->ft[2*i-1]);
      st->ft[2*i] = MULT16_16_P15(st->gain2[i],st->ft[2*i]);
   }
   st->ft[0] = MULT16_16_P15(st->gain2[0],st->ft[0]);
   st->ft[2*N-1] = MULT16_16_P15(st->gain2[N-1],st->ft[2*N-1]);

```

This loop implements a complex multiplication by a real vector
containing the different attenuations weights can be achieved by
**arm_cmplx_mult_real_f32.**

<https://arm-software.github.io/CMSIS-DSP/latest/group__CmplxByRealMult.html>

There are several trivial replacements of addition, multiplication,
subtraction, zeroing loops which can be mapped respectively to
**arm_add_f32/ arm_mult_f32/ arm_sub_f32 / arm_fill_f32**

Conversion of 16-bit integer audio sample to float can be accomplished
using the **arm_q15_to_float** operation.

It can also be noted that recent C compilers like LLVM or Arm Compiler6
are able to auto vectorize such trivial loops.

*Note about fixed-point arithmetic.*

Kernels implemented with Fixed-point are generally more challenging for
vectorizers because requiring efficient idiom recognition capabilities
to map saturation, rounding, scaling to the proper instruction.

Arm Compiler 6 can recognize many of these. For example, here is a Q.15
fixed-point addition and multiplication scalar loops and their generated
Helium vectorized low overhead loop:

- Q.15 addition

```C
  while (blkCnt > 0U) {
    *pDst++ = (q15_t) __SSAT(((q31_t) *pSrcA++ + *pSrcB++), 16);
    blkCnt--;
  }

```

```ASM
.LBB0_4:
        dlstp.16        lr, r3
.LBB0_5:                                @ =>This Inner Loop Header: Depth=1
        vldrh.u16       q0, [r0], #16
        vldrh.u16       q1, [r1], #16
        vqadd.s16       q0, q0, q1
        vstrh.16        q0, [r2], #16
        letp    lr, .LBB0_5

```

- Q.15 multiplication

```C
while (blkCnt > 0U) {
    *pDst++ = (q15_t) __SSAT(((q31_t)*pSrcA++ * *pSrcB++) >> 15, 16);
    blkCnt--;
  }

```

```
.LBB0_4:                                @ %vector.body
        vldrh.u16       q0, [r0], #16
        vldrh.u16       q1, [r1], #16
        vqdmulh.s16     q0, q1, q0
        vstrb.8 q0, [r2], #16
        le      lr, .LBB0_4

```
Rounding variants can also be detected, like rounded average for exampke
(`VRHADD`)


```C
*pDst++ = ((int32_t)*pSrcA++ + *pSrcB++ + 1) >> 1;
```

Will lead to

```ASM
 vrhadd.s16      q0, q0, q1
```

After substituting some of the AEC and ANR loops with CMSIS-DSP kernels,
the Audiomark score continues to grow to `108.98 Audiomark` or `3.40
Audiomarks / Mhz`.

The new global cycle repartition, given by the MDK Performance Analyser is now the
following:

| Audiomark component               |       |
|-----------------------------------|:-------:|
| Neural Net                        | **74.5%** |
| CMSIS-DSP FFT (ABF, MFCC)         | 6.3%  |
| ANR                               | 6.0%  |
| ABF                               | 3.9%  |
| AEC                               | 4.5%  |
| MFCC                              | 0.1%  |
| CMSIS-DSP misc.                   | 3.3%  |
| misc. (memcpy, memset, math.lib.) | 1.3%  |

By summing the CMSIS-NN and CMSIS-DSP kernels contribution it can be
estimated that **84%** of the total Audiomark software is covered by
optimized functions, which still leaves a subset of the remaining 16%
for hand-improvement. This might appear as a relatively low percentage,
but Amdhal’s law reminds us that this could substantially affect the
overall gain brough by Helium.

Important Notes regarding CMSIS DSP additions:

It can be inefficient to issue calls to CMSIS DSP routines using tiny
vector length since function call overhead including stack and loop
handling could be costlier than effective arithmetic processing. Use of
link-time-optimization option could remove this overhead through
inlining.

In addition to this important point, it can be inefficient to cascade
multiple consecutive calls to basic CMSIS DSP routines (e.g. Basic and
Complex Math group) operating on small vector size as requiring several
passes of saving / re-loading of the same data for further processing.
It can be more interesting to create fused variants combining all
operations into one, but this requires some modest amount of
handwriting. This limit, inherent to C language, might be addressed in
future revisions of the DSP libraries, using higher level languages like
C++.

---
id: "helium-introduction-hand-optimization"
type: "concept"
domain: "optimization"
title: "Introduction: Audiomark Front-end optimization / Hand optimization"
summary: "Part of: Audiomark Front-end optimization"
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:Performance_analysis/ml-dsp-front-end-optimization-with-helium.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/Performance_analysis/ml-dsp-front-end-optimization-with-helium.md#hand-optimization"
license: "Apache-2.0"
mode: "V"
---

_Part of: Audiomark Front-end optimization_

Before digging straight into hand-optimization, it is important to
identify remaining hot spots after enabling of ARM optimized NN and DSP
libraries.

MDK Performance Analyser or TARMAC analysis tools can provide statistics about individual
function contribution, but depending on the SW structure, functions
partitioning and compiler inlining decisions, function-level boundary
visibility might not be sufficient.

To increase the level of details concerning cycle repartition it is
possible to:

- Use MDK execution profiler which exposes the total duration associated
  to source code (C or Asm level)

- Prevent function inlining (temporary) by adding compiler specific
  directive like **\_\_attribute\_\_ ((noinline))** supported by Arm
  Compiler, LLVM or GCC.

- Turn loop constructions into small utility functions, with the proper
  (temporary) directive preventing inlining.

By looking at Audiomark functions repartition, after addition of
CMSIS-NN/DSP optimization, top contributing functions are ANR main body
(**speex_preprocess_run**), AEC main body (**speex_echo_cancellation**)
and ABF main body (**ee_abf_f32**).

Most of their subfunctions are inlined when benchmark is compiled with
speed optimization like **Ofast** and do not appear in the function
performance breakdown.

Since these functions are relatively large pieces of SW with many loops
which can be nested, optimization starting point is not obvious at this
stage.

#### MDK Execution profiler

Running Audiomark with the MDK execution profiler exposes time spent by
the CM55 for each line of C code or assembly covered.

Hot spots, which are not surrounded by C functions, can still be visible
by looking at the duration reported by the Execution profiler over
various loop structures.

For example, **699 ms** are spent in one of the echo canceller loops
computing the “*Normal learning rate*” calculation, which, compared to
the total **2.48 seconds**, makes it a good candidate for optimization.

####

#### Turning loops into functions

To get additional insight on the different relative loops contribution,
it can be useful to turn inline loops into individual functions.

This provides following advantages:

- It exposes the loop contribution to the profiler. This still requires
  adding compiler directive to prevent inlining with \_\_attribute\_\_
  ((noinline)) if using AC6/LLVM.

- It eases code / assembly inspection allowing to confirm or not
  auto-vectorization. Additional compiler diagnostic options can give
  hints on what prevent vectorization to succeed (e.g. AC6/LLVM options
  -Rpass=vectorize -Rpass-missed=vectorize -Rpass-analysis=vectorize)

- It allows building simple unit tests to verify hand-optimization
  quality if required.

As seen below, MDK execution profiler identifies one of the hot spot to
be related to Normal learning rate calculation loop. The total
**speex_echo_cancellation** to 2.48 sec and the loop contribution is
**699.2 ms**.



C code extract is the following:

([https://github.com/eembc/Audiomark/blob/main/lib/speexdsp/libspeexdsp/mdf.c](https://github.com/eembc/audiomark/blob/main/lib/speexdsp/libspeexdsp/mdf.c),
line 1230)

```C code
   if (st->adapted)
   {
      /* Normal learning rate calculation once we're past the minimal adaptation phase */
      for (i=0;i<=st->frame_size;i++)
      {
         spx_word32_t r, e;
         /* Compute frequency-domain adaptation mask */
         r = MULT16_32_Q15(st->leak_estimate,SHL32(st->Yf[i],3));
         e = SHL32(st->Rf[i],3)+1;
…
         /*st->power_1[i] = adapt_rate*r/(e*(1+st->power[i]));*/
         st->power_1[i] = FLOAT_SHL(FLOAT_DIV32_FLOAT(r,FLOAT_MUL32U(e,st->power[i]+10)),WEIGHT_SHIFT+16);
      }
   }

```
 
A simple function that will wrap such loop can be created as follows:

```C
void mdf_nominal_learning_rate_calc(spx_word32_t * pRf, spx_word32_t * power, spx_word32_t * pYf, spx_float_t * power_1, spx_word16_t leak_estimate, spx_word16_t RER, uint16_t frame_size)
{
    int             i;

    for (i = 0; i < frame_size; i++) {
        spx_word32_t    r, e;
        /* Compute frequency-domain adaptation mask */
        r = MULT16_32_Q15(leak_estimate, SHL32(pYf[i], 3));
        e = SHL32(pRf[i], 3) + 1;
…
        power_1[i] = FLOAT_SHL(FLOAT_DIV32_FLOAT(r, FLOAT_MUL32U(e, power[i] + 10)), WEIGHT_SHIFT + 16);
    }
}
```

Inline loop will be replaced with a function call:

```C
mdf_nominal_learning_rate_calc(st->Rf, st->power, st->Yf, st->power_1, st->leak_estimate, RER, st->frame_size + 1);
```

For profiling purposes, such functions will have the noinline attribute
to prevent compiler inlining. This attribute will be removed in the
final code. The compiler will decide if inlining is beneficial or not as
long the callee function is visible from its caller source. Link-time
optimization can enable cross-file inlining.

The same process can be repeated for all loops of interests identified
by a profiler.

Audiomark AEC and ANR components are following such approaches and all
the converted loops functions definitions can be found in the following
files:

- lib/speexdsp/libspeexdsp/mfd_opt_generic.c
- lib/speexdsp/libspeexdsp/preprocess_opt_generic.c
- lib/speexdsp/libspeexdsp/filterbank_opt_generic.c

Each Helium optimized function can be individually enabled using
dedicate compile options. Decision on which one to enable depends on
compiler vectorization capabilities and MVE intrinsic handling
performance. More details about this can be found in:

<https://github.com/eembc/Audiomark/tree/main#libspeexdsp-optimizations>

#### Helium Conversion

As mentioned earlier, recent Arm Compilers and LLVM versions can
vectorize loops to apply Helium instructions. Creating small functions
around loops allows one to easily identify which ones can benefit
automatically from compiler optimization without any explicit Helium
additions.

Optimization may still be needed if the compiler involved is not up to
date with the latest Helium vectorization standards and Helium intrinsic
handling which can be found in AC6/LLVM.

As an example, one of the AEC loops, performing smoothing of two signals
implemented the following way:

```C
void smooth_fe_nrg(spx_word32_t * in1, spx_word16_t c1, spx_word32_t * in2, spx_word16_t c2, spx_word32_t * pDst, uint16_t frame_size)
{
    int             j;

    for (j = 0; j <= frame_size; j++)
        pDst[j] = MULT16_32_Q15(c1, in1[j]) + 1 + MULT16_32_Q15(c2, in2[j]);
}
```

Arm Compiler 6.20 or Arm Clang 16.0 using Ofast options will generate
Helium vectorized code:

```ASM
.LBB0_3:
        vmov.f32        q0, #1.000000e+00
        dlstp.32        lr, r4
.LBB0_4:                                @ =>This Inner Loop Header: Depth=1
        vldrw.u32       q1, [r0], #16
        vmov    q2, q0
        vfma.f32        q2, q1, r1
        vldrw.u32       q1, [r2], #16
        vfma.f32        q2, q1, r3
        vstrw.32        q2, [r12], #16
        letp    lr, .LBB0_4
.LBB0_5:
```

*Note*: Wise Helium programmers would observe that the `VMOV`` position is
not optimal. Moving this one before the first vector load would allow to
absorb one stall before the last vector store and the first vector load
of the next iteration.

If benchmark has been compiled with compiler having lagging
auto-vectorization capabilities, loop could make use of MVE intrinsics
and the smoothing routine would be implemented in this following manner:

```C
void smooth_fe_nrg(spx_word32_t * in1, spx_word16_t c1, spx_word32_t * in2, spx_word16_t c2, spx_word32_t * pDst, uint16_t frame_size)
{
    spx_word32_t   *pDst1 = pDst;
    int32_t         blkCnt = frame_size;

    /* Compute 4 outputs at a time */
    while (blkCnt > 0) {
        mve_pred16_t    tpred = vctp32q(blkCnt);
        float32x4_t     vecIn1, vecIn2;
        float32x4_t     vecDst = vdupq_n_f32(1.0f);

        vecIn1 = vld1q_z(in1, tpred);   vecIn2 = vld1q_z(in2, tpred);

        vecDst = vfmaq_m(vfmaq_m(vecDst, vecIn1, c1, tpred), vecIn2, c2, tpred);
        vst1q_p(pDst, vecDst, tpred);
        blkCnt -= 4;

        in1 += 4;       in2 += 4;        pDst += 4;
    }
}
```

*Note*: This implementation uses tail-predicated MVE syntax by converting
loop counter into predicate using `VCTP32Q`, which is then passed to
surrounding intrinsics inside the loop body. At the time of writing, GCC
compiler 13 does not support efficient conversion of tail predicated
loops. A non-predicated variant with extra tail handling will provide
better performance.

There are cases where vectorization process occurs but does not generate
the most optimal code.

As an example, the ANR final Overlap-Add loop is summing two
floating-point signals, saturate, round, convert to 16-bit and store
into a 16-bit integer destination buffer.

```C
void vect_ola(const spx_word16_t * pSrcA, const spx_word16_t * pSrcB, spx_int16_t * pDst, uint32_t blockSize)
{
    int             i;

    for (i = 0; i < blockSize; i++)
        pDst[i] = WORD2INT(ADD32(EXTEND32(pSrcA[i]), EXTEND32(pSrcB[i])));
}
```

Looking at the generated assembly confirms code vectorization, but
saturation/rounding stage does make use of native Helium operators
`VQMOVNBQ`/`VCTAQ_S32_F32` and uses extra compare and select plus
unwanted predicate manipulations.

```ASM
        mov     r4, r0
.LBB0_4:                                @ =>This Inner Loop Header: Depth=1
        vldrw.u32       q2, [r4], #16
        vldrw.u32       q3, [r7], #16
        vadd.f32        q2, q3, q2
        vcmp.f32        ge, q2, r8
        vstr    p0, [sp]                        @ 4-byte Spill
        vldr    p0, [sp]                        @ 4-byte Reload
        vcvt.s32.f32    q3, q2
        vpst
        vcmpt.f32       le, q2, r5
        vpsel   q3, q3, q0
        vldr    p0, [sp]                        @ 4-byte Reload
        vpst
        vcmpt.f32       gt, q2, r5
        vpsel   q2, q1, q3
        vstrh.32        q2, [r6], #8
        le      lr, .LBB0_4
```

The MVE Intrinsic conversion is straightforward once appropriate Helium
operators are in use.

```C
void vect_ola(const spx_word16_t * pSrcA, const spx_word16_t * pSrcB, spx_int16_t * pDst, uint32_t blockSize)
{
    int             i;

    int16x8_t       converted = vdupq_n_s16(0);
    for (i = 0; i < blockSize; i += 4) {
        float32x4_t     vtmp = vld1q(pSrcA) + vld1q(pSrcB);

        converted = vqmovnbq(vuninitializedq(converted), vcvtaq_s32_f32(vtmp));
        vstrhq_s32(pDst, converted);
        pDst += 4;         pSrcA += 4;         pSrcB += 4;
    }
}
```

Finally, there are cases like the **mdf_nominal_learning_rate_calc**
which was identified by the MDK Execution profiler which can
fundamentally not be vectorized as using unsupported Helium features
like vector division or double precision support.

```C
void mdf_nominal_learning_rate_calc(spx_word32_t * pRf, spx_word32_t * power,
                                           spx_word32_t * pYf, spx_float_t * power_1, spx_word16_t leak_estimate, spx_word16_t RER, uint16_t frame_size)
{
    int             i;

    for (i = 0; i < frame_size; i++) {
        spx_word32_t    r, e;
        /* Compute frequency-domain adaptation mask */
        r = MULT16_32_Q15(leak_estimate, SHL32(pYf[i], 3));
        e = SHL32(pRf[i], 3) + 1;
#ifdef FIXED_POINT
        if (r > SHR32(e, 1))
            r = SHR32(e, 1);
#else
        if (r > .5 * e)
            r = .5 * e;
#endif
        r = MULT16_32_Q15(QCONST16(.7, 15), r) + MULT16_32_Q15(QCONST16(.3, 15), (spx_word32_t) (MULT16_32_Q15(RER, e)));
        /*st->power_1[i] = adapt_rate*r/(e*(1+st->power[i])); */
        power_1[i] = FLOAT_SHL(FLOAT_DIV32_FLOAT(r, FLOAT_MUL32U(e, power[i] + 10)), WEIGHT_SHIFT + 16);
    }
}
```

Given that such a loop is still contributing to a non-negligeable part
of the ANR complexity, it is desirable to optimize it.

Removing the double-precision constants which are unneeded here
immediately helps the compiler which can trigger vectorization, except
for the division, which is expected.


```ASM
.LBB0_9:                                @ =>This Inner Loop Header: Depth=1
        vldrw.u32       q5, [r4], #16
        vadd.f32        q5, q5, q1
        vldrw.u32       q4, [r5], #16
        vmul.f32        q4, q4, r11
        vmul.f32        q6, q5, q2
        vminnm.f32      q6, q4, q6
        vmul.f32        q4, q5, r10
        vfma.f32        q4, q6, r9
        vldrw.u32       q6, [r7], #16
        vadd.f32        q6, q6, q3
        vmul.f32        q5, q6, q5
        vdiv.f32        s19, s19, s23
```

With the help of the CMSIS-DSP intrinsic implementing a vector division
emulation (**vdiv_f32**) defined in arm_vec_math.h (and based on the
Newton method, the 4 scalar divisions which are all multicycles on CM55
can be replaced with a faster vector variant.

*Note*: Helium vdiv_f32 division precision might be lower than
`VDIV.F32` therefore it might be important to quantify the deviation.
IEEE-754 compliance might be another point to consider when choosing the
Helium accelerated version. For the Audiomark application, the deviation
introduced by **vdiv_f32** compared to reference is negligeable and ANR
unit test is passing.

The Helium version making use of this **vdiv_f32** operator can be found
below.

```C
void mdf_nominal_learning_rate_calc(spx_word32_t * pRf, spx_word32_t * power,
                                         spx_word32_t * pYf, spx_float_t * power_1, spx_word16_t leak_estimate, spx_word16_t RER, uint16_t len)
{
    int             blockSize = len >> 2;
    float32_t       cst_0_7 = QCONST16(.7, 15);
    float32_t       cst_0_3 = QCONST16(.3, 15);

    do {
        float32x4_t     vecYf = vld1q(pYf);
        float32x4_t     vecRf = vld1q(pRf);

        /* Compute frequency-domain adaptation mask */
        float32x4_t     vecR = vmulq(vecYf, leak_estimate);
        float32x4_t     vecE = vaddq(vecRf, 1.0f);
        float32x4_t     vecEh = vmulq(vecE, 0.5f);

        /* if (r > .5 * e)  r = .5 * e; */
        vecR = vpselq(vecEh, vecR, vcmpgtq(vecR, vecEh));

        vecR = vfmaq(vmulq(vecR, cst_0_7), vmulq(vecE, RER), cst_0_3);

        /*st->power_1[i] = adapt_rate*r/(e*(1+st->power[i])); */
        float32x4_t     vecPwr = vld1q(power);
        vecPwr = vmulq(vecE, vaddq(vecPwr, 10.f));

        vst1q(power_1, vdiv_f32(vecR, vecPwr));

        pRf += 4;
        pYf += 4;
        power += 4;
        blockSize -= 1;
        power_1 += 4;
    }
    while (blockSize > 0);
}
```

#### Effect on score

Adding extra AEC/ANR loop optimizations with Helium allows Audiomark
score to grow from `108.5` or `3.4 Audiomarks / MHz` to `117.4` or
`3.66 Audiomarks / MHz` with a duration of 56.76 seconds.


For a pure Cortex-M55 implementation, without extra side acceleration,
it can be seen that final score is converging.

Adding Helium front-end optimization is no longer paying much and it is
safe to limit further Helium enhancements at this stage.

The DSP front-end / NN back-end repartition is roughly *20* vs *80%*,
equivalent to *11.2* and *45.5* seconds.

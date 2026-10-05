---
id: "helium-introduction-audiomark-initial-profiling"
type: "concept"
domain: "optimization"
title: "Introduction: Initial ML application profiling (Cortex-M only) / Audiomark initial profiling"
summary: "Part of: Initial ML application profiling (Cortex-M only)"
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:Performance_analysis/ml-dsp-front-end-optimization-with-helium.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/Performance_analysis/ml-dsp-front-end-optimization-with-helium.md#audiomark-initial-profiling"
license: "Apache-2.0"
mode: "V"
---

_Part of: Initial ML application profiling (Cortex-M only)_

Using Corstone-300 running on an MPS3 FPGA ([AN552](https://developer.arm.com/documentation/dai0552/latest/)) allows to benefit
from passive profiling thanks to ETM. MDK Performance Analyser provides direct access to
the benchmark cycle repartition.

It is possible to run Audiomark entirely from Corstone-300 AN552 2 x
512Kb TCMs, from Internal SRAM with caches enabled or a mixed
environment. In this case, profiling will guide how to best partitioning
code and data between SRAM and TCMs.

#### Cortex-M55 without Helium

Without Helium, Audiomark DSP and ML repartition is respectively 13 and
87 %. Both are largely benefiting from ARMv7M E DSP SIMD operations
available on most of Cortex-M4, Cortex-M7 and Cortex-M33

This already tells us that the ROI optimizing DSP front-end is low,
efforts trying to optimize the front-end won’t translate in a
significant boost in final benchmark score.

The Audiomark console output reports that test duration is **240.0 seconds**
for running 10 iterations, translating to **7.68 billion** instructions.

The score is around `27.77 Audiomarks`, translating to `0.87 Audiomarks /
Mhz` as MPS3 FPGA is running at 32kHz.

The Neural Networks library contribute **87%** of the total load, so an
equivalent of **208.5** sec and involves following CMSIS-NN kernels.

```
- arm_nn_mat_mult_nt_t_s8
- arm_depthwise_conv_3x3_s8
- arm_nn_mat_mult_kernel_s8_s16
- arm_convolve_s8
- arm_avgpool_s8
- arm_s8_to_s16_unordered_with_offset
```

Main ABF, AEC, ANR and MFCC constitute most of the **13 %** remaining
corresponding to an equivalent of **31.2 sec**. These are making use of
CMSIS-DSP FFT, Basic and Complex maths routines (ABF, MFCC), Kiss-FFT
and few filter bank utility routines for the AEC/ANR.

A long tail of low contributing routines is completing the rest of the
processing load.

MDK Performance Analyser reports following cycle repartition over the entire Audiomark
execution (excluding training phase)

| **sorted**                              | **time** | **unit** | **calls** | **contribution** |
|-----------------------------------------|:----------:|:----------:|:---------:|:-------:|
| **arm_nn_mat_mult_nt_t_s8**             | 129.134  | s        | 2976    | **53.83%** |
| **arm_depthwise_conv_3x3_s8**           | 55.626   | s        | 2976    | **23.19%** |
| **arm_nn_mat_mult_kernel_s8_s16**       | 19.024   | s        | 46128   | **7.93%**  |
| **speex_echo_cancellation**             | 4.73     | s        | 930     | 1.97%  |
| **kf_work**                             | 4.295    | s        | 41099   | 1.79%  |
| **speex_preprocess_run**                | 3.494    | s        | 930     | 1.46%  |
| **arm_convolve_s8**                     | 3.354    | s        | 744     | **1.40%**  |
| **ee_abf_f32**                          | 2.989    | s        | 933     | 1.25%  |
| **arm_radix8_butterfly_f32**            | 2.424    | s        | 23064   | 1.01%  |
| **kf_shuffle**                          | 1.582    | s        | 897668  | 0.66%  |
| **arm_cmplx_mult_cmplx_f32**            | 1.58     | s        | 64625   | 0.66%  |
| **\_\_rt_memcpy**                       | 1.571    | s        | 3166397 | 0.65%  |
| **arm_avgpool_s8**                      | 1.135    | s        | 744     | **0.47%**  |
| **kiss_fftr2**                          | 676.409  | ms       | 5586    | 0.28%  |
| **arm_bitreversal_32**                  | 673.855  | ms       | 11904   | 0.28%  |
| **arm_cmplx_dot_prod_f32**              | 597.132  | ms       | 241800  | 0.25%  |
| **kiss_fftri2**                         | 507.789  | ms       | 4728    | 0.21%  |
| **arm_cmplx_mag_f32**                   | 456.814  | ms       | 4464    | 0.19%  |
| **arm_cmplx_conj_f32**                  | 450.293  | ms       | 249176  | 0.19%  |
| **arm_cfft_radix8by2_f32**              | 420.01   | ms       | 11160   | 0.18%  |
| **\_\_hardfp_cos**                      | 343.479  | ms       | 34049   | 0.14%  |
| **kiss_fft_alloc**                      | 342.894  | ms       | 35460   | 0.14%  |
| **spx_fft**                             | 322.079  | ms       | 5588    | 0.13%  |
| **arm_s8_to_s16_unordered_with_offset** | 276.032  | ms       | 93000   | **0.12%**  |
| **stage_rfft_f32**                      | 250.08   | ms       | 744     | 0.10%  |
| **filterbank_compute_psd16**            | 247.051  | ms       | 3061    | 0.10%  |
| **preprocess_analysis**                 | 210.553  | ms       | 937     | 0.09%  |
| **filterbank_compute_bank32**           | 209.734  | ms       | 1977    | 0.09%  |


The non-Helium CMSIS-NN / DSP library used in Audiomark are already
benefiting from ARMv7M-E DSP acceleration supporting dual 16-bit
MAC operation and providing already good uplift compared to the baseline
version. The paper CMSIS-NN: [Efficient Neural Network Kernels for Arm
Cortex-M CPUs](https://arxiv.org/pdf/1801.06601.pdf) describes some of
the key optimizations concepts leveraging DSP instructions, which have
been applied in the original CMSIS-NN version. The operators and data
format in use in this document are no longer in use and have been
superseded with TFLu ones, but the optimization strategies are still
valid.

This optimized code is surrounded by the `ARM_MATH_DSP` compilation
defined directive which is automatically picked by the compiler when
using an Arm MCU having DSP option is available.

#### Cortex-M55 with Helium

Enabling Helium SIMD allows a drastic benchmark duration reduction from
**240** down to **67.3 sec** for 10 iterations and a score growing to `99.06
Audiomark`, equivalent to `3.1 Audiomarks / Mhz` on MPS3.

This gain comes mainly from the vectorization of the CMSIS-NN and DSP
libraries. By using the Cortex-M55 CPU option the compiler will
automatically pick the Helium variants of the libraries.

These are surrounded by `ARM_MATH_MVEI` or `ARM_MATH_MVEF` compilation
defined directives denoting Helium with integer or floating-point data
type.

Half-floating point Helium kernels are surrounded by
`ARM_MATH_MVE_FLOAT16` directives, but these are one in used in current
Audiomark version.

The KWS Neural network part is entirely built with CMSIS-NN kernels,
meaning that all its parts will get accelerated.

On the contrary, the DSP front-end is not a pure aggregate of DSP
library routines, and, as a result, Helium acceleration will be
initially constrained only to parts which are making use of CMSIS-DSP
APIs like the Real FFT or the Complex vector operations, like
multiplication, transpose, and dot inside the ABF.

In addition, 8-bit arithmetic operations heavily used inside the Neural
networks will generally get a bigger boost than single-precision
arithmetic operations used in the DSP front-end kernels.

Combining these 2 effects, explains why DSP front-end contribution ratio
will increase when Helium gets enabled.

Running Audiomark with the MDK Performance Analyser shows that Neural Networks libraries
are now contributing to **67.7 %** of the total load, equivalent of **45.6 sec**
and its top contributing functions are:

```
- arm_nn_mat_mult_nt_t_s8
- arm_nn_depthwise_conv_nt_t_s8
- arm_depthwise_conv_s8_opt
- arm_convolve_s8
- arm_avgpool_s8
```

By comparing the Neural Network processing durations, with and without
Helium, we can quantify the Helium improvement by a factor of `4.6` (208.5
divided by 45.6 sec)

Most of the TFL-u operators will always be handled in an optimized
manner inside CMSIS-NN library and we don’t expect SW developers to
re-implement these by themselves or re-improve these further without
prior checking with ARM.

New APIs are continuously being added and updated, so it’s important to
stay close to the latest releases of the CMSIS-NN library.

##### arm_nn_mat_mult_nt_t_s8 optimizations

Here we will describe a typical Helium optimization as applied in the
CMSIS-NN library and focus on the top contributing kernel involved in
the Audiomark DS-CNN, reported by the MDK Performance Analyser: the
**arm_nn_mat_mult_nt_t_s8 s8** matrix multiplication with the transposed
right-hand-side (RHS) matrix utility function. Source code can be found
in CMSIS-NN git repository inside ARM-software.

<https://github.com/ARM-software/CMSIS-NN/blob/main/Source/NNSupportFunctions/arm_nn_mat_mult_nt_t_s8.c>

Without Helium, the inner loop optimization technique is based on the
maximization of ARMv7M-E dual 16-bit mac operations (`SMLAD`) and
minimization of 8-bit to 16-bit extensions (`SXTB16`) by minimizing reload
occurrences of matrix elements and work on expanded elements inside the
general-purpose registers (GPRS). To make optimal use of the GPRS, the
loop is heavily unrolled to process blocks of 2x16 matrix inputs and to
generate 2x2 matrix outputs.

The inner loop extract can be found below:

```C
for (; rhs_cols_idx <= (rhs_cols - 16); rhs_cols_idx += 16)
{
    val1 = arm_nn_read_s8x4_ia((const int8_t **)&rhs_ptr);
    val0 = arm_nn_read_s8x4_ia((const int8_t **)&lhs_ptr);

    val2 = SXTB16(val1);            val3 = SXTB16(val0);
    val1 = SXTB16_RORn(val1, 8);    val0 = SXTB16_RORn(val0, 8);

    res00 = SMLAD(val3, val2, res00);
    res00 = SMLAD(val0, val1, res00);

    val4 = arm_nn_read_s8x4((const int8_t *)&rhs_ptr[rhs_off0]);
    val5 = SXTB16(val4);            val4 = SXTB16_RORn(val4, 8);

    res01 = SMLAD(val3, val5, res01);
    res01 = SMLAD(val0, val4, res01);

```

Ignoring the loop handling overhead, the inner loop runs in
approximately **80 cycles** and process 32 dual 16-bit MAC operations, hence a MAC cost of
**1.25 cycle per MAC**.

The Helium version of the **arm_nn_mat_mult_nt_t_s8 s8** operates in a
slightly different manner as does not require the extra complexity
needed to fully benefit from the in-register SIMD capability.

It simply runs operations on 4 adjacent rows consisting of four 8-bit
vector load (`VLDRB`) for the left-hand side rows, one vector load for the
right-hand side columns and four 8-bit dot-product (`VMLADAVA`).

It is also opportunistically computing the summation over the RHS-matrix
column which is used later for quantization (`VADDVA`).

The inner loop structure of the Helium variant can be found below:

```ASM
   vldrb.8         q0, [%[col]], #16
2:
   vaddva.s8      %[sum], q0
   vldrb.8         q1, [%[row0]], #16
   vmladava.s8    %[out0], q0, q1
   vldrb.8         q2, [%[row1]], #16
   vmladava.s8     %[out1], q0, q2
   vldrb.8         q3, [%[row2]], #16
   vmladava.s8     %[out2], q0, q3
   vldrb.8         q4, [%[row3]], #16
   vmladava.s8     %[out3], q0, q4
   vldrb.8         q0, [%[col]], #16
   letp            lr, 2b
1:

```


ARMv8.1-M provides low overhead loop handling, therefore total loop cost
after the first iteration is **10 cycles** to process 4 x 16 8-bit MAC,
hence a MAC cost of **0.1562 cycle per MAC**, which is an 8 times boost over the
scalar version.

It can be noted that such loop is a good target for auto-vectorizer and
a plain C form as follow can be used:

```C++
for (int j = 0; j < rhs_cols; j++)
{
    int32_t col = col_base[j];
    sum_tmp += col;
    acc_n0 += lhs_vec[j] * col;
    acc_n1 += ip_row_1[j] * col;
    acc_n2 += ip_row_2[j] * col;
    acc_n3 += ip_row_3[j] * col;
}

```

*Note about Cortex-M55 Helium loop performance analysis*

Tools like [LLVM-MCA](https://www.llvm.org/docs/CommandGuide/llvm-mca.html) are able to give some interesting hints about loop performance by providing static scheduling information as seen by the compiler. The level of precision can differ from real behavior and **LLVM-MCA** does not track some of the dynamic behaviors like memory alignement, DTCM bank conflicts and others, but the tool remains usefull for a quick analysis pass over specific loops.

For this particular **arm_nn_mat_mult_nt_t_s8 s8** loop, where Helium instructions are perfectly distributed between load and artimetic units an IPC of 1 should be expected and is confirmed by **LLVM-MCA**.

```bash
llvm-mca -mtriple=arm-none-eabi -mcpu=cortex-m55 arm_nn_mat_mult_nt_t_s8_loop.s --all-view
```

```
Dispatch Width:    2
uOps Per Cycle:    1.00
IPC:               1.00 <<<
Block RThroughput: 10.0
```

**LLVM-MCA** is also able to reveal the interleaving of the loop instructions dispatched betwwen the Cortex-M55 Helium Units and a timeline showing that no stall occurs.
Details about Cortex-M55 unit partitioning can be found in the [Arm® Cortex®-M55 Processor Software Optimization Guide](https://documentation-service.arm.com/static/63ac5ce1396e6135830ba9fe)

```
Resources:
[0]   - M55UnitALU
[1]   - M55UnitLoadStore
[2]   - M55UnitVecALU
[3]   - M55UnitVecFPALU
[4]   - M55UnitVecSys


Resource pressure per iteration:
[0]    [1]    [2]    [3]    [4]
 -     10.00   -     10.00   -

Resource pressure by instruction:
[0]    [1]    [2]    [3]    [4]    Instructions:
 -     2.00    -      -      -     vldrb.u8     q0, [r0], #16
 -      -      -     2.00    -     vaddva.s8    r2, q0
 -     2.00    -      -      -     vldrb.u8     q1, [r1], #16
 -      -      -     2.00    -     vmlava.s8    r4, q0, q1
 -     2.00    -      -      -     vldrb.u8     q2, [r5], #16
 -      -      -     2.00    -     vmlava.s8    r6, q0, q2
 -     2.00    -      -      -     vldrb.u8     q3, [r7], #16
 -      -      -     2.00    -     vmlava.s8    r8, q0, q3
 -     2.00    -      -      -     vldrb.u8     q4, [r9], #16
 -      -      -     2.00    -     vmlava.s8    r10, q0, q4


Timeline view:
                    0123456789          0123456789          0123456789          0123456789
Index     0123456789          0123456789          0123456789          0123456789

[0,0]     DE   .    .    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vldrb.u8   q0, [r0], #16
[0,1]     .DeE .    .    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vaddva.s8  r2, q0
[0,2]     . DE .    .    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vldrb.u8   q1, [r1], #16
[0,3]     .  DeE    .    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vmlava.s8  r4, q0, q1
[0,4]     .   DE    .    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vldrb.u8   q2, [r5], #16
[0,5]     .    DeE  .    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vmlava.s8  r6, q0, q2
[0,6]     .    .DE  .    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vldrb.u8   q3, [r7], #16
[0,7]     .    . DeE.    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vmlava.s8  r8, q0, q3
[0,8]     .    .  DE.    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vldrb.u8   q4, [r9], #16
[0,9]     .    .   DeE   .    .    .    .    .    .    .    .    .    .    .    .    .   .   vmlava.s8  r10, q0, q4
[1,0]     .    .    DE   .    .    .    .    .    .    .    .    .    .    .    .    .   .   vldrb.u8   q0, [r0], #16
[1,1]     .    .    .DeE .    .    .    .    .    .    .    .    .    .    .    .    .   .   vaddva.s8  r2, q0
[1,2]     .    .    . DE .    .    .    .    .    .    .    .    .    .    .    .    .   .   vldrb.u8   q1, [r1], #16

```

##### CMSIS-NN Helium optimization

As for the **arm_nn_mat_mult_nt_t_s8**, the CMSIS-NN contains native
Helium optimization for most of the typical neural network kernels and
tracks operator format and quantization specifications of TFLu

The complete list of Helium optimizer kernels can be found in
<https://github.com/ARM-software/CMSIS-NN/#mve-extension>

Unless exceptions, like use of alternative data format like single or
half-precision float, it is not expected for SW developers to
re-implement and re-optimize NN kernels with Helium Neural network by
hand.

TFL-u is still evolving, new operators are continuously being added in
the framework, so it’s important to stay close to the latest CMSIS-NN
releases to benefit from Helium accelerated variants.

Some of the recent improvements can be tracked on github [Issues ·
ARM-software/CMSIS-NN ·
GitHub](https://github.com/ARM-software/CMSIS-NN/issues?q=label%3Aimprovement+)

CMSIS-NN is also taking care of compilers having suboptimal Helium
performance like GCC versions lower than version 13.0 by using inline
assembly for selected important kernels.

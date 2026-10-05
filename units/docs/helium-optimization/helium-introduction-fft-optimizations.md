---
id: "helium-introduction-fft-optimizations"
type: "concept"
domain: "optimization"
title: "Introduction: ML application optimization with Ethos-U55 / FFT optimizations"
summary: "Part of: ML application optimization with Ethos-U55"
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:Performance_analysis/ml-dsp-front-end-optimization-with-helium.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/Performance_analysis/ml-dsp-front-end-optimization-with-helium.md#fft-optimizations"
license: "Apache-2.0"
mode: "V"
---

_Part of: ML application optimization with Ethos-U55_

CMSIS-DSP Complex FFT and Real FFT which are the second top contributing
functions could benefit from additional optimizations related to some
advantages provided by hand assembly.

Arm Compiler and CLANG are very good at handling Helium Intrinsic based
SW which is found in the CMSIS-DSP library, but there are some tricky
categories of optimizations which cannot be handled by compilers. In the
case of the FFT, reaching optimum point in the Radix-4 kernel requires
making use of software pipelining which is one of the tasks which is
typically too complex to be solved optimally.

For the compiled CFFT Radix-4 loop, **LLVM-MCA** shows an IPC of `0.78`

```
Dispatch Width:    2
uOps Per Cycle:    0.78
IPC:               0.78
Block RThroughput: 28.0

```
It also reveals presence of several adjacent Helium instructions belonging to the same group and which would lead to structural Hazards.

```
Resources:
[0]   - M55UnitALU
[1]   - M55UnitLoadStore
[2]   - M55UnitVecALU
[3]   - M55UnitVecFPALU
[4]   - M55UnitVecSys


Resource pressure per iteration:
[0]    [1]    [2]    [3]    [4]
 -     22.00   -     28.00   -

Resource pressure by instruction:
[0]    [1]    [2]    [3]    [4]    Instructions:
 -     2.00    -      -      -     vldrw.u32    q0, [r1]
 -     2.00    -      -      -     vldrw.u32    q1, [r9]
 -      -      -     2.00    -     vadd.f32     q3, q1, q0
 -     2.00    -      -      -     vldrw.u32    q2, [r11]
 -      -      -     2.00    -     vsub.f32     q0, q1, q0
 -     2.00    -      -      -     vldrw.u32    q4, [r10]
 -      -      -     2.00    -     vadd.f32     q5, q4, q2
 -      -      -     2.00    -     vadd.f32     q6, q5, q3
 -     2.00    -      -      -     vstrb.8      q6, [r9], #16
 -      -      -     2.00    -     vsub.f32     q3, q3, q5
 -     2.00    -      -      -     vldrw.u32    q5, [r5], #16
 -      -      -     2.00    -     vcmul.f32    q6, q5, q3, #0
 -      -      -     2.00    -     vcmla.f32    q6, q5, q3, #270
 -     2.00    -      -      -     vstrb.8      q6, [r11], #16
 -      -      -     2.00    -     vsub.f32     q1, q2, q4
 -     2.00    -      -      -     vldrw.u32    q3, [r0], #16
 -      -      -     2.00    -     vcadd.f32    q2, q0, q1, #270
 -      -      -     2.00    -     vcmul.f32    q4, q3, q2, #0
 -      -      -     2.00    -     vcmla.f32    q4, q3, q2, #270
 -     2.00    -      -      -     vstrb.8      q4, [r1], #16
 -      -      -     2.00    -     vcadd.f32    q2, q0, q1, #90
 -     2.00    -      -      -     vldrw.u32    q0, [r6], #16
 -      -      -     2.00    -     vcmul.f32    q1, q0, q2, #0
 -      -      -     2.00    -     vcmla.f32    q1, q0, q2, #270
 -     2.00    -      -      -     vstrb.8      q1, [r10], #16

```

Effect on the timeline can be visualized as well. Even if estimated timing are differing from real behavior, which can be observed with a cycle accurate Cortex-M55 model, it gives interesting information about Structural and Read after Write Hazards.

```
Timeline view:
                    0123456789          0123456789          0123456789          0123456789
Index     0123456789          0123456789          0123456789          0123456789

[0,0]     DE   .    .    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vldrw.u32  q0, [r1]
[0,1]     . DE .    .    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vldrw.u32  q1, [r9]
[0,2]     .  DE.    .    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vadd.f32   q3, q1, q0
[0,3]     .   DE    .    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vldrw.u32  q2, [r11]
[0,4]     .    DE   .    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vsub.f32   q0, q1, q0
[0,5]     .    .DE  .    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vldrw.u32  q4, [r10]
[0,6]     .    . DE .    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vadd.f32   q5, q4, q2
[0,7]     .    .   DE    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vadd.f32   q6, q5, q3
[0,8]     .    .    DE   .    .    .    .    .    .    .    .    .    .    .    .    .   .   vstrb.8    q6, [r9], #16
[0,9]     .    .    .DE  .    .    .    .    .    .    .    .    .    .    .    .    .   .   vsub.f32   q3, q3, q5
[0,10]    .    .    . DE .    .    .    .    .    .    .    .    .    .    .    .    .   .   vldrw.u32  q5, [r5], #16
[0,11]    .    .    .  DeE    .    .    .    .    .    .    .    .    .    .    .    .   .   vcmul.f32  q6, q5, q3, #0
[0,12]    .    .    .    DeE  .    .    .    .    .    .    .    .    .    .    .    .   .   vcmla.f32  q6, q5, q3, #270
[0,13]    .    .    .    .DE  .    .    .    .    .    .    .    .    .    .    .    .   .   vstrb.8    q6, [r11], #16

```

A perfectly optimized CFFT ASM implementation taking advantage of SW
pipelining in the inner radix-2/4 core loops, provides around 10% gain
compared to a compiled version.

Including an optimal SW pipeliner in a compiler would require an
exhaustive gigantic exploration of all loop construction variations with
different possibilities of pre-amble / post-amble. This would cause
compilation times to explode which is not desirable in commercial
compilers.

Such tasks can be handled by alternative methods like the one described
in <https://eprint.iacr.org/2022/1303.pdf>

Cortex-M55 optimized FFT in assembly can be found in
<https://github.com/ARM-software/EndpointAI/blob/master/Kernels/ARM-Optimized/DSP/Source/TransformFunctions/>

These are using the exact same API found in CMSIS-DSP FFT and can be
easily substituted.


**LLVM-MCA**

```
Dispatch Width:    2
uOps Per Cycle:    0.89
IPC:               0.89
Block RThroughput: 28.0
```

It is highlighting a more optimal way of dispatching instructions. Some unavoidable stalls are remaining, but reduced compared to the compiled version.

```
Resources:
[0]   - M55UnitALU
[1]   - M55UnitLoadStore
[2]   - M55UnitVecALU
[3]   - M55UnitVecFPALU
[4]   - M55UnitVecSys


Resource pressure per iteration:
[0]    [1]    [2]    [3]    [4]
 -     22.00   -     28.00   -

Resource pressure by instruction:
[0]    [1]    [2]    [3]    [4]    Instructions:
 -      -      -     2.00    -     vadd.f32     q6, q0, q2
 -      -      -     2.00    -     vsub.f32     q3, q0, q2
 -     2.00    -      -      -     vldrw.u32    q0, [r0]
 -      -      -     2.00    -     vadd.f32     q7, q0, q1
 -     2.00    -      -      -     vldrw.u32    q2, [r1, #16]
 -      -      -     2.00    -     vsub.f32     q4, q6, q7
 -      -      -     2.00    -     vadd.f32     q5, q6, q7
 -     2.00    -      -      -     vldrw.u32    q7, [r2], #16
 -      -      -     2.00    -     vsub.f32     q1, q0, q1
 -     2.00    -      -      -     vldrw.u32    q0, [r3], #16
 -      -      -     2.00    -     vcmul.f32    q6, q0, q4, #0
 -     2.00    -      -      -     vstrw.32     q5, [r4], #16
 -      -      -     2.00    -     vcmla.f32    q6, q0, q4, #90
 -     2.00    -      -      -     vstrw.32     q6, [r0], #16
 -      -      -     2.00    -     vcadd.f32    q5, q3, q1, #90
 -      -      -     2.00    -     vcmul.f32    q6, q7, q5, #0
 -     2.00    -      -      -     vldrw.u32    q0, [r4]
 -      -      -     2.00    -     vcmla.f32    q6, q7, q5, #90
 -     2.00    -      -      -     vldrw.u32    q5, [r5], #16
 -      -      -     2.00    -     vcadd.f32    q4, q3, q1, #270
 -     2.00    -      -      -     vldrw.u32    q1, [r6, #16]
 -      -      -     2.00    -     vcmul.f32    q7, q5, q4, #0
 -     2.00    -      -      -     vstrw.32     q6, [r1], #16
 -      -      -     2.00    -     vcmla.f32    q7, q5, q4, #90
 -     2.00    -      -      -     vstrw.32     q7, [r6], #16
```

And the timeline view is showing a smoother execution with less pipeline bubbles.

```
                    0123456789          0123456789          0123456789          0123456789
Index     0123456789          0123456789          0123456789          0123456789

[0,0]     DE   .    .    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vadd.f32   q6, q0, q2
[0,1]     . DE .    .    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vsub.f32   q3, q0, q2
[0,2]     .  DE.    .    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vldrw.u32  q0, [r0]
[0,3]     .   DE    .    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vadd.f32   q7, q0, q1
[0,4]     .    DE   .    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vldrw.u32  q2, [r1, #16]
[0,5]     .    .DE  .    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vsub.f32   q4, q6, q7
[0,6]     .    .  DE.    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vadd.f32   q5, q6, q7
[0,7]     .    .   DE    .    .    .    .    .    .    .    .    .    .    .    .    .   .   vldrw.u32  q7, [r2], #16
[0,8]     .    .    DE   .    .    .    .    .    .    .    .    .    .    .    .    .   .   vsub.f32   q1, q0, q1
[0,9]     .    .    .DE  .    .    .    .    .    .    .    .    .    .    .    .    .   .   vldrw.u32  q0, [r3], #16
[0,10]    .    .    . DeE.    .    .    .    .    .    .    .    .    .    .    .    .   .   vcmul.f32  q6, q0, q4, #0
[0,11]    .    .    .  DE.    .    .    .    .    .    .    .    .    .    .    .    .   .   vstrw.32   q5, [r4], #16
[0,12]    .    .    .   DeE   .    .    .    .    .    .    .    .    .    .    .    .   .   vcmla.f32  q6, q0, q4, #90
[0,13]    .    .    .    DE   .    .    .    .    .    .    .    .    .    .    .    .   .   vstrw.32   q6, [r0], #16
[0,14]    .    .    .    .DE  .    .    .    .    .    .    .    .    .    .    .    .   .   vcadd.f32  q5, q3, q1, #90
[0,15]    .    .    .    .  DeE    .    .    .    .    .    .    .    .    .    .    .   .   vcmul.f32  q6, q7, q5, #0
[0,16]    .    .    .    .   DE    .    .    .    .    .    .    .    .    .    .    .   .   vldrw.u32  q0, [r4]
[0,17]    .    .    .    .    DeE  .    .    .    .    .    .    .    .    .    .    .   .   vcmla.f32  q6, q7, q5, #90
[0,18]    .    .    .    .    .DE  .    .    .    .    .    .    .    .    .    .    .   .   vldrw.u32  q5, [r5], #16
[0,19]    .    .    .    .    . DE .    .    .    .    .    .    .    .    .    .    .   .   vcadd.f32  q4, q3, q1, #270
```

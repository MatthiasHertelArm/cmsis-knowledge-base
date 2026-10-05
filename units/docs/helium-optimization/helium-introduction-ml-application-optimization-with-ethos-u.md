---
id: "helium-introduction-ml-application-optimization-with-ethos-u"
type: "concept"
domain: "optimization"
title: "Introduction: ML application optimization with Ethos-U55"
summary: "Arm Corstone-300 platform allows Cortex-M55 to be assisted with the Ethos-U55-128 NPU."
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:Performance_analysis/ml-dsp-front-end-optimization-with-helium.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/Performance_analysis/ml-dsp-front-end-optimization-with-helium.md#ml-application-optimization-with-ethos-u55"
license: "Apache-2.0"
mode: "V"
---

Arm Corstone-300 platform allows Cortex-M55 to be assisted with the
Ethos-U55-128 NPU.

Offloading Audiomark DS-CNN to Ethos-U using the Helium optimized code
baseline will allow to reduce a good amount of the 80% of the NN
execution time when entirely running on Cortex-M55.

The CMSIS-NN processing part will be replaced by the TFL interpreter and
the Ethos-U driver which we can expect to be low in terms of CPU
resource as the full network can be handled by the NPU and no Cortex-M
fallback is required.

The MCU will enter sleep mode after command stream processing by the
Ethos-U driver for the whole duration of the inference until reception
of the Ethos IRQ.

The DSP front-end duration is unaffected and will remain close to 11
seconds.

Thanks to Ethos-U, the total Audiomark duration is reduced to 15
seconds, leading to a score of `450 Audiomarks` or `14.06
Audiomark/Mhz`.

The DSP front-end vs NN back-end balance, seen by the MCU is now
completely reversed with roughly **98** vs **2%**. This excludes the 17% sleep
time while Cortex-M55 waits for the IRQ signaling the end of the
Ethos-U55 processing.

Adding NPU suddenly puts the DSP front-end as the limiting factor for
performance, and new optimizations opportunities, which are obviously
more complex than the ones applied in previous stage, should be
identified.

The same process for searching optimization opportunities described
earlier can be iterated until reaching a point where cycle reduction is
no longer paying.

In the context of Audiomark, the top contributing functions from the DSP
front-end reported by MDK Performance Analyser are the following:

```
- ee_abf_f32 (ABF core)
- arm_cfft_f32 + arm_rfft_fast_f32 
- speex_echo_cancellation (AEC main)
- th_cmplx_mult_cmplx_f32 (used in ABF)
- speex_preprocess_run (ANR)
- arm_cmplx_dot_prod_f32 (used in ABF)
```

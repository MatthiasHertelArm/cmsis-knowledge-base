---
id: "helium-introduction-initial-ml-application-profiling-cortex"
type: "concept"
domain: "optimization"
title: "Introduction: Initial ML application profiling (Cortex-M only)"
summary: "There are many ways to conduct application profiling. This process can be classified into 2 main categories: Active and passive profiling."
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:Performance_analysis/ml-dsp-front-end-optimization-with-helium.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/Performance_analysis/ml-dsp-front-end-optimization-with-helium.md#initial-ml-application-profiling-cortex-m-only"
license: "Apache-2.0"
mode: "V"
---

There are many ways to conduct application profiling. This process can
be classified into 2 main categories: **Active** and **passive** profiling.

**Active** profiling requires developers to add instrumentation through the
software and to collect information like timestamps or PMU events at
specific points. This implies a capability of editing and recompiling
the software and a mechanism to export the profiling information out of
the device or the simulator.

MDK Event Recorder is one possible way for performing such
instrumentation. Documentation can be found in
<https://www.keil.com/pack/doc/compiler/EventRecorder/html/index.html>

In a benchmark like Audiomark, calls to different components are
centralized in a top-level control function **ee_Audiomark_run**. Adding
instrumentation markers around the different component’s entry points,
respectively **ee_abf_f32**, **ee_aec_f32**, **ee_anr_f32** and
**ee_kws_f32** for ABF, AEC, ANR and KWS, allows to derive estimation of
the DSP front-end / NN back-end ratio.

Additional markers can be added inside the font-end components to get
more visibility and decide where to start the optimization process.

When there is no prior knowledge on the cycle repartition, such process
can be tedious, requiring several instrumentation iterations to get a
good overview of the cycle repartition.

Decision for adding markers can be driven by a dichotomy approach or by
visual code inspections and heavy loop identification.

It can be noted that such active profiling can already be part of RTOS
services for tracking task transitions or can be easily enabled when
using stream-based solution like [CMSIS Stream](https://github.com/ARM-software/CMSIS-Stream/) allowing adding Event
Recorder points at node transitions. If the granularity provided by such
a mechanism is not enough, manual instrumentation will still be
required.

On the other hand, passive profiling provides automated methods for
expositing cycle repartition information without SW editing and does not
require prior in-depth knowledge of the code been profiled. This is
generally the most convenient approach for developers but not available
to the majority of the targets. For this reason, it might be interesting
to run the initial profiling pass on one of the ARM FPGA like
[MPS2](https://www.arm.com/products/development-tools/development-boards/mps2-plus)
or
[MPS3](https://www.arm.com/products/development-tools/development-boards/mps3) covering all the Cortex-M Cores and Ethos-U to benefit from their
extended trace capabilities.


**Passive** profiling relies on specific hardware or simulation support
capabilities exposing execution trace to the outside and tools for
processing and presenting the profiling data in a friendly way,

Keil MDK Performance Analyzer (PA) with ETM or Arm Virtual Hardware
associated with TARMAC plugin and TARMAC Trace utilities
([TARMAC-trace-utilities](https://github.com/ARM-software/tarmac-trace-utilities))
falls in this category.

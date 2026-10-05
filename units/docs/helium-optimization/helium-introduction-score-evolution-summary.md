---
id: "helium-introduction-score-evolution-summary"
type: "concept"
domain: "optimization"
title: "Introduction: ML application optimization with Ethos-U55 / Score evolution summary"
summary: "Part of: ML application optimization with Ethos-U55"
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:Performance_analysis/ml-dsp-front-end-optimization-with-helium.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/Performance_analysis/ml-dsp-front-end-optimization-with-helium.md#score-evolution-summary"
license: "Apache-2.0"
mode: "V"
---

_Part of: ML application optimization with Ethos-U55_

| | CM55 only  AudioMark Baseline No Helium | CM55 only AudioMark Baseline Helium enabled (CMSIS NN/DSP + Autovec) | CM55 only AudioMark with extra CMSIS DSP additions (AEC/ANR)	| CM55 only AudioMark with extra custom Helium additions (AEC/ANR)	| CM55 + Ethos-U55 AudioMark with extra custom Helium additions (AEC/ANR)	| CM55 + Ethos-U55 AudioMark with extra custom Helium additions and further Helium optimization |
|-|:-----------------------------------------:|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| AudioMark Score					| 27.77	| 99.06	| 108.98 | *117.4* | 450	 | x |
| AudioMark / Mhz Score				| 0.87	| 3.1	| 3.4	 | *3.66*	 | 14.06 | x |
| NN back-end contribution (%)		| 87	| 67.7	| 74.5	 | 80	 | 2	 | x |
| DSP front-end contribution (%)	| 13	| 32.3	| 25.5	 | 20	 | 98	 | x |


# Extra Profiling utilities

In addition to existing tools like MDK Performance Analyzer, MDK
Execution Profiler, ARM DS Streamline, utility scripts can be
constructed to post-process the tracing information provided by HW or
models to derive targeted profiling information to assist optimization
operations or to be used in a CI/CD environment when used as part of an
MLOps process.

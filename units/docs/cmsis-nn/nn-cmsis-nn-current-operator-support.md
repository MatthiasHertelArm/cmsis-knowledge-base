---
id: "nn-cmsis-nn-current-operator-support"
type: "concept"
domain: "optimization"
title: "CMSIS NN: Current Operator Support"
summary: "In general optimizations are written for an architecture feature. This falls into one of the following categories. Based on feature flags for a processor or architecture provided to the compiler, the right implementation is picked."
status: "draft"
collection: "cmsis-nn"
source: "ARM-software/CMSIS-NN@71cbe3d:README.md"
doc_source: "https://github.com/ARM-software/CMSIS-NN/blob/71cbe3d/README.md#current-operator-support"
license: "Apache-2.0"
mode: "V"
---

In general optimizations are written for an architecture feature. This falls into one of the following categories.
Based on feature flags for a processor or architecture provided to the compiler, the right implementation is picked.
### Pure C
 There is always a pure C implementation for an operator. This is used for processors like Arm Cortex-M0 or Cortex-M3.
### DSP Extension
Processors with DSP extension uses Single Instruction Multiple Data(SIMD) instructions for optimization. Examples of
processors here are Cortex-M4 or a Cortex-M33 configured with optional DSP extension.

### MVE Extension
Processors with Arm Helium Technology use the Arm M-profile Vector Extension(MVE) instructions for optimization.
Examples are Cortex-M55 or Cortex-M85 configured with MVE.

The float columns below summarize the current experimental float coverage. Float kernels are available in pure C reference form and, for the operators listed below, in Helium-optimized form where available. Float support is primarily intended for cores with Helium and hardware floating-point support; on cores that only provide the classic DSP extension, float kernels may still compile through the scalar C path but are not a performance target.

| Operator        | C 
 int8 | C
int16 | C
int4* | C
float16/float32 | DSP
int8 | DSP
int16 | DSP
int4* | MVE
int8 | MVE
int16 | MVE
int4* | MVE
float16/float32 |
| --------------- | ----------- | ---------- |------------|----------------------|-------------| -------------|--------------|-------------| -------------|--------------|------------------------|
| Conv2D          | Yes         | Yes        | Yes        | Yes                  | Yes         | Yes          | Yes          | Yes         | Yes          | Yes          | Yes                    |
| DepthwiseConv2D | Yes         | Yes        | Yes        | Yes                  | Yes         | Yes          | Yes          | Yes         | Yes          | Yes          | Yes                    |
| TransposeConv2D | Yes         | No         | No         | Yes                  | Yes         | No           | No           | Yes         | No           | No           | Yes                    |
| Fully Connected | Yes         | Yes        | Yes        | Yes                  | Yes         | Yes          | Yes          | Yes         | Yes          | Yes          | Yes                    |
| Batch Matmul    | Yes         | Yes        | No         | Yes                  | Yes         | Yes          | No           | Yes         | Yes          | No           | Yes                    |
| Add             | Yes         | Yes        | N/A        | Yes                  | Yes         | Yes          | N/A          | Yes         | Yes          | N/A          | Yes                    |
| Minimum         | Yes         | No         | N/A        | Yes                  | No          | No           | N/A          | Yes         | No           | N/A          | Yes                    |
| Maximum         | Yes         | No         | N/A        | Yes                  | No          | No           | N/A          | Yes         | No           | N/A          | Yes                    |
| Mul             | Yes         | Yes        | N/A        | Yes                  | Yes         | Yes          | N/A          | Yes         | Yes          | N/A          | Yes                    |
| MaxPooling      | Yes         | Yes        | N/A        | Yes                  | Yes         | Yes          | N/A          | Yes         | Yes          | N/A          | Yes                    |
| AvgPooling      | Yes         | Yes        | N/A        | Yes                  | Yes         | Yes          | N/A          | Yes         | Yes          | N/A          | Yes                    |
| Softmax         | Yes         | Yes        | N/A        | Yes                  | Yes         | Yes          | N/A          | Yes         | No           | N/A          | Yes                    |
| LSTM            | Yes         | Yes        | No         | Yes                  | Yes         | Yes          | No           | Yes         | Yes          | No           | Yes                    |
| SVDF            | Yes         | No         | No         | Yes                  | Yes         | No           | No           | Yes         | No           | No           | Yes                    |
| Pad             | Yes         | No         | N/A        | Yes                  | No          | No           | N/A          | Yes         | No           | N/A          | Yes                    |
| Transpose       | Yes         | No         | N/A        | Yes                  | No          | No           | N/A          | Yes         | No           | N/A          | Yes                    |

* int4 weights + int8 activations

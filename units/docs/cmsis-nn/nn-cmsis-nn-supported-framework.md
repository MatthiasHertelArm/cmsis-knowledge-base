---
id: "nn-cmsis-nn-supported-framework"
type: "concept"
domain: "optimization"
title: "CMSIS NN: Supported Framework"
summary: "The library follows the int8 and int16 quantization specification of TensorFlow Lite for Microcontrollers. This means CMSIS-NN is bit-exact with Tensorflow Lite reference kernels. In some cases TFL and TFLM reference kernels may not be bit-exact."
status: "draft"
collection: "cmsis-nn"
source: "ARM-software/CMSIS-NN@71cbe3d:README.md"
doc_source: "https://github.com/ARM-software/CMSIS-NN/blob/71cbe3d/README.md#supported-framework"
license: "Apache-2.0"
mode: "V"
---

The library follows the [int8](https://www.tensorflow.org/lite/performance/quantization_spec) and int16 quantization specification of TensorFlow Lite for Microcontrollers.
This means CMSIS-NN is bit-exact with Tensorflow Lite reference kernels. In some cases TFL and TFLM reference kernels may not be bit-exact. In that case CMSIS-NN follows TFLM reference kernels. The unit test readme provides an [overview](https://github.com/ARM-software/CMSIS-NN/blob/main/Tests/UnitTest/README.md#tests-depending-on-tflm-interpreter).

### Experimental Float API
CMSIS-NN also provides experimental float32 and float16 APIs. The float API intentionally follows the same CMSIS-NN integer style, which is itself shaped by TFLM integration patterns, to keep the public surface consistent across data types. This includes float16 even though TFLM does not define a float16 operator contract.

The float API is primarily intended for Cortex-M CPUs with Arm Helium Technology (MVE). Pure C scalar reference implementations are provided for correctness, bring-up, and fallback, but practical deployment is expected to target MVE-enabled CPUs. In general, float kernels should be reserved for specific use cases where integer quantization is not possible or not acceptable, and where the neural network remains modest enough for Cortex-M class devices. CMSIS-NN float support is intended to integrate with frameworks that can carry float16 operator flows, such as [ExecuTorch](https://executorch.ai/).

For the float operators that support `arm_nn_weight_format_flt`, MVE
performance is generally better when constant weights are provided in the
packed `NTxN` layout instead of the standard `NT x T` layout. This avoids the
gather-heavy RHS access pattern of the standard formulation and is therefore
the preferred deployment format when offline repacking is available.

The floating-point scalar code can also be compiled for Arm A-class CPUs with `float16`
support and may benefit from NEON or SVE auto-vectorization. However, this is
not an intended deployment target for CMSIS-NN float support, and the resulting
performance is expected to be suboptimal compared to libraries designed for that
class of processor. For Arm A-class CPUs, prefer optimized inference libraries
such as Arm Compute Library or XNNPACK.

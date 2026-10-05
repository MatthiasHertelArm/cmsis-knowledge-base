---
id: "etarm-arm-cortex-m-backend-cmsis-nn-supported-operators"
type: "concept"
domain: "edge-ai"
title: "Arm Cortex-M Backend: CMSIS-NN Supported Operators"
summary: "The backend pass pipeline replaces quantized ATen operators with CMSIS-NN kernel calls. See the CMSIS-NN API documentation for the full list of available kernels."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:docs/source/backends/arm-cortex-m/arm-cortex-m-overview.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/docs/source/backends/arm-cortex-m/arm-cortex-m-overview.md#cmsis-nn-supported-operators"
license: "BSD-3-Clause"
mode: "V"
---

The backend pass pipeline replaces quantized ATen operators with [CMSIS-NN](https://arm-software.github.io/CMSIS-NN/latest/) kernel calls. See the [CMSIS-NN API documentation](https://arm-software.github.io/CMSIS-NN/latest/modules.html) for the full list of available kernels.

| ATen Op                        | CMSIS-NN Kernel        | 8w8a | 8w16a | 4w8a |
|--------------------------------|------------------------|------|-------|------|
| `aten.convolution`             | `arm_convolve`         | ✅   | ⬜    | ⬜   |
| `aten.convolution` (depthwise) | `arm_depthwise_conv`   | ✅   | ⬜    | ⬜   |
| `aten.convolution` (transposed)| `arm_transpose_conv`   | ✅   | ⬜    | ⬜   |
| `aten.linear`                  | `arm_fully_connected`  | ✅   | ⬜    | ⬜   |
| `aten.bmm`                     | `arm_batch_matmul`     | ✅   | ⬜    | ⬜   |
| `aten.add`                     | `arm_elementwise_add`  | ✅   | ⬜    | N/A  |
| `aten.mul`                     | `arm_elementwise_mul`  | ✅   | ⬜    | N/A  |
| `aten.max_pool2d`              | `arm_max_pool`         | ✅   | ⬜    | N/A  |
| `aten.avg_pool2d`              | `arm_avgpool`          | ✅   | ⬜    | N/A  |
| `aten._softmax`                | `arm_softmax`          | ✅   | ⬜    | N/A  |
| `aten.minimum`                 | `arm_minimum`          | ✅   | ⬜    | N/A  |
| `aten.maximum`                 | `arm_maximum`          | ✅   | ⬜    | N/A  |
| `aten.permute_copy`            | `arm_transpose`        | ✅   | ⬜    | N/A  |
| `aten.constant_pad_nd`         | `arm_pad`              | ✅   | ⬜    | N/A  |
| —                              | LSTM                   | ⬜   | ⬜    | ⬜   |
| —                              | SVDF                   | ⬜   | ⬜    | ⬜   |

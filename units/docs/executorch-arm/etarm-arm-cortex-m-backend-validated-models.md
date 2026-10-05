---
id: "etarm-arm-cortex-m-backend-validated-models"
type: "concept"
domain: "edge-ai"
title: "Arm Cortex-M Backend: Validated Models"
summary: "The following models are exported, INT8 quantized, lowered, and validated end-to-end on the Corstone-300 FVP:"
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:docs/source/backends/arm-cortex-m/arm-cortex-m-overview.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/docs/source/backends/arm-cortex-m/arm-cortex-m-overview.md#validated-models"
license: "BSD-3-Clause"
mode: "V"
---

The following models are exported, INT8 quantized, lowered, and validated
end-to-end on the Corstone-300 FVP:

| Model              | Task                               | Input shape   | Source                                            | Test                                                     |
|--------------------|------------------------------------|---------------|---------------------------------------------------|----------------------------------------------------------|
| `mv2`              | Image classification               | `1x3x224x224` | `examples/models/mobilenet_v2/`                   | `backends/cortex_m/test/models/test_mobilenet_v2.py`     |
| `mv3`              | Image classification               | `1x3x224x224` | `examples/models/mobilenet_v3/`                   | `backends/cortex_m/test/models/test_mobilenet_v3.py`     |
| `ds_cnn`           | Keyword spotting (MLPerf Tiny)     | `1x1x49x10`   | `examples/models/mlperf_tiny/ds_cnn.py`           | `backends/cortex_m/test/models/test_ds_cnn.py`           |
| `mobilenet_v1_025` | Visual Wake Words (MLPerf Tiny)    | `1x3x96x96`   | `examples/models/mlperf_tiny/mobilenet_v1_025.py` | `backends/cortex_m/test/models/test_mobilenet_v1_025.py` |
| `resnet8`          | Image classification (MLPerf Tiny) | `1x3x32x32`   | `examples/models/mlperf_tiny/resnet8.py`          | `backends/cortex_m/test/models/test_resnet8.py`          |
| `deep_autoencoder` | Anomaly detection (MLPerf Tiny)    | `1x640`       | `examples/models/mlperf_tiny/deep_autoencoder.py` | `backends/cortex_m/test/models/test_deep_autoencoder.py` |

:::{note}
`mobilenet_v1_025` is the MLPerf Tiny Visual Wake Words benchmark
(MobileNetV1 with width multiplier 0.25) — the canonical person-detection
reference model for TinyML.
:::

---
id: "alp-analyze-ethos-u-models-with-mlia-4-analyze-tosa-with-vela-compare-fp32-and-int8-tosa-a"
type: "concept"
domain: "edge-ai"
title: "Analyze machine learning models for Arm Ethos-U with Arm ML Inference Advisor: Analyze TOSA IR artifacts with MLIA and Vela: Compare FP32 and INT8 TOSA artifact"
summary: "The model artifacts repository includes floating-point and quantized TOSA variants:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/4-analyze-tosa-with-vela.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/4-analyze-tosa-with-vela/#compare-fp32-and-int8-tosa-artifacts"
license: "CC-BY-SA-4.0"
mode: "V"
---

The model artifacts repository includes floating-point and quantized TOSA variants:

```output
tosa/mv2_fp32.tosa
tosa/mv2_int8.tosa
```

Start by running Arm ML Inference Advisor (MLIA) on the FP32 TOSA model:

```bash
mlia check tosa/mv2_fp32.tosa \
  --target-profile ethos-u85-256 \
  --compatibility \
  --backend vela \
  --json
```

The result is similar to the FP32 LiteRT check. The model can be expressed as an artifact, but it's not in the supported quantized integer form required for Ethos-U acceleration with this target profile. The important distinction is that TOSA describes an intermediate graph form rather than a complete runtime deployment.

Run the same MLIA compatibility check on the quantized INT8 TOSA model:

```bash
mlia check tosa/mv2_int8.tosa \
  --target-profile ethos-u85-256 \
  --compatibility \
  --backend vela \
  --json
```

The INT8 TOSA report shows `status` as `ok` and `accelerator_operator_percentage` as `100.0`. The model format is now TOSA, but the target profile and Vela backend configuration are the same as the LiteRT run.

The difference from the FP32 TOSA artifact is that the INT8 artifact has the quantized representation required for Ethos-U acceleration. The operator support checks pass, and MLIA expects the operator work to map to the NPU path.

You can also run a performance check using the INT8 `.tosa` model:

```bash
mlia check tosa/mv2_int8.tosa \
  --target-profile ethos-u85-256 \
  --performance \
  --backend vela \
  --json
```

The report is similar to the INT8 LiteRT performance result. The model maps to the NPU path. MLIA reports NPU-scoped estimated metrics, and the advice points you toward operators that dominate estimated cycles or have low utilization.

Whether TOSA with MLIA is useful depends on your workflow. Many developers will likely use ExecuTorch or LiteRT artifacts directly.

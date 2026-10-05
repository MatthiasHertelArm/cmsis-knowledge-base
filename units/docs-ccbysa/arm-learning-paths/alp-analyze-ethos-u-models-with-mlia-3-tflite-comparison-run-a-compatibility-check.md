---
id: "alp-analyze-ethos-u-models-with-mlia-3-tflite-comparison-run-a-compatibility-check"
type: "concept"
domain: "edge-ai"
title: "Analyze machine learning models for Arm Ethos-U with Arm ML Inference Advisor: Analyze LiteRT artifacts with MLIA and Vela: Run a compatibility check"
summary: "Start by asking Arm ML Inference Advisor (MLIA) whether a LiteRT model can map to the selected target profile."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/3-tflite-comparison.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/3-tflite-comparison/#run-a-compatibility-check"
license: "CC-BY-SA-4.0"
mode: "V"
---

Start by asking Arm ML Inference Advisor (MLIA) whether a LiteRT model can map to the selected target profile.

LiteRT is a compact model format and runtime stack for deploying machine learning models on mobile, embedded, and edge devices. In embedded ML workflows, a `.tflite` file is often the artifact handed to backend tools for target-specific compatibility checks, compilation, or runtime deployment.

The model artifacts repository includes floating-point and quantized MobileNetV2 LiteRT variants:

```output
tflite/mv2_fp32.tflite
tflite/mv2_int8.tflite
```

From the `ml-model-artifacts` directory, run MLIA on the FP32 LiteRT artifact:

```bash
mlia check tflite/mv2_fp32.tflite \
  --target-profile ethos-u85-256 \
  --compatibility \
  --backend vela \
  --json
```

The `--json` option makes the output easier to inspect, compare, and automate.

You can also use the shorter `-t` and `-b` options instead of `--target-profile` and `--backend`. Note that `--compatibility` and `vela` are both defaults that can be omitted:

```bash
mlia check tflite/mv2_fp32.tflite -t ethos-u85-256 --json
```

The report should show the FP32 LiteRT model as incompatible for Ethos-U acceleration, with `accelerator_operator_percentage` set to `0`. This is expected because Ethos-U acceleration requires supported quantized integer workloads. The failed checks explain that the input, output, and weight tensors are missing quantization parameters.

This doesn't mean LiteRT is the problem. It means that this particular LiteRT artifact isn't in the numeric form the selected Ethos-U target needs. Use a quantized model instead.

Run the same compatibility check on the quantized INT8 model:

```bash
mlia check tflite/mv2_int8.tflite \
  --target-profile ethos-u85-256 \
  --compatibility \
  --backend vela \
  --json
```

You'll generate a lengthy report, saved in the `mlia-output` directory in the root of the `mlia` execution directory. The following is a small snippet of the report:

```output
{
  "target": {
    "configuration": {
      "target": "ethos-u85",
      "mac": 256
    }
  },
  "model": {
    "name": "mv2_int8.tflite",
    "format": "tflite"
  },
  "backends": [
    {
      "id": "vela",
      "name": "Vela Compiler",
      "version": "5.0.0"
    }
  ],
  "results": [
    {
      "kind": "compatibility",
      "status": "ok",
      "metrics": [
        {
          "name": "accelerator_operator_percentage",
          "value": 100.0
        }
      ]
    }
  ]
}
```

The following table describes the fields in the generated report, and what they mean:

| Field | What it tells you |
| --- | --- |
| `schema_version`, `run_id`, `timestamp` | Which output schema was used, and how you can identify this specific run later. |
| `tool` | The MLIA version that generated the report. |
| `target` | The selected target profile and its configuration, such as Ethos-U85 with 256 MACs. |
| `model` | The artifact name, format, and hash. |
| `context` | The CLI command that produced the report. |
| `backends` | The backend MLIA used, including the Vela version and compiler configuration. |
| `results` | The answer MLIA produced for the requested check. |
| `checks` | The individual operator support checks. |
| `entities` | The operators MLIA analyzed, including placement and operator type. |

For the INT8 LiteRT file, the important result is that the `status` is `ok` and `accelerator_operator_percentage` is `100.0`. That means Vela found the operators in this quantized MobileNetV2 LiteRT artifact compatible with the selected `ethos-u85-256` target profile. MLIA therefore expects the operator work to map to the NPU path for this compatibility check.

The result doesn't prove runtime latency or application accuracy. It tells you that the model is a good candidate for the next step: performance estimation and deeper deployment testing.

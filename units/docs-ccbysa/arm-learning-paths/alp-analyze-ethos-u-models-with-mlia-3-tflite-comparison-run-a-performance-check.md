---
id: "alp-analyze-ethos-u-models-with-mlia-3-tflite-comparison-run-a-performance-check"
type: "concept"
domain: "edge-ai"
title: "Analyze machine learning models for Arm Ethos-U with Arm ML Inference Advisor: Analyze LiteRT artifacts with MLIA and Vela: Run a performance check"
summary: "Next, ask MLIA for a target-aware performance estimate using the INT8 LiteRT model:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/3-tflite-comparison.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/3-tflite-comparison/#run-a-performance-check"
license: "CC-BY-SA-4.0"
mode: "V"
---

Next, ask MLIA for a target-aware performance estimate using the INT8 LiteRT model:

```bash
mlia check tflite/mv2_int8.tflite \
  --target-profile ethos-u85-256 \
  --performance \
  --backend vela \
  --json
```

Because this run uses Vela, the performance report uses the same top-level structure as the compatibility report. The `results` object now contains estimated performance metrics, operator-level breakdowns, and advice:

```output
{
  "results": [
    {
      "kind": "performance",
      "status": "ok",
      "warnings": [
        "The performance figures above refer to NPU only"
      ],
      "metrics": [
        {
          "name": "npu_cycles",
          "value": 3623146
        },
        {
          "name": "total_cycles",
          "value": 5006357
        },
        {
          "name": "inference_time",
          "unit": "ms",
          "value": 5.006357
        },
        {
          "name": "inferences_per_second",
          "unit": "inferences/s",
          "value": 199.74604288108097
        },
        {
          "name": "target_utilization",
          "unit": "%",
          "value": 72.3709076280417
        }
      ],
      "advice": [
        {
          "category": "performance",
          "severity": "warning",
          "message": "The following layers make up the majority of operator cycles..."
        },
        {
          "category": "performance",
          "severity": "warning",
          "message": "Among the layers with the highest impact, 5 layers have been identified with low MAC utilization..."
        },
        {
          "category": "performance",
          "severity": "warning",
          "message": "Among the layers with the highest impact, 5 layers have been identified as possibly memory bound..."
        }
      ]
    }
  ]
}
```

The following table describes the fields in the generated report, and what they mean:

| Field | What it tells you |
| --- | --- |
| `warnings` | Important scope limits for the result, such as the estimate referring to NPU work only. |
| `metrics` | Summary estimates for cycles, inference time, throughput, utilization, model size, and memory use. |
| `breakdowns` | Per-operator metrics, including operator cycles, memory access cycles, multiply-accumulates (MAC) count, and MAC utilization. |
| `advice` | MLIA's interpretation of the metrics, including which layers dominate cycles or might be inefficient. |
| `availability` and `reason` | Why a metric isn't available from the selected backend, if MLIA can't report it. |

For this INT8 LiteRT file, the Vela-backed estimate reports the following:

- About `5.01M` total cycles
- About `5.01 ms` inference time for batch size 1
- About `199.7` inferences per second
- About `72.4%` target utilization
- About `3.62M` NPU cycles, plus SRAM and DRAM access cycles

Treat these as target-aware estimates for the NPU portion of the model rather than final runtime measurements from hardware.

In this report, MLIA advises on where to investigate to improve target performance. The advice identifies the ten layers that make up most operator cycles. It flags five high-impact layers with low MAC utilization, and five high-impact layers as possibly memory-bound.

Low MAC utilization can be expected for layers with small channel counts, small spatial dimensions, or heavy memory movement. These are the layers to consider adjusting.

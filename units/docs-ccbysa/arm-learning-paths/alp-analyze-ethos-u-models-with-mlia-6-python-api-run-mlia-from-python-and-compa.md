---
id: "alp-analyze-ethos-u-models-with-mlia-6-python-api-run-mlia-from-python-and-compa"
type: "concept"
domain: "edge-ai"
title: "Analyze machine learning models for Arm Ethos-U with Arm ML Inference Advisor: (Optional) Use the MLIA Python API: Run MLIA from Python and compare two models"
summary: "The Arm ML Inference Advisor (MLIA) CLI is the best way to learn the tool, inspect output, and debug your environment."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/6-python-api.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/6-python-api/#run-mlia-from-python-and-compare-two-models"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Arm ML Inference Advisor (MLIA) CLI is the best way to learn the tool, inspect output, and debug your environment.

Use the Python API when you want another product, dashboard, workflow runner, or CI system to integrate MLIA.

The `mlia` Python package exposes the same advisor functionality used by the CLI. Use `run_advisor()` as the main API entry point. Use helper functions such as `list_targets()`, `list_target_profiles()`, and `list_backends()` to discover what the installed environment supports.

The following example shows how you can use the API to analyze two LiteRT model variants, and print results and advice:

```bash
cat > compare_mlia_models.py <<'PY'
from pathlib import Path

from mlia import run_advisor


models = [
    Path("tflite/mv2_fp32.tflite"),
    Path("tflite/mv2_int8.tflite"),
]

for model in models:
    result = run_advisor(
        advice_category="compatibility",
        target_profile="ethos-u85-256",
        model=model,
        backends=["vela"],
    )

    print()
    print(model)

    for item in result["results"]:
        print(item["kind"], item["status"])

        for advice in item.get("advice", []):
            print("advice:", advice["severity"], advice["message"].splitlines()[0])
PY
```

Run the comparison script:

```bash
python compare_mlia_models.py
```

The expected result is that `mv2_fp32.tflite` reports `compatibility incompatible`, while `mv2_int8.tflite` reports `compatibility ok`.

You might still see warning advice for both models. For example, MLIA can report that `SOFTMAX` is a suboptimal activation even when the quantized model is otherwise compatible with the NPU.

Compatibility tells you whether the model can map to the target. Advice can still point out ways to improve it.

You can extend the example to do the following:

- Extract selected metrics into a dashboard
- Compare performance between model revisions
- Fail a CI job if a key metric regresses
- Surface advice messages in an internal model review tool

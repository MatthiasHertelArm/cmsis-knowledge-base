---
id: "ethint-cmsis-ethos-u-integration-example-ml-layer"
type: "concept"
domain: "edge-ai"
title: "CMSIS Ethos-U integration example: ML Layer"
summary: "The project selects ML layer with multiple models:"
status: "draft"
collection: "cmsis-ethos-integration"
source: "Arm-Examples/CMSIS-Ethos-Integration@9b906f5:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/README.md#ml-layer"
license: "Apache-2.0"
mode: "V"
---

The project selects ML layer with multiple models:

```yaml
  layers:
    - layer: $SolutionDir()$/Model/ML-MyModels.clayer.yml
```

`Model/ML-MyModels.clayer.yml` lists LiteRT framework, dependencies and ML models.
Its `MODEL_*` defines enable the matching descriptors and test calls in `Source/app_main.cpp`.

Each model group lists the `README.md` file, `VELA_SUMMARY.md` with recorded compilation settings
and memory requirements, the source and compiled model and reference data for tests.

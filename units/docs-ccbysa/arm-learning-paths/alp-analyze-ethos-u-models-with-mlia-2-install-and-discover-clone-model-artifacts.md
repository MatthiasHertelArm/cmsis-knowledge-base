---
id: "alp-analyze-ethos-u-models-with-mlia-2-install-and-discover-clone-model-artifacts"
type: "concept"
domain: "edge-ai"
title: "Analyze machine learning models for Arm Ethos-U with Arm ML Inference Advisor: Install MLIA and discover capabilities: Clone model artifacts"
summary: "Clone prebuilt artifacts from the Arm ML model artifacts repository:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/2-install-and-discover.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/2-install-and-discover/#clone-model-artifacts"
license: "CC-BY-SA-4.0"
mode: "V"
---

Clone prebuilt artifacts from the Arm ML model artifacts repository:

```bash
git lfs install
git clone --filter=blob:none --sparse https://github.com/arm-education/ml-model-artifacts.git
cd ml-model-artifacts
git sparse-checkout set pte tflite tosa
git lfs pull \
  --include="pte/toy_conditional_select_int8_ethos_u55_256.pte,pte/toy_conditional_select_int8_ethos_u85_256.pte,tflite/mv2_fp32.tflite,tflite/mv2_int8.tflite,tosa/mv2_fp32.tosa,tosa/mv2_int8.tosa" \
  --exclude=""
git lfs checkout
```

This downloads only the artifacts that are required for you to complete the Learning Path. It avoids larger unrelated files, such as transformer `.pte`, `.etdp`, and `.etrecord` artifacts.

Confirm that the artifacts are real model files rather than Git LFS pointer files:

```bash
wc -c tflite/mv2_int8.tflite
```

The output is a size of several megabytes, similar to:

```output
3942808 tflite/mv2_int8.tflite
```

If the file is about 100 to 200 bytes, it's still a Git LFS pointer file. Run the `git lfs pull` command again from the `ml-model-artifacts` directory, then rerun the size check.

The model artifacts are provided for learning and analysis exercises. Use the artifacts to explore MLIA workflows, model formats, and target-aware advice rather than accuracy reference models.

The repository contains model artifacts such as:

```output
ml-model-artifacts/
├── pte/
│   ├── toy_conditional_select_int8_ethos_u55_256.pte
│   └── toy_conditional_select_int8_ethos_u85_256.pte
├── tflite/
│   ├── mv2_fp32.tflite
│   └── mv2_int8.tflite
└── tosa/
    ├── mv2_fp32.tosa
    └── mv2_int8.tosa
```

---
id: "mlek-troubleshooting-inference-results-are-incorrect-for-my-c"
type: "concept"
domain: "edge-ai"
title: "Troubleshooting: Inference results are incorrect for my custom files"
summary: "Ensure that the files you are using match the requirements of the model you are using. Ensure that cmake parameters are set accordingly. More information on these cmake parameters is detailed in their separate sections."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/troubleshooting.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/troubleshooting.md#inference-results-are-incorrect-for-my-custom-files"
license: "Apache-2.0"
mode: "V"
---

Ensure that the files you are using match the requirements of the model you are using. Ensure that cmake parameters are
set accordingly. More information on these cmake parameters is detailed in their separate sections.

> **Note:** Preprocessing of the files can also affect the inference result, such as the rescaling and padding
> operations performed for image classification.

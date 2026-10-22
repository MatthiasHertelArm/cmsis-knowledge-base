---
id: "etarm-mobilesam-prompt-segmentation-on-e"
type: "concept"
domain: "edge-ai"
title: "MobileSAM Prompt Segmentation on Ethos-U"
summary: "This example turns a point on an image into an object mask."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@6368414:examples/arm/mobilesam_prompt_segmentation_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/6368414/examples/arm/mobilesam_prompt_segmentation_example_ethos_u/README.md"
license: "BSD-3-Clause"
mode: "V"
---

This example turns a point on an image into an object mask. It shows the full
ExecuTorch flow: export MobileSAM, quantize it, delegate it to Ethos-U85, run it
on the Corstone-320 FVP, and compare the target result with the host result.

There is one tested configuration: MobileSAM `vit_t`, a `448x448` input, and
Ethos-U85-256. The image can change at runtime, but the point prompt is embedded
in the exported model. Changing the prompt requires re-exporting the model.

---
id: "etarm-mobilesam-prompt-segmentation-on-e-run-it"
type: "concept"
domain: "edge-ai"
title: "MobileSAM Prompt Segmentation on Ethos-U: Run It"
summary: "The final command performs the complete flow and prints MobileSAM example: PASS. Its main result is:"
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@6368414:examples/arm/mobilesam_prompt_segmentation_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/6368414/examples/arm/mobilesam_prompt_segmentation_example_ethos_u/README.md#run-it"
license: "BSD-3-Clause"
mode: "V"
---

From the ExecuTorch repository root:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
./install_executorch.sh --optional-dependency ethos_u
./examples/arm/setup.sh --i-agree-to-the-contained-eula
./examples/arm/mobilesam_prompt_segmentation_example_ethos_u/run.sh
```

The final command performs the complete flow and prints
`MobileSAM example: PASS`. Its main result is:

`arm_test/mobilesam/result/fvp_comparison.png`

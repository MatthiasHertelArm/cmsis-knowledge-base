---
id: "alp-silero-vad-ethos-u-4-validate-output-compare-the-host-and-fvp-resul"
type: "concept"
domain: "edge-ai"
title: "Deploy Silero VAD on Arm Ethos-U with ExecuTorch: Validate the FVP speech probabilities: Compare the host and FVP results"
summary: "Compare the saved host reference with the probabilities in the FVP serial log:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/4-validate-output.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/4-validate-output/#compare-the-host-and-fvp-results"
license: "CC-BY-SA-4.0"
mode: "V"
---

Compare the saved host reference with the probabilities in the FVP serial log:

```bash
source .venv/bin/activate
python3 examples/arm/silero_vad_example_ethos_u/runtime/compare_vad_probs.py \
  --expected silero-vad-work/export/expected_probs.bin \
  --actual-log silero-vad-work/fvp/fvp.log \
  --threshold 0.55 \
  --atol 0.25 \
  --mean-atol 0.02
```

The output is similar to:

```output
Compared 79 probability values
Max abs error: 0.156800 at frame 22
Mean abs error: 0.018459
Threshold mismatches at 0.550: 0
```

The comparison confirms that the host and FVP produced the same number of finite probabilities, and the numerical differences stay within tolerance. It also confirms that every frame has the same speech or silence decision.

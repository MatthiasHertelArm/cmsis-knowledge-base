---
id: "alp-silero-vad-ethos-u-2-run-example-export-the-model"
type: "concept"
domain: "edge-ai"
title: "Deploy Silero VAD on Arm Ethos-U with ExecuTorch: Export Silero VAD for Ethos-U85: Export the model"
summary: "Run the exporter and save its output for the delegation check:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/2-run-example.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/2-run-example/#export-the-model"
license: "CC-BY-SA-4.0"
mode: "V"
---

Run the exporter and save its output for the delegation check:

```bash
set -o pipefail

python3 examples/arm/silero_vad_example_ethos_u/model_export/export_silero_vad_ethos_u.py \
  --jit-model silero-vad-work/assets/silero_vad.jit \
  --calibration-audio silero-vad-work/assets/calibration.wav \
  --validation-audio silero-vad-work/assets/validation.wav \
  --output-path silero-vad-work/export/silero_vad_ethos_u.pte \
  --expected-output-path silero-vad-work/export/expected_probs.bin \
  --num-calibration-frames 32 \
  --num-validation-frames 0 2>&1 | \
  tee silero-vad-work/export/export.log
```

The output is similar to:

```output
Wrote expected probabilities to silero-vad-work/export/expected_probs.bin
Lowering to Ethos-U85...
Exported model saved to silero-vad-work/export/silero_vad_ethos_u.pte
```

Verify the generated outputs and the number of reference probabilities:

```bash
for artifact in \
  silero-vad-work/export/silero_vad_ethos_u.pte \
  silero-vad-work/export/expected_probs.bin \
  silero-vad-work/export/export.log; do
  test -s "$artifact" || {
    echo "Missing export artifact: $artifact" >&2
    exit 1
  }
done

test "$(wc -c < silero-vad-work/export/expected_probs.bin)" -eq $((79 * 4)) || {
  echo "Expected 79 float32 reference probabilities" >&2
  exit 1
}

test "$(grep -c 'CPU operators = 0' silero-vad-work/export/export.log)" -eq 2 || {
  echo "Expected both Vela subgraphs to contain no CPU operators" >&2
  exit 1
}

echo "Export artifacts and Ethos-U lowering verified."
```

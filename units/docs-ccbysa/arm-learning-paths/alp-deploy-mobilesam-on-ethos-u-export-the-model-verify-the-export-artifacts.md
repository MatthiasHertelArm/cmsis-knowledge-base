---
id: "alp-deploy-mobilesam-on-ethos-u-export-the-model-verify-the-export-artifacts"
type: "concept"
domain: "edge-ai"
title: "Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch: Export MobileSAM for Ethos-U85: Verify the export artifacts"
summary: "The files under arm_test/mobilesam/export/ support the remaining steps:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/export-the-model.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/export-the-model/#verify-the-export-artifacts"
license: "CC-BY-SA-4.0"
mode: "V"
---

The files under `arm_test/mobilesam/export/` support the remaining steps:

| Artifact | Path |
|---|---|
| ExecuTorch program | `mobilesam.pte` |
| Preprocessed float32 input tensor | `input.bin` |
| Resized and padded input image | `input.png` |
| Floating-point host mask | `fp32_mask.png` |
| Quantized host mask | `quantized_mask.png` |
| Host mask metrics | `metrics.json` |
| Delegation report | `delegation.txt` |
| TOSA and Vela artifacts | `artifacts/` |

Check that these artifacts exist before building the runner:

```bash
export_dir=arm_test/mobilesam/export

for artifact in \
  mobilesam.pte \
  input.bin \
  input.png \
  fp32_mask.png \
  quantized_mask.png \
  metrics.json \
  delegation.txt; do
  test -s "$export_dir/$artifact" || {
    echo "Missing export artifact: $export_dir/$artifact" >&2
    exit 1
  }
done

test -n "$(find "$export_dir/artifacts" -type f -print -quit)" || {
  echo "No TOSA or Vela artifacts found in $export_dir/artifacts" >&2
  exit 1
}
```

The checks complete without output when the artifacts are present. The point prompt is embedded in the `.pte`, which is compiled into the runner. The image remains a runtime input: the runner reads `input.bin` through semihosting, which lets the FVP access files on the host.

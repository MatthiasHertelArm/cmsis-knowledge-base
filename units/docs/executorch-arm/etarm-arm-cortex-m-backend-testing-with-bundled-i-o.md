---
id: "etarm-arm-cortex-m-backend-testing-with-bundled-i-o"
type: "concept"
domain: "edge-ai"
title: "Arm Cortex-M Backend: Testing with Bundled I/O"
summary: "The tutorial above produces a plain .pte."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@24a6116:docs/source/backends/arm-cortex-m/arm-cortex-m-overview.md"
doc_source: "https://github.com/pytorch/executorch/blob/24a6116/docs/source/backends/arm-cortex-m/arm-cortex-m-overview.md#testing-with-bundled-i-o"
license: "BSD-3-Clause"
mode: "V"
---

The tutorial above produces a plain `.pte`. For programmatic testing,
`aot_arm_compiler --bundleio` instead produces a bundled (`.bpte`) program
that embeds reference inputs and expected outputs; the Cortex-M test runner
loads the bundle via semihosting and self-checks its outputs against the
embedded references, emitting `Test_result: PASS` or `Test_result: FAIL`
on the UART.

The driver for this flow is `examples/arm/run.sh`, which exports the model,
builds the Cortex-M test runner, launches the Corstone-300 FVP with
semihosting enabled, and checks the bundled output. Run it from the
ExecuTorch repo root after `./install_executorch.sh`:

```bash
# One-time: install the Arm toolchain + FVP.
examples/arm/setup.sh --i-agree-to-the-contained-eula
source examples/arm/arm-scratch/setup_path.sh

# Per model: export, build, and run on the FVP in one step.
# (Quantization is the default for the cortex-m55+int8 target.)
examples/arm/run.sh \
    --model_name=<model> \
    --target=cortex-m55+int8 \
    --bundleio
```

Replace `<model>` with any of the validated-model names in the table
below. Without `--calibration_data`, calibration falls back to the model's
`get_example_inputs()` (random data) — enough for bundled-I/O numerical
parity, but not for task-accuracy claims. On `Test_result: FAIL`, inspect
the FVP UART log for the per-tensor diff; supplying a representative
calibration dataset via `--calibration_data=<dir>` often resolves
mismatches caused by random-input calibration.

:::{important}
Bundled I/O checks INT8 **numerical parity** between the exported `.bpte`
and the eager-mode quantized model on reference inputs; it does not
validate task accuracy (VWW / KWS / ImageNet).
:::

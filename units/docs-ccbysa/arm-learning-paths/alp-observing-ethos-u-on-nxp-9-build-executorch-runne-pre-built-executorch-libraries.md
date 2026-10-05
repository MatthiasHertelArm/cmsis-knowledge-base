---
id: "alp-observing-ethos-u-on-nxp-9-build-executorch-runne-pre-built-executorch-libraries"
type: "concept"
domain: "edge-ai"
title: "Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration: Build Cortex-M33 firmware for ExecuTorch: Pre-built ExecuTorch libraries"
summary: "The repository includes pre-built static libraries in executorch/lib/, cross-compiled for Cortex-M33 with size optimization (-Os, MinSizeRel):"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/9-build-executorch-runner-for-cm33.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/9-build-executorch-runner-for-cm33/#pre-built-executorch-libraries"
license: "CC-BY-SA-4.0"
mode: "V"
---

The repository includes pre-built static libraries in `executorch/lib/`, cross-compiled for Cortex-M33 with size optimization (`-Os`, MinSizeRel):

| Library | Size | Purpose |
|---------|------|---------|
| `libexecutorch.a` | 52KB | ExecuTorch runtime |
| `libexecutorch_core.a` | 217KB | Core runtime (gc-sections removes unused code) |
| `libexecutorch_delegate_ethos_u.a` | 19KB | Ethos-U NPU delegate backend |
| `libquantized_ops_lib_selective.a` | 7KB | Registers only `quantize_per_tensor.out` and `dequantize_per_tensor.out` |
| `libquantized_kernels.a` | 242KB | Kernel implementations (gc-sections removes unused code) |
| `libkernels_util_all_deps.a` | 308KB | Kernel utilities (gc-sections removes unused code) |

**Note:**
The selective quantized ops library registers only the two CPU operators needed at the NPU delegation boundary. The full `libquantized_ops_lib.a` registers all quantized operators and pulls in approximately 92KB of kernel code, which overflows the 128KB ITCM. If you rebuild the libraries from source, you must build this selective library separately.

---
id: "etarm-examples-for-arm-backends-ethos-u-setup-sh"
type: "concept"
domain: "edge-ai"
title: "Examples for Arm backends Ethos-U, VGF and Cortex-M: setup.sh"
summary: "setup.sh downloads the Arm cross-compilation toolchain and Corstone FVP simulators, installs the backend dependencies, and generates setup_path.sh scripts for adding those tools to your environment. Optional flags also install VGF/MLSDK and Vulkan dependencies."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:examples/arm/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/examples/arm/README.md#setup-sh"
license: "BSD-3-Clause"
mode: "V"
---

`setup.sh` downloads the Arm cross-compilation toolchain and Corstone FVP
simulators, installs the backend dependencies, and generates `setup_path.sh`
scripts for adding those tools to your environment. Optional flags also install
VGF/MLSDK and Vulkan dependencies.

Example to install the default Arm backend dependencies and add them to your current shell:

```bash
./examples/arm/setup.sh --i-agree-to-the-contained-eula
source examples/arm/arm-scratch/setup_path.sh
```

The Arm toolchain dependencies have their own Python constraints. In
particular, the pinned `tosa-tools==2026.5.0` has no Python 3.14 distribution;
making visualization optional does not remove that separate limitation.

Model Explorer visualization is optional and currently supports Python
3.10-3.12. Add `--enable-model-explorer` to install it and the TOSA/PTE adapters in
an isolated directory, keeping their dependencies separate from the TOSA
toolchain:

```bash
./examples/arm/setup.sh \
  --i-agree-to-the-contained-eula \
  --enable-model-explorer
```

Run visualization from an ExecuTorch environment on the same platform and
Python major/minor version used for setup. The interpreter is resolved from
the active environment, allowing a replacement environment or a moved
scratch directory without retaining the original interpreter path.
The PTE adapter currently also brings in the VGF adapter as a transitive
dependency; `run.sh` exposes only TOSA/PTE visualization.

Select the graph format explicitly when enabling Model Explorer. For example,
to visualize the generated TOSA graph:

```bash
./examples/arm/run.sh \
  --model_name=examples/arm/example_modules/add.py \
  --target=ethos-u55-128 \
  --build_only \
  --model_explorer \
  --visualize_tosa
```

Use `--visualize_pte` instead of `--visualize_tosa` to visualize the generated
PTE and its delegated graphs.
When `run.sh` automatically invokes setup on a fresh checkout,
`--model_explorer` also enables installation of the visualization dependencies.

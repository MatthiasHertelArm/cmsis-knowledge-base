---
id: "etarm-smollm2-ethos-u-quickstart-0-prerequisites"
type: "concept"
domain: "edge-ai"
title: "SmolLM2 -> Ethos-U Quickstart: 0. Prerequisites"
summary: "Run all commands from the repository root."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:examples/arm/smollm2_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/examples/arm/smollm2_example_ethos_u/README.md#0-prerequisites"
license: "BSD-3-Clause"
mode: "V"
---

Run all commands from the repository root.

Use an activated Python environment before running the setup commands below,
because `examples/arm/setup.sh` installs Python packages into the active
environment. A conda environment or Python `venv` both work; see
[`docs/source/using-executorch-building-from-source.md`](https://github.com/pytorch/executorch/blob/658390c/examples/arm/smollm2_example_ethos_u/../../../docs/source/using-executorch-building-from-source.md)
for the general ExecuTorch environment setup.

```bash
cd /path/to/executorch
source /path/to/venv/bin/activate
```

Install the Arm Ethos-U dependencies and generate `setup_path.sh`:

```bash
examples/arm/setup.sh \
  --i-agree-to-the-contained-eula \
  --enable-ethos-u-deps
```

Source the generated Arm setup:

```bash
source examples/arm/arm-scratch/setup_path.sh
```

Install the helper Python packages used by this example:

```bash
pip install -U "huggingface_hub[cli]" datasets
pip install -e ./extension/llm/tokenizers/
```

Build the ExecuTorch Arm libraries once so the runner wrappers can find the
`executorch` package in `arm_test`:

```bash
bash backends/arm/scripts/build_executorch.sh
```

If you want the broader Arm backend setup flow, see `examples/arm/README.md`.

---
id: "alp-silero-vad-ethos-u-1-prepare-environment-create-an-isolated-executorch"
type: "concept"
domain: "edge-ai"
title: "Deploy Silero VAD on Arm Ethos-U with ExecuTorch: Prepare the environment and model inputs: Create an isolated ExecuTorch environment"
summary: "The Silero VAD Ethos-U example is available in the upstream ExecuTorch repository. Use the tested main-branch commit so that the commands and generated artifacts match the Learning Path."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/1-prepare-environment.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/1-prepare-environment/#create-an-isolated-executorch-environment"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Silero VAD Ethos-U example is available in the upstream ExecuTorch repository. Use the tested main-branch commit so that the commands and generated artifacts match the Learning Path.

Clone ExecuTorch and check out the tested revision:

```bash
git clone https://github.com/pytorch/executorch.git
cd executorch
git checkout 4fd161058ebe2b9d80d11242a9d21811c0e92dac
git submodule sync --recursive
git submodule update --init --recursive
```

Confirm the checked-out revision:

```bash
git rev-parse --short=12 HEAD
```

The expected output is:

```output
4fd161058ebe
```

Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Install ExecuTorch and its Python dependencies:

```bash
CMAKE_ARGS="-DEXECUTORCH_BUILD_MLX=OFF" \
  env -u DEBUG ./install_executorch.sh \
  --minimal --optional-dependency ethos_u

python - <<'PY'
import executorch.codegen.tools.selective_build
from executorch.backends.arm.ethosu import EthosUPartitioner
from executorch.backends.arm.quantizer import EthosUQuantizer

print("ExecuTorch installation verified")
PY
```

The installation script initializes the Git submodules that are needed by the build. The script also installs the matching PyTorch and ExecuTorch packages. The command omits the unrelated MLX backend and optional packages used by other examples.

---
id: "cet-executorch-on-ethos-u-quick-start"
type: "concept"
domain: "edge-ai"
title: "ExecuTorch on Ethos-U: Quick start"
summary: "The steps below build the default Corstone-320 / Ethos-U85-256 application using cmsis-executorch.csolution.yml. The alternative cmsis-executorch-u55.csolution.yml targets Corstone-300 / Ethos-U55-128. Both can be built and run entirely in Keil Studio for VS Code."
status: "draft"
collection: "cmsis-executorch"
source: "Arm-Examples/CMSIS-Executorch@0a243f1:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Executorch/blob/0a243f1/README.md#quick-start"
license: "Apache-2.0"
mode: "V"
---

The steps below build the default Corstone-320 / Ethos-U85-256 application
using `cmsis-executorch.csolution.yml`. The alternative
`cmsis-executorch-u55.csolution.yml` targets Corstone-300 / Ethos-U55-128.
Both can be built and run entirely in Keil Studio for VS Code.

### 1. Create the application

On [GitHub](https://github.com/Arm-Examples/CMSIS-Executorch), select **Use this
template** to create your application repository, then clone it and open its
folder in VS Code. In the CMSIS view, select **... > Select Active Solution
from Workspace**, then choose `cmsis-executorch.csolution.yml` for this Quick
start.

### 2. Set up the project tools

When the folder opens, Arm Environment Manager installs the tools listed in
`vcpkg-configuration.json`.

To set up ML model export, select **Terminal > Run Task > Create Python environment
(uv)**. This task uses [Astral's uv](https://docs.astral.sh/uv/) from `PATH` and can
download a supported Python (`>=3.10,<3.14`) before installing the dependencies.
Alternatively, **Create Python environment (pip)** uses a compatible Python
already installed on the host. Python 3.14 is not supported because
tosa-tools 2026.5.0 has no 3.14 wheels.

The [`PyTorch::ExecuTorch`](https://www.keil.arm.com/packs/executorch-pytorch/)
pack is resolved through the Arm pack service. To install it manually instead:

```bash
cpackget add PyTorch::ExecuTorch@1.5.1
```

> [!IMPORTANT]
> The pack and [ExecuTorch Python exporter](https://docs.pytorch.org/executorch/stable/getting-started.html)
> versions must match, as the generated `.pte` is consumed by the runtime in
> `PyTorch::ExecuTorch@1.5.1`. The matching `executorch==1.5.1` wheel is pinned
> in `requirements.txt`.

### 3. Build and run

The repository contains the generated U85 AI layer, so the default solution
builds immediately. After changing the ML model or target, select **Terminal > Run
Task > Create AI layer**. The task exports the ML model for the active solution's
NPU from its `*.cbuild-mlops.yml` file and rewrites `ai_layer/`.

To use Ethos-U55-128 instead, select
`cmsis-executorch-u55.csolution.yml` as the active solution and run **Create AI
layer** before building.

Use the CMSIS action buttons to build the application, then select **Run** or
**Debug**. Keil Studio starts the selected FVP simulation model automatically.
On macOS, where Arm ships no native FVP, set `model:` in the active csolution's
target-set to `${workspaceFolder}/.vscode/fvp.sh` and copy
`.vscode/launch.json.mac` to
`.vscode/launch.json`. Docker Desktop must be running; the first Run or Debug
builds the container image (about 100 MB download).

A successful run prints the Ethos-U configuration, output logits, and a pass
result:

```text
Ethos-U version info:
    Arch:       v2.0.0
    MACs/cc:    256
    Cmd stream: v1
ExecuTorch Ethos-U85-256 application: 8720 byte model
Output: 10 element(s): -0.0142 0.0206 0.0601 -0.0886 0.0791 0.0522 -0.0301 -0.0775 -0.2800 -0.0095
Test_result: PASS
```

### Command-line build

The same workflow from the VS Code Terminal (or any shell with the tools from
`vcpkg-configuration.json` on the path) is three commands plus the one-time
venv setup.

#### 0. Create the Python environment (once)

On Linux or macOS:

```bash
./setup_venv.sh
```

On Windows:

```powershell
.\setup_venv.bat
```

The setup script creates `.venv/` and installs the packages required to
quantize and export the ML model. It is safe to run again; use `--recreate` when
you want a completely new environment. The wrappers use `python3` (`python` on
Windows); point them at another interpreter with `PYTHON=python3.12 ./setup_venv.sh`.

With [Astral's uv](https://docs.astral.sh/uv/getting-started/installation/) on `PATH`,
`./setup_venv.sh --uv --python 3.12` (or `.\setup_venv.bat ...`) creates the
environment with `uv venv` for that Python version, downloading the interpreter
if needed, and installs with `uv pip`. Add `--recreate` to change the Python
version of an existing environment.

#### 1. Generate the MLOps information

```bash
cbuild setup cmsis-executorch.csolution.yml --active SSE-320-U85 --packs
```

This resolves the packs and the active target and writes
`cmsis-executorch.cbuild-mlops.yml`: the processor, NPU and Vela
settings of the target, and the location of the AI layer. (`--packs`
installs missing packs and is only needed on a fresh checkout; the layers'
RTE configuration is committed, so no `--update-rte` is required.)

#### 2. Create the AI layer

```bash
python3 create_ai_layer.py cmsis-executorch.cbuild-mlops.yml
```

This is the MLOps step. The script reads the NPU and Vela settings from the
file, quantizes and exports `model/model.py` for that NPU, and writes the
complete AI layer into `ai_layer/`: the component selection and the ML model as a
C array. It runs itself in `.venv` when started with another interpreter (use
`python` on Windows).

#### 3. Build the application

```bash
cbuild cmsis-executorch.csolution.yml --active SSE-320-U85
```

A plain CMSIS build; no Python is involved. The resulting image is:

```text
out/cmsis-executorch/SSE-320-U85/Debug/cmsis-executorch.axf
```

#### 4. Run on the FVP

```bash
FVP_Corstone_SSE-320 \
    -f board/Corstone-320/fvp_config.txt --simlimit 60 \
    -a out/cmsis-executorch/SSE-320-U85/Debug/cmsis-executorch.axf
```

This is the FVP command the Run and Debug buttons use too. On macOS, call
`.vscode/fvp.sh` with the same arguments; it runs the FVP simulation model in
Docker.

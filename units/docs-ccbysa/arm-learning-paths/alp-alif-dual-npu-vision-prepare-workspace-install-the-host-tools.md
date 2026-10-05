---
id: "alp-alif-dual-npu-vision-prepare-workspace-install-the-host-tools"
type: "concept"
domain: "edge-ai"
title: "Run parallel vision inference on an Alif Ensemble E8 with Zephyr: Prepare the board and workspace: Install the host tools"
summary: "Confirm that the Xcode Command Line Tools are installed on your host machine:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/prepare-workspace.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/prepare-workspace/#install-the-host-tools"
license: "CC-BY-SA-4.0"
mode: "V"
---

Confirm that the Xcode Command Line Tools are installed on your host machine:

```bash
xcode-select -p
```

If the command reports that the tools are missing, install them before you continue:

```bash
xcode-select --install
```

Install Git, CMake, and Python 3.12 with Homebrew. Then, create the `west` Python environment:

```bash
brew install git cmake python@3.12
mkdir -p $HOME/alif-dual-npu
cd $HOME/alif-dual-npu
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install \
  west==1.5.0 \
  pyelftools==0.33 \
  fdt==0.3.3 \
  ninja==1.13.2
```

Confirm that `west` and `ninja` are available:

```bash
west --version
ninja --version
```

If available, both commands print a version number.

**Note:**

- If CMake reports that it can't find `ninja`, install it in the active virtual environment:

  ```bash
  source $HOME/alif-dual-npu/.venv/bin/activate
  python -m pip install ninja
  ```
  Run the build again with `--pristine`.

- If the Alif flash runner can't import `fdt`, activate the same environment and install the missing module:

  ```bash
  source $HOME/alif-dual-npu/.venv/bin/activate
  python -m pip install fdt
  ```

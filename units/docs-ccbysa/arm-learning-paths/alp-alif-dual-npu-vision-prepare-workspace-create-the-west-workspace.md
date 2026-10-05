---
id: "alp-alif-dual-npu-vision-prepare-workspace-create-the-west-workspace"
type: "concept"
domain: "edge-ai"
title: "Run parallel vision inference on an Alif Ensemble E8 with Zephyr: Prepare the board and workspace: Create the west workspace"
summary: "Clone the SDK fork that contains the dual-NPU sample at the validated revision, then initialize a local west workspace from that checkout. The fork's main branch stays synchronized with the Alif SDK main branch."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/prepare-workspace.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/prepare-workspace/#create-the-west-workspace"
license: "CC-BY-SA-4.0"
mode: "V"
---

Clone the SDK fork that contains the dual-NPU sample at the validated revision,
then initialize a local `west` workspace from that checkout.
The fork's `main` branch stays synchronized with the Alif SDK `main`
branch.

The dual-NPU application is maintained separately on the
`dual-npu-main-integration` branch, which also includes the support for MT9M114,
image signal processor, and MW405:

```bash
cd $HOME/alif-dual-npu
source .venv/bin/activate
git clone --branch dual-npu-main-integration --single-branch \
  https://github.com/varunchariArm/sdk-alif.git sdk-alif
git -C sdk-alif checkout d194c62d41422ccae9355637d91c4344e0d55d24
west init -l sdk-alif
west config manifest.project-filter +executorch
west update --narrow
python -m pip install -r zephyr/scripts/requirements.txt
west sdk install --toolchains arm-zephyr-eabi
```

The manifest project appears at `sdk-alif`. The remaining projects appear under `modules`, `bootloader`, `tools`, and `zephyr`.

**Note:**
Don't initialize from `alifsemi/sdk-alif` directly. The dual-NPU application hasn't yet
been merged there. Use the fork's `dual-npu-main-integration` branch which contains the application.


Initialize the ExecuTorch submodules:

```bash
git -C modules/lib/executorch submodule update --init --recursive
```

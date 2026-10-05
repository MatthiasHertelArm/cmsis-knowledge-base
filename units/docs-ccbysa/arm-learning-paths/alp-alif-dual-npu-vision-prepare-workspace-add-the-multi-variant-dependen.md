---
id: "alp-alif-dual-npu-vision-prepare-workspace-add-the-multi-variant-dependen"
type: "concept"
domain: "edge-ai"
title: "Run parallel vision inference on an Alif Ensemble E8 with Zephyr: Prepare the board and workspace: Add the multi-variant dependencies"
summary: "You'll use the multi-variant support merged into the Ethos-U core driver main branch."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/prepare-workspace.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/prepare-workspace/#add-the-multi-variant-dependencies"
license: "CC-BY-SA-4.0"
mode: "V"
---

You'll use the multi-variant support merged into the Ethos-U core driver
`main` branch. This support allows one Cortex-M55 to manage the U55 and U85
through one driver registry, avoiding the system power overhead of assigning
each NPU to a separate microcontroller unit.

Clone the current `main` branch:

```bash
git clone --branch main \
  https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-core-driver.git \
  modules/ethos-u-core-driver-src
git -C modules/ethos-u-core-driver-src merge-base --is-ancestor \
  b7cd193afde80afe8bbae9a26d2ca6586554f054 HEAD
```

The Alif `west` manifest also downloads Zephyr's `hal_ethos_u` module. That
module is a separately maintained snapshot. Its manifest revision doesn't
yet contain the merged multi-variant implementation. The explicit clone
therefore remains necessary. The ancestor test is a guard rather than a pin:
it permits newer `main` revisions while rejecting an old or stale checkout
that can't run U55 and U85 through the same driver registry.

Clone and pin CMSIS-NN:

```bash
git clone https://github.com/ARM-software/CMSIS-NN.git \
  modules/cmsis-nn-src
git -C modules/cmsis-nn-src checkout \
  d933672e7ca97eec70ef43230baee7b20c2a28ae
```

Create the Python environment that's used by the ExecuTorch CMake integration:

```bash
python3.12 -m venv .venv-executorch
source .venv-executorch/bin/activate
python -m pip install --upgrade pip
python -m pip install \
  -r modules/lib/executorch/requirements-examples.txt
python -m pip install \
  west==1.5.0 \
  -r zephyr/scripts/requirements-base.txt
cd modules/lib/executorch
env -u DEBUG CMAKE_ARGS="-DEXECUTORCH_BUILD_MLX=OFF" \
  ./install_executorch.sh
cd ../../..
deactivate
```

Python 3.12 is used for compatibility with the pinned ExecuTorch revision.

**Note:**
Removing a host `DEBUG` variable prevents ExecuTorch from
interpreting a non-numeric shell value as its numeric build option. You don't need the optional `ethos_u` Python dependency group for the firmware build.


Apply the sample's ExecuTorch integration and Zephyr SRAM placement patches,
then check the dependencies:

```bash
./sdk-alif/samples/modules/executorch/dual_npu_vision/setup_workspace.sh
```

The output is similar to:

```output
Applied ExecuTorch dual-NPU patch.
Applied Zephyr SRAM1 placement patch.
Ethos-U core driver main: ...
Workspace dependencies are ready.
```

If you run the script again, it reports that both patches are already applied.
Run the script again after `west update`, which can restore either module checkout.

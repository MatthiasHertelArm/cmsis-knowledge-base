---
id: "alp-alif-image-classification-aws-ec2-setup-set-up-the-arm-ethos-u-toolcha"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Compile the model on an Arm cloud instance: Set up the Arm/Ethos-U toolch"
summary: "ExecuTorch includes a setup script that downloads the Arm GNU toolchain, CMSIS, and the Vela compiler. We expect this script to fail due to a known issue."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/aws-ec2-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/aws-ec2-setup/#set-up-the-arm-ethos-u-toolchain"
license: "CC-BY-SA-4.0"
mode: "V"
---

ExecuTorch includes a setup script that downloads the Arm GNU toolchain, CMSIS, and the Vela compiler. We expect this script to fail due to a known issue. If / when it does, check that it has failed in the expected place, and if so, move onto the next steps - don't try to fix it yourself:

```bash
./examples/arm/setup.sh --i-agree-to-the-contained-eula
```

The script fails at the `tosa_serialization_lib` build step due to a pybind11 version incompatibility. This is a known issue. When you see an error containing `def_property family doesn't currently support keep_alive`, fix the dependency and complete the setup manually.

First, install a compatible version of pybind11 and the required build tools:

```bash
pip install "pybind11<2.14" scikit-build-core setuptools_scm
```

Next, build and install the serialization library using those local packages:

```bash
CMAKE_POLICY_VERSION_MINIMUM=3.5 pip install --no-build-isolation \
  --no-dependencies \
  ~/alif/executorch/examples/arm/arm-scratch/tosa-tools/serialization
```

Then install the Ethos-U Vela compiler, which the setup script didn't reach due to the earlier failure:

```bash
pip install --no-dependencies \
  -r ~/alif/executorch/backends/arm/requirements-arm-ethos-u.txt
```

Re-run the setup script to complete the remaining steps:

```bash
./examples/arm/setup.sh --i-agree-to-the-contained-eula
```

Source the environment paths that the setup script generated:

```bash
source examples/arm/arm-scratch/setup_path.sh
```

After the setup script, reinstall ExecuTorch and its dependencies:

```bash
python -m pip install -e . --no-build-isolation
pip install "torchao==0.15.0"
```

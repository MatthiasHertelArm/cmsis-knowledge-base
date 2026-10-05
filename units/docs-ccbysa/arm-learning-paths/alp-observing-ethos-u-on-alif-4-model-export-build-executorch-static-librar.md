---
id: "alp-observing-ethos-u-on-alif-4-model-export-build-executorch-static-librar"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: (Optional) Export PyTorch model to ExecuTorch format: Build ExecuTorch static libraries"
summary: "The firmware links against ExecuTorch runtime libraries. Build the bare-metal Cortex-M libraries inside the container:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/4-model-export.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/4-model-export/#build-executorch-static-libraries"
license: "CC-BY-SA-4.0"
mode: "V"
---

The firmware links against ExecuTorch runtime libraries. Build the bare-metal Cortex-M libraries inside the container:

```bash
cd $ET_HOME
source ~/executorch-venv/bin/activate
rm -rf arm_test/cmake-out
bash backends/arm/scripts/build_executorch.sh
```

**Note:**
This step can take several minutes.


When the build finishes, list the generated static libraries:

```bash
find arm_test/cmake-out -type f -name "*.a" | sort
```

The output is similar to:

```output
libexecutorch.a
libexecutorch_core.a
libexecutorch_delegate_ethos_u.a
libcortex_m_ops_lib.a
libcmsis-nn.a
```

---
id: "alp-observing-ethos-u-on-alif-3-docker-executorch-setu-install-executorch"
type: "concept"
domain: "edge-ai"
title: "3 docker executorch setup: Install ExecuTorch"
summary: "After activating the environment, install ExecuTorch:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/3-docker-executorch-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/3-docker-executorch-setup/#install-executorch"
license: "CC-BY-SA-4.0"
mode: "V"
---

After activating the environment, install ExecuTorch:

```bash
cd $ET_HOME
# Install ExecuTorch in editable mode
CMAKE_BUILD_PARALLEL_LEVEL=2 pip install --no-build-isolation -e .
```

**Note:**
The `--no-build-isolation` flag is required so ExecuTorch finds the PyTorch installation from `install_requirements.sh`. 

`CMAKE_BUILD_PARALLEL_LEVEL=2` limits the number of parallel CMake build jobs during installation. This limit reduces peak memory usage and helps avoid out-of-memory failures.


Verify the installation:

```bash
python3 -c "from executorch.exir import to_edge; print('ExecuTorch installed successfully')"
```

The output is similar to:

```output
ExecuTorch installed successfully
```

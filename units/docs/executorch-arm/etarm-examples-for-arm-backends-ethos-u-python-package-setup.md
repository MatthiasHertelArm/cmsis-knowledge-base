---
id: "etarm-examples-for-arm-backends-ethos-u-python-package-setup"
type: "concept"
domain: "edge-ai"
title: "Examples for Arm backends Ethos-U, VGF and Cortex-M: Python package setup"
summary: "For Ethos-U examples, install the current checkout and the dependencies needed for ahead-of-time (AOT) export in a clean Python environment:"
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@6368414:examples/arm/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/6368414/examples/arm/README.md#python-package-setup"
license: "BSD-3-Clause"
mode: "V"
---

For Ethos-U examples, install the current checkout and the dependencies needed
for ahead-of-time (AOT) export in a clean Python environment:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
./install_executorch.sh --optional-dependency ethos_u
```

After the base dependencies are installed, the equivalent editable package
command is `pip install -e '.[ethos_u]' --no-build-isolation`. The `ethos_u`
extra provides host-side export dependencies; it does not install the Arm
toolchain, FVPs, or target runtime. Run `setup.sh` below to install the cross
compiler, FVPs, and backend tools used by these examples.

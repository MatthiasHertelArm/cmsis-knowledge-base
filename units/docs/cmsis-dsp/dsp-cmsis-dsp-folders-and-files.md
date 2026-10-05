---
id: "dsp-cmsis-dsp-folders-and-files"
type: "concept"
domain: "optimization"
title: "CMSIS-DSP: Folders and files"
summary: "The only folders required to build and use CMSIS-DSP Library are:"
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:README.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/README.md#folders-and-files"
license: "Apache-2.0"
mode: "V"
---

The only folders required to build and use CMSIS-DSP Library are:

* Source
* Include
* PrivateInclude
* ComputeLibrary (only when using Neon)
* dsppp/Include (when using the C++ API)

Other folders are part of different projects, tests or examples.

### Folders

* cmsisdsp
  * Required to build the CMSIS-DSP PythonWrapper for the Python repository
  * It contains all Python packages
* ComputeLibrary:
  * Some kernels required when building CMSIS-DSP with Neon acceleration
* dsppp:
  * DSP++ C++ API headers, tests and examples
* Examples:
  * Examples of use of CMSIS-DSP on bare metal Cortex-M
  * Require the use of CMSIS Build tools
* Include:
  * Include files for CMSIS-DSP
* PrivateInclude:
  * Some include needed to build CMSIS-DSP
* PythonWrapper:
  * C code for the CMSIS-DSP PythonWrapper
  * Examples for the PythonWrapper
* Scripts:
  * Debugging scripts
  * Script to generate some coefficient tables used by CMSIS-DSP
* Source:
  * CMSIS-DSP source
* Testing:
  * CMSIS-DSP Test framework for bare metal Cortex-M and Cortex-A
  * Require the use of CMSIS build tools

### Files

Some files are needed to generate the PythonWrapper:

* PythonWrapper_README.md
* LICENSE
* MANIFEST.in
* pyproject.toml
* setup.py

# License

CMSIS-DSP  is licensed under [(figure: License)](https://github.com/ARM-software/CMSIS-DSP/blob/main/LICENSE).

# Contributions and Pull Requests

Contributions are accepted under [(figure: License)](https://github.com/ARM-software/CMSIS-DSP/blob/main/LICENSE). Only submit contributions where you have authored all of the code.

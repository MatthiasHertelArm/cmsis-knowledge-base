---
id: "mlek-building-the-ml-embedded-code-samp-preparing-build-environment"
type: "concept"
domain: "edge-ai"
title: "Building the ML embedded code sample applications from sources: Build process / Preparing build environment"
summary: "Certain third-party sources are required to be present on the development machine to allow the example sources in this repository to link against."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/building.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/building.md#preparing-build-environment"
license: "Apache-2.0"
mode: "V"
---

_Part of: Build process_

#### Fetching submodules

Certain third-party sources are required to be present on the development machine to allow the example sources in this
repository to link against.

1. [TensorFlow Lite Micro repository](https://github.com/tensorflow/tensorflow)
2. [ExecuTorch repository](https://github.com/pytorch/executorch)
3. [Ethos-U NPU core driver repository](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-core-driver)
4. [Ethos-U NPU core platform repository](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-core-platform)
5. [CMSIS-6](https://github.com/ARM-software/CMSIS_6.git)
6. [CMSIS-DSP](https://github.com/ARM-software/CMSIS-DSP.git)
7. [CMSIS-NN](https://github.com/ARM-software/CMSIS-NN.git)
8. [CMSIS-DFP](https://github.com/ARM-software/Cortex_DFP.git)

> **Note:** If you are using non git project sources, run `python3 ./scripts/py/download_dependencies.py` and ignore further git
> instructions. Proceed to [Fetching resource files](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#fetching-resource-files) section.

To pull the submodules:

```sh
git submodule update --init -j 4  # set the number of parallel threads to use
```

This downloads all required components and places them in a tree under `dependencies` directory.

```tree
dependencies
  ├── cmsis-5
  ├── cmsis-6
  ├── cmsis-dsp
  ├── cmsis-nn
  ├── core-driver
  ├── core-platform
  ├── cortex-dfp
  ├── executorch
  └── tensorflow
```

> **Note:** The default source paths for the `TPIP` sources assume the above directory structure. However, all the
> relevant paths can be overridden by CMake configuration arguments `TENSORFLOW_SRC_PATH`, `EXECUTORCH_SRC_PATH`,
> `ETHOS_U_NPU_DRIVER_SRC_PATH`, `CMSIS_SRC_PATH`, `CMSIS_DSP_SRC_PATH`, `CMSIS_NN_SRC_PATH` and `CORTEX_DFP_SRC_PATH`.

#### Fetching resource files

Every ML use-case example in this repository also depends on external neural network models. To download these, run the
following command from the root of the repository:

```sh
python3 ./set_up_default_resources.py
```

This fetches every model into the `resources_downloaded` directory. It also optimizes the models using the Vela compiler
for the default 128 MACs configuration of the Arm® *Ethos™-U55* NPU, the default 256 MACs configuration of the
Arm® *Ethos™-U65* NPU and the 256 MACs configuration of the Arm® *Ethos™-U85* NPU.

> **Note:** This script requires Python 3.10 to 3.12 inclusive. Please make sure all
> [build prerequisites](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#build-prerequisites) are satisfied. If your
> environment points to a different system-installed Python3 version, choose a supported
> version explicitly after installing it:
> ```sh
> python3.10 ./set_up_default_resources.py
> ```
>
> **Note:** This script also installs required version of CMake into the virtual environment, which can be used by activating it.

Additional command line arguments supported by this script are:

- `--additional-ethos-u-config-name`: if you need to optimize the models for a different Ethos-U configuration,
  you can pass a list of additional configurations for Vela compiler. For example, to optimize the downloaded models
  for *Ethos™-U55* 32 MAC configuration and *Ethos™-U65* 512 MAC configuration, you can choose to run:

  ```sh
  python3 ./set_up_default_resources.py \
    --additional-ethos-u-config-name ethos-u55-32 \
    --additional-ethos-u-config-name ethos-u65-512
  ```

  > **Note:** As the argument name suggests, the configuration names are **in addition to** the default ones:
  > `ethos-u55-128`, `ethosu-u65-256` and `ethosu-u85-256`.

- `--arena-cache-size`: the size of the arena cache memory area, in bytes.
  The default value is:
  - the internal SRAM size for Corstone-300 implementation on MPS3 specified by AN552,
  when optimizing for the default 128 MACs configuration of the Arm® *Ethos™-U55* NPU.
  - the default value specified in the Vela configuration file [default_vela.ini](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/../../scripts/vela/default_vela.ini),
  when optimizing for the default 256 MACs configuration of the Arm® *Ethos™-U65* NPU
  or the default 256 MACs configuration of the Arm® *Ethos™-U85* NPU.

- `--use-case-resources-file`: Path to a JSON file pointing to resources to be downloaded. See the default
  [use_case_resources.json](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/../../resources/use_case_resources.json) as an example.

- `--downloads-dir`: Root directory where the resources are downloaded.

- `--ml-frameworks`: Select whether TensorFlow Lite Micro and/or ExecuTorch models are downloaded and optimised.
  defaults to `tflm`.

- `--use-case`: Limit the model downloading and optimisation to the specified list of use cases.

- `--parallel`: Specify the number of threads used to download and optimise modules in parallel.

- `--requirements-file`: Provide the path to a requirements.txt file that will be installed into the Python environment.

- `--use-case-resources-file`: Provide paths to additional files of the same structure as
  [use_case_resources.json](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/../../resources/use_case_resources.json) for downloading and optimising additional models.

- `--http-header`: When downloading models from other locations, e.g. services that require authorisation,
  this argument can be used to set additional HTTP headers that are needed for the download to succeed.

> **NOTE**: If you provide a different location by providing `downloads-dir` option, ensure `RESOURCES_PATH` is set
> correctly for the associated CMake configuration. See [build options](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/building.md#build-options) for details.

---
id: "mlek-building-the-ml-embedded-code-samp-build-prerequisites"
type: "concept"
domain: "edge-ai"
title: "Building the ML embedded code sample applications from sources: Build prerequisites"
summary: "Before proceeding, it is essential that the following prerequisites have been fulfilled:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/building.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/building.md#build-prerequisites"
license: "Apache-2.0"
mode: "V"
---

Before proceeding, it is *essential* that the following prerequisites have been fulfilled:

- GNU Arm embedded toolchain version 13.2.1 or higher, OR
- Arm Compiler version 6.22 or higher, OR
- Arm Toolchain for Embedded (ATfE) version 20.1.0 or higher (experimental support)

Test the compiler by running:

  ```commandline
  armclang --version
  ```

  ```log
  Product: Hardware Success Kit (Early Access)
  Component: Arm Compiler for Embedded 6.23
  Tool: armclang [5f103000]
  ```

Alternatively, use:

  ```commandline
  arm-none-eabi-gcc --version
  ```

  ```log
  arm-none-eabi-gcc (Arm GNU Toolchain 13.3.Rel1 (Build arm-13.24)) 13.3.1 20240614
  Copyright (C) 2023 Free Software Foundation, Inc.
  This is free software; see the source for copying conditions.  There is NO
  warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
  ```

For ATfE/LLVM:
  ```commandline
  clang --version
  ```

  ```log
  clang version 20.1.0
  Target: aarch64-unknown-linux-gnu
  Thread model: posix
  ```

> **Note:** If required, add the compiler to the path (can be added to ~/.bashrc to be set permanently):
>
`export PATH=/path/to/armclang/bin:$PATH`, OR
>
`export PATH=/path/to/gcc-arm-none-eabi-toolchain/bin:${PATH}`, OR
>
`export PATH=/path/to/atfe-or-llvm-toolchain/bin:${PATH}`

- If you are using the proprietary Arm Compiler, ensure that the compiler license has been correctly configured.

- CMake version 3.21.0 or above is installed and available on the path. Test CMake by running:

    ```commandline
    cmake --version
    ```

    ```log
    cmake version 3.22.4
    ```

> **Note:** Required version of CMake is also installed in the Python3 virtual environment created by
> `set_up_default_resources.py` script. See [Fetching resource files](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./building.md#fetching-resource-files) section.
>
> To add CMake to the PATH on Ubuntu for example, use: `export PATH=/absolute/path/for/cmake/:${PATH}`
> Once `set_up_default_resources.py` has been executed, activating the virtual environment will enable you
> to use that CMake. Alternatively, from the root of the repository, you could use:
>
> `export PATH=$(readlink -e resources_downloaded/env/bin):${PATH}`

- Python 3.10, 3.11 or 3.12 is installed. Check your current installed version of Python by running:

    ```commandline
    python3 --version
    ```

    ```log
    Python 3.10.12
    ```

  > **Note:** If you do not have a supported version of Python installed, see the
  > [Troubleshooting](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./troubleshooting.md#how-to-update-python3-package-to-a-supported-version)
  > section for instructions on how to install and use one.

- The build system creates a Python virtual environment during the build process. Please make sure that Python virtual
  environment module is installed by running:

    ```commandline
    python3 -m venv
    ```

- The build system uses external Python libraries during the building process. Please make sure that the latest pip and
  libsndfile versions are installed.

  ```commandline
  pip3 --version
  ```

  ```log
  pip 22.0.2 from /usr/lib/python3/dist-packages/pip
  ```

- Make

    ```commandline
    make --version
    ```

    ```log
    GNU Make 4.1

    ...
    ```

> **Note:** Add it to the path environment variable, if needed.

- Access to the internet to download the third-party dependencies, specifically: TensorFlow Lite Micro, ExecuTorch,
  Arm® *Ethos™-U55* NPU driver, and CMSIS. Instructions for downloading these are listed under:
  [preparing build environment](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./building.md#preparing-build-environment).

> **NOTE**: A Docker image built from the `Dockerfile` provided will have all the above packages installed and
> available for use. The GNU Embedded toolchain is available by default and the environment of the image will
> have certain helper variables set for running the FVP within a non-interactive terminal. Run `env` to see the
> list.

### Third-party build prerequisites

- The following software is needed by TensorFlow Lite Micro.

  - xxd
  - unzip
  - Python Pillow
  - curl

> **Note:** Due to the fast-paced nature of development, this list might not be exhaustive.
Please refer to Tensorflow Lite Micro documentation for more info.

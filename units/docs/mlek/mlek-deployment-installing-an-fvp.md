---
id: "mlek-deployment-installing-an-fvp"
type: "concept"
domain: "edge-ai"
title: "Deployment: Fixed Virtual Platform / Installing an FVP"
summary: "An additional step is needed to run the Corstone™-320 FVP. The FVP requires the libpython3.9.so.1.0 library which may not be present on recent Ubuntu versions."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/deployment.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/deployment.md#installing-an-fvp"
license: "Apache-2.0"
mode: "V"
---

_Part of: Fixed Virtual Platform_

To install an FVP:

- Unpack the archive downloaded from [Arm® Ecosystem FVPs](https://developer.arm.com/tools-and-software/open-source-software/arm-platforms-software/arm-ecosystem-fvps).

- Run the installation script in the extracted package. For example, `Arm® Corstone™-300` package will have
  `FVP_Corstone_SSE-300.sh`.

- Follow the instructions to install the FVP to your required location.

> **Note**: The installation process is the same for other supported FVPs (Arm® Corstone™-310, Corstone™-315, Corstone™-320).

#### Arm® Corstone™-320 FVP

An additional step is needed to run the Corstone™-320 FVP.  The FVP requires the `libpython3.9.so.1.0` library which may not be present on recent Ubuntu versions.

There are a few ways to add this library to your environment.  Do *one of* the following:

1. The library is packaged with the FVP and can be added to the local environment by running the following:

    ```commandline
    source ~/FVP_Corstone_SSE-320/scripts/runtime.sh
    ```
    
    (Assuming the default FVP installation directory of `~/FVP_Corstone_SSE-320`).

2. Another approach described in the release notes (`~/FVP_Corstone_SSE-320/doc/Corstone_SSE-320_FVP_ReleaseNotes.txt`) is to build Python3.9 from source:

    ```commandline
    sudo apt-get update
    sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
      libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xzutils \
      tk-dev liblzma-dev tk-dev
    wget https://www.python.org/ftp/python/3.9.18/Python-3.9.18.tgz
    tar xzf Python-3.9.18.tgz
    cd Python-3.9.18
    ./configure --enable-optimizations --prefix=/opt/python/3.9.18/
    make -j "$(nproc)"
    sudo make altinstall

    # Before running the FVP, set the following environment variable:
    export PYTHONHOME=/opt/python/3.9.18
    ```

3. Finally, one other approach is to install the library from the deadsnakes PPA.

    > Note: Arm® is not affiliated with deadsnakes - use at your own risk

    The deadsnakes PPA can be added as follows:

    ```commandline
    sudo apt update
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    ```

    The library can then be installed as follows:
    
    ```commandline
    sudo apt update
    sudo apt install libpython3.9-dev
    ```

The Corstone™-320 FVP can now be run in the same way as the other FVPs.

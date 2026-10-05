---
id: "mlek-troubleshooting-no-matching-distribution-found-for-vela"
type: "concept"
domain: "edge-ai"
title: "Troubleshooting: No matching distribution found for Vela"
summary: "Vela 3.9.0 increases Python requirement to at least version 3.9, if not installed on your system the following error will occur:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/troubleshooting.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/troubleshooting.md#no-matching-distribution-found-for-vela"
license: "Apache-2.0"
mode: "V"
---

Vela 3.9.0 increases Python requirement to at least version 3.9, if not installed on your system the following error will occur:

```log
python3 -m pip install ethos-u-vela==3.9.0
ERROR: Could not find a version that satisfies the requirement ethos-u-vela==3.9.0 (from versions: 0.1.0, 1.0.0, 1.1.0, 1.2.0, 2.0.0, 2.0.1, 2.1.1, 3.0.0, 3.1.0, 3.2.0)
ERROR: No matching distribution found for ethos-u-vela==3.9.0
```

This project supports Python 3.10 to 3.12 inclusive. Ensure that one of these
versions is installed, and check your current installed version of Python by running:

```commandline
python3 --version
```

### How to update Python3 package to a supported version

1. Check your current installed version of Python by running:

   ```commandline
   python3 --version
   ```

   For example:
   ```log
   Python 3.8.0
   ```

2. Install one of the supported Python versions (3.10, 3.11, or 3.12) together
   with the matching virtual environment and development packages. For example,
   to install Python 3.10:

   ```commandline
   sudo apt update
   sudo apt install python3.10 python3.10-venv libpython3.10 libpython3.10-dev
   ```

    If the packages aren't available, Python 3.10 can be installed from source:

    ```commandline
    sudo apt-get update
    sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
      libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xzutils \
      tk-dev liblzma-dev tk-dev
    wget https://www.python.org/ftp/python/3.10.15/Python-3.10.15.tgz
    tar xzf Python-3.10.15.tgz
    cd Python-3.10.15.tgz
    ./configure --enable-optimizations --prefix=/opt/python/3.10.15/
    make -j "$(nproc)"
    sudo make altinstall
    ```

    Alternatively, it is possible to install the packages from the deadsnakes PPA:

    > Note: Arm® is not affiliated with deadsnakes - use at your own risk

    ```commandline
    sudo apt update
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.10 python3.10-venv libpython3.10 libpython3.10-dev
    ```

3. Explicitly specify this Python when executing the set-up Python scripts. For example:

    ```commandline
    python3.10 ./set_up_default_resources.py
    ```
> **Note:**: We do not recommend updating the Python version system-wide as it might break
> various desktop utilities for your OS distribution. However, if you are using a container
> or any other sandboxed environment, you can choose to update it using the following steps.
>
> * Update the `python3` alternatives (set as 1 your previous version displayed at step 1):
>
>   ```commandline
>   sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
>   sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 2
>   ```
>
> * At the prompt, update the configuration by selecting Python3.9 as the chosen default alternative:
>
>   ```commandline
>   sudo update-alternatives --config python3
>   ```
> * Python3.10 is now set as default, you can check it by running:
>
>   ```commandline
>   python3 --version
>   ```
>
>   ```log
>   Python 3.10.0
>   ```

Next section of the documentation: [Appendix](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/appendix.md).

---
id: "alp-zephyr-zephyr-install-the-required-software"
type: "concept"
domain: "rtos"
title: "Run the Zephyr RTOS on Arm Corstone-300: Build and run Zephyr applications: Install the required software to build Zephyr"
summary: "The repository is needed to install the Zephyr dependencies."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr/zephyr.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr/zephyr/#install-the-required-software-to-build-zephyr"
license: "CC-BY-SA-4.0"
mode: "V"
---

1. Add the Kitware repository to your sources list

The repository is needed to install the Zephyr dependencies.

```bash { env="DEBIAN_FRONTEND=noninteractive" }
wget https://apt.kitware.com/kitware-archive.sh
sudo bash kitware-archive.sh
```

2. Install the Zephyr prerequisites

Use the `apt` command to install the required software:

```bash { env="DEBIAN_FRONTEND=noninteractive" }
sudo -E apt install --no-install-recommends -y git cmake ninja-build gperf ccache dfu-util device-tree-compiler wget python3-dev python3-pip python3-setuptools python3-tk python3-wheel xz-utils file make gcc gcc-multilib g++-multilib libsdl2-dev libmagic1 xterm
```

3. Install the Python dependencies 

Install Python dependencies and activate a new virtual environment:

```bash { cwd="/shared" }
sudo apt install -y python3-venv
ls -al
mkdir zephyrproject
python3 -m venv zephyrproject/.venv
source zephyrproject/.venv/bin/activate
pip install west
```

4. Download the Zephyr source code and install additional python dependencies declared in the source:

```bash { env_source="/shared/zephyrproject/.venv/bin/activate",cwd="/shared" }
west init zephyrproject
cd zephyrproject
west update
west zephyr-export
pip install -r zephyr/scripts/requirements.txt
```

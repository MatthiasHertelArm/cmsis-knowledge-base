---
id: "alp-mlek-build-build-the-example-application"
type: "concept"
domain: "edge-ai"
title: "Build and run the Arm Machine Learning Evaluation Kit examples: Build the ML Evaluation Kit examples: Build the example application"
summary: "Run the following commands to install some necessary tools."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/mlek/build.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/mlek/build/#build-the-example-application"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Install the dependencies

Run the following commands to install some necessary tools.

```bash
sudo apt update
sudo apt install unzip python3-venv python3-pip -y
```
### Install the compiler

The examples can be built with [Arm Compiler for Embedded](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded) or [Arm GNU Toolchain](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain).

Install the GNU toolchain (`gcc`).

```bash
wget https://developer.arm.com/-/media/Files/downloads/gnu/13.3.rel1/binrel/arm-gnu-toolchain-13.3.rel1-x86_64-arm-none-eabi.tar.xz

tar -xf arm-gnu-toolchain-13.3.rel1-x86_64-arm-none-eabi.tar.xz

export PATH=~/arm-gnu-toolchain-13.3.rel1-x86_64-arm-none-eabi/bin/:$PATH

```

**Tip:**
You can review the installation guides for further details.

- [Arm Compiler for Embedded](https://learn.arm.com/install-guides/armclang/)
- [Arm GNU Toolchain](https://learn.arm.com/install-guides/gcc/arm-gnu/)



### Clone the repository

Clone the ML Evaluation Kit repository, and navigate into the new directory:

```bash
git clone "https://git.gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit.git"
cd ml-embedded-evaluation-kit
git submodule update --init
```

### Run the build script

The default build is Ethos-U55  and Corstone-300. The default build for Ethos-U85 is Corstone-320. Use the `npu-config-name` flag to set Ethos-U85.

The default compiler is `gcc`, but `armclang` can also be used. Number after `ethos-u85-*` is the number of MACs, 128-2048 (2^n).

Use `--make-jobs` to specify `make -j` value.

You can select either compiler to build applications. You can also try them both and compare the results.

- Build with Arm GNU Toolchain (`gcc`):

```
./build_default.py --npu-config-name ethos-u85-256 --toolchain gnu --make-jobs 8
```

- Build with Arm Compiler for Embedded (`armclang`):

```console
./build_default.py --npu-config-name ethos-u85-256 --toolchain arm --make-jobs 8
```

**Tip:**
Use `./build_default.py --help` for additional information.



The build will take a few minutes.

When the build is complete, you will find the examples (`.axf` files) in the `cmake-build-*/bin` directory. The `cmake-build` directory names are specific to the compiler used and Ethos-U85 configuration. Verify that the files have been created by observing the output of the `ls` command

```bash
ls cmake-build-mps4-sse-320-ethos-u85-256-gnu/bin/
```

The next step is to install the FVP and run the built example applications.

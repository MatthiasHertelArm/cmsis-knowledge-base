---
id: "alp-yolo-on-himax-dev-env-install-software-tools"
type: "concept"
domain: "edge-ai"
title: "Run a computer vision model on a Himax microcontroller: Set up the environment: Install software tools"
summary: "Follow the instructions below to install the required development tools."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/yolo-on-himax/dev-env.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/yolo-on-himax/dev-env/#install-software-tools"
license: "CC-BY-SA-4.0"
mode: "V"
---

Follow the instructions below to install the required development tools.

### Install Python and Pip

You will use Python to build the firmware image and pip to install additional dependencies. 

Verify Python is installed by running:

```bash
python3 --version
```

You should see an output like the following:

```output
Python 3.12.7
```

On Ubuntu, you may need to install `pip` and `venv` with the following commands:

```bash
sudo apt update
sudo apt install python3-pip python3-venv -y
```

Verify Pip is installed correctly:

```bash
pip3 --version
```

The output is similar to:

```output
pip 24.0 from /usr/lib/python3/dist-packages/pip (python 3.12)
```

It is good practice to manage Python packages through a virtual environment. 

Create one with the steps below.

```bash
python3 -m venv $HOME/yolo-venv
source $HOME/yolo-venv/bin/activate
```

Your terminal displays `(yolo-venv)` in the prompt indicating the virtual environment is active.

You also need the Git distributed version control system installed. 

Run the command below to verify that Git is installed on your system:

```bash
git --version
```

If it is installed, you will see output similar to:

```output
git version 2.39.3
```

### Install Make

Install the Make build tool, which is used to build the firmware in the next section.


  **Linux:**
sudo apt update
sudo apt install make -y
  
  **macOS:**
brew install make
  


After Make is installed, run it to print the version.

```bash
make --version
```

The output is similar to:

```output
GNU Make 4.3
Built for x86_64-pc-linux-gnu
Copyright (C) 1988-2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
```

**Note:**
If you are using macOS, you need to verify that your installation is for GNU Make - not the BSD version. You should see GNU in the version output.


### Install the Arm GNU toolchain

The toolchain is used to compile code on the host for the embedded device architecture.


  **x86 Linux:**
cd $HOME
wget https://developer.arm.com/-/media/Files/downloads/gnu/13.2.rel1/binrel/arm-gnu-toolchain-13.2.rel1-x86_64-arm-none-eabi.tar.xz
tar -xvf arm-gnu-toolchain-13.2.rel1-x86_64-arm-none-eabi.tar.xz
export PATH="$HOME/arm-gnu-toolchain-13.2.Rel1-x86_64-arm-none-eabi/bin/:$PATH"
  
  **macOS:**
cd $HOME
wget https://developer.arm.com/-/media/Files/downloads/gnu/13.3.rel1/binrel/arm-gnu-toolchain-13.3.rel1-darwin-arm64-arm-none-eabi.tar.xz
tar -xvf arm-gnu-toolchain-13.3.rel1-darwin-arm64-arm-none-eabi.tar.xz
export PATH="$HOME/arm-gnu-toolchain-13.3.rel1-darwin-arm64-arm-none-eabi/bin/:$PATH"
  


**Note:**
You can add the `export` command to your `.bashrc` or `.zshrc` file to set the search path for each new shell.



Now that your development environment is ready, move to the next section where you will generate the firmware image.

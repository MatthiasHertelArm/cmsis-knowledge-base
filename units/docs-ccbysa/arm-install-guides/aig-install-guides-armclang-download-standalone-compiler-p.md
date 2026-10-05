---
id: "aig-install-guides-armclang-download-standalone-compiler-p"
type: "concept"
domain: "project"
title: "Arm Compiler for Embedded: Download standalone compiler packages"
summary: "You can download individual compiler packages for all supported host platforms from the Arm Product Download Hub or the Arm Tools Artifactory."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/armclang.md"
doc_source: "https://learn.arm.com/install-guides/armclang/#download-standalone-compiler-packages"
license: "CC-BY-SA-4.0"
mode: "V"
---

You can download individual compiler packages for all supported host platforms from the [Arm Product Download Hub](#pdh) or the [Arm Tools Artifactory](#artifactory).

### Download Arm Compiler for Embedded from the Product Download Hub
You can download all compiler packages from the [Arm Product Download Hub](https://developer.arm.com/downloads) (requires login).

You can find download links to all available versions in the [Arm Compiler downloads index](https://developer.arm.com/documentation/ka005198).

You can use all compiler versions standalone or [integrated](#armds) into your Arm Development Studio installation. For more information on downloading a legacy Arm Compiler release, see [What should I do if I want to download a legacy release of Arm Compiler?](https://developer.arm.com/documentation/ka005184)

For more information on usage, see [Arm Product Download Hub](https://learn.arm.com/install-guides/armclang/../pdh).

### Install compiler packages

The installation steps depend on your operating system.

#### Windows

To install on Windows, unzip the downloaded package, launch the installer, and follow on-screen prompts.
```console
win-x86_64\setup.exe
```

#### Linux
To install on Linux hosts, `untar` the downloaded package and run the install script. The exact filenames are version and host dependent.

You can use the `uname -m` call to determine whether your machine is running `aarch64` or `x86_64`, and target the downloaded package accordingly.

```console
mkdir tmp
mv ARMCompiler6.24_standalone_linux-`uname -m`.tar.gz tmp
cd tmp
tar xvfz ARMCompiler6.24_standalone_linux-`uname -m`.tar.gz
./install_`uname -m`.sh --i-agree-to-the-contained-eula --no-interactive -d /home/$USER/ArmCompilerforEmbedded6.24
```

Remove the install data when complete:
```console
cd ..
rm -r tmp
```
Add the `bin` directory of the installation to the `PATH` and confirm `armclang` can be invoked.


  **bash:**
export PATH=/home/$USER/ArmCompilerforEmbedded6.24/bin:$PATH
armclang --version
  
  **csh/tcsh:**
set path=(/home/$USER/ArmCompilerforEmbedded6.24/bin $path)
armclang --version
  


### Download Arm Compiler for Embedded from the Arm Tools Artifactory
The Arm Compiler for Embedded, as well as other tools and utilities, are available in the [Arm Tools Artifactory](https://www.keil.arm.com/artifacts/). The Keil Studio VS Code [Extensions](https://learn.arm.com/install-guides/armclang/../keilstudio_vs) use the artifactory to fetch and install and the necessary components.

You can also fetch directly from the artifactory. This is particularly useful for automated CI/CD flows.

```bash
wget https://artifacts.tools.arm.com/arm-compiler/6.24/19/standalone-linux-armv8l_64-rel.tar.gz
```

The artifactory packages don't have their own installers. You should manually extract files and configure. For example:

```bash
mkdir ArmCompilerforEmbedded6.24
tar xvzf ./standalone-linux-armv8l_64-rel.tar.gz -C ./ArmCompilerforEmbedded6.24 --strip-components=1
rm ./standalone-linux-armv8l_64-rel.tar.gz
export PATH=/home/$USER/ArmCompilerforEmbedded6.24/bin:$PATH
export AC6_TOOLCHAIN_6_24_0=/home/$USER/ArmCompilerforEmbedded6.24/bin
```

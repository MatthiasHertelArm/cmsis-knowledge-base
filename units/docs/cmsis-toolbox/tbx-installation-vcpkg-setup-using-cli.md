---
id: "tbx-installation-vcpkg-setup-using-cli"
type: "concept"
domain: "project"
title: "Installation: vcpkg Setup using CLI"
summary: "The vcpkg is a package management tool that includes features to manage tool artifacts. Arm provides an artifactory system for tools. For more information, refer to Arm Tools Available in vcpkg."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/installation.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/installation/#vcpkg-setup-using-cli"
license: "Apache-2.0"
mode: "V"
---

The [vcpkg](https://vcpkg.io/en/) is a package management tool that includes features to manage tool artifacts. Arm provides an artifactory system for tools. For more information, refer to [Arm Tools Available in vcpkg](https://artifacts.tools.arm.com).

!!! Note
    Microsoft changed the name of the shell version from `vcpkg` to `vcpkg-shell`. Depending on the version that you are using, you may need to call `vcpkg-shell` from the command line instead of `vcpkg`.

The following describes how to set up the CMSIS-Toolbox with `vcpkg` in a command-line (CLI) environment. In many examples, the file `vcpkg-configuration.json` already exists, which describes the tool environment required for the example. Refer to the last step to create a new `vcpkg-configuration.json` file.

### Install and enable vcpkg

The command to install and enable `vcpkg` depends on the shell.

**Windows Command Prompt (cmd):**

```bat
curl -LO https://aka.ms/vcpkg-init.cmd && .\vcpkg-init.cmd
%USERPROFILE%\.vcpkg\vcpkg-init.cmd
```

**Windows PowerShell:**

```ps1
iex (iwr -useb https://aka.ms/vcpkg-init.ps1)
. ~/.vcpkg/vcpkg-init.ps1
```

**Linux (x64)/macOS:**

```sh
. <(curl https://aka.ms/vcpkg-init.sh -L)
. ~/.vcpkg/vcpkg-init
```

!!! Note
    vcpkg is currently not working on
    - MSYS Bash (such as Git Bash) on Windows.
    - Linux (aarch64)

### Activate tools

The required tools are specified in the `vcpkg-configuration.json` file, which can be found in the current or any parent directory.

```txt
vcpkg-shell activate
```

!!! Note
    In case that activate fails, update registries to access the latest versions of the tools artifacts:
    `vcpkg-shell x-update-registry --all`

### Deactivate tools

The configuration is deactivated with:

```txt
vcpkg-shell deactivate
```

### Create `vcpkg-configuration.json`

To create a new `vcpkg-configuration.json` file including the artifacts cmsis-toolbox, cmake, ninja, and arm-none-eabi-gcc use this sequence of commands:

```txt
vcpkg-shell new --application
vcpkg-shell add artifact arm:cmsis-toolbox [--version major.minor.patch]
vcpkg-shell add artifact arm:cmake
vcpkg-shell add artifact arm:ninja
vcpkg-shell add artifact arm:arm-none-eabi-gcc
vcpkg-shell activate
```

Alternatively, you may use an existing repository, for example [github.com/Open-CMSIS-Pack/vscode-get-started](
https://github.com/Open-CMSIS-Pack/vscode-get-started) with a `vcpkg-configuration.json` file.

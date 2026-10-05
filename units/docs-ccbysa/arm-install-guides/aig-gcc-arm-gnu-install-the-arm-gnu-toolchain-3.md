---
id: "aig-gcc-arm-gnu-install-the-arm-gnu-toolchain-3"
type: "concept"
domain: "project"
title: "Arm GNU Toolchain: Install the Arm GNU Toolchain on Windows"
summary: "The steps depend on the release version."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/gcc/arm-gnu.md"
doc_source: "https://learn.arm.com/install-guides/gcc/arm-gnu/#install-the-arm-gnu-toolchain-on-windows"
license: "CC-BY-SA-4.0"
mode: "V"
---

The steps depend on the release version.

### Releases prior to 15.2.Rel1

Double-click the installer, such as `arm-gnu-toolchain-14.3.rel1-mingw-w64-i686-arm-none-eabi.exe`, and follow the on-screen instructions.

The installer can also be run on the command line. When run on
the command-line, you can set the following options:
  - `/S` Run in silent mode
  - `/P` Adds the installation `bin` directory to the system `PATH`
  - `/R` Adds Install Folder registry entry for the install.

For example, to install the tools silently, update the search path and add the registry entry run. Replace `<version>` with a release version prior to 15.2.Rel1 of your choice:

```console
arm-gnu-toolchain-<version>-mingw-w64-i686-arm-none-eabi.exe /S /P /R
```

The zip package is a backup to Windows installer for those who can't run the installer. You can unzip the package and then run the tools directly.

### Releases starting from 15.2.Rel1

Double-click on the installer, such as  `arm-gnu-toolchain-15.2.rel1-mingw-w64-i686-arm-none-eabi.msi`, and follow on-screen instructions.

To install silently from the command line, run the following. Replace `<version>` with a release version starting from 15.2.Rel1 of your choice:

```console
 msiexec /i arm-gnu-toolchain-<version>-mingw-w64-i686-arm-none-eabi.msi EULA=1 /quiet
```

The zip package is a backup to Windows installer for those who can't run the installer. You can unzip the package and then run the tools directly.

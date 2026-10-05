---
id: "aig-gcc-arm-gnu-install-the-arm-gnu-toolchain-2"
type: "concept"
domain: "project"
title: "Arm GNU Toolchain: Install the Arm GNU Toolchain on macOS"
summary: "Downloads for macOS are available as tar files (.tar.xz) and package files (.pkg)."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/gcc/arm-gnu.md"
doc_source: "https://learn.arm.com/install-guides/gcc/arm-gnu/#install-the-arm-gnu-toolchain-on-macos"
license: "CC-BY-SA-4.0"
mode: "V"
---

Downloads for `macOS` are available as tar files (`.tar.xz`) and package files (`.pkg`).

### tar files
For `.tar.xz` files, unpack the downloaded file to the install directory. Replace the `<version>` and `<host-arch>` with the version and host architecture of your choice:

```console
tar xJf arm-gnu-toolchain-<version>-<host-arch>-<TRIPLE>.tar.xz -C /path/to/install/dir
```

### pkg files
For `.pkg` files, use the installer. Replace the `<version>` and `<host-arch>` with the version and host architecture of your choice:

```console
sudo installer -pkg arm-gnu-toolchain-<version>-<host-arch>-<TRIPLE>.pkg -target /
```

### Update the search path

Use a text editor to add the `bin` directory as a new line in `/etc/paths`.

For example, for version 15.2.rel1, the path could be: `/Applications/ArmGNUToolchain/15.2.rel1/arm-none-eabi/bin`

The `/etc/paths` file is a list of paths to search:

```console
/usr/local/bin
/System/Cryptexes/App/usr/bin
/usr/bin
/bin
/usr/sbin
/sbin
/Applications/ArmGNUToolchain/15.2.rel1/arm-none-eabi/bin
```

### Apple Silicon

The following is a specific example for macOS with Apple Silicon and the AArch32 bare-metal target:

**Note:**
The following commands use Arm GNU Toolchain version 15.2.Rel1. The same commands work with other versions. Replace the file used in these steps with the file for your version of choice. To find the latest version, see [Arm GNU Toolchain downloads](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads).


```console
wget https://developer.arm.com/-/media/Files/downloads/gnu/15.2.rel1/binrel/arm-gnu-toolchain-15.2.rel1-darwin-arm64-arm-none-eabi.pkg
sudo installer -pkg arm-gnu-toolchain-15.2.rel1-darwin-arm64-arm-none-eabi.pkg -target /
echo '/Applications/ArmGNUToolchain/15.2.rel1/arm-none-eabi/bin' | sudo tee -a /etc/paths
```

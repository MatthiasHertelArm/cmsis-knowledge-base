---
id: "aig-install-guides-llvm-embedded-install-arm-toolchain-for-embe-2"
type: "concept"
domain: "project"
title: "Arm Toolchain for Embedded: Install Arm Toolchain for Embedded on macOS"
summary: "To download the latest release from GitHub, copy and paste the following URL into your browser:"
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/llvm-embedded.md"
doc_source: "https://learn.arm.com/install-guides/llvm-embedded/#install-arm-toolchain-for-embedded-on-macos"
license: "CC-BY-SA-4.0"
mode: "V"
---

To download the latest release from GitHub, copy and paste the following URL into your browser:

```console
https://github.com/arm/arm-toolchain/releases/download/release-22.1.0-ATfE/ATfE-22.1.0-Darwin-universal.dmg
```

Install the toolchain by opening the `.dmg` file and following the instructions.

Add the ATfE `bin` directory to your `PATH`:

```command
export PATH=/Applications/ATfE-22.1.0-Darwin-universal/bin:$PATH
```

The toolchain binaries might be quarantined. Navigate to the `bin` directory and use the `xattr` command to remove the quarantine:

```command
cd /Applications/ATfE-22.1.0-Darwin-universal/bin
find . -type f -perm +0111 | xargs xattr -d com.apple.quarantine
```

You can now [test your installation](#test).

---
id: "aig-install-guides-armds-how-do-i-get-started-with-arm"
type: "concept"
domain: "project"
title: "Arm Development Studio: How do I get started with Arm Development Studio?"
summary: "To verify everything is working, configure a toolchain and run the compiler from your command prompt. On Linux:"
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/armds.md"
doc_source: "https://learn.arm.com/install-guides/armds/#how-do-i-get-started-with-arm-development-studio"
license: "CC-BY-SA-4.0"
mode: "V"
---

To verify everything is working, configure a toolchain and run the compiler from your command prompt. On Linux:

```command
cd $HOME/developmentstudio-2026.0-1/bin
./suite_exec --toolchain "Arm Toolchain for Embedded Professional" bash -c "clang --version"
```

The output is similar to:

```output
Arm Toolchain for Embedded Professional 22.1.0 build 92, based on clang version 22.1.0
Target: aarch64-unknown-linux-gnu
Thread model: posix
InstalledDir: /home/ubuntu/developmentstudio-2026.0-1/sw/atfe-pro22.1.0/bin
```

**License:**
The compiler reports its version without a license, but running it to build code requires a valid license. See [How do I set up the product license?](#how-do-i-set-up-the-product-license) to set up an evaluation or full license.


You should now be ready to use Arm Development Studio. See the [Get started with Arm Development Studio](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/armds/) learning path for more information.

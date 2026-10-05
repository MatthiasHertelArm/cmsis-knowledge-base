---
id: "aig-install-guides-armds-how-do-i-configure-the-command"
type: "concept"
domain: "project"
title: "Arm Development Studio: How do I configure the command line?"
summary: "You will see Arm DS <version> Command Prompt installed. This configures all necessary environment variables for use with the tools. You can select an appropriate toolchain with:"
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/armds.md"
doc_source: "https://learn.arm.com/install-guides/armds/#how-do-i-configure-the-command-line"
license: "CC-BY-SA-4.0"
mode: "V"
---

### How do I configure the Windows command line?

You will see `Arm DS <version> Command Prompt` installed. This configures all necessary environment variables for use with the tools. You can select an appropriate toolchain with:
```command
select_toolchain
```
or set a default version with:
```command
select_default_toolchain
```
**Toolchains:**
By default, only the supplied `Arm Toolchain for Embedded Professional` is installed with Arm Development Studio. Other versions can be installed and [registered](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio/Register-a-compiler-toolchain).


### How do I configure the Linux command line?

Navigate to the `bin` directory of your install, for example:
```command
cd $HOME/developmentstudio-2026.0-1/bin
```
Use `suite_exec` to start an appropriate command prompt, for example:
```command
./suite_exec --toolchain "Arm Toolchain for Embedded Professional" bash
```
To remove the need for the `--toolchain` option, first run:
```command
./select_default_toolchain
```
and select the desired toolchain. You can then configure with:
```command
./suite_exec bash
```
**Toolchains:**
By default, only the supplied `Arm Toolchain for Embedded Professional` is installed with Arm Development Studio. Other versions can be installed and [registered](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio/Register-a-compiler-toolchain).

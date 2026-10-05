---
id: "alp-armds-build-build-an-example-from-the-comm"
type: "concept"
domain: "project"
title: "Get started with Arm Development Studio: Import and build example project: Build an example from the command line"
summary: "You can also build projects from the command line, either via directly invoking the build tools, or by using make tools."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/armds/build.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/armds/build/#build-an-example-from-the-command-line"
license: "CC-BY-SA-4.0"
mode: "V"
---

You can also build projects from the command line, either via directly invoking the build tools, or by using make tools.

Windows users will find an `Arm DS <version> Command Prompt` in their installation. Linux users can use the supplied `suite_exec` script to set up the path to a compiler. 

To ensure the appropriate compiler is selected, enter:
```console
armclang --version
```

To build the example project above `unzip` the project from the supplied archive:.
```console
unzip <install_dir>/examples/Bare-metal_examples_Armv7.zip "startup_Cortex-M3_AC6/*" .
cd startup_Cortex-M3_AC6
```

Once in the project directory run `make` to build the project:

```console
make
```

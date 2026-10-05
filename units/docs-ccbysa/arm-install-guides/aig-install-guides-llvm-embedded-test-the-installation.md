---
id: "aig-install-guides-llvm-embedded-test-the-installation"
type: "concept"
domain: "project"
title: "Arm Toolchain for Embedded: Test the installation"
summary: "Use the --version option to verify the correct compiler is being invoked:"
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/llvm-embedded.md"
doc_source: "https://learn.arm.com/install-guides/llvm-embedded/#test-the-installation"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Verify the clang installation

Use the `--version` option to verify the correct compiler is being invoked:

```command
clang --version
```

The output is similar to:

```output
clang version 22.1.0
Target: aarch64-unknown-linux-gnu
Thread model: posix
InstalledDir: /home/ubuntu/ATfE-22.1.0-Linux-AArch64/bin
Arm Toolchain ID: E0075 (44010d72)
```

### Build a sample application with clang

Use a text editor to create an example source file named `hello.c` with the following code:

```c
#include <stdio.h>

int main()
{
  printf("hello");
  return 0;
}
```

Several compiler options are needed. For more information, see [Using the toolchain](https://github.com/arm/arm-toolchain/blob/arm-software/embedded/README.md#using-the-toolchain).

To build for Armv6-M, run:

```command
clang --target=armv6m-none-eabi -fno-exceptions -fno-rtti -lcrt0-semihost -lsemihost -T picolibc.ld -o hello_v6m hello.c
```

To build for Armv7-M, run:

```command
clang --target=armv7m-none-eabi -fno-exceptions -fno-rtti -lcrt0-semihost -lsemihost -T picolibc.ld -o hello_v7m hello.c
```

### Run the example applications

The applications can be run on [Fixed Virtual Platforms (FVP)](https://learn.arm.com/install-guides/fm_fvp/fvp/).

**Note:**
There is no FVP release for macOS.


To run the Armv6-M example on a Cortex-M0 FVP:

```command
FVP_MPS2_Cortex-M0 -a hello_v6m
```

To run the Armv7-M example on a Cortex-M3 FVP:

```command
FVP_MPS2_Cortex-M3 -a hello_v7m
```

The output includes the `hello` message along with diagnostic output from the FVP:

```output
telnetterminal1: Listening for serial connection on port 5000
telnetterminal2: Listening for serial connection on port 5002
telnetterminal0: Listening for serial connection on port 5001
hello
Info: /OSCI/SystemC: Simulation stopped by user.
```

You're now ready to use Arm Toolchain for Embedded.

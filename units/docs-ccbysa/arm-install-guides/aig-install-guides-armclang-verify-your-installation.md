---
id: "aig-install-guides-armclang-verify-your-installation"
type: "concept"
domain: "project"
title: "Arm Compiler for Embedded: Verify your installation"
summary: "To verify everything works, compile a Hello World example."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/armclang.md"
doc_source: "https://learn.arm.com/install-guides/armclang/#verify-your-installation"
license: "CC-BY-SA-4.0"
mode: "V"
---

To verify everything works, compile a `Hello World` example.

Use a text editor to copy and paste the folowing code into a file named `hello.c`:

```C
// hello.c
#include <stdio.h>
int main() {
  printf("Hello World\n");
  return 0;
}
```

Compile the code with `armclang`:

```console
armclang --target=aarch64-arm-none-eabi hello.c
```

If the command completes with no errors, the compiler is working.

For more information about the example, see the [Arm Compiler for Embedded User Guide](https://developer.arm.com/documentation/100748/latest/Getting-Started/Compiling-a-Hello-World-example).

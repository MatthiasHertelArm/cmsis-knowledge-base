---
id: "alp-zephyr-vsworkbench-2-development-code-walkthrough-hello-world"
type: "concept"
domain: "rtos"
title: "Build Zephyr projects with Workbench for Zephyr in VS Code: Build a Zephyr application with Workbench for Zephyr: Code walkthrough: hello_world"
summary: "The following code shows a basic Zephyr application that prints a message to the console:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/2_development.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_vsworkbench/2_development/#code-walkthrough-hello-world"
license: "CC-BY-SA-4.0"
mode: "V"
---

The following code shows a basic Zephyr application that prints a message to the console:

```c
#include <zephyr/kernel.h>
#include <zephyr/stdio.h>

int main(void)
{
    printk("Hello World! %s\n", CONFIG_BOARD_TARGET); // Prints board name to serial console
    return 0;
}
```

`CONFIG_BOARD_TARGET` expands to your target board and revision identifier.

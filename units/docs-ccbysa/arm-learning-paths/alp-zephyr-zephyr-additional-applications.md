---
id: "alp-zephyr-zephyr-additional-applications"
type: "concept"
domain: "rtos"
title: "Run the Zephyr RTOS on Arm Corstone-300: Build and run Zephyr applications: Additional applications"
summary: "You can try some of the other sample applications included or build your own."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr/zephyr.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr/zephyr/#additional-applications"
license: "CC-BY-SA-4.0"
mode: "V"
---

You can try some of the other sample applications included or build your own.

To build the [Dining Philosophers](https://docs.zephyrproject.org/latest/samples/philosophers/README.html) example, use:

```console
west build -p auto -b mps3_an547 samples/philosophers
```

Run the new executable at `build/zephyr/zephyr.elf` on the FVP as [above](#runzephyr). The output will be seen in a terminal.

---
id: "alp-zephyr-cs320-mps4-how-to-2-understand-zephyr-board-suppor"
type: "concept"
domain: "rtos"
title: "how to 2: Understand Zephyr board support architecture"
summary: "Zephyr organizes hardware support in the following hierarchy:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_cs320_mps4/how-to-2.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_cs320_mps4/how-to-2/#understand-zephyr-board-support-architecture"
license: "CC-BY-SA-4.0"
mode: "V"
---

Zephyr organizes hardware support in the following hierarchy:

```output
Board → SoC → CPU Cluster → CPU Core → Architecture
```

For Corstone-320 MPS4, this hierarchy maps as follows:

| Level | Value | Description |
|-------|-------|-------------|
| Board | `mps4` | Board name used with `west build -b` |
| SoC | `corstone320` | Corstone-320 subsystem |
| CPU Cluster | `m85` | Cortex-M85 cluster |
| CPU Core | — | Single Cortex-M85 core |
| Architecture | — | ARMv8.1-M with Helium |

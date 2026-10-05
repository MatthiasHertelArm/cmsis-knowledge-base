---
id: "alp-migration-4-development-environmen-cross-platform-build"
type: "concept"
domain: "project"
title: "Development environment: Cross-platform build"
summary: "The cross-platform build using buildx enables you to build an aarch64 container on an x86_64 machine. Once built, the cross-platform built container can be run on that same x86_64 machine using QEMU behind the scenes, quite convenient!"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/migration/4_development_environment.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/migration/4_development_environment/#cross-platform-build"
license: "CC-BY-SA-4.0"
mode: "V"
---

The cross-platform build using `buildx` enables you to build an `aarch64` container on an `x86_64` machine. Once built, the cross-platform built container can be run on that same `x86_64` machine using QEMU behind the scenes, quite convenient!

To build the container, run the following command:

```bash
docker buildx build --platform linux/aarch64 -t sobel_gcc_example .
```

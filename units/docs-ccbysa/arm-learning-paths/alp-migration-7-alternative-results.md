---
id: "alp-migration-7-alternative-results"
type: "concept"
domain: "project"
title: "Migrating x86_64 workloads to aarch64: Evaluating performance on Arm hardware (Optional): Results"
summary: "The output is the same as when running using QEMU. A noticeable difference compared to QEMU is that the SIMD implementation runs faster, which is expected. QEMU should not be used for performance measurement purposes."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/migration/7_alternative.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/migration/7_alternative/#results"
license: "CC-BY-SA-4.0"
mode: "V"
---

The output is the same as when running using QEMU. A noticeable difference compared to QEMU is that the _SIMD_ implementation runs faster, which is expected. QEMU should not be used for performance measurement purposes.

In the results presented below, a value >1 is faster and a value <1 is slower in comparison to the normalized value. In short, higher values are better.

### AWS EC2

| | Graviton2 | | Graviton3 | |
| --- | --- | --- | --- | --- | --- | --- |
| Compiler | GCC 12.2.0 | ACfL 22.1 | GCC 12.2.0 | ACfL 22.1 |
| Non-SIMD | 1.0 | 1.0 | 1.7 | 1.8 |
| SIMD     | 3.4 | 3.8 | 5.8 | 6.7 |
| OpenCV   | 0.3 | 0.3 | 0.4 | 0.5 |

The results in the table above have been normalized to the _Graviton2 Non-SIMD_ value, giving the relative speed-up. 

You observe the following:
* Graviton3 runs the Sobel filter workload faster than Graviton2
* ACfL performs slightly better than GCC for the _SIMD_ implementation of the Sobel filter

### Raspberry Pi 4

| | Raspberry Pi 4 | |
| --- | --- | --- |
| Compiler | GCC 11.3.0 | ACfL 22.1 |
| Non-SIMD | 1.0 | 0.9 |
| SIMD     | 2.7 | 3.0 |
| OpenCV   | 0.3 | 0.3 |  

The results in the table above have been normalized to the _Raspberry Pi 4 Non-SIMD_ value, giving the relative speed-up. 

You observe the following:
* ACfL performs slightly better than GCC for the _SIMD_ implementation of the Sobel filter

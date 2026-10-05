---
id: "armsw-readme-mainpage-omit-from-toc-2-the-platform-and-dependency"
type: "concept"
domain: "optimization"
title: "README {#mainpage} <!-- omit from toc -->: 2 The Platform and Dependency"
summary: "README {#mainpage} <!-- omit from toc -->: 2 The Platform and Dependency"
status: "draft"
collection: "arm-software-readmes"
source: "ARM-software/Arm-2D@3dd16b2:README.md"
doc_source: "https://github.com/ARM-software/Arm-2D/blob/3dd16b2/README.md#2-the-platform-and-dependency"
license: "Apache-2.0"
mode: "V"
---

### 2.1 Processors and Hardware

**The library is targeting ALL Cortex-M processors with/without various hardware 2D image accelerators:**

- Armv6-M processors: Cortex-M0/M0+/M1/SC000
- Armv7-M processors: Cortex-M3/M4/M7/SC300
- Armv8-M processors: Cortex-M23/M33/Star-MC1/M35P
- Armv8.1-M processors: Cortex-M52/M55/M85

**The library is designed with ACI (Arm Custom Instructions) in mind.** Accelerations implemented with user-defined instructions can be integrated into the library easily as software extensions and it is transparent for upper-layer software.

**The library is designed with 2D image accelerators in mind and follows the feature-agnostic principle.**  The support for 2DGPU (or other Accelerators) can be easily added as software extensions and it is transparent for upper-layer software.

**The library is designed with resource constraints in mind.** **For Cortex-M processors with 8K~32K SRAM that cannot afford a complete framebuffer**, Arm-2D introduces a feature called **Generic Partial Framebuffer**, enabling those existing MCUs to run GUI applications in a decent frame rate.

### 2.2 Dependency

- The library depends on **CMSIS 5.7.0 and above** (If you want to use Arm-2D with Cortex-M55, CMSIS 5.8.0 is required).
- The library is developed with the **C11** standard and depends on some **widely adopted GCC extensions**.
  - See **section 3.2** for details.
- The library supports **Arm Compiler 6**, **GCC**, **LLVM** and **IAR**
  - See **section 5** for details.

> [!NOTE]
>
> The supports of Arm Compiler 5 is deprecated.

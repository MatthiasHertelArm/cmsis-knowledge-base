---
id: "armsw-readme-mainpage-omit-from-toc-overview"
type: "concept"
domain: "optimization"
title: "README {#mainpage} <!-- omit from toc -->: Overview"
summary: "Today, for IoT endpoint devices, white goods, handheld devices and wearables, Arm-2d provides comprehensive low-level graphics processing capabilities."
status: "draft"
collection: "arm-software-readmes"
source: "ARM-software/Arm-2D@3dd16b2:README.md"
doc_source: "https://github.com/ARM-software/Arm-2D/blob/3dd16b2/README.md#overview"
license: "Apache-2.0"
mode: "V"
---

**Arm-2D is an open-source project for 2.5D image processing on Cortex processors.** Since its [first experimental release on March 30, 2021](https://github.com/ARM-software/EndpointAI/commit/e8e51c507a97accfb98758fd12fb713e3d366de0), and [the official v1.1.0 release on December 7, 2022](https://github.com/ARM-software/Arm-2D/releases/tag/v1.1.0), Arm-2D has experienced a period of rapid and exciting development. Through active community engagement and extensive real-world validation across numerous open-source and commercial projects, the library has evolved into a robust and mature solution.

Today, for IoT endpoint devices, white goods, handheld devices and wearables, Arm-2d provides comprehensive low-level graphics processing capabilities.  Especially for resource-constrained, low-power platforms, it is one of the optimal choices for building sophisticated modernised GUI applications, delivering exceptional performance without compromising functionality.

**Arm-2D consists of:**

- Generic software **pixel pipeline** infrastructure for graphic processing
  - A set of rules for adding new algorithms and colour formats
  - A default software implementation and **SIMD acceleration** when [Helium technology](https://developer.arm.com/architectures/instruction-sets/simd-isas/helium) is available.
  - Supports adding **3rd party hardware accelerators** at the low level in a "feature-agnostic" manner.
- A **CMSIS-Pack** for ease of use
- Examples and Documents

 

**Position in Ecosystem:**

- **Focuses on low-level** and works as **a hardware abstraction layer** for 2.5D image processing.
- **Arm-2D is NOT designed as a GUI.**
  - No content creation, complex shape drawing or Scalable Vector Graphics (SVG) support
- **Arm-2D is used as a facto GUI in the community**
  - Given its high performance, low memory footprint nature and rich toolbox, it is used as an optimal (and sometimes the only) solution for resource-constrained platforms, 
  - **With the same performance and efficiency as the built-in APIs**, Arm-2D enables customers to add their own shape-drawing algorithms and load customised image formats easily using a generic loader (or its derived classes).
  
- **Provide conveniences for Arm eco-partners to create value through differentiation.**
  - Provide default implementations of commonly used 2.5D operations and enable 3rd parties to accelerate application-specific algorithms.

**Focus and Objectives:**

- **Help industry partners with technology adoption**
  - Guidance for the integration of Arm-2D into graphic stacks
- **Optimisation for ultra-small memory footprint**
  - Enable Deep Embedded microcontrollers to use modernised GUIs.
  - Helping customers to cost down

---
id: "armsw-readme-mainpage-omit-from-toc-1-introduction"
type: "concept"
domain: "optimization"
title: "README {#mainpage} <!-- omit from toc -->: 1 Introduction"
summary: "With the increasing introduction of smart IoT edge devices into our daily lives, users accustomed to smartphone-like graphical user interfaces (GUIs) now expect a similar modernized experience, even when using microcontroller-based products."
status: "draft"
collection: "arm-software-readmes"
source: "ARM-software/Arm-2D@3dd16b2:README.md"
doc_source: "https://github.com/ARM-software/Arm-2D/blob/3dd16b2/README.md#1-introduction"
license: "Apache-2.0"
mode: "V"
---

### 1.1 The Background

With the increasing introduction of smart IoT edge devices into our daily lives, users accustomed to smartphone-like graphical user interfaces (GUIs) now expect a similar modernized experience, even when using microcontroller-based products. This trend has been long recognized and understood by Arm's ecosystem partners.

Consequently, many silicon vendors have integrated dedicated hardware accelerators into their microcontroller products to improve the 2D image processing. At the same time, GUI service providers have updated their product lines to cater to microcontroller-based GUI applications. Many open-source embedded GUI stacks, such as [LVGL](https://lvgl.io/), are gaining popularity on GitHub.

In reality, using GUIs with microcontrollers is not a new concept. However, with the recent rise of IoT and AI, the limitations of simple and monotonous GUIs have become more apparent and less tolerable. Pursuing a user experience comparable to a smartphone has become a fundamental requirement for many products.

Interestingly, seemingly complex GUIs are often created using simple techniques like 2D image copying and tiling. Even translucent effects are achievable on microcontrollers running at tens or hundreds of MHz.

Technologies for 2D graphics have been mature since the era of 8-bit gaming consoles. If an 8-bit 6502 processor could produce impressive graphics effects, there is no reason why the most advanced Cortex-M processors today cannot achieve even more.

### 1.2 The Problems in Current Solutions

As shown in **Figure 1-2**, Linux based systems have a complete ecosystem that provides GPU drivers and GUI software services. In contrast, resource-constrained embedded systems do not have such luxury. To enhance the MCU ecosystem, Arm-2D is introduced.

**Figure 1-2 Ecosystem Comparison between Rich Embedded and Constraint Embedded System in GUI**

(figure:  Ecosystem Comparison)

When we look at the traditionally embedded  GUI architecture(as shown in **Figure 1-3** ), there are four layers: 1) the application and designer layer, 2) the GUI software service layer, 3) the rendering layer, and 3) the hardware driver layer.

**Arm-2D focuses on accelerating the low-level 2D image processing**, and will not touch upper layers of the GUI software stacks, hence avoiding competing with GUI service providers in the same ecosystem. In fact, because Arm has proposed an abstraction layer for the low-level 2D image processing, **a whole ecological level of cooperation can be quickly established** between chip manufacturers that provide hardware accelerators and software providers that provide GUI services. **Everyone can concentrate on enlarging their own values**. For example, by adding arm-2d adaptor drivers for their proprietary 2D accelerators, silicon vendors can achieve a wide range of support from GUI providers who build/port their GUI stack upon Arm-2D APIs.

**Figure 1-3 The Hierarchy of a Typical Embedded GUI System.**

(figure: The Hierarchy of a Typical Embedded GUI System)

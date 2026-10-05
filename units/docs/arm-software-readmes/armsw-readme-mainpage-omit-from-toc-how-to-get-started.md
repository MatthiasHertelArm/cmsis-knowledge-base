---
id: "armsw-readme-mainpage-omit-from-toc-how-to-get-started"
type: "concept"
domain: "optimization"
title: "README {#mainpage} <!-- omit from toc -->: How to Get Started"
summary: "Potential users of Arm-2D may have different backgrounds and purposes. Whoever you are, e.g."
status: "draft"
collection: "arm-software-readmes"
source: "ARM-software/Arm-2D@3dd16b2:README.md"
doc_source: "https://github.com/ARM-software/Arm-2D/blob/3dd16b2/README.md#how-to-get-started"
license: "Apache-2.0"
mode: "V"
---

Potential users of Arm-2D may have different backgrounds and purposes. Whoever you are,  e.g. an application engineer from a silicon vendor who develops drivers, a GUI stack system engineer, or an application developer, based on the purposes , there are two ways to get started with Arm-2D:

- [Getting Started as a GUI Application Designer](https://github.com/ARM-software/Arm-2D/blob/3dd16b2/./documentation/getting_started_as_an_application_designer.md)
  - In some resource-constrained systems, Flash (ROM) and SRAM are limited (e.g., 64K Flash, 8K SRAM), or the memory reserved for GUI applications is limited; such systems cannot afford the cost of a decent GUI stack.
    Meanwhile, these kinds of low-cost systems usually don't have a complex HMI; it is possible to use the arm-2d APIs to design applications directly.
  - Embedded video processing can preprocess the frame buffer captured from cameras using Arm-2D. 
- [Getting Started as a GUI System Developer](https://github.com/ARM-software/Arm-2D/blob/3dd16b2/./documentation/getting_started_as_a_gui_stack_developer.md)
    - Silicon vendors can provide drivers to further accelerate Arm-2D, enabling their customers to take advantage of the proprietary hardware accelerators. 
    - GUI Stack System engineers can use the Arm-2D APIs to accelerate the low-level operations. 
    - Homebrew GUI designers can create entirely new GUI stacks faster and easier with Arm-2D.
    - ...

We are optimistic that anyone can find something interesting in Arm-2D.

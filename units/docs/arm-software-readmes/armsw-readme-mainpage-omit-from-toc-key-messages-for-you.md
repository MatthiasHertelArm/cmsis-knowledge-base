---
id: "armsw-readme-mainpage-omit-from-toc-key-messages-for-you"
type: "concept"
domain: "optimization"
title: "README {#mainpage} <!-- omit from toc -->: Key Messages for You"
summary: "README {#mainpage} <!-- omit from toc -->: Key Messages for You"
status: "draft"
collection: "arm-software-readmes"
source: "ARM-software/Arm-2D@3dd16b2:README.md"
doc_source: "https://github.com/ARM-software/Arm-2D/blob/3dd16b2/README.md#key-messages-for-you"
license: "Apache-2.0"
mode: "V"
---

- **Arm-2D always keeps light-weight**
  - Arm-2D maintains an ultra-low memory footprint for both ROM and RAM.
  - Arm-2D uses standard linker features to remove unused functions and data whenever possible.
    - Only functions that are actually used will take up memory.
- **Arm-2D always maintains a flat, straightforward framework: API Wrappers, Frontend, and Backend.**
  - API wrappers take user input and generate task descriptors for the following stages.
  - The frontend is responsible for the commonly used and necessary services.
    - The Frontend validates user tasks, then breaks them down into **simplified backend tasks that are friendly to hardware accelerators.** 
    - The Frontend maintains a low memory footprint.
  - The Backend is the place for low-level implementations of specific 2D processing algorithms.
    - **The linker will remove unused low-level implementations.**



- **Arm-2D always keeps backward compatibility**
  - Older APIs will still be usable in newer versions (even if they are marked as deprecated)
  - Arm-2D available for ALL Cortex-M processors

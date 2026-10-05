---
id: "alp-context-switch-cortex-m-example-overview-of-the-example-code"
type: "concept"
domain: "rtos"
title: "Learn about context switching on Arm Cortex-M processors: Example Arm DS project to demonstrate context switching operations: Overview of the example code"
summary: "With this example you can create a very simple RTOS (Real Time Operating System) capable of dealing with context switching and thread isolation. For simplicity, only two threads, thread A and thread B, are created."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/context-switch-cortex-m/example.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/context-switch-cortex-m/example/#overview-of-the-example-code"
license: "CC-BY-SA-4.0"
mode: "V"
---

With this example you can create a very simple RTOS (Real Time Operating System) capable of dealing with context switching and thread isolation. For simplicity, only two threads, thread A and thread B, are created.

Basic context switching and thread isolation requirements considered for this example are listed below:
  - Two isolated threads called thread A and thread B are created
  - Both thread A and thread B are executed in unprivileged mode.
  - Each thread has its own dedicated process stack.
  - The MPU regions are set up in a way such that the data and code corresponding to Thread A is not accessible to Thread B and vice versa.
  - A System Tick Timer (SysTick) generates regular SysTick exception as an interruption to switch between threads.
  - The SysTick handler acts as real-time kernel code and is responsible for context switching. The Systick handler is also responsible for MPU reprogramming which is needed for thread isolation.
  - The MPU regions for SysTick handler are set up in a way so that both threads cannot access the memory used by kernel code (i.e.) SysTick handler.
More details about the algorithm and structure used in this example can be found in [Chapter: Use-Case-Examples of Armv8-M Memory Model and MPU User Guide](https://developer.arm.com/documentation/107565/0101/Use-case-examples/rtos-context-switch).

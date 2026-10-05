---
id: "avh-development-workflow"
type: "concept"
domain: "test"
title: "Development Workflow"
summary: "Using Arm FVP models enables a flexible approach that combines desktop and cloud-native development tools thus simplifying and accelerating the development of embedded software."
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:DoxyGen/overview/src/workflow.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/overview/src/workflow.md"
license: "Apache-2.0"
mode: "V"
---

Using Arm FVP models enables a flexible approach that combines desktop and cloud-native development tools thus
simplifying and accelerating the development of embedded software.

# Continuous Integration (CI)

New functionality can be quickly developed on a simulation model with frequent changes being automatically verified
upon the code commits to a cloud based version control system such as GitHub which executes a complete CI/CD
integration flow. Figure below illustrates the concept.

(figure: Continuous Integration (CI) workflow) workflow")

1. **Local development** is done by engineers on local machines using common embedded tools such as Keil MDK with Arm
   FVP models used for simulation. See [FVPs on Desktop](https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/overview/src/../../infrastructure/html/avh_desktop.html) for details. The
   software can also be already prepared for real hardware as explained in Physical_Hardware.
2. A **code repository** is used as a source code management system for synchronization, storage and version control.
3. **CI pipeline** implements the continuous integration flow (for example GitHub Actions) that gets triggered on every
   code update in the target repository.
4. **CI execution** includes automated program build and testing and is performed in the cloud with results being
   reported back to the repository and user. See [Infrastructure](https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/overview/src/../../infrastructure/html/index.html) for details.
5. **Failure analysis and local debug**: developers can observe the CI test results and in case of any failures also
   use a local setup to reproduce and debug the issues.

Learn more about benefits from CI workflow at CI_Benefits.

# Migration to Physical Hardware

[Modular programming](https://en.wikipedia.org/wiki/Modular_programming) recommends to separate the functionality of a
program into independent, interchangeable modules that use defined interfaces that abstract the hardware functionality.

This **"software-first"** design concept simplifies code re-use and allows to implement "Virtual Drivers" and
"Hardware Drivers" that expose the same API and implement the same logical behavior. If built correctly, it overcomes
many issues that are typically found in monolithic software and enables a staged
[software validation](https://en.wikipedia.org/wiki/Software_testing) with multiple test levels such as unit,
integration, and system testing.

To simplify re-targeting from Arm FVP simulation models to final production hardware, the examples implement the
concept of [software layers](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#software-layers). This
makes it easy to work on a combination of simulated and physical hardware. The picture below exemplifies this concept.

(figure: AVH Re-target to Hardware)

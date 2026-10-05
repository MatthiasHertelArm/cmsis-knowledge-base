---
id: "spec-recommended-terminology-system-description-terminology"
type: "concept"
domain: "pack"
title: "Recommended terminology: System description terminology"
summary: "This section describes concepts required for describing system on chip (SoC) products, leveraging TrustZone-enabled cores and multi-cores. These concepts can also be used more widely to describe multi-SoC systems."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doc/Glossary.md"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/Glossary.html"
license: "Apache-2.0"
mode: "V"
---

This section describes concepts required for describing system on chip (SoC) products, leveraging TrustZone-enabled cores and multi-cores.  
These concepts can also be used more widely to describe multi-SoC systems.  

- **Binary program**
A binary program can be:
  - A bare-metal binary,
  - A monolithic OS binary and all the services running on top of it,
  - An OS that can install modules. Each module can be a binary on its own but still from an execution perspective as the OS is required for this service to run we consider it as a single binary in term of execution context. 
  - A virtual machine or interpreter 
- **Execution Context**
An execution context identifies the “cradle” allowing to run a binary program on a given hardware platform.  
  - A context of execution has a 1-to-1 association to a hardware execution unit. 
  - If we support virtual machines or interpreters, then the virtual machine is associated with one execution context. The programs interpreted by the virtual machine (VM) are stored as data sections in memory, and considered as execution modules within the VM's execution context.
- **Execution Domain**
An execution domain is a container aggregating all the platform resources (internal and external memories, peripherals) that an execution context can use “exclusively”. For shared resources (available for several execution contexts), we introduce the concept of shared execution domain.
- **Execution Module**
An execution module is an entity that has no standalone execution possibility. It relies on a “backbone" binary providing system services. So, an execution module is always associated with an execution context.
- **Hardware Execution Unit**
A hardware execution unit is either a cluster (i.e. group of cores), or a core, or a TrustZone world within a core (virtualization). This is the hardware entity (virtual or physical) running a binary program.  
- **System On Chip**
A SoC (system on chip) can be a microcontroller (MCU) or a microprocessor (MP). 
  - A SoC can have one or several processors.  
  - A processor can have one or several cores (core = CPU+FPU+…). For example, a Cortex-A7 cluster can have two Cortex-A7 cores.

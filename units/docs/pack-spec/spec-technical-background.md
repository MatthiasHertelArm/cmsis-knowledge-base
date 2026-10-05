---
id: "spec-technical-background"
type: "concept"
domain: "pack"
title: "Technical background"
summary: "The CMSIS-Pack format is used to deliver a software package and is aimed to be scalable for future requirements. It provides a management process and supports a tool independent distribution for:"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_creation.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/cp_Packs.html"
license: "Apache-2.0"
mode: "V"
---

The **CMSIS-Pack** format is used to deliver a software package and is aimed to be scalable for future requirements.
It provides a management process and supports a tool independent distribution for:

 - Device support for tool chains and software applications to target a specific device:
   - Information about the processor and it's features.
   - C and assembly files for the device startup and access to the memory mapped peripheral registers.
   - Parameters, technical information, and data sheets about the device family and the specific devices.
   - Device description and available peripherals.
   - Memory layout of internal and external RAM and ROM address ranges.
   - Flash algorithms for programming the device.
   - Debug and trace configurations as well as System View Description files for device specific display of the memory mapped
     peripheral registers.

 - Board support for rapid development in the prototyping stage:
   - Information about the development board and it's features.
   - Parameters, technical information, and data sheets about the board, the mounted microcontroller and peripheral devices.
   - Drivers for on-board peripheral devices

 - Software components simplify the re-use of software and the management of third-party software. They contain:
   - A collection of source modules, header and configuration files as well as libraries.
   - Documentation of the software, including features and APIs.
  
 - Application Programming Interfaces specify one or more APIs for software components
   that are part of another software pack.

 - pdsc_examples_pg can be used as a reference and starting point for similar applications. They contain:
  - Fully defined application projects that work out of the box in the specified build and debug environments.
  - Documentation about the purpose of the example, how to build, configure and execute the application.
  
 - Code templates help to understand the basic concepts of a software component better and to give the user a
   good starting point for implementing his application.

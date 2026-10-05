---
id: "alp-bare-metal-hello-run-the-image-on-the-fvp"
type: "concept"
domain: "project"
title: "Create an Armv8-A embedded application: Create and build a Hello World example project: Run the image on the FVP"
summary: "You can now run the executable image hello.axf from the command line using the Fixed Virtual Platform (FVP)."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/bare-metal/hello.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/bare-metal/hello/#run-the-image-on-the-fvp"
license: "CC-BY-SA-4.0"
mode: "V"
---

You can now run the executable image `hello.axf` from the command line using the Fixed Virtual Platform (FVP).
```console
FVP_Base_AEMvA -a hello.axf
```
The code starts at the default entry point, ` __main()` in the Arm libraries. These libraries perform a number of setup activities, including:

- Copying all the code and data from the image into memory.
- Setting up an area of memory for the application stack and heap.
- Branching to the main() function to run the application.

The code executes on the FVP, and the message "Hello World!" appears on screen 4 times, as the same code is executed on each of the 4 processors in the model.
```output
Hello World!
Hello World!
Hello World!
Hello World!
```

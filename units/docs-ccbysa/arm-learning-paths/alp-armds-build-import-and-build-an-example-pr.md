---
id: "alp-armds-build-import-and-build-an-example-pr"
type: "concept"
domain: "project"
title: "Get started with Arm Development Studio: Import and build example project: Import and build an example project"
summary: "Development Studio provides a number of useful example projects to help you get started."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/armds/build.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/armds/build/#import-and-build-an-example-project"
license: "CC-BY-SA-4.0"
mode: "V"
---

Development Studio provides a number of useful example projects to help you get started. 

To import a project:

1. Click `File > Import... > Arm Development Studio > Examples & Programming Libraries` and click `Next`.

2. Expand `Examples` and expand the example types to see the available examples.

For example, expand `Armv7 Bare-Metal` and select `startup_Cortex-M3_AC6` with a check mark and click `Finish` to import the project into your workspace.

**Filter:**
Enter `m3` (or similar) in the text box at top of pane to easily locate the example project.


The imported project is now in your workspace, and can be seen in the `Project Explorer` pane.

Expand the project view to see the various source files. Click on any source to view (and edit). A detailed `readme` is provided for each project highlighting key learnings of the selected project. 

Most projects include a `.scat` file. This is a [Scatter loading](https://developer.arm.com/documentation/101754/latest/armlink-Reference/Scatter-loading-Features/The-scatter-loading-mechanism/Overview-of-scatter-loading) description file, which defines the target memory map to the linker.

3. Build the project by clicking the `hammer` icon.

The build output is shown in the `Console` pane.

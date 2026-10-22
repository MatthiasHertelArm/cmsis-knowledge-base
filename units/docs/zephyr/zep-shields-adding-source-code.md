---
id: "zep-shields-adding-source-code"
type: "concept"
domain: "bring-up"
title: "Shields: Adding Source Code"
summary: "It is possible to add source code to shields, as a way to meet configuration requirements that are specific to the shield (e.g: initialization routines, timing constraints, etc), in order to enable it for proper operation with the …"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/porting/shields.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/porting/shields.rst"
license: "Apache-2.0"
mode: "V"
---

It is possible to add source code to shields, as a way to meet configuration
requirements that are specific to the shield (e.g: initialization routines,
timing constraints, etc), in order to enable it for proper operation with the
different Zephyr components.


**Note:** Source code in shields shall not be used for purposes other than the one described above. Generic functionalities that could be reused among shields (and/or targets) shall not be captured here.

To effectively incorporate source code: add a `CMakeLists.txt` file, as
well as the corresponding source files (referenced in CMake similar to other
areas of Zephyr, e.g: boards).

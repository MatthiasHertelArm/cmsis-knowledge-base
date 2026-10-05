---
id: "zep-tf-m-build-system-footprint-and-memory-usage"
type: "concept"
domain: "security"
title: "TF-M Build System: Footprint and Memory Usage"
summary: "The build system offers targets to view and analyse RAM and ROM usage in generated images. The tools run on the final images and give information about size of symbols and code being used in both RAM and ROM."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/tfm/build.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/tfm/build.rst"
license: "Apache-2.0"
mode: "V"
---

The build system offers targets to view and analyse RAM and ROM usage in generated images.
The tools run on the final images and give information about size of symbols and code being used in both RAM and ROM.
For more information on these tools look here: footprint_tools

Use the `tfm_ram_report` to get the RAM report for TF-M secure firmware (tfm_s).

Use the `tfm_rom_report` to get the ROM report for TF-M secure firmware (tfm_s).

Use the `bl2_ram_report` to get the RAM report for TF-M MCUboot, if enabled.

Use the `bl2_rom_report` to get the ROM report for TF-M MCUboot, if enabled.

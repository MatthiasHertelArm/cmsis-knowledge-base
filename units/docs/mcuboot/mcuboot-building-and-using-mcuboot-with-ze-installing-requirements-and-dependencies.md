---
id: "mcuboot-building-and-using-mcuboot-with-ze-installing-requirements-and-dependencies"
type: "concept"
domain: "boot-update"
title: "Building and using MCUboot with Zephyr: Installing requirements and dependencies"
summary: "MCUboot is included as part of Zephyr. Follow the getting started guide for the version of Zephyr you wish to use to get Zephyr itself, including MCUboot. Install additional packages required for development with MCUboot:"
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/readme-zephyr.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/readme-zephyr.md#installing-requirements-and-dependencies"
license: "Apache-2.0"
mode: "V"
---

MCUboot is included as part of Zephyr. Follow the getting started guide for the
version of Zephyr you wish to use to get Zephyr itself, including MCUboot.
Install additional packages required for development with MCUboot:

```
  cd ~/zephyrproject-rtos/bootloader/mcuboot  # or to your directory where MCUboot is
  pip3 install --user -r scripts/requirements.txt
```

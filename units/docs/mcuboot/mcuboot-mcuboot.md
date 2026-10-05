---
id: "mcuboot-mcuboot"
type: "concept"
domain: "boot-update"
title: "MCUboot"
summary: "[(figure: Package on PyPI)][pypi] [(figure: Coverity Scan Build Status)][coverity] [(figure: Build Status (Sim))][sim] [(figure: Build Status (Mynewt))][mynewt] [(figure: Build Status (Espressif))][espressif] [(figure: Publishing Status (imgtool))][imgtool] [(figure: Build Status (Travis CI))][travis] [(figure: Apache 2.0)][license]"
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:README.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/README.md"
license: "Apache-2.0"
mode: "V"
---

[(figure: Package on PyPI)][pypi]
[(figure: Coverity Scan Build Status)][coverity]
[(figure: Build Status (Sim))][sim]
[(figure: Build Status (Mynewt))][mynewt]
[(figure: Build Status (Espressif))][espressif]
[(figure: Publishing Status (imgtool))][imgtool]
[(figure: Build Status (Travis CI))][travis]
[(figure: Apache 2.0)][license]

[pypi]: https://pypi.org/project/imgtool/
[coverity]: https://scan.coverity.com/projects/mcuboot
[sim]: https://github.com/mcu-tools/mcuboot/actions?query=workflow:Sim
[mynewt]: https://github.com/mcu-tools/mcuboot/actions?query=workflow:Mynewt
[espressif]: https://github.com/mcu-tools/mcuboot/actions?query=workflow:Espressif
[imgtool]: https://github.com/mcu-tools/mcuboot/actions?query=workflow:imgtool
[travis]: https://travis-ci.org/mcu-tools/mcuboot
[license]: https://github.com/mcu-tools/mcuboot/blob/main/LICENSE

This is MCUboot version 2.5.0-rc1

MCUboot is a secure bootloader for 32-bits microcontrollers. It defines a
common infrastructure for the bootloader and the system flash layout on
microcontroller systems, and provides a secure bootloader that enables easy
software upgrade.

MCUboot is not dependent on any specific operating system and hardware and
relies on hardware porting layers from the operating system it works with.
Currently, MCUboot works with the following operating systems and SoCs:
- [Zephyr](https://www.zephyrproject.org/)
- [Apache Mynewt](https://mynewt.apache.org/)
- [Apache NuttX](https://nuttx.apache.org/)
- [RIOT](https://www.riot-os.org/)
- [Mbed OS](https://os.mbed.com/)
- [Espressif](https://www.espressif.com/)
- [Cypress/Infineon](https://www.cypress.com/)

RIOT is supported only as a boot target. We will accept any new
port contributed by the community once it is good enough.

---
id: "tfm-the-kconfig-system"
type: "concept"
domain: "security"
title: "The Kconfig System"
summary: "The Kconfig system is an alternative tool to the CMake config system for users to change config options of TF-M."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/configuration/kconfig_system.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/configuration/kconfig_system.html"
license: "BSD-3-Clause"
mode: "V"
---

The Kconfig system is an alternative tool to the CMake config system for users to change config
options of TF-M.

It handles dependencies and validations automatically when you change configurations so that the
generated configuration options are always valid.

To use the Kconfig system, enable `USE_KCONFIG_TOOL` in command line.
And enable `MENUCONFIG` to launch configuration GUI.

The Kconfig system consists of The Kconfig tool and the The Kconfig files.

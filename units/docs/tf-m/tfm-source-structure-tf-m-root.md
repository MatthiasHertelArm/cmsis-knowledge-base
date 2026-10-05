---
id: "tfm-source-structure-tf-m-root"
type: "concept"
domain: "security"
title: "Source Structure: / (TF-M root)"
summary: "This table describes the structure under the root folder with part of possible folders."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/source_structure/source_structure.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/source_structure/source_structure.html#tf-m-root"
license: "BSD-3-Clause"
mode: "V"
---

This table describes the structure under the root folder with part of
possible folders.

========================= ====================================
Folder name               Description
========================= ====================================
bl1                       The 1st stage immutable bootloader
bl2                       MCUBoot based 2nd stage bootloader
cmake                     Cmake files of the build system
config                    Configuration system files
docs                      The documentation
interface                 RoT service API for client calls
lib                       The 3rd party libraries
platform               Platform intermedia files
secure_fw              The secure firmware
tools                     Tools in scripts for building
========================= ====================================

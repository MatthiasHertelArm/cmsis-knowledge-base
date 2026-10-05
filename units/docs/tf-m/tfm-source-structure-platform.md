---
id: "tfm-source-structure-platform"
type: "concept"
domain: "security"
title: "Source Structure: platform"
summary: "The platform folder contains SW ports of all :ref:supported platforms <supported_platforms> and the files necessary for :ref:adding a new platform <adding_platform>. Please refer to :ref:platform folder document <platform_folder> for more information."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/source_structure/source_structure.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/source_structure/source_structure.html#platform"
license: "BSD-3-Clause"
mode: "V"
---

The `platform` folder contains SW ports of all :ref:`supported platforms
<supported_platforms>` and the files necessary for :ref:`adding a new platform
<adding_platform>`. Please refer to :ref:`platform folder document
<platform_folder>` for more information.

========================= =============================================
Folder name               Description
========================= =============================================
include                   HAL and platform public headers
ext                       Platform ports and related files
========================= =============================================


### platform/ext

This folder can include imported files licensed differently from TF-M's
BSD-3 license. More details are in the dedicated document platform_ext_folder.

========================= =============================================
Folder name               Description
========================= =============================================
accelerator               Supported Crypto HW accelerators
cmsis                     A copy of essential CMSIS headers
common                    Common HAL implementation
driver                    Driver headers for porting
target/<vendor>           Vendor specific folders with ported platforms
========================= =============================================

Each `vendor` is assigned one folder for usage under `target/`.
A `vendor` contributes platform's ports and manages the structure inside it.

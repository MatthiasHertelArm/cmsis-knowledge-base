---
id: "tfm-trusted-firmware-m-profile-medium-overview"
type: "concept"
domain: "security"
title: "Trusted Firmware-M Profile Medium Design: Implementation / Overview"
summary: "The basic idea is to add dedicated profile CMake configuration files under folder config/profile for TF-M Profile Medium default configuration, the same as Profile Small does."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/configuration/profiles/tfm_profile_medium.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/configuration/profiles/tfm_profile_medium.html#overview"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Implementation_

The basic idea is to add dedicated profile CMake configuration files under
folder `config/profile` for TF-M Profile Medium default configuration, the
same as Profile Small does.

The top-level Profile Medium config file collects all the necessary
configuration flags and set them to default values, to explicitly enable the
features required in Profile Medium and disable the unnecessary ones, during
TF-M build.

A platform/use case can provide a configuration extension file to overwrite
Profile Medium default setting and append other configurations.
This configuration extension file can be added via parameter
`TFM_EXTRA_CONFIG_PATH` in build command line.

The behaviour of the Profile Medium build flow (particularly the order of
configuration loading and overriding) can be found at
tfm_cmake_configuration

The details of configurations will be covered in each module in
Implementation details.

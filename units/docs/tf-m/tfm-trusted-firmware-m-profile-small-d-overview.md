---
id: "tfm-trusted-firmware-m-profile-small-d-overview"
type: "concept"
domain: "security"
title: "Trusted Firmware-M Profile Small Design: Implementation / Overview"
summary: "The basic idea is to add dedicated profile CMake configuration files under folder config/profile for TF-M Profile Small default configuration."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/configuration/profiles/tfm_profile_small.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/configuration/profiles/tfm_profile_small.html#overview"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Implementation_

The basic idea is to add dedicated profile CMake configuration files under
folder `config/profile` for TF-M Profile Small default configuration.

The top-level Profile Small config file collects all the necessary
configuration flags and set them to default values, to explicitly enable the
features required in Profile Small and disable the unnecessary ones, during
TF-M build.

A platform/use case can provide a configuration extension file to overwrite
Profile Small default setting and append other configurations.
This configuration extension file can be added via parameter
`TFM_EXTRA_CONFIG_PATH` in build command line.

The behavior of the Profile Small build flow (particularly the order of
configuration loading and overriding) can be found at
tfm_cmake_configuration

The details of configurations will be covered in each module in
Implementation details.

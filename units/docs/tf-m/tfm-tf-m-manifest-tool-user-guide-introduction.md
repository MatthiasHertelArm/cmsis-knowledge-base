---
id: "tfm-tf-m-manifest-tool-user-guide-introduction"
type: "concept"
domain: "security"
title: "TF-M Manifest Tool User Guide: Introduction"
summary: "The TF-M manifest tool is a python script which is used to parse Secure Partition manifests and generate source header files defined by FF-M [1] such as psa_manifest/pid.h and psa_manifest/sid.h. It also generates TF-M specific files for building."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/services/tfm_manifest_tool_user_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_manifest_tool_user_guide.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

The TF-M manifest tool is a python script which is used to parse Secure
Partition manifests and generate source header files defined by FF-M [1]_ such
as `psa_manifest/pid.h` and `psa_manifest/sid.h`.
It also generates TF-M specific files for building.

In the TF-M build system, the manifest tool is invoked during building
automatically. Arguments are passed through CMake variables and they are
customizable.
See Usage in TF-M Build System for more details.

It can be also used as a standalone tool.

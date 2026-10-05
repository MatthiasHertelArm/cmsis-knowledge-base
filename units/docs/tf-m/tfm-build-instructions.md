---
id: "tfm-build-instructions"
type: "concept"
domain: "security"
title: "Build instructions"
summary: "As you know from the introduction TF-M implements SPE with a set of secure services. TF-M application as NSPE client uses those services through isolation boundary via PSA-FF-M API. Both SPE and NSPE are separate binaries and built independently."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/building/tfm_build_instruction.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/building/tfm_build_instruction.html"
license: "BSD-3-Clause"
mode: "V"
---

**Warning:** The build process was changed a lot in Q3 2023 and included into the release v2.0. For building instructions for early versions please refer to the documentation of respective versions.

As you know from the introduction TF-M implements
`SPE` with a set of secure services.
TF-M application as `NSPE` client uses those services through isolation boundary via
`PSA-FF-M` API.
Both SPE and NSPE are separate binaries and built independently.
SPE and NSPE binaries are combined and signed making the final image for downloading onto targets
when building NSPE.

This document describes the process of building a single SPE alone.
Refer to Building Tests on how to build TF-M
regression tests and PSA Arch tests to verify TF-M.
TF-M uses [CMake](https://cmake.org/overview/) **v3.21** or higher.
Before starting please make sure you have all required software installed and
configured as explained in the
TF-M getting started.

The additional building materials you can find in the following links:TF-M source folder

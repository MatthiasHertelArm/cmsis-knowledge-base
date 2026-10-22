---
id: "tfm-first-things-first-build-and-run-instructions"
type: "concept"
domain: "security"
title: "First Things First: Build and run instructions"
summary: "Trusted Firmware M source code is available on git.trustedfirmware.org."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/getting_started/tfm_getting_started.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/getting_started/tfm_getting_started.html#build-and-run-instructions"
license: "BSD-3-Clause"
mode: "V"
---

Trusted Firmware M source code is available on
[git.trustedfirmware.org](https://git.trustedfirmware.org/TF-M/trusted-firmware-m.git/).

To build & run TF-M:

    - Follow the this guide to set up and check your environment.
    - Follow the
      Build instructions
      to compile and build the TF-M source.
    - Follow the Run TF-M examples on Arm platforms
      for information on running the example.

To port TF-M to a another system or OS, follow the
OS Integration Guide

Contributing Process contains guidance on how to
contribute to this project.


# Set up build environments


TF-M officially supports a limited set of build environments and setups. In
this context, official support means that the environments listed below
are actively used by team members and active developers, hence users should
be able to recreate the same configurations by following the instructions
described below. In case of problems, the TF-M team provides support
only for these environments, but building in other environments can still be
possible.

The following environments are supported:


# Install python dependencies


Clone the TF-M source code, and then install the TF-M's additional Python
dependencies.


# Install a toolchain


To compile TF-M code, at least one of the supported compiler toolchains have to
be available in the build environment. The currently supported compiler
versions are:

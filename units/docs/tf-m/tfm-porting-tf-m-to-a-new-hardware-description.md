---
id: "tfm-porting-tf-m-to-a-new-hardware-description"
type: "concept"
domain: "security"
title: "Porting TF-M to a New Hardware: Platform Folder / Description"
summary: "Depending on the level of integration you want with TF-M some files or information will be mandatory for the build system to build working firmware."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/platform/porting_tfm_to_a_new_hardware.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/platform/porting_tfm_to_a_new_hardware.html#description"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Platform Folder_

Depending on the level of integration you want with TF-M some files or
information will be mandatory for the build system to build working firmware.

Please note that platform folder provides source for building both `SPE`
and `NSPE` parts. The SPE builds directly from the source tree while files
necessary for NSPE platform support are installed to `<Artifact folder>`
for building TF-M application as described in the
Build instructions.

Questions to be answered:
    - Will the platform use MCUboot as the second stage bootloader?

      BL2/MCUboot provides a secure bootloader that enables simple software
      upgrades.

      This optional second stage bootloader is set-up via the bl2 target in
      the CMakelists.txt file (see below).

    - Will the platform support the Non-Secure world application?

      A platform can be designed to only support the secure world, in which
      case we would refer to it as a secure enclave. TF-M build system allows
      the developer to strip all Non-Secure world related code out of the
      final image. Most platforms, and especially the ones intended to be
      generic or to have a Non-Secure application will require Non-Secure world
      support. In that case a platform shall instruct build system on the file
      set for exporting to Non-Secure world.

    - How does the non-secure world communicate with the secure world?

      TF-M supports running the non-secure world on the same CPU as the secure
      world, communicating via TrustZone or running the non-secure world on
      a separate CPU, communicating via a mailbox. The platform is responsible
      for configuring toolchains with correct CPU and architecture related
      features for secure and non-secure worlds.

      The architecture for secure world is configured in the cpuarch.cmake
      file (see below).

    - How does the FLASH need to be split between worlds?

      The flash split is very dependent on the support of BL2 and NS world.
      When porting a new platform, one shall arrange enough flash size for each
      of them.

      If supporting upgrades (via MCUboot), additional flash area will be
      required to store the updates before upgrading the whole system.

    - How does the RAM need to be split between worlds?

      The RAM split is very dependent on the support of the NS world.

      If you're not porting the platform for a specific project but are enabling
      the Non-Secure world, you should ensure that you leave enough RAM
      available for it to run.


TF-M S world size in RAM and Flash varies greatly with different build
options.

TF-M project provides [metrics](https://qa-reports.linaro.org/tf/tf-m/metrics/?environment=DefaultProfileM&environment=DefaultProfileS&environment=DefaultProfileL&metric=:summary:)
of the S world size for existing platforms, which may help to get a rough
guide to the sizes needed.

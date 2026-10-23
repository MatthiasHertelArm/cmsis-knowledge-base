---
id: "tfm-code-sharing-between-independently-how-to-use-code-sharing"
type: "concept"
domain: "security"
title: "Code sharing between independently linked XIP binaries: How to use code sharing?"
summary: "Considering the above, code sharing is an optional feature, which is disabled by default. It can be enabled from the command line with a compile time switch:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/software/code_sharing.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/code_sharing.html#how-to-use-code-sharing"
license: "BSD-3-Clause"
mode: "V"
---

Considering the above, code sharing is an optional feature, which is disabled
by default. It can be enabled from the command line with a compile time switch:

 - `TFM_CODE_SHARING`: Set to `ON` to enable code sharing.

With the default settings, only the common part of the mbed-crypto library is
shared, between MCUboot and the SPE. However, there might be other device
specific code (e.g. device drivers) that could be shared. The shared
cryptography code consists mainly of the SHA-256 algorithm, the `bignum` library
and some RSA related functions. If image encryption support is enabled in
MCUboot, then AES algorithms can be shared as well.

Sharing code between the SPE and an external project is possible, even if
MCUboot isn't used as the bootloader. For example, a custom bootloader can also
be built in such a way as to create the necessary artifacts to share some of its
code with the SPE. The same artifacts must be created like the case of MCUboot:

 - `shared_symbols_name.txt`: Contains the name of the shared symbols. Used by
    the script that prevents symbol collision.
 - `shared_symbols_address.txt`: Contains the type, address and name of shared
   symbols. Used by the linker when linking runtime SPE.
 - `shared_code.axf`: GNUARM specific. The stripped version of the firmware
   component, only contains the shared code. It is used by the linker when
   linking the SPE.


The artifacts of the shared code extraction steps must be preserved to be
able to link them to any future SPE version.
When an external project is sharing code with the SPE, the `SHARED_CODE_PATH`
compile time switch must be set to the path of the artifacts mentioned above.

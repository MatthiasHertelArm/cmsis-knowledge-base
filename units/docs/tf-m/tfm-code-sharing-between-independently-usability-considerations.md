---
id: "tfm-code-sharing-between-independently-usability-considerations"
type: "concept"
domain: "security"
title: "Code sharing between independently linked XIP binaries: Usability considerations"
summary: "Functions that only use local variables can be shared easily. However, functions that rely on global variables are a bit tricky."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/software/code_sharing.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/code_sharing.html#usability-considerations"
license: "BSD-3-Clause"
mode: "V"
---

Functions that only use local variables can be shared easily. However, functions
that rely on global variables are a bit tricky. They can still be shared, but
all global variables must be placed in the shared symbol section, to prevent
overwriting and to enable the retention of their values.

Some global variables might need to be reinitialised to their original values by
runtime firmware, if they have been used by the bootloader, but need to have
their original value when runtime firmware starts to use them. If so, the
reinitialising functionality must be implemented explicitly, because the low
level startup code in the SPE does not initialise the shared variables, which
means they retain their value after MCUboot stops running.

If a bug is discovered in the shared code, it cannot be fixed with a firmware
upgrade, if the bootloader code is immutable. If this is the case, disabling
code sharing might be a solution, as the new runtime firmware could contain the
fixed code instead of relying on the unfixed shared code. However, this would
increase code footprint.

API backward compatibility also can be an issue. If the API has changed in newer
version of the shared code. Then new code cannot rely on the shared version.
The changed code and all the other shared code where it is referenced from must
be ignored and the updated version of the functions must be compiled in the
SPE binary. The Mbed TLS library is API compatible with its current version
(`v2.24.0`) since the `mbedtls-2.7.0 release` (2018-02-03).

To minimise the risk of incompatibility, use the same compiler flags to build
both firmware components.

The artifacts of the shared code extraction steps must be preserved so as to
remain available if new SPE firmware (that relies on shared code) is built and
released. Those files are necessary to know the address of shared symbols when
linking the SPE.

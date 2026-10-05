---
id: "tfm-code-sharing-between-independently-technical-challenge"
type: "concept"
domain: "security"
title: "Code sharing between independently linked XIP binaries: Technical challenge"
summary: "Code sharing in a regular OS environment is easily achievable with dynamically linked libraries. However, this is not the case in Cortex-M systems where applications might run bare-metal, or on top of an RTOS, which usually lacks dynamic loading functionality."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/software/code_sharing.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/code_sharing.html#technical-challenge"
license: "BSD-3-Clause"
mode: "V"
---

Code sharing in a regular OS environment is easily achievable with dynamically
linked libraries. However, this is not the case in Cortex-M systems where
applications might run bare-metal, or on top of an RTOS, which usually lacks
dynamic loading functionality. One major challenge to be solved in the Cortex-M
space is how to share code between independently linked XIP applications that
are tied to a certain memory address range to be executable and have absolute
function and global data memory addresses. In this case, the code is not
relocatable, and in most cases, there is no loader functionality in the system
that can perform code relocation. Also, the lack of an MMU makes the address
space flat, constant and not reconfigurable at runtime by privileged code.

One other difficulty is that the bootloader and the runtime use the same RAM
area during execution. The runtime firmware is executed strictly after the
bootloader, so normally, it can reuse the whole secure RAM area, as it would be
the exclusive user. No attention needs to be paid as to where global data is
placed by the linker. The bootloader does not need to retain its state. The low
level startup of the runtime firmware can freely overwrite the RAM with its data
without corrupting bootloader functionality. However, with code sharing between
bootloader and runtime firmware, these statements are no longer true. Global
variables used by the shared code must either retain their value or must be
reinitialised during low level startup of the runtime firmware. The startup code
is not allowed to overwrite the shared global variables with arbitrary data. The
following design proposal provides a solution to these challenges.

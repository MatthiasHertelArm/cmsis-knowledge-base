---
id: "tfm-first-things-first-arm-compiler-minimum-v6-21"
type: "concept"
domain: "security"
title: "First Things First: Arm Compiler (minimum v6.21)"
summary: "First Things First: Arm Compiler (minimum v6.21)"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/getting_started/tfm_getting_started.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/getting_started/tfm_getting_started.html#arm-compiler-minimum-v6-21"
license: "BSD-3-Clause"
mode: "V"
---

**Note:** When compiling for a Cortex-M52 target, a Cortex-M85 target, or with an -mcpu=<name> option that includes the **+pacbti** feature modifier, and when configured without *User based* Licensing, the compiler could incorrectly report one of these errors: * `Cortex-M52 is not available with the current toolkit edition and license` * `Cortex-M85 is not available with the current toolkit edition and license` The use of -target-feature **+pacbti** is disallowed in this variant of Armclang. Please use Armclang version 6.24+ which does not have this issue.

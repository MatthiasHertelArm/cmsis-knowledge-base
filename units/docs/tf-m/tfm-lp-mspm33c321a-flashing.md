---
id: "tfm-lp-mspm33c321a-flashing"
type: "concept"
domain: "security"
title: "LP_MSPM33C321A: Flashing"
summary: "Use Code Composer Studio (CCS) to program the device via a project-less debug session (Target Configuration for MSPM33C321A, then Debug Without Program/connect to the target)."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/ti/LP_MSPM33C321A/readme.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/ti/LP_MSPM33C321A/.html#flashing"
license: "BSD-3-Clause"
mode: "V"
---

Use [Code Composer Studio (CCS)](https://www.ti.com/tool/CCSTUDIO) to program
the device via a project-less debug session (Target Configuration for
`MSPM33C321A`, then `Debug Without Program`/connect to the target).


### Erasing


With the target connected, erase the device using the Scripting Console:

- `Scripts > MSPM33C321A_Commands > MSPM33_Mailbox_MassErase_Auto` erases
  the main flash bank.
- `Scripts > MSPM33C321A_Commands > MSPM33_Mailbox_FactoryReset_Auto` also
  erases the data flash bank. Use this if PS/ITS/NV counters (stored in the
  data bank) need to be reset as well.


### Programming


Load the Non-Secure image first, then the Secure image, at their respective
addresses:

- Non-Secure image (`tfm_ns.bin`): `0x00080000`
- Secure image (`tfm_s.bin`): `0x10000000`


**Important:** Before loading either image, set the flash programmer option to **Do not erase Flash memory**. If flash-erase-on-load is left enabled, loading the Secure image second will erase the previously loaded Non-Secure image.

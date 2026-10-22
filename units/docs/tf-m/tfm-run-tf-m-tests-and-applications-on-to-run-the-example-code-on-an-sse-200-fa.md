---
id: "tfm-run-tf-m-tests-and-applications-on-to-run-the-example-code-on-an-sse-200-fa"
type: "concept"
domain: "security"
title: "Run TF-M tests and applications on Arm platforms: Execute TF-M regression tests on MPS2 boards and FVP / To run the example code on an SSE-200 Fast-Model"
summary: "Part of: Execute TF-M regression tests on MPS2 boards and FVP"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/building/run_tfm_examples_on_arm_platforms.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/building/run_tfm_examples_on_arm_platforms.html#to-run-the-example-code-on-an-sse-200-fast-model"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Execute TF-M regression tests on MPS2 boards and FVP_

Using FVP_MPS2_AEMv8M provided by Arm Development Studio 2019.1.


#### Example application and regression tests without BL2 bootloader

Add `tfm_s.axf` and `tfm_ns.axf` to symbol files in Debug Configuration
menu.

```bash

<DS_PATH>/sw/models/bin/FVP_MPS2_AEMv8M \
--parameter fvp_mps2.platform_type=2 \
--parameter cpu0.baseline=0 \
--parameter cpu0.INITVTOR_S=0x10000000 \
--parameter cpu0.semihosting-enable=0 \
--parameter fvp_mps2.DISABLE_GATING=0 \
--parameter fvp_mps2.telnetterminal0.start_telnet=1 \
--parameter fvp_mps2.telnetterminal1.start_telnet=0 \
--parameter fvp_mps2.telnetterminal2.start_telnet=0 \
--parameter fvp_mps2.telnetterminal0.quiet=0 \
--parameter fvp_mps2.telnetterminal1.quiet=1 \
--parameter fvp_mps2.telnetterminal2.quiet=1 \
--application cpu0=<build_dir>/bin/tfm_s.axf \
--data cpu0=<build_dir>/bin/tfm_ns.bin@0x00100000
```

#### Example application and regression tests with BL2 bootloader

To test TF-M with bootloader, one must apply the following changes:

- Add `bl2.axf` to symbol files in DS-5 in Debug Configuration
  menu.
- Replace the last two lines of the previous command with this:

```bash

--application cpu0=<build_dir>/bin/bl2.axf \
--data cpu0=<build_dir>/tfm_s_ns_signed.bin@0x10080000
```

##### Test software upgrade with BL2 bootloader

BL2 bootloader is mandatory to test software update. Furthermore, two TF-M blobs
must be built. Outputs of example application and regression test can be used to
test it. Load output of example application to the primary slot (0x10080000) and
output of regression test to the secondary slot (0x10180000). Add the following
line to the end of the previous chapter:

```bash

--data cpu0=<build_dir>/tfm_s_ns_signed.bin@0x10180000
```

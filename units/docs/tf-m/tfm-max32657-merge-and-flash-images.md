---
id: "tfm-max32657-merge-and-flash-images"
type: "concept"
domain: "security"
title: "MAX32657: Merge and Flash Images"
summary: "Follow the steps below to program the flash with a compiled TF-M image (i.e. S, NS or both)."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/platform/adi/max32657/README.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/adi/max32657/.html#merge-and-flash-images"
license: "BSD-3-Clause"
mode: "V"
---

Follow the steps below to program the flash with a compiled TF-M image (i.e. S, NS or both).


Generate Intel hex files from the output binary (bin) files as follows:

```console

srec_cat build_spe/bin/tfm_s_signed.bin -binary --offset 0x01010000 -o build_spe/bin/tfm_s_signed.hex -intel
srec_cat build_test/bin/tfm_ns_signed.bin -binary --offset 0x01060000 -o build_test/bin/tfm_ns_signed.hex -intel
```
Merge hex files as follows:

```console

srec_cat build_spe/bin/bl2.hex -Intel build_spe/bin/tfm_s_signed.hex -Intel build_test/bin/tfm_ns_signed.hex -Intel -o tfm_merged.hex -Intel
```
Alternatively, you can merge hex files with [mergehex.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/build/mergehex.py)

```console

python /PATH/TO/mergehex.py -o tfm_merged.hex build_spe/bin/bl2.hex build_spe/bin/tfm_s_signed.hex build_test/bin/tfm_ns_signed.hex
```

**Note:** Use bl2_signed.hex instead bl2.hex if Secure Boot ROM is enabled.

Flash them with JLink as follows:

```console

JLinkExe -device MAX32657 -if swd -speed 2000 -autoconnect 1
J-Link>h
J-Link>r
J-Link>erase
J-Link>loadfile build_spe/bin/tfm_merged.hex
```

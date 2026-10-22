---
id: "tfm-secure-boot-signing-the-secure-image-manually-in-cas"
type: "concept"
domain: "security"
title: "Secure boot: Signing the images manually / Signing the secure image manually in case of multiple image boot"
summary: "TITLE: Versatile Express Images Configuration File [IMAGES] TOTALIMAGES: 3 ;Number of Images (Max: 32) IMAGE0ADDRESS: 0x00000000 IMAGE0FILE: \\Software\\bl2.axf ; BL2 bootloader IMAGE1ADDRESS: 0x10080000 IMAGE1FILE: \\Software\\tfm_sig1.bin ; TF-M default test binary blob IMAGE2ADDRESS: 0x10180000 IMAGE2FILE: \\Software\\tfm_sig2.bin ; TF-M regression …"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/booting/tfm_secure_boot.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/tfm_secure_boot.html#signing-the-secure-image-manually-in-case-of-multiple-image-boot"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Signing the images manually_

:
```
python3 bl2/ext/mcuboot/scripts/imgtool.py sign \
    --layout <build_dir>/bl2/ext/mcuboot/CMakeFiles/signing_layout_s.dir/signing_layout_s.c.obj \
    -k <tfm_dir>/bl2/ext/mcuboot/root-RSA-3072.pem \
    --public-key-format full \
    --align 1 \
    -v 1.2.3+4 \
    -d "(1,1.2.3+0)" \
    -s 42 \
    -H 0x400 \
    <build_dir>/bin/tfm_s.bin \
    <build_dir>/bin/tfm_s_signed.bin

## Testing firmware upgrade

As downloading the new firmware image is out of scope for MCUBoot, the update
process is started from a state where the original and the new image are already
programmed to the appropriate memory slots. To generate the original and a new
firmware package, TF-M is built twice with different build configurations.


### Overwriting firmware upgrade

Run TF-M build twice with `MCUBOOT_IMAGE_NUMBER` set to "1" in both cases
(single image boot), but with two different build configurations: default and
regression. Save the artifacts between builds, because second run can overwrite
original binaries. Download default build to the primary slot and regression
build to the secondary slot.


#### Executing firmware upgrade on FVP_MPS2_AEMv8M

```bash

<ARM_DS_PATH>/sw/models/bin/FVP_MPS2_AEMv8M  \
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
--application cpu0=<build_dir>/bin/bl2.axf \
--data cpu0=<default_build_dir>/bin/tfm_s_ns_signed.bin@0x10080000 \
--data cpu0=<regresssion_build_dir>/bin/tfm_s_ns_signed.bin@0x10180000
```

#### Executing firmware upgrade on SSE 200 FPGA on MPS2 board


:
```
TITLE: Versatile Express Images Configuration File
[IMAGES]
TOTALIMAGES: 3                     ;Number of Images (Max: 32)
IMAGE0ADDRESS: 0x00000000
IMAGE0FILE: \Software\bl2.axf      ; BL2 bootloader
IMAGE1ADDRESS: 0x10080000
IMAGE1FILE: \Software\tfm_sig1.bin ; TF-M default test binary blob
IMAGE2ADDRESS: 0x10180000
IMAGE2FILE: \Software\tfm_sig2.bin ; TF-M regression test binary blob
```
The following message will be shown in case of successful firmware upgrade:

:
```
[INF] Starting bootloader
[INF] Swap type: test
[INF] Image upgrade secondary slot -> primary slot
[INF] Erasing the primary slot
[INF] Copying the secondary slot to the primary slot: 0x100000 bytes
[INF] Bootloader chainload address offset: 0x80000
[INF] Jumping to the first image slot
[Sec Thread] Secure image initializing!

#### Execute test suites for the Secure area ####
Running Test Suite PSA protected storage S interface tests (TFM_PS_TEST_2XXX)...
...
```
To update the secure and non-secure images separately (multiple image boot),
set the `MCUBOOT_IMAGE_NUMBER` switch to "2" (this is the default
configuration value) and follow the same instructions as in case of single image
boot.


#### Executing multiple firmware upgrades on SSE 200 FPGA on MPS2 board


:
```
TITLE: Versatile Express Images Configuration File
[IMAGES]
TOTALIMAGES: 4                     ;Number of Images (Max: 32)
IMAGE0ADDRESS: 0x00000000
IMAGE0FILE: \Software\bl2.axf      ; BL2 bootloader
IMAGE1ADDRESS: 0x10080000
IMAGE1FILE: \Software\tfm_sign.bin ; TF-M default test binary blob
IMAGE2ADDRESS: 0x10180000
IMAGE2FILE: \Software\tfm_ss1.bin  ; TF-M regression test secure (signed) image
IMAGE3ADDRESS: 0x10200000
IMAGE3FILE: \Software\tfm_nss1.bin ; TF-M regression test non-secure (signed) image
```
Note that both the concatenated binary blob (the images are signed separately
and then concatenated) and the separate signed images can be downloaded to the
device because on this platform (AN521) both the primary slots and the secondary
slots are contiguous areas in the Flash (see Integration with TF-M). The
following message will be shown in case of successful firmware upgrades:

:
```
[INF] Starting bootloader
[INF] Swap type: test
[INF] Swap type: test
[INF] Image upgrade secondary slot -> primary slot
[INF] Erasing the primary slot
[INF] Copying the secondary slot to the primary slot: 0x80000 bytes
[INF] Image upgrade secondary slot -> primary slot
[INF] Erasing the primary slot
[INF] Copying the secondary slot to the primary slot: 0x80000 bytes
[INF] Bootloader chainload address offset: 0x80000
[INF] Jumping to the first image slot
[Sec Thread] Secure image initializing!
TFM level is: 1
[Sec Thread] Jumping to non-secure code...

#### Execute test suites for the Secure area ####
Running Test Suite PSA protected storage S interface tests (TFM_PS_TEST_2XXX)...
...
```

### Swapping firmware upgrade

Follow the same instructions and platform related configurations as in case of
overwriting build including these changes:

- Set the `MCUBOOT_UPGRADE_STRATEGY` compile time switch to "SWAP"
  before build.
- Set the `MCUBOOT_IMAGE_NUMBER` compile time switch to "1" (single image
  boot) or "2" (multiple image boot) before build.

During single image boot the following message will be shown in case of
successful firmware upgrade, `Swap type: test` indicates that images were
swapped:

:
```
[INF] Starting bootloader
[INF] Image 0: magic= good, copy_done=0x3, image_ok=0x3
[INF] Scratch: magic=  bad, copy_done=0x0, image_ok=0x2
[INF] Boot source: primary slot
[INF] Swap type: test
[INF] Bootloader chainload address offset: 0x80000
[INF] Jumping to the first image slot
[Sec Thread] Secure image initializing!

#### Execute test suites for the Secure area ####
Running Test Suite PSA protected storage S interface tests (TFM_PS_TEST_2XXX)...
...
```

### Direct execute-in-place firmware upgrade

Follow the same instructions and platform related configurations as in case of
overwriting build including these changes:

- Set the `MCUBOOT_UPGRADE_STRATEGY` compile time switch to "DIRECT_XIP"
  before build.
- set `MCUBOOT_EXECUTION_SLOT` to `1` in the regression build dir.
- Make sure the image version number was increased between the two build runs
  either by specifying it manually or by checking in the build log that it was
  incremented automatically.


#### Executing firmware upgrade on FVP_MPS2_AEMv8M


```bash

<ARM_DS_PATH>/sw/models/bin/FVP_MPS2_AEMv8M  \
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
--application cpu0=<build_dir>/bin/bl2.axf \
--data cpu0=<default_build_dir>/bin/tfm_s_ns_signed.bin@0x10080000 \
--data cpu0=<regresssion_build_dir>/bin/tfm_s_ns_signed.bin@0x10180000
```

#### Executing firmware upgrade on SSE 200 FPGA on MPS2 board


:
```
TITLE: Versatile Express Images Configuration File
[IMAGES]
TOTALIMAGES: 3                     ;Number of Images (Max: 32)
IMAGE0ADDRESS: 0x00000000
IMAGE0FILE: \Software\bl2.axf      ; BL2 bootloader
IMAGE1ADDRESS: 0x10080000
IMAGE1FILE: \Software\tfm_sign.bin ; TF-M default test binary blob
IMAGE2ADDRESS: 0x10180000
IMAGE2FILE: \Software\tfm_sig1.bin ; TF-M regression test binary blob
```

#### Executing firmware upgrade on Musca-B1 boards

After the two images have been built, they can be concatenated to create the
combined image using `srec_cat`:

- Linux::
```
srec_cat bin/bl2.bin -Binary -offset 0xA000000 tfm_sign.bin -Binary -offset 0xA020000 tfm_sign_1.bin -Binary -offset 0xA100000 -o tfm.hex -Intel
```
- Windows::
```
srec_cat.exe bin\bl2.bin -Binary -offset 0xA000000 tfm_sign.bin -Binary -offset 0xA020000 tfm_sign_1.bin -Binary -offset 0xA100000 -o tfm.hex -Intel
```
The following message will be shown in case of successful firmware upgrade,
notice that image with higher version number (`version=1.2.3.5`) is executed:

:
```
[INF] Starting bootloader
[INF] Image 0: version=1.2.3.4, magic= good, image_ok=0x3
[INF] Image 1: version=1.2.3.5, magic= good, image_ok=0x3
[INF] Booting image from the secondary slot
[INF] Bootloader chainload address offset: 0xa0000
[INF] Jumping to the first image slot
[Sec Thread] Secure image initializing!

#### Execute test suites for the Secure area ####
Running Test Suite PSA protected storage S interface tests (TFM_PS_TEST_2XXX)...
...
```

#### Executing firmware upgrade on CoreLink SSE-200 Subsystem for MPS3 (AN524)


:
```
TITLE: Arm MPS3 FPGA prototyping board Images Configuration File

[IMAGES]
TOTALIMAGES: 3                     ;Number of Images (Max: 32)

IMAGE0UPDATE: AUTO                 ;Image Update:NONE/AUTO/FORCE
IMAGE0ADDRESS: 0x00000000
IMAGE0FILE: \SOFTWARE\bl2.bin      ;BL2 bootloader
IMAGE1UPDATE: AUTO
IMAGE1ADDRESS: 0x00040000
IMAGE1FILE: \SOFTWARE\tfm_sig0.bin ;TF-M example application binary blob
IMAGE2UPDATE: AUTO
IMAGE2ADDRESS: 0x000C0000
IMAGE2FILE: \SOFTWARE\tfm_sig1.bin ;TF-M regression test binary blob
```

### RAM loading firmware upgrade

To enable RAM loading, please set `MCUBOOT_UPGRADE_STRATEGY` to "RAM_LOAD"
(either in the configuration file or through the command line), and then specify
a destination load address in RAM where the image can be copied to and executed
from. The `S_IMAGE_LOAD_ADDRESS` macro must be specified in the target
dependent files, and if multiple image boot is enabled then
`NS_IMAGE_LOAD_ADDRESS` must also be defined. For example with Musca-S, its
`flash_layout.h` file in the `platform` folder should include ``#define
S_IMAGE_LOAD_ADDRESS #0xA0020000``


#### Executing firmware upgrade on Musca-S board

After two images have been built, they can be concatenated to create the
combined image using `srec_cat`:

- Linux::
```
srec_cat bin/bl2.bin -Binary -offset 0xA000000 tfm_sign_old.bin -Binary -offset 0xA020000 tfm_sign_new.bin -Binary -offset 0xA100000 -o tfm.hex -Intel
```
- Windows::
```
srec_cat.exe bin\bl2.bin -Binary -offset 0xA000000 tfm_sign_old.bin -Binary -offset 0xA020000 tfm_sign_new.bin -Binary -offset 0xA100000 -o tfm.hex -Intel
```
The following message will be shown in case of successful firmware upgrade when,
RAM loading is enabled, notice that image with higher version number
(`version=0.0.0.2`) is executed:

:
```
[INF] Starting bootloader
[INF] Image 0: version=0.0.0.1, magic= good, image_ok=0x3
[INF] Image 1: version=0.0.0.2, magic= good, image_ok=0x3
[INF] Image has been copied from the secondary slot in flash to SRAM address 0xA0020000
[INF] Booting image from SRAM at address 0xA0020000
[INF] Bootloader chainload address offset: 0x20000
[INF] Jumping to the first image slot
[Sec Thread] Secure image initializing!
```


## Integration with Firmware Update service

The shim layer of the Firmware Update partition calls the APIs in
bootutil_misc.c to control the image status.

- Call `boot_set_pending_multi()` to make the image as a candidate image for
  booting.
- Call `boot_set_confirmed_multi()` to make the image as a permanent image.

Currently, in direct-xip mode and ram-load mode, TF-M cannot get the
information of which slot contains the running image from the bootloader.
So the Firmware Update partition cannot decide where to write the new
image. As a result, the firmware update service is not supported in
direct-xip mode and ram-load mode.
--------------------------------

*SPDX-FileCopyrightText: Copyright The TrustedFirmware-M Contributors*

*SPDX-License-Identifier: BSD-3-Clause*

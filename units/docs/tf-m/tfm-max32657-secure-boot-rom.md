---
id: "tfm-max32657-secure-boot-rom"
type: "concept"
domain: "security"
title: "MAX32657: Secure Boot ROM"
summary: "MAX32657 has Secure Boot ROM that used to authenticate user code via ECDSA 256 public key. The Secure Boot ROM is disabled on default, to enable it user need to provision device first."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/adi/max32657/README.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/adi/max32657/.html#secure-boot-rom"
license: "BSD-3-Clause"
mode: "V"
---

MAX32657 has Secure Boot ROM that used to authenticate user code via ECDSA 256 public key.
The Secure Boot ROM is disabled on default, to enable it user need to provision device first.

ADI provides enable_secure_boot.py (under <CMAKE_BINARY_DIR>/lib/ext/tesa-toolkit-src/devices/max32657/scripts/bl1_provision)
script to simply provision the device. This script reads user certificate via command line parameter
then writes user key on the device and disables debug interface.

To create pub & private key pair for MAX32657 run:

```bash

openssl ecparam -out <MY_CERT_FILE.pem> -genkey -name prime256v1
```

**Note:** Debug interface will be disabled after secure boot is enabled. User must write final firmware before provisioning the device. It can be written during device provision, Just add your final firmware hex file in JLinkScript under <CMAKE_BINARY_DIR>/lib/ext/tesa-toolkit-src/devices/max32657/scripts/bl1_provision folder.

After secure boot has been enabled BL2 image must be signed with user certificate
otherwise Secure Boot ROM will not validate BL2 image and will not execute it.
The sign process will be done automatically if BL1 be ON `-DBL1=ON`
The sign key can be specified over command line option -DTFM_BL2_SIGNING_KEY_PATH=<MY_KEY_FILE>
or by setting the flag in <TF-M base folder>/platform/ext/target/adi/max32657/config.cmake
Development purpose test certificate is here:
<CMAKE_BINARY_DIR>/lib/ext/tesa-toolkit-src/devices/max32657/keys/bl1_dummy.pem
It shall not been used for production purpose just for development purpose.


**Note:** The signature generation depends on ecdsa that's have to be installed:: pip3 install ecdsa

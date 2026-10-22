---
id: "tfm-max32657-bl2-and-tf-m-provisioning"
type: "concept"
domain: "security"
title: "MAX32657: BL2 and TF-M Provisioning"
summary: "On default -DPLATFORM_DEFAULT_PROVISIONING=ON and -DTFM_DUMMY_PROVISIONING=ON which will use default provisioning and dummpy keys, these configuration is fine for development purpose but for production customer specific keys shall be used Provisioning bundles can be generated with the -DPLATFORM_DEFAULT_PROVISIONING=OFF flag."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/platform/adi/max32657/README.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/adi/max32657/.html#bl2-and-tf-m-provisioning"
license: "BSD-3-Clause"
mode: "V"
---

On default `-DPLATFORM_DEFAULT_PROVISIONING=ON` and `-DTFM_DUMMY_PROVISIONING=ON`
which will use default provisioning and dummpy keys, these configuration is fine
for development purpose but for production customer specific keys shall be used
Provisioning bundles can be generated with the `-DPLATFORM_DEFAULT_PROVISIONING=OFF` flag.
The provisioning bundle binary will be generated and it's going to contain
the provisioning code and provisioning values.

If `-DPLATFORM_DEFAULT_PROVISIONING=OFF` and `-DTFM_DUMMY_PROVISIONING=ON` then the keys in
the `tf-m/platform/ext/target/common/provisioning/provisioning_config.cmake` and the
default MCUBoot signing keys will be used for provisioning.

If `-DPLATFORM_DEFAULT_PROVISIONING=OFF` and `-DTFM_DUMMY_PROVISIONING=OFF` are set
then unique values can be used for provisioning. The keys and seeds can be changed by
passing the new values to the build command, or by setting the `-DPROVISIONING_KEYS_CONFIG` flag
to a .cmake file that contains the keys. An example config cmake file can be seen at
`tf-m/platform/ext/target/common/provisioning/provisioning_config.cmake`.
Otherwise new random values are going to be generated and used. For the image signing
the ${MCUBOOT_KEY_S} and ${MCUBOOT_KEY_NS} will be used. These variables should point to
.pem files that contain the code signing private keys. The public keys are going to be generated
from these private keys and will be used for provisioning. The hash of the public key is going to
be written into the `provisioning_data.c` automatically.

If `-DMCUBOOT_GENERATE_SIGNING_KEYPAIR=ON` is set then a new mcuboot signing public and private
keypair is going to be generated and it's going to be used to sign the S and NS binaries.

The new generated keypair can be found in the `<build dir>/bin` folder or in the
`<install directory>/image_signing/keys` after installation.
The generated provisioning_data.c file can be found at
`<build directory>/platform/target/provisioning/provisioning_data.c`


**Note:** The provisioning bundle generation depends on pyelftools that's have to be installed:: pip3 install pyelftools


### UART Console


MAX32657 has one UART (UART0) peripheral which is routed for Non-Secure console output by default.
S and NS firmware can not use UART at the same time.
If TFM_S_REG_TEST been defined the UART console will be routed to the Secure side otherwise it will
be on NS side.

--------------

*Copyright 2025 Analog Devices, Inc. All rights reserved.
*SPDX-License-Identifier: BSD-3-Clause*

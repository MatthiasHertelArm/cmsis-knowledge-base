---
id: "tfm-corstone-sse-310-with-ethos-u55-u6-building-tf-m"
type: "concept"
domain: "security"
title: "Corstone SSE-310 with Ethos-U55/U65 Example Subsystem for Arm Ecosystem FVP and for MPS3 (AN555): Building TF-M"
summary: "-DTFM_PLATFORM=arm/mps3/corstone310/an555"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/platform/arm/mps3/corstone310/README.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/arm/mps3/corstone310/.html#building-tf-m"
license: "BSD-3-Clause"
mode: "V"
---

### Follow the instructions in Building instructions.



### Build instructions with platform name: arm/mps3/corstone310/an555

`-DTFM_PLATFORM=arm/mps3/corstone310/an555`


**Note:** For Ethos-U55/U65 IP this platform support only provides base address, interrupt number and an example NPU setup as non-secure, unprivileged.


### Build instructions with platform name: arm/mps3/corstone310/fvp

`-DTFM_PLATFORM=arm/mps3/corstone310/fvp`


**Note:** For Ethos-U55/U65 IP this platform support only provides base address, interrupt number and an example NPU setup as non-secure, unprivileged.


**Note:** The built binaries can be run on the Corstone-310 Ethos-U55/U65 Ecosystem FVP (FVP_SSE310_MPS3). At least Ecosystem FVP version 11.22 is required.


**Note:** Provisioning bundles can be generated with the `-DPLATFORM_DEFAULT_PROVISIONING=OFF` flag. The provisioning bundle binary will be generated and it's going to contain the provisioning code and provisioning values.


**Note:** If `-DPLATFORM_DEFAULT_PROVISIONING=OFF` and `-DTFM_DUMMY_PROVISIONING=ON` then the keys in the `tf-m/platform/ext/target/arm/mps3/common/provisioning/provisioning_config.cmake` and the default MCUBoot signing keys will be used for provisioning. If `-DPLATFORM_DEFAULT_PROVISIONING=OFF` and `-DTFM_DUMMY_PROVISIONING=OFF` are set then unique values can be used for provisioning. The keys and seeds can be changed by passing the new values to the build command, or by setting the `-DPROVISIONING_KEYS_CONFIG` flag to a .cmake file that contains the keys. An example config cmake file can be seen at `tf-m/platform/ext/target/arm/mps3/common/provisioning/provisioning_config.cmake`. Otherwise new random values are going to be generated and used. For the image signing the ${MCUBOOT_KEY_S} and ${MCUBOOT_KEY_NS} will be used. These variables should point to .pem files that contain the code signing private keys. The public keys are going to be generated from these private keys and will be used for provisioning. The hash of the public key is going to be written into the `provisioning_data.c` automatically. If `-DMCUBOOT_GENERATE_SIGNING_KEYPAIR=ON` is set then a new mcuboot signing public and private keypair is going to be generated and it's going to be used to sign the S and NS binaries. The new generated keypair can be found in the `<build dir>/bin` folder or in the `<install directory>/image_signing/keys` after installation. The generated provisioning_data.c file can be found at `<build directory>/platform/target/provisioning/provisioning_data.c`


**Note:** The provisioning bundle generation depends on pyelftools that's have to be installed:: pip3 install pyelftools

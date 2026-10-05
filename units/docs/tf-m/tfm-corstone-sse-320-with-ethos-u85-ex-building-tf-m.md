---
id: "tfm-corstone-sse-320-with-ethos-u85-ex-building-tf-m"
type: "concept"
domain: "security"
title: "Corstone SSE-320 with Ethos-U85 Example Subsystem for Ecosystem FVP: Building TF-M"
summary: "Corstone SSE-320 with Ethos-U85 Example Subsystem for Ecosystem FVP: Building TF-M"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/platform/arm/mps4/corstone320/README.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/platform/arm/mps4/corstone320/.html#building-tf-m"
license: "BSD-3-Clause"
mode: "V"
---

### Follow the instructions in Building instructions.



### Build instructions with platform name: arm/mps4/corstone320

`-DTFM_PLATFORM=arm/mps4/corstone320`


**Note:** The built binaries can be run on the Corstone-320 Ethos-U85 Ecosystem FVP (FVP_Corstone_SSE-320).


**Note:** If `-DTFM_DUMMY_PROVISIONING=ON` then the keys in the `tf-M/platform/ext/target/arm/mps4/common/provisioning/bundle_cm/cm_provisioning_config.cmake`, `tf-M/platform/ext/target/arm/mps4/common/provisioning/bundle_dm/dm_provisioning_config.cmake` and default MCUBoot signing and encryption keys will be used for provisioning. If `-DTFM_DUMMY_PROVISIONING=OFF` is set then unique values can be used for provisioning. The keys and seeds can be changed by passing the new values to the build command, or by setting the `-DDM_PROVISIONING_KEYS_CONFIG` and  `-DCM_PROVISIONING_KEYS_CONFIG` flag to the `.cmake` files which contain the keys. An example config cmake file can be seen at `tf-m/platform/ext/target/arm/mps4/common/provisioning/bundle_cm/cm_provisioning_config.cmake` and `tf-m/platform/ext/target/arm/mps4/common/provisioning/bundle_dm/dm_provisioning_config.cmake`. Otherwise new random values are going to be generated and used (or default values in some cases). For signing the BL2 image, `${TFM_BL1_2_CM_SIGNING_KEY_PATH}` key will be used. This should point to a valid LMS `.pub` file. The private key is found with the `.prv` extension. If `-DTFM_GENERATE_BL1_2_CM_SIGNING_KEY=ON` is set, then a new signing public and private keypair is going to be generated and it's going to be used to sign the the BL2 image. For the image signing the `${MCUBOOT_KEY_S}` and `${MCUBOOT_KEY_NS}` will be used. These variables should point to `.pem` files that contain the code signing private keys. The public keys are going to be generated from these private keys and will be used for provisioning. The hash of the public key is going to be written into the `provisioning_data.c` automatically. For the BL2 image encryption the `TFM_BL2_ENCRYPTION_KEY_PATH` has to be set to a .bin file which contains the encryption key. (For an example, see `tf-m/bl1/bl1_2/bl2_dummy_encryption_key.bin`) If `-DMCUBOOT_GENERATE_SIGNING_KEYPAIR=ON` is set then a new MCUBoot signing public and private keypair is going to be generated and it's going to be used to sign the S and NS binaries. The new generated keypair can be found in the `<build dir>/bin` folder or in the `<install directory>/image_signing/keys` after installation. The generated provisioning_data.c file can be found at `<build directory>/platform/target/provisioning/provisioning_data.c`


**Note:** The provisioning bundle generation depends on pyelftools that's have to be installed:: pip3 install pyelftools

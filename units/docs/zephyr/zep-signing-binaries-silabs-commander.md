---
id: "zep-signing-binaries-silabs-commander"
type: "concept"
domain: "project"
title: "Signing Binaries: silabs_commander"
summary: "The silabs_commander tool is used to apply sign or MIC or encrypt binaries for Silicon Labs devices."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/sign.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/sign.rst"
license: "Apache-2.0"
mode: "V"
---

The `silabs_commander` tool is used to apply sign or MIC or encrypt binaries for Silicon Labs
devices. It can be invoked either by `west sign` when the `sign.tool` configuration is set to
`silabs_commander` or by `west build` if `CONFIG_SIWX91X_SIGN_KEY` or
`CONFIG_SIWX91X_MIC_KEY` is set.

If one of `CONFIG_SIWX91X_SIGN_KEY` or `CONFIG_SIWX91X_MIC_KEY` is set, `west flash` will
automatically flash the signed version of the binary.

`silabs_commander` require Simplicity Commander to be install on the host. The provisionning of the
key on the device is described in UG574 SiWx917 SoC Manufacturing Utility User Guide.

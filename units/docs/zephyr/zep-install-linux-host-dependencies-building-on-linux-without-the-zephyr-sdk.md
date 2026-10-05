---
id: "zep-install-linux-host-dependencies-building-on-linux-without-the-zephyr-sdk"
type: "concept"
domain: "project"
title: "Install Linux Host Dependencies: Building on Linux without the Zephyr SDK"
summary: "The Zephyr SDK is provided for convenience and ease of use. It provides toolchains for all Zephyr target architectures, and does not require any extra flags when building applications or running tests."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/getting_started/installation_linux.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/getting_started/installation_linux.rst"
license: "Apache-2.0"
mode: "V"
---

The Zephyr SDK is provided for convenience and ease of use. It provides
toolchains for all Zephyr target architectures, and does not require any extra
flags when building applications or running tests. In addition to
cross-compilers, the Zephyr SDK also provides prebuilt host tools. It is,
however, possible to build without the SDK's toolchain by using another
toolchain as described in the toolchains section.

As already noted above, the SDK also includes prebuilt host tools.  To use the
SDK's prebuilt host tools with a toolchain from another source, you must set the
`ZEPHYR_SDK_INSTALL_DIR` environment variable to the Zephyr SDK
installation directory. To build without the Zephyr SDK's prebuilt host tools,
the `ZEPHYR_SDK_INSTALL_DIR` environment variable must be unset.

To make sure this variable is unset, run:

```console

unset ZEPHYR_SDK_INSTALL_DIR
```

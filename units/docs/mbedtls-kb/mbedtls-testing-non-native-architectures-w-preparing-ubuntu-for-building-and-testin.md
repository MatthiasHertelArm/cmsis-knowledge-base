---
id: "mbedtls-testing-non-native-architectures-w-preparing-ubuntu-for-building-and-testin"
type: "concept"
domain: "security"
title: "Testing non-native architectures with QEMU: Preparing Ubuntu for building and testing with QEMU"
summary: "Add other targets to your package sources in a new file /etc/apt/sources.list.d/ubuntu-foreign.list. Note that ordinary Ubuntu mirrors only have PC builds, so you need a ports mirror. For example:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/testing/testing-qemu.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/testing/testing-qemu.md#preparing-ubuntu-for-building-and-testing-with-qemu"
license: "Apache-2.0"
mode: "V"
---

Add other targets to your package sources in a new file `/etc/apt/sources.list.d/ubuntu-foreign.list`. Note that ordinary Ubuntu mirrors only have PC builds, so you need a `ports` mirror. For example:

```
deb [arch=arm64,armhf,ppc64,s390x] http://fr.ports.ubuntu.com/ubuntu-ports focal main restricted universe multiverse
deb [arch=arm64,armhf,ppc64,s390x] http://fr.ports.ubuntu.com/ubuntu-ports focal-security main restricted universe multiverse
deb [arch=arm64,armhf,ppc64,s390x] http://fr.ports.ubuntu.com/ubuntu-ports focal-updates main restricted universe multiverse
```

Then install `libc6-dev` for the desired architectures.

```
sudo apt-get update
sudo apt-get install libc6-dev:arm64 libc6-dev:armhf libc6-dev:ppc64 libc6-dev:s390x
```

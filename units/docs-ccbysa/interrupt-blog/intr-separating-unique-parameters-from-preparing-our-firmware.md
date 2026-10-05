---
id: "intr-separating-unique-parameters-from-preparing-our-firmware"
type: "concept"
domain: "debug"
title: "Separating Unique Parameters from Firmware Binaries: Preparing our Firmware"
summary: "The first thing we have to do is to look for hardcoded identifiers and remove them from our firmware. For example, it is common to declare a device ID as a C-array:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-10-06-separating-unique-parameters.md"
doc_source: "https://interrupt.memfault.com/blog/separating-unique-parameters#preparing-our-firmware"
license: "CC-BY-SA-4.0"
mode: "V"
---

The first thing we have to do is to look for hardcoded identifiers and remove
them from our firmware. For example, it is common to declare a device ID as a
C-array:

```c
const uint8_t device_eui[8] = { 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff };
```

Instead, let's allocate some storage for those identifiers and point our
firmware to it.

You can choose to put unique parameters in any non-volatile storage
available on the device. If you're lucky enough to have memory-mapped flash
available on your MCU, this is often the simplest place to use.

In this case, we have plenty of flash so we will allocate some addresses towards
the end of our flash and use them to store our identifiers:

```c
#define KEYS_BASE_ADDR          0x18000
const uint8_t *device_eui   =   (uint8_t *) KEYS_BASE_ADDR;
const uint8_t *app_eui      =   (uint8_t *) KEYS_BASE_ADDR + 8;
const uint8_t *app_key      =   (uint8_t *) KEYS_BASE_ADDR + 16;
```

You may also create a section in your linker script to achieve the same result.

> **A Note on Security** In this post, we store encryption keys in standard flash
> memory. Whether or not this is a good idea depends on your application.
> Although most MCUs allow you to enable readback protection, these mechanisms
> have been defeated for a number of popular devices [^nrf51_bug]
> [^ncc_readback]. Secure key storage can instead be done using secure elements
> like the ATECC608A[^atecc608a], or special purpose registers if your device
> includes them.
> More advanced security considerations are a topic for another post.

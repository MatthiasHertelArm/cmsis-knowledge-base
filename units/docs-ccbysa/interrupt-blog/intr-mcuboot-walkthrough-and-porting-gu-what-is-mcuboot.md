---
id: "intr-mcuboot-walkthrough-and-porting-gu-what-is-mcuboot"
type: "concept"
domain: "debug"
title: "MCUboot Walkthrough and Porting Guide: What is MCUboot?"
summary: "MCUboot is a library which can be integrated into a bootloader to securely perform firmware updates. The project seeks to standardize two key areas:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-11-04-mcuboot-overview.md"
doc_source: "https://interrupt.memfault.com/blog/mcuboot-overview#what-is-mcuboot"
license: "CC-BY-SA-4.0"
mode: "V"
---

[MCUboot](https://github.com/mcu-tools/mcuboot) is a library which can be integrated into a bootloader to securely
perform firmware updates. The project seeks to standardize two key areas:

1. Secure Bootloader Functionality: that is, a bootloader that will only launch images that are cryptographically verified
2. Standardized Flash Layout: A common way to define the flash layout of an embedded system. That is, a way to define, where binaries live and how other regions of flash are used.

In addition to these features, MCUboot also includes options for encrypting/decrypting firmware
binaries, performing upgrades in a fault-tolerant manner (i.e resumption across unexpected
reboots), and recovering the system if a bad firmware image is installed.

For a custom project, MCUboot is a C library you would include in your bootloader and main
application. The surface area for the bootloader is one function which will be called to determine
the image to boot or install upgrades:

```c
int main(void) {
  // ...
  struct boot_rsp rsp;
  int rv = boot_go(&rsp);

  if (rv == 0) {
    // 'rsp' contains the start address of the image
    your_platform_do_boot(&rsp);
  }
  ```

Your main application can also use the MCUboot library to read information about the images which
are installed and mark images as ready to be installed after they have been downloaded.

---
id: "zep-tf-m-requirements-software-requirements"
type: "concept"
domain: "security"
title: "TF-M Requirements: Software Requirements"
summary: "The Python modules required when building TF-M binaries are listed in the TF-M repository under tools/requirements.txt."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/tfm/requirements.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/tfm/requirements.rst"
license: "Apache-2.0"
mode: "V"
---

The Python modules required when building TF-M binaries are listed in the
TF-M repository under `tools/requirements.txt`.

You can install them via:

```bash

$ pip3 install -r "$(west list trusted-firmware-m -f '{abspath}')/tools/requirements.txt"
```
They are used by TF-M's signing utility to prepare firmware images for
validation by the bootloader.

Part of the process of generating binaries for QEMU and merging signed
secure and non-secure binaries on certain platforms also requires the use of
the `srec_cat` utility.

This can be installed on Linux via:

```bash

$ sudo apt-get install srecord
```
And on OS X via:

```bash

$ brew install srecord
```
For Windows-based systems, please make sure you have a copy of the utility
available on your system path. See, for example:
[SRecord for Windows](https://sourceforge.net/projects/srecord/files/srecord-win32)

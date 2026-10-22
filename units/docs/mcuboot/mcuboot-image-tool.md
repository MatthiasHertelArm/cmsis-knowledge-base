---
id: "mcuboot-image-tool"
type: "concept"
domain: "boot-update"
title: "Image tool"
summary: "The Python program scripts/imgtool.py can be used to perform the operations that are necessary to manage keys and sign images. Using this script should be preferred to the manual steps described in doc/signed_images.md."
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@725d63c:docs/imgtool.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/725d63c/docs/imgtool.md"
license: "Apache-2.0"
mode: "V"
---

The Python program `scripts/imgtool.py` can be used to perform the
operations that are necessary to manage keys and sign images.  Using
this script should be preferred to the manual steps described in
`doc/signed_images.md`.

This program is written for Python3, and has several dependencies on
Python libraries.  These can be installed using 'pip3':

    pip3 install --user -r scripts/requirements.txt

---
id: "zep-tf-m-build-system"
type: "concept"
domain: "security"
title: "TF-M Build System"
summary: "When building a valid ns board target, TF-M will be built in the background, and linked with the Zephyr non-secure application."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/tfm/build.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/tfm/build.rst"
license: "Apache-2.0"
mode: "V"
---

When building a valid `_ns` board target, TF-M will be built in the
background, and linked with the Zephyr non-secure application. No knowledge
of TF-M's build system is required in most cases, and the following will
build a TF-M and Zephyr image pair, and run it in qemu with no additional
steps required:

```bash

$ west build -p auto -b mps2/an521/cpu0/ns samples/tfm_integration/psa_protected_storage/ -t run
```
The outputs and certain key steps in this build process are described here,
however, since you will need to understand and interact with the outputs, and
deal with signing the secure and non-secure images before deploying them.

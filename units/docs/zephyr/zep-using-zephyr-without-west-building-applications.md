---
id: "zep-using-zephyr-without-west-building-applications"
type: "concept"
domain: "project"
title: "Using Zephyr without west: Building applications"
summary: "You can build a Zephyr application using CMake and Ninja (or make) directly without west installed if you specify any modules manually."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/without-west.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/without-west.rst"
license: "Apache-2.0"
mode: "V"
---

You can build a Zephyr application using CMake and Ninja (or make) directly
without west installed if you specify any modules manually.

When building with west installed, the Zephyr build system will use it to set
ZEPHYR_MODULES.

If you don't have west installed and your application does not need any of
these repositories, the build will still work.

If you don't have west installed and your application *does* need one
of these repositories, you must set `ZEPHYR_MODULES`
yourself as shown above.

See modules for more details.

Similarly, if your application requires binary blobs and you are not using
west, you will need to download and place those blobs in the right places
instead of using `west blobs`. See bin-blobs for more details.

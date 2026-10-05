---
id: "zep-using-zephyr-without-west"
type: "concept"
domain: "project"
title: "Using Zephyr without west"
summary: "This page provides information on using Zephyr without west. This is not recommended for beginners due to the extra effort involved. In particular, you will have to do work \"by hand\" to replace these features:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/without-west.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/without-west.rst"
license: "Apache-2.0"
mode: "V"
---

This page provides information on using Zephyr without west. This is
not recommended for beginners due to the extra effort involved. In
particular, you will have to do work "by hand" to replace these
features:

- cloning the additional source code repositories used by Zephyr in
  addition to the main zephyr repository, and keeping them up to date
- specifying the locations of these repositories to the Zephyr build
  system
- flashing and debugging without understanding detailed usage of the
  relevant host tools


**Note:** If you have previously installed west and want to stop using it, uninstall it first: .. code-block:: console pip3 uninstall west Otherwise, Zephyr's build system will find it and may try to use it.

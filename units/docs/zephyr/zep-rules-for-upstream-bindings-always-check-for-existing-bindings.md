---
id: "zep-rules-for-upstream-bindings-always-check-for-existing-bindings"
type: "concept"
domain: "project"
title: "Rules for upstream bindings: Always check for existing bindings"
summary: "Zephyr aims for devicetree dt-source-compatibility. Therefore, if there is an existing binding for your device in an authoritative location, you should try to replicate its properties when writing a Zephyr binding, and you must justify any Zephyr-specific divergences."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/bindings-upstream.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/bindings-upstream.rst"
license: "Apache-2.0"
mode: "V"
---

Zephyr aims for devicetree dt-source-compatibility. Therefore, if there
is an existing binding for your device in an authoritative location, you should
try to replicate its properties when writing a Zephyr binding, and you must
justify any Zephyr-specific divergences.

In particular, this rule applies if:

- There is an existing binding in the mainline Linux kernel. See
  `Documentation/devicetree/bindings` in Linus's tree for existing
  bindings and the Linux devicetree documentation for more information.

- Your hardware vendor provides an official binding outside of the Linux
  kernel.

.. _Linus's tree:
   https://github.com/torvalds/linux/

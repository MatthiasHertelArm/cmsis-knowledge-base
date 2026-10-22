---
id: "zep-introduction-to-devicetree-binding"
type: "concept"
domain: "project"
title: "Introduction to Devicetree Bindings"
summary: "Devicetree nodes are matched to bindings using their :ref:compatible properties <dt-important-props>."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/bindings-intro.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/bindings-intro.rst"
license: "Apache-2.0"
mode: "V"
---

**Note:** For a detailed syntax reference, see dt-bindings-file-syntax.

Devicetree nodes are matched to bindings using their :ref:`compatible
properties <dt-important-props>`.

During the build_configuration_phase, the build system tries to match
each node in the devicetree to a binding file. When this succeeds, the build
system uses the information in the binding file both when validating the node's
contents and when generating macros for the node.

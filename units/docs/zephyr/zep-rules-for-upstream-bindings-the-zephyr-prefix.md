---
id: "zep-rules-for-upstream-bindings-the-zephyr-prefix"
type: "concept"
domain: "project"
title: "Rules for upstream bindings: The `zephyr,` prefix"
summary: "You must add this prefix to property names in the following cases:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/bindings-upstream.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/bindings-upstream.rst"
license: "Apache-2.0"
mode: "V"
---

You must add this prefix to property names in the following cases:

- Zephyr-specific extensions to bindings we share with upstream Linux. One
  example is the `zephyr,vref-mv` ADC channel property which is common to ADC
  controllers defined in `dts/bindings/adc/adc-controller.yaml`.
  This channel binding is partially shared with an analogous Linux binding, and
  Zephyr-specific extensions are marked as such with the prefix.

- Configuration values that are specific to a Zephyr device driver. One example
  is the `zephyr,lazy-load` property in the `ti,bq274xx`
  binding. Though devicetree in general is a hardware description and
  configuration language, it is Zephyr's only mechanism for configuring driver
  behavior for an individual `struct device`. Therefore, as a compromise,
  we do allow some software configuration in Zephyr's devicetree bindings, as
  long as they use this prefix to show that they are Zephyr specific.

You may use the `zephyr,` prefix when naming a devicetree compatible that is
specific to Zephyr. One example is
`zephyr,ipc-openamp-static-vrings`. In this case, it's permitted
but not required to add the `zephyr,` prefix to properties defined in the
binding.

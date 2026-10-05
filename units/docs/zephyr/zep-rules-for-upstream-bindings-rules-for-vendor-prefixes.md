---
id: "zep-rules-for-upstream-bindings-rules-for-vendor-prefixes"
type: "concept"
domain: "project"
title: "Rules for upstream bindings: Rules for vendor prefixes"
summary: "The following general rules apply to vendor prefixes in :ref:compatible <dt-important-props> properties."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/bindings-upstream.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/bindings-upstream.rst"
license: "Apache-2.0"
mode: "V"
---

The following general rules apply to vendor prefixes in :ref:`compatible
<dt-important-props>` properties.

- If your device is manufactured by a specific vendor, then its compatible
  should have a vendor prefix.

  If your binding describes hardware with a well known vendor from the list in
  `dts/bindings/vendor-prefixes.txt`, you must use that vendor
  prefix.

- If your device is not manufactured by a specific hardware vendor, do **not**
  invent a vendor prefix. Vendor prefixes are not mandatory parts of compatible
  properties, and compatibles should not include them unless they refer to an
  actual vendor. There are some exceptions to this rule, but the practice is
  strongly discouraged.

- Do not submit additions to Zephyr's `dts/bindings/vendor-prefixes.txt`
  file unless you also include users of the new prefix. This means at least a
  binding and a devicetree using the vendor prefix, and should ideally include
  a device driver handling that compatible.

  For custom bindings, you can add a custom
  `dts/bindings/vendor-prefixes.txt` file to any directory in your
  DTS_ROOT. The devicetree tooling will respect these
  prefixes, and will not generate warnings or errors if you use them in your
  own bindings or devicetrees.

- We sometimes synchronize Zephyr's vendor-prefixes.txt file with the Linux
  kernel's equivalent file; this process is exempt from the previous rule.

- If your binding is describing an abstract class of hardware with Zephyr
  specific drivers handling the nodes, it's usually best to use `zephyr` as
  the vendor prefix. See dt_vendor_zephyr for examples.

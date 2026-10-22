---
id: "zep-phandles-getting-phandles"
type: "concept"
domain: "project"
title: "Phandles: Getting phandles"
summary: "The usual way to get a phandle for a devicetree node is from one of its node labels. For example, with this devicetree:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/phandles.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/phandles.rst"
license: "Apache-2.0"
mode: "V"
---

The usual way to get a phandle for a devicetree node is from one of its node
labels. For example, with this devicetree:

```DTS

/ {
        lbl_a: node-1 {};
        lbl_b: lbl_c: node-2 {};
};
```
You can write the phandle for:

- `/node-1` as `&lbl_a`
- `/node-2` as either `&lbl_b` or `&lbl_c`

Notice how the `&nodelabel` devicetree syntax is similar to the "address of"
C syntax.

---
id: "zep-devicetree-bindings-syntax-dependency-mode"
type: "concept"
domain: "project"
title: "Devicetree bindings syntax: Properties / dependency-mode"
summary: "The dependency-mode setting controls how phandle properties are treated when calculating the dependency graph in Zephyr."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/bindings-syntax.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/bindings-syntax.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Properties_

The `dependency-mode` setting controls how phandle properties are treated when
calculating the dependency graph in Zephyr.

By default, any phandle property creates a dependency between
the node containing the property and the node it references. The `dependency-mode`
setting allows you to override this behavior.


#### Possible values


The `dependency-mode` setting accepts the following values:

`normal` or unspecified
  The default behavior. The referencing node depends on the referenced node
  (the node pointed to by the phandle).

`reverse`
  Reverses the dependency direction. Instead of the referencing node depending
  on the referenced node, the referenced node depends on the referencing node.

`ignore`
  The phandle property does not create a dependency.

`child-ignore`
  Similar to `ignore`, but the dependency is only ignored if the referenced
  node is a child of the referencing node. If the referenced node is not a child,
  a normal dependency is created.

  Use this when a phandle may reference either a child node (no dependency needed)
  or an external node (dependency required).


#### Using dependency-mode


The `dependency-mode` setting is specified within a property definition in a
binding file. Here's an example:

```YAML

compatible: "vendor,ethernet-controller"

properties:
  phy-handle:
    type: phandle
    description: |
      Specifies a reference to a node representing a PHY device.
    dependency-mode: ignore
```
Another example using `child-ignore`:

```YAML

compatible: "vendor,node-with-optional-phandle"

properties:
  optional-ref:
    type: phandle
    description: |
      References either a child node or an external device.
      Child node references create no dependency, but external
      device references do.
    dependency-mode: child-ignore
```
Example DTS using that binding:

```DTS

root {
        external_dev: external-device@2000 {
                compatible = "vendor,external-device";
                reg = <0x2000 0x100>;
        };

        parent_dev: parent-device@1000 {
                compatible = "vendor,node-with-optional-phandle";
                reg = <0x1000 0x100>;
                optional-ref = <&internal_child>; /* child: ignored dependency */

                internal_child: internal-device {
                        compatible = "vendor,internal-device";
                };
        };

        peer_dev: peer-device@3000 {
                compatible = "vendor,node-with-optional-phandle";
                reg = <0x3000 0x100>;
                optional-ref = <&external_dev>; /* external: normal dependency */
        };
};
```

#### Default behavior


If `dependency-mode` is not specified, the default value is `normal`, which
means the referencing node depends on the referenced node.

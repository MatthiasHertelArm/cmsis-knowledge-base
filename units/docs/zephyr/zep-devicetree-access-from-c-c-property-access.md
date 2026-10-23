---
id: "zep-devicetree-access-from-c-c-property-access"
type: "concept"
domain: "project"
title: "Devicetree access from C/C++: Property access"
summary: "The right API to use to read property values depends on the node and property."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/api-usage.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/api-usage.rst"
license: "Apache-2.0"
mode: "V"
---

The right API to use to read property values depends on the node and property.

- dt-checking-property-exists
- simple-properties
- reg-properties
- interrupts-properties
- phandle-properties


### Checking properties and values


You can use `DT_NODE_HAS_PROP()` to check if a node has a property. For
the example devicetree above:

```c

DT_NODE_HAS_PROP(DT_NODELABEL(i2c1), clock_frequency)  /* expands to 1 */
DT_NODE_HAS_PROP(DT_NODELABEL(i2c1), not_a_property)   /* expands to 0 */
```

### Simple properties


Use `DT_PROP(node_id, property)` to read basic integer, boolean, string,
numeric array, and string array properties.

For example, to read the `clock-frequency` property's value in the
above example:

```c

DT_PROP(DT_PATH(soc, i2c_40002000), clock_frequency)  /* This is 100000, */
DT_PROP(DT_NODELABEL(i2c1), clock_frequency)          /* and so is this, */
DT_PROP(DT_ALIAS(sensor_controller), clock_frequency) /* and this. */
```

**Important:** The DTS property `clock-frequency` is spelled `clock_frequency` in C. That is, properties also need special characters converted to underscores. Their names are also forced to lowercase.

Properties with `string` and `boolean` types work the exact same way. The
`DT_PROP()` macro expands to a string literal in the case of strings, and the
number 0 or 1 in the case of booleans. For example:

```c

#define I2C1 DT_NODELABEL(i2c1)

DT_PROP(I2C1, status)  /* expands to the string literal "okay" */
```

**Note:** Don't use DT_NODE_HAS_PROP() for boolean properties. Use DT_PROP() instead as shown above. It will expand to either 0 or 1 depending on if the property is present or absent.

Properties with type `array`, `uint8-array`, and `string-array` work
similarly, except `DT_PROP()` expands to an array initializer in these cases.
Here is an example devicetree fragment:

```devicetree

foo: foo@1234 {
        a = <1000 2000 3000>; /* array */
        b = [aa bb cc dd];    /* uint8-array */
        c = "bar", "baz";     /* string-array */
};
```
Its properties can be accessed like this:

```c

#define FOO DT_NODELABEL(foo)

int a[] = DT_PROP(FOO, a);           /* {1000, 2000, 3000} */
unsigned char b[] = DT_PROP(FOO, b); /* {0xaa, 0xbb, 0xcc, 0xdd} */
char* c[] = DT_PROP(FOO, c);         /* {"bar", "baz"} */
```
You can use `DT_PROP_LEN()` to get logical array lengths in number of
elements.

```c

size_t a_len = DT_PROP_LEN(FOO, a); /* 3 */
size_t b_len = DT_PROP_LEN(FOO, b); /* 4 */
size_t c_len = DT_PROP_LEN(FOO, c); /* 2 */
```
`DT_PROP_LEN()` cannot be used with the special `reg` or `interrupts`
properties. These have alternative macros which are described next.


### reg properties


See dt-important-props for an introduction to `reg`.

Given a node identifier `node_id`, `DT_NUM_REGS(node_id)` is the
total number of register blocks in the node's `reg` property.

You **cannot** read register block addresses and lengths with ``DT_PROP(node,
reg)``. Instead, if a node only has one register block, use
`DT_REG_ADDR` or `DT_REG_SIZE`:

- `DT_REG_ADDR(node_id)`: the given node's register block address
- `DT_REG_SIZE(node_id)`: its size

Use `DT_REG_ADDR_BY_IDX` or `DT_REG_SIZE_BY_IDX` instead if the
node has multiple register blocks:

- `DT_REG_ADDR_BY_IDX(node_id, idx)`: address of register block at index
  `idx`
- `DT_REG_SIZE_BY_IDX(node_id, idx)`: size of block at index `idx`

The `idx` argument to these must be an integer literal or a macro that
expands to one without requiring any arithmetic. In particular, `idx` cannot
be a variable. This won't work:

```c

/* This will cause a compiler error. */

for (size_t i = 0; i < DT_NUM_REGS(node_id); i++) {
        size_t addr = DT_REG_ADDR_BY_IDX(node_id, i);
}
```

### interrupts properties


See dt-important-props for a brief introduction to `interrupts`.

Given a node identifier `node_id`, `DT_NUM_IRQS(node_id)` is the total
number of interrupt specifiers in the node's `interrupts` property.

The most general purpose API macro for accessing these is
`DT_IRQ_BY_IDX`:

```c

DT_IRQ_BY_IDX(node_id, idx, val)
```
Here, `idx` is the logical index into the `interrupts` array, i.e. it is
the index of an individual interrupt specifier in the property. The `val`
argument is the name of a cell within the interrupt specifier. To use this
macro, check the bindings file for the node you are interested in to find the
`val` names.

Most Zephyr devicetree bindings have a cell named `irq`, which is the
interrupt number. You can use `DT_IRQN` as a convenient way to get a
processed view of this value.


**Warning:** Here, "processed" reflects Zephyr's devicetree dt-scripts, which change the `irq` number in zephyr.dts to handle hardware constraints on some SoCs and in accordance with Zephyr's multilevel interrupt numbering. This is currently not very well documented, and you'll need to read the scripts' source code and existing drivers for more details if you are writing a device driver.


### phandle properties



**Note:** See dt-phandles for a detailed guide to phandles.

Property values can refer to other nodes using the `&another-node` phandle
syntax introduced in dt-writing-property-values. Properties which
contain phandles have type `phandle`, `phandles`, or `phandle-array` in
their bindings. We'll call these "phandle properties" for short.

You can convert a phandle to a node identifier using `DT_PHANDLE`,
`DT_PHANDLE_BY_IDX`, or `DT_PHANDLE_BY_NAME`, depending on the
type of property you are working with.

One common use case for phandle properties is referring to other hardware in
the tree. In this case, you usually want to convert the devicetree-level
phandle to a Zephyr driver-level struct device.
See dt-get-device for ways to do that.

Another common use case is accessing specifier values in a phandle array. The
general purpose APIs for this are `DT_PHA_BY_IDX` and `DT_PHA`.
There are also hardware-specific shorthands like `DT_GPIO_CTLR_BY_IDX`,
`DT_GPIO_CTLR`,
`DT_GPIO_PIN_BY_IDX`, `DT_GPIO_PIN`,
`DT_GPIO_FLAGS_BY_IDX`, and `DT_GPIO_FLAGS`.

See `DT_PHA_HAS_CELL_AT_IDX` and `DT_PROP_HAS_IDX` for ways to
check if a specifier value is present in a phandle property.

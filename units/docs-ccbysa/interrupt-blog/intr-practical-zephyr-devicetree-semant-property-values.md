---
id: "intr-practical-zephyr-devicetree-semant-property-values"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree semantics (Part 4): Zephyr's Devicetree API / Property values"
summary: "Using the node identifiers and the property's name in the \"lowercase-and-underscores\" form, we can access the property's value using the macro DT_PROP."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-15-practical_zephyr_dt_semantics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics#property-values"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Zephyr's Devicetree API_

Using the [node identifiers](#node-identifiers) and the property's name in the "lowercase-and-underscores" form, we can access the property's value using the macro `DT_PROP`. The macro is very straight-forward since all it needs to do is paste the node ID, separated by `_P_` with the provided property name.

> **Note:** Have a look at the documentation of `DT_PROP`. You'll find that its documentation matches with what we've seen for each type in the section about [basic types](#basic-types) (only enumerations are not explicitly mentioned in `DT_PROP`'s documentation).

In `props-basics.overlay`, we defined several properties that we'll now access using the Devicetree API:

`dts/playground/props-phandles.overlay`
```dts
/ {
  label_with_props: node_with_props {
    compatible = "custom-props-basics";
    existent-boolean;
    int = <1>;
    array = <0xA second_value: 0xB 0xC>;
    uint8-array = [ 12 34  ];
    string = string_value: "foo bar baz";
    string-array = "foo", "bar", "baz";
    enum-int = <200>;
    enum-string = "whatever";
  };
};
```


#### Simple values

An unsurprising but common pattern that you'll see in Zephr modules that use the Devicetree API are structures that map to a node's properties. This is especially prominent in device drivers that use [instance-based APIs](https://docs.zephyrproject.org/latest/build/dts/api/api.html#devicetree-inst-apis), e.g., `DT_INST_PROP`.

> **Note:** Instance-based APIs are in general recommended for device drivers. For the sake of simplicity, we've only specified individual nodes and don't use multiple instances. Refer to the [official documentation](https://docs.zephyrproject.org/latest/build/dts/api/api.html#devicetree-inst-apis) for details.

The following is an overly simplified example that retrieves all one-dimensional values from `/node_with_props`. For demonstration purposes, we're passing different macros for the node's identifier:

```c
typedef struct
{
    bool boolean_exists;
    int32_t int_value;
    char *string_value;
    int32_t enum_int_value;
    char *enum_string_value;
} values_t;

const values_t values = {
    .boolean_exists    = DT_PROP(NODE_PROPS_ALIAS_BY_LABEL, existent_boolean),
    .int_value         = DT_PROP(NODE_PROPS_ALIAS_BY_PATH, int),
    .string_value      = DT_PROP(NODE_PROPS_ALIAS_BY_STRING, string),
    .enum_int_value    = DT_PROP(NODE_PROPS_CHOSEN_BY_PATH, enum_int),
    .enum_string_value = DT_PROP(NODE_PROPS_CHOSEN_BY_LABEL, enum_string),
};

printk("values = {\n");
printk("  .boolean_exists     = %d\n", values.boolean_exists);    // = 1
printk("  .int_value          = %d\n", values.int_value);         // = 1
printk("  .string_value       = %s\n", values.string_value);      // = "foo bar baz"
printk("  .enum_int_value     = %d\n", values.enum_int_value);    // = 200
printk("  .enum_string_value  = %s\n", values.enum_string_value); // = "whatever"
printk("}\n");
```

Knowing that all of the given node identifiers resolve to `DT_N_S_node_with_props`, we can easily determine the macros and thus values pasted by `DT_PROP` that we've seen in the [section about basic types](#basic-types):

- `DT_N_S_node_with_props_P_existent_boolean`
- `DT_N_S_node_with_props_P_int`
- `DT_N_S_node_with_props_P_string`
- `DT_N_S_node_with_props_P_enum_int`
- `DT_N_S_node_with_props_P_enum_string`

For our enumerations `enum-int` and `enum-string`, additional macros such as `DT_ENUM_IDX` exist to access the index of the selected value within its list of possible values. This can be useful, e.g., to avoid string comparisons in enumerations that use the type `string`.

```c
// DT_ENUM_IDX resolves to DT_N_S_node_with_props_P_enum_int_ENUM_IDX
// "The index within 'enum_int' of the selected value '200' is 1."
printk(
    "The index within 'enum_int' of the selected value '%d' is %d.\n",
    values.enum_int_value,
    DT_ENUM_IDX(NODE_PROPS_CHOSEN_AS_STRING, enum_int));

// DT_ENUM_IDX resolves to DT_N_S_node_with_props_P_enum_string_ENUM_IDX
// "The index within 'enum_string' of the selected value 'whatever' is 0."
printk(
    "The index within 'enum_string' of the selected value '%s' is %d.\n",
    values.enum_string_value,
    DT_ENUM_IDX(NODE_PROPS_CHOSEN_AS_STRING, enum_string));
```

Enumerations and strings also allow to retrieve a _token_ matching its value. Such tokens can be used, e.g., to create unique variable names during compile time. Tokens can also be used to declare structure fields (though this is mostly done using [specifier cells](#specifier-cells)). For the sake of completeness, we'll declare a variable using the `string` property's value as a token:

```c
// Resolves to DT_N_S_node_with_props_P_string_STRING_TOKEN
// and thus the variable name foo_bar_baz.
#define STRING_TOKEN DT_STRING_TOKEN(NODE_PROPS_BY_PATH, string)

uint8_t STRING_TOKEN = 0U;
STRING_TOKEN += 1U;
printk("STRING_TOKEN = %d\n", STRING_TOKEN);
```


#### Scalar values

As we've seen in the [basic types section](#basic-types), the macros for scalar types provide initializer lists and can therefore also be assigned to variable-length arrays. In addition, a `_LEN` macro is generated, accessible via the `DT_PROP_LEN`:

```c
// cell_array = {10 /* 0xa */, 11 /* 0xb */, 12 /* 0xc */};
const uint32_t cell_array[] = DT_PROP(NODE_PROPS_BY_LABEL, array);
// bytestring = {18 /* 0x12 */, 52 /* 0x34 */};
const uint8_t bytestring[]  = DT_PROP(NODE_PROPS_BY_PATH, uint8_array);

const size_t cell_array_exp_length = DT_PROP_LEN(NODE_PROPS_BY_LABEL, array);
const size_t bytestring_exp_length = DT_PROP_LEN(NODE_PROPS_BY_LABEL, uint8_array);

if ((cell_array_exp_length != (sizeof(cell_array) / sizeof(uint32_t))) ||
    (bytestring_exp_length != (sizeof(bytestring) / sizeof(uint8_t))))
{
    // This is unreachable code, since the `_LEN` macro matches the
    // number of elements in the generated initializer list.
    printk("Something's wrong!\n");
}
```

Scalar types also provide `_FOREACH` macros. These macros are expanded for each element in the scalar type during compile time and thus apply a given macro for each element. The following shows how to use the `DT_FOREACH_PROP_ELEM` macro, which in turn uses the generated macro of the corresponding property:

```c
#define PRINTK_STRING(node_id, prop, idx)                                \
    do                                                                   \
    {                                                                    \
        printk("[%d] -- %s\n", idx, DT_PROP_BY_IDX(node_id, prop, idx)); \
    } while (0);

// This expands to one printk statement for each element in /node_with_props's
// property string-array _at compile-time_.
DT_FOREACH_PROP_ELEM(NODE_PROPS_BY_LABEL, string_array, PRINTK_STRING);
// [0] -- foo
// [1] -- bar
// [2] -- baz
```

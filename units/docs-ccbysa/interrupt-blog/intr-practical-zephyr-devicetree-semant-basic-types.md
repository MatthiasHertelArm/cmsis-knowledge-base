---
id: "intr-practical-zephyr-devicetree-semant-basic-types"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree semantics (Part 4): Bindings by example / Basic types"
summary: "In the previous article, we've seen all of the types supported by devicetrees in Zephyr. We'll now use the same node, but extend it by two properties called enum-int and enum-string, since enumerations are represented differently in bindings."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-15-practical_zephyr_dt_semantics.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_dt_semantics#basic-types"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Bindings by example_

In the previous article, we've seen all of the types supported by devicetrees in Zephyr. We'll now use the same node, but extend it by two properties called `enum-int` and `enum-string`, since *enum*erations are represented differently in bindings. In the previous article, we've seen that Zephyr's Devicetree generator ignores _value_ labels. We'll throw in two of those, named `second_value` and `string_value`, for good practice, and also add the `label_with_props` for `/node_with_props`:

`dts/playground/props-basics.overlay`
```dts
/ {
  label_with_props: node_with_props {
    compatible = "custom-props-basics";
    existent-boolean;
    int = <1>;
    array = <1 second_value: 2 3>;
    uint8-array = [ 12 34 ];
    string = string_value: "foo bar baz";
    string-array = "foo", "bar", "baz";
    enum-int = <200>;
    enum-string = "whatever";
  };
};
```

Now we need to extend our binding by adding an entry for each of the node's properties under the _properties_ key:

`dts/bindings/custom-props-basics.yaml`
```yaml
description: Custom properties
compatible: "custom-props-basics"

properties:
  existent-boolean:
    type: boolean
  int:
    type: int
    required: true
  array:
    type: array
  uint8-array:
    type: uint8-array
  string:
    type: string
  string-array:
    type: string-array
  enum-int:
    type: int
    enum:
      - 100
      - 200
      - 300
  enum-string:
    type: string
    enum:
      - "whatever"
      - "works"
```

After recompiling ...

```bash
$ rm -rf ../build
$ west build --no-sysbuild --board nrf52840dk/nrf52840 --build-dir ../build -- \
  -DEXTRA_DTC_OVERLAY_FILE="dts/playground/props-basics.overlay"
```

... we can now find macros for all of our properties in `devicetree_generated.h` for the node `/node_with_props`, and the comment block also indicates which binding was selected to generate the macros.

`build/zephyr/include/generated/devicetree_generated.h`
```c
/*
 * Devicetree node: /node_with_props
 *
 * Node identifier: DT_N_S_node_with_props
 *
 * Binding (compatible = custom-props-basics):
 *   /path/to/dts/bindings/custom-props-basics.yaml
 */

/* Node's full path: */
#define DT_N_S_node_with_props_PATH "/node_with_props"
/* --snip-- */
/* Generic property macros: */
/* --snip-- */
```

Let's have a look at the generated macros listed beyond the marker _Generic property macros_.

#### `boolean`

For the property `existent-boolean` of type `boolean`, the Devicetree generator produces the following macros:

```c
#define DT_N_S_node_with_props_P_existent_boolean 1
#define DT_N_S_node_with_props_P_existent_boolean_EXISTS 1
```

Using what we've learned in the section about [understanding Devicetree macro names](#understanding-devicetree-macro-names), we can easily understand the basename `DT_N_S_node_with_props_P_existent_boolean` of the generated macros:

`DT` is the Devicetree prefix, `N` indicates that what follows is a node's path, `S` is a forward slash `/`, and finally `P` indicates the start of a property. Thus `DT_N_S_node_with_props_P_existent_boolean` essentially translates to `node=/node_with_props`, `property=existent_boolean`.

Since the `existent-boolean` property is present in the node in our overlay, its value translates to `1`. If we'd _remove_ the property from our node, we'd end up with the following:

```c
#define DT_N_S_node_with_props_P_existent_boolean 0
#define DT_N_S_node_with_props_P_existent_boolean_EXISTS 1
```

Thus, the value of *boolean*s is `0` if the property is _false_, or `1` if it is _true_.

What about `_EXISTS`? Remember that any path or property name is transformed to its _lowercase_ form in the Devicetree macros. `_EXIST` is all uppercase, which indicates that it isn't something that we defined, but a macro that is generated for use with the [Devicetree API](#zephyrs-devicetree-api).

For properties of any type but `boolean`s, Zephyr's Devicetree generator creates a matching `_EXISTS` macro _only_ if the property _exists_ in the Devicetree. If a property is not present, no macros are generated. *Boolean*s are an exception where this macro is _always_ generated since a missing property value means that the property is set to _false_.

> **Note:** In case you're wondering if it is possible to _unset_ or delete a boolean that is defined somewhere else in the Devicetree - yes it is, and we'll try it out in the section ["deleting properties"](#deleting-properties).

#### `int`

For the property `int` of type `int` of our node `/node_with_props`, Zephyr's Devicetree generator produces the following macros:

```c
#define DT_N_S_node_with_props_P_int 1
#define DT_N_S_node_with_props_P_int_EXISTS 1
```

Unsurprisingly, for properties of type `int` the value of the macro is an _integer literal_ (in decimal format). As mentioned in the [previous section](#boolean), the macro `_EXISTS` is created for every property that _exists_ in the Devicetree. If we tried to remove the property from our Devicetree node, however, we'd get the following error when rebuilding since we specified `int` as a _required_ property in our binding:

```
...
-- Found devicetree overlay: dts/playground/props-basics.overlay
devicetree error: 'int' is marked as required in 'properties:' in /path/to/dts/bindings/custom-props-basics.yaml, but does not appear in <Node /node_with_props in '/opt/nordic/ncs/v3.2.1/zephyr/misc/empty_file.c'>
```

If we'd remove `required: true` from the binding file _and_ delete the node's property in the overlay, _both_ macros would indeed be removed from `devicetree_generated.h`; any search for `N_S_node_with_props_P_int` would fail.

> **Note:** Knowing how macros work in `C`, you might be curious why Zephyr _removes_ the `_EXISTS` macro instead of defining its value to _0_. After all, without using the compile time switches `#ifdef` or `#if defined()` you can't check a macro's value if the macro is not defined - or can you? Turns out there is a neat trick that allows to do this, and Zephyr makes use of it, but we won't go into detail about this trick in this article. If you still want to know how this works, have a look at the documentation of the `IS_ENABLED` macro in `zephyr/include/zephyr/sys/util_macro.h` and the macros it expands to. It is explained nicely in the macros' documentation!

> **Note:** In case you specify the value of a node's property of type `int` in the Devicetree in the _hexadecimal_ format, at the time of writing the integer literal is converted to its _decimal_ value in `devicetree_generated.h`.

#### `array` and `uint8-array`

The following macros are produced for our `array` property of type `array`:

```c
#define DT_N_S_node_with_props_P_array {10 /* 0xa */, 11 /* 0xb */, 12 /* 0xc */}
#define DT_N_S_node_with_props_P_array_IDX_0 10
#define DT_N_S_node_with_props_P_array_IDX_0_EXISTS 1
#define DT_N_S_node_with_props_P_array_IDX_1 11
#define DT_N_S_node_with_props_P_array_IDX_1_EXISTS 1
#define DT_N_S_node_with_props_P_array_IDX_2 12
#define DT_N_S_node_with_props_P_array_IDX_2_EXISTS 1
/* array_FOREACH_ ... */
#define DT_N_S_node_with_props_P_array_LEN 3
#define DT_N_S_node_with_props_P_array_EXISTS 1
```

For properties of the type `array` and `uint8-array`, the Devicetree generator produces _initializer expressions_ in braces, whose elements are integer literals. In the [Devicetree API section](#zephyrs-devicetree-api), we'll use those expressions as, well, initialization values for our variables or constants. The macro with the suffix `_LEN` defines the number of elements in the array.

For each element and its position _n_ within the array, the generator also produces the macros `_IDX_n` and `_IDX_n_EXISTS`. In addition, several `_FOREACH` macros (hidden in the snippet) are generated that expand an expression for each element in the array _at compile time_.

For the node's `uint8-array` property with the corresponding type, a similar set of macros is generated. Only the `_FOREACH` macros are slightly different, but that doesn't concern us right now (in case you're still curious, check out the documentation of `DT_FOREACH_PROP_ELEM` in the [Zephyr's Devicetree API documentation](https://docs.zephyrproject.org/latest/build/dts/api/api.html)).

```c
#define DT_N_S_node_with_props_P_uint8_array {18 /* 0x12 */, 52 /* 0x34 */}
#define DT_N_S_node_with_props_P_uint8_array_IDX_0 18
#define DT_N_S_node_with_props_P_uint8_array_IDX_0_EXISTS 1
#define DT_N_S_node_with_props_P_uint8_array_IDX_1 52
#define DT_N_S_node_with_props_P_uint8_array_IDX_1_EXISTS 1
/* --snip-- uint8_array_FOREACH_ ... */
#define DT_N_S_node_with_props_P_uint8_array_LEN 2
#define DT_N_S_node_with_props_P_uint8_array_EXISTS 1
```

Just like for our `int` property, if we'd remove the `array` or `uint8-array` property from our node in the Devicetree, no macros (not even the `_EXISTS` macros) are generated for the property.

#### `string`

The following is a snipped of our `devicetree_generated.h` for the property `string`:

```c
#define DT_N_S_node_with_props_P_string "foo bar baz"
#define DT_N_S_node_with_props_P_string_STRING_UNQUOTED foo bar baz
#define DT_N_S_node_with_props_P_string_STRING_TOKEN foo_bar_baz
#define DT_N_S_node_with_props_P_string_STRING_UPPER_TOKEN FOO_BAR_BAZ
/* --snip-- string_FOREACH_ ... */
#define DT_N_S_node_with_props_P_string_EXISTS 1
```

For properties of the type `string`, the Devicetree generator produces _string literals_. The generator also produces macros with a special suffix:

- `_STRING_UNQUOTED` contains the string literals without quotes and thus all values as _tokens_.
- `_STRING_TOKEN` produces a single token out of the string literals. Special characters and spaces are replaced by underscores.
- `_STRING_UPPER_TOKEN` produces the same token as `_STRING_TOKEN`, but in uppercase letters.

In addition, the generator also produces `_FOREACH` macros, which expand for each _character_ in the string. E.g., for our value "foo bar baz" with the string length _11_, the `_FOREACH` macro would expand _11_ times.

> **Note:** The characters used by the token in `_STRING_TOKEN` are not converted to lowercase. If we use the value _"Foo Bar Baz"_ for `string`, the generated token would be `Foo_Bar_Baz`. Only the `_STRING_UPPER_TOKEN` is always all uppercase.

A string's value as a token can be useful, e.g., when using the token to form a `C` variable or code. It is very rarely used, though (in case you're curious, try looking for `DT_INST_STRING_TOKEN` in the Zephyr repository).

Again, no macros are generated in case the property does not exist in the Devicetree.

#### `string-array`

The following macros are produced for our `string-array` property of the same-named type:

```c
#define DT_N_S_node_with_props_P_string_array {"foo", "bar", "baz"}
#define DT_N_S_node_with_props_P_string_array_IDX_0 "foo"
#define DT_N_S_node_with_props_P_string_array_IDX_0_STRING_UNQUOTED foo
#define DT_N_S_node_with_props_P_string_array_IDX_0_STRING_TOKEN foo
#define DT_N_S_node_with_props_P_string_array_IDX_0_STRING_UPPER_TOKEN FOO
#define DT_N_S_node_with_props_P_string_array_IDX_0_EXISTS 1
/* --snip-- the same IDX_n_ macros are generated for "bar" and "baz" */
/* --snip-- string_array_FOREACH_ ... */
#define DT_N_S_node_with_props_P_string_array_LEN 3
#define DT_N_S_node_with_props_P_string_array_EXISTS 1
```

`string-array`s are handled similarly to `array` and `uint8-array`: Instead of _integer_ literals, the Devicetree generator produces _initializer expressions_ in braces whose elements are _string_ literals. The macro with the suffix `_LEN` defines the number of elements in the array.

For each element and its position _n_ within the array, the generator also produces the macros `_IDX_n` like we've seen for properties of type `string` - except that the generator won't produce `_FOREACH` macros for the characters within each string literal. Instead, several `_FOREACH` macros (hidden in the snippet) are generated that expand an expression for each element in the array _at compile time_.

No macros are generated in case the property does not exist in the Devicetree.

#### `enum`

For enumerations, the generator produces the same macros as it would for the corresponding base type, e.g., `int` or `string`, and in addition it generates `_ENUM` macros that indicate the position within the enumeration (and some more for `string`s).

For our enumeration `enum-int` with the allowed values _100_, _200_, and _300_, the generator produced the following macros for the selected value _200_:

```c
#define DT_N_S_node_with_props_P_enum_int 200
#define DT_N_S_node_with_props_P_enum_int_ENUM_IDX 1
#define DT_N_S_node_with_props_P_enum_int_EXISTS 1
```

Thus, in addition to the macros that would also have been generated if the property was a plain `int`, the generator produced an additional `_ENUM` macro indicating the index of the selected value within the enumeration.

The following is produced for `enum-string` with the allowed values _"whatever"_ and _"works"_, for the selected value _"whatever"_:

```c
#define DT_N_S_node_with_props_P_enum_string "whatever"
#define DT_N_S_node_with_props_P_enum_string_STRING_UNQUOTED whatever
#define DT_N_S_node_with_props_P_enum_string_STRING_TOKEN whatever
#define DT_N_S_node_with_props_P_enum_string_STRING_UPPER_TOKEN WHATEVER
#define DT_N_S_node_with_props_P_enum_string_ENUM_IDX 0
#define DT_N_S_node_with_props_P_enum_string_ENUM_TOKEN whatever
#define DT_N_S_node_with_props_P_enum_string_ENUM_UPPER_TOKEN WHATEVER
/* --snip-- enum_string_FOREACH_ ... */
#define DT_N_S_node_with_props_P_enum_string_EXISTS 1
```

Here, the generator produced the same macros that we'd get if `enum-string` was a plain `string` (including the character-based `_FOREACH` macros), and again we get the index of the chosen value within the enumeration. In addition, the generator produces `TOKEN` and `TOKEN_UPPER` macros with an `ENUM` prefix - to make the tokens accessible using the Devicetree API macros for enumerations.

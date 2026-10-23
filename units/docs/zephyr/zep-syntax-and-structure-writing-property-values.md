---
id: "zep-syntax-and-structure-writing-property-values"
type: "concept"
domain: "project"
title: "Syntax and structure: Writing property values"
summary: "This section describes how to write property values in DTS format. The property types in the table below are described in detail in dt-bindings."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/intro-syntax-structure.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/intro-syntax-structure.rst"
license: "Apache-2.0"
mode: "V"
---

This section describes how to write property values in DTS format. The property
types in the table below are described in detail in dt-bindings.

Some specifics are skipped in the interest of keeping things simple; if you're
curious about details, see the devicetree specification.


* - Property type
  - How to write
  - Example

* - string
  - Double quoted
  - `a-string = "hello, world!";`

* - int
  - between angle brackets (`<` and `>`)
  - `an-int = <1>;`

* - boolean
  - for `true`, with no value (for `false`, use `/delete-property/`)
  - `my-true-boolean;`

* - array
  - between angle brackets (`<` and `>`), separated by spaces
  - `foo = <0xdeadbeef 1234 0>;`

* - uint8-array
  - in hexadecimal *without* leading `0x`, between square brackets (`[` and `]`).
  - `a-byte-array = [00 01 ab];`

* - string-array
  - separated by commas
  - `a-string-array = "string one", "string two", "string three";`

* - phandle
  - between angle brackets (`<` and `>`)
  - `a-phandle = <&mynode>;`

* - phandles
  - between angle brackets (`<` and `>`), separated by spaces
  - `some-phandles = <&mynode0 &mynode1 &mynode2>;`

* - phandle-array
  - between angle brackets (`<` and `>`), separated by spaces
  - `a-phandle-array = <&mynode0 1 2>, <&mynode1 3 4>;`
Additional notes on the above:

- The values in the `phandle`, `phandles`, and `phandle-array` types are
  described further in dt-phandles

- Boolean properties are true if present. They should not have a value.
  A boolean property is only false if it is completely missing in the DTS.

- The `foo` property value above has three *cells* with values 0xdeadbeef, 1234,
  and 0, in that order. Note that hexadecimal and decimal numbers are allowed and
  can be intermixed. Since Zephyr transforms DTS to C sources, it is not
  necessary to specify the endianness of an individual cell here.

- 64-bit integers are written as two 32-bit cells in big-endian order. The value
  0xaaaa0000bbbb1111 would be written `<0xaaaa0000 0xbbbb1111>`.

- The `a-byte-array` property value is the three bytes 0x00, 0x01, and 0xab, in
  that order.

- Parentheses, arithmetic operators, and bitwise operators are allowed. The
  `bar` property contains a single cell with value 64:

```devicetree

bar = <(2 * (1 << 5))>;
```
  Note that the entire expression must be parenthesized.

- A cell whose parenthesized expression evaluates to a negative value, such as
  `<(-1)>` or `<(4 - 6)>`, is preserved as a signed value for `int` and
  `array` typed properties. Cells written as positive decimal or hexadecimal
  literals (including `0xffffffff`), or whose expression evaluates to a
  non-negative value, remain unsigned.

- Property values refer to other nodes in the devicetree by their *phandles*.
  You can write a phandle using `&foo`, where `foo` is a :ref:`node label
  <dt-node-labels>`. Here is an example devicetree fragment:

```devicetree

foo: device@0 { };
device@1 {
        sibling = <&foo 1 2>;
};
```
  The `sibling` property of node `device@1` contains three cells, in this order:

  #. The `device@0` node's phandle, which is written here as `&foo` since
     the `device@0` node has a node label `foo`
  #. The value 1
  #. The value 2

  In the devicetree, a phandle value is a cell -- which again is just a 32-bit
  unsigned int. However, the Zephyr devicetree API generally exposes these
  values as *node identifiers*. Node identifiers are covered in more detail in
  dt-from-c.

- Array and similar type property values can be split into several `<>`
  blocks, like this:

```devicetree

foo = <1 2>, <3 4>;                         // Okay for 'type: array'
foo = <&label1 &label2>, <&label3 &label4>; // Okay for 'type: phandles'
foo = <&label1 1 2>, <&label2 3 4>;         // Okay for 'type: phandle-array'
```
  This is recommended for readability when possible if the value can be
  logically grouped into blocks of sub-values.

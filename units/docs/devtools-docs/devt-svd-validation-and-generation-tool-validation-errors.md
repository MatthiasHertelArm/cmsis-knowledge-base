---
id: "devt-svd-validation-and-generation-tool-validation-errors"
type: "concept"
domain: "pack"
title: "SVD Validation and Generation Tool: Error and Warning Messages / Validation errors"
summary: "SVD Validation and Generation Tool: Error and Warning Messages / Validation errors"
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/svdconv/SVDConv/README.md#validation-errors"
license: "Apache-2.0"
mode: "V"
---

_Part of: Error and Warning Messages_

| Message Number |  Type |  Message Text |  Action|
|----------------|---------|---------------|--------|
| M201 |  ERROR |  Tag `<'TAG'>` unknown or not allowed on this level." |  Check tag|
| M202 |  ERROR |  Parse error: `<'TAG'>` = 'VALUE' |  Check tag/value.|
| M203 |  ERROR |  Value already set: `<'TAG'>` = 'VALUE' |  Check tag/value.|
| M204 |  ERROR |  Parse Error: 'VALUE' |  Check value.|
| M205 |  WARNING |  Tag `<'TAG'>` empty |  Assign value to tag.|
| M206 |  ERROR |  DerivedFrom not found: 'NAME' |  Check derivate.|
| M207 |  ERROR |  Expression marker found but no `<dim>` specified: 'NAME' |  Specify dimension.|
| M208 |  ERROR |  Ignoring `<dimIndex>` because specified `<name>` requires Array generation. |  Generate an array.|
| M209 |  WARNING |  CPU section not set. This is required for CMSIS Headerfile generation and debug support. |  Add CPU section.|
| M210 |  WARNING |  Use new Format CMSIS-SVD >= V1.1 and add `<CPU>` Section. |  Update schema and add CPU section.|
| M211 |  ERROR |  Ignoring 'LEVEL' 'NAME' (see previous message) |  |
| M212 |  ERROR |  Address Block `<usage>` parse error: 'NAME' |  Correct address block.|
| M213 |  ERROR |  Expression for 'NAME' incomplete, `<'TAG'>` missing. |  Add tag.|
| M214 |  ERROR |  Peripheral 'NAME' `<dim>` single-instantiation is not supported (use Array instead). |  Correct Regs to Reg[s].|
| M215 |  WARNING |  Size of `<dim>` is only one element for 'NAME', is this intended? |  Check single element.|
| M216 |  WARNING |  Unsupported character found in 'NAME' : 'HEX'. |  Correct name.|
| M217 |  WARNING |  Forbidden Trigraph '??CHAR' found in 'NAME'. |  |
| M218 |  WARNING |  Unsupported ESC sequence found in 'NAME' : 'CHAR'. |  Correct escape sequence.|
| M219 |  ERROR |  C Code generation error: 'MSG' |  |
| M220 |  WARNING |  C Code generation warning: 'MSG' |  |
| M221 |  WARNING |  Input filename must end with .svd: 'NAME' |  Correct input filename extension.|
| M222 |  WARNING |  Input filename has no extension: 'NAME' |  Correct input filename extension.|
| M223 |  ERROR |  Input File Name 'INFILE' does not match the tag `<name>` in the `<device>` section: 'NAME' |  Correct the MCU name.|
| M224 |  WARNING |  Deprecated: 'NAME' Use 'NAME2' instead |  Update SVD file.|
| M225 |  ERROR |  Upper/lower case error: 'NAME', should be 'NAME2'" |  Update SVD file.|
| M226 |  ERROR |  SFD Code generation error: 'MSG' |  |
| M227 |  WARNING |  SFD Code generation warning: 'MSG' |  |
| M228 |  ERROR |  Enumerated Value Container: Only one Item allowed on this Level! |  Remove additional items.|
| M229 |  ERROR |  Register 'NAME' is not an array, `<dimArrayIndex>` is not applicable |  Correct SVD.|
| M230 |  ERROR |  Value 'NAME':'NUM' out of Range for 'LEVEL' 'NAME2'['NUM2']. |  Correct SVD.|
| M231 |  ERROR |  Value `<isDefault>` not allowed for 'LEVEL'. |  Correct SVD.|
| M232 |  ERROR |  Tag `<'TAG'>` name 'NAME' must not have specifier 'CHAR'. Ignoring entry." |  Correct SVD.|
| M233 |  ERROR |  Parse error: `<'TAG'>` = 'VALUE' |  Correct SVD.|
| M234 |  ERROR |  No valid items found for 'LEVEL' 'NAME' |  Correct SVD.|
| M235 |  ERROR |  'LEVEL' 'NAME' cannot be an array. |  Correct SVD.|
| M236 |  ERROR |  Expression for `<'TAG'>` 'NAME' not allowed. |  Correct SVD.|
| M237 |  ERROR |  Nameless 'LEVEL' must have `<'TAG'>`. |  Correct SVD.|
| M238 |  ERROR |  'LEVEL' must not have `<'TAG'>`." |  Correct SVD.|
| M239 |  ERROR |  Dimed 'LEVEL' 'NAME' must have an expression. |  Correct SVD.|
| M240 |  ERROR |  Tag `<'TAG'>` unknown or not allowed on 'LEVEL2':'LEVEL'. |  Correct SVD.|
| M241 |  ERROR |  Parse Error: 'VALUE' invalid for Array generation |  Correct SVD.|
| M242 |  WARNING |  'LEVEL' 'NAME' `<dimArrayIndex>` found, but no `<dim>` |  Correct SVD.|
| M243 |  WARNING |  'LEVEL' 'NAME' `<dimArrayIndex>` found, but `<dim>` does not describe an array |  Correct SVD.|
| M249 |  ERROR |  Dimension expansion exceeds the per-input limit of 'NUM' generated indices and model copies. |  Reduce the total expanded model size.|
| M250 |  ERROR |  Dimension 'NAME' has an invalid or overflowing index/address range. |  Correct the dimension range or increment.|

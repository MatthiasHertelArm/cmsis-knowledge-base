---
id: "mbedtls-switching-to-the-new-code-style-coding-style-overview"
type: "concept"
domain: "security"
title: "Switching to the new code style: Coding style overview"
summary: "The following table summarizes the old and new coding style (before/after January 2023)."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/rewrite-branch-for-coding-style.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/rewrite-branch-for-coding-style.md#coding-style-overview"
license: "Apache-2.0"
mode: "V"
---

The following table summarizes the old and new coding style (before/after January 2023).

| Aspect | Old | New |
| ------ | --- | --- |
| Indentation | 4 spaces | 4 spaces |
| Indentation of `case` | one level deeper than `switch` | one level deeper than `switch` |
| Maximum line length | 80 preferred | 80 preferred |
| **Spacing inside parentheses** | always except `define` and casts: `if( f( x ) )` | **never**: `if (f(x))` |
| Spacing inside square brackets | no: `a[i]` | no: `a[i]` |
| **Spacing before opening parenthesis** | no: `if( f( x ) )` | **after keyword or binary operator**: `if (f(x))` |
| Spacing before opening square bracket | no: `a[i]` | no: `a[i]` |
| Spacing after unary prefix operator | optional: `!c` or `! c` | **no**: `!c` |
| Spacing around binary operator | yes: `( x + y ) * z` | yes: `(x + y) * z` |
| Parentheses around return value | mandatory: `return( x );` | **generally not**: `return x;` |
| **Single-line if/loop body** | separate line, braces optional | separate line, **braces mandatory** |
| Opening brace | on its own line | **on the same line** except for functions |

For a more detailed description of the coding style, please refer to the [coding standards](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/../development/mbedtls-coding-standards.md).

---
id: "dbgx-arm-cmsis-debugger-number-formats"
type: "concept"
domain: "debug"
title: "Arm CMSIS Debugger: Debugger User Interface / Number formats"
summary: "Expressions can be represented in different number formats. The debuggers default format is natural. If you wish to change the radix, there are multiple ways to do so:"
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@28c1601:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/28c1601/README.md#number-formats"
license: "Apache-2.0"
mode: "V"
---

_Part of: Debugger User Interface_

Expressions can be represented in different number formats. The debuggers default format is `natural`. If you wish to
change the radix, there are multiple ways to do so:

- To change it globally, right-click for example in an editor window and select **Set Global Output Radix to ...**.
  This allows you to switch the global radix between `decimal` and `hexadecimal`.
- To change the radix of a single expression, you can edit it for example in the
  [**Live Watch**](#trace-and-live-view) or [**WATCH**](#watch) view. Then, add a "`,`"
  to the expression, directly followed by one of these format specifiers (make sure no space is between the `,` and the
  format specifier):

| Specifier | Format |
|-----------|--------|
| `x` | `hexadecimal` |
| `d` | `decimal` |
| `o` | `octal` |
| `t` or `b` | `binary` |
| `z` | `zero-hexadecimal` (includes leading zeros) |

- You can also use this syntax in the [**DEBUG CONSOLE**](#debug-console).

#### Examples

```txt
counter,d
value,o
number,t
```

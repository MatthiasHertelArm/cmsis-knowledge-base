---
id: "dbgx-arm-cmsis-debugger-debug-console"
type: "concept"
domain: "debug"
title: "Arm CMSIS Debugger: Debugger User Interface / Debug Console"
summary: "The Debug Console enables viewing and interacting with the output of your code running in the debugger. Expressions can be evaluated with the Debug Console REPL (Read-Eval-Print Loop) feature."
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@12cb62a:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/README.md#debug-console"
license: "Apache-2.0"
mode: "V"
---

_Part of: Debugger User Interface_

The **Debug Console** enables viewing and interacting with the output of your code running in the debugger.
Expressions can
be evaluated with the **Debug Console REPL** (Read-Eval-Print Loop) feature.

With the CMSIS Debug extension, you can use the Debug Console REPL to enter
[GDB commands](https://sourceware.org/gdb/current/onlinedocs/gdb.html/index.html) while debugging. Before entering
a GDB command, you have to explicitly enter a "greater-than"-character `>` so that the following strings can be
evaluated as a GDB command.

Debug Console input uses the mode of the active editor, which means that it supports syntax coloring, indentation, auto
closing of quotes and other language features.

<!-- markdownlint-disable-next-line MD036 -->
**Example**

The following example shows how to check the currently set breakpoints with the `> info break` command. Afterwards, the
application is run with the `> continue` command.

(figure: Entering GDB commands in the Debug Console REPL)

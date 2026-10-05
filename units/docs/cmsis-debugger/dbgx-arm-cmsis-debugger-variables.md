---
id: "dbgx-arm-cmsis-debugger-variables"
type: "concept"
domain: "debug"
title: "Arm CMSIS Debugger: Debugger User Interface / VARIABLES"
summary: "During debugging, you can inspect variables, expressions, and registers in the VARIABLES section of the Run and Debug view or by hovering over a variable or expression in the source code editor."
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@28c1601:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/28c1601/README.md#variables"
license: "Apache-2.0"
mode: "V"
---

_Part of: Debugger User Interface_

During debugging, you can inspect variables, expressions, and registers in the **VARIABLES** section of the **Run and Debug view** or by hovering over a variable or expression in the source code editor. Variable values and expressions are evaluated in the context of the selected stack frame in the [**CALL STACK**](#call-stack) section. In the case of multi-core, the content is relative to the active debug session.

(figure: VARIABLES section)

To change the value of a variable during the debugging session, right-click on the variable in the **VARIABLES** section and select **Set Value**.

You can use the **Copy Value action** to copy the variable's value, or the **Copy as Expression action** to copy an
expression to access the variable. You can then use this expression in the [**WATCH**](#watch) section.

To filter variables by their name or value, use the Alt/Opt + Ctrl/Cmd + F keyboard shortcut while the focus is on the
**VARIABLES section**, and type a search term.

(figure: Searching in VARIABLES section)

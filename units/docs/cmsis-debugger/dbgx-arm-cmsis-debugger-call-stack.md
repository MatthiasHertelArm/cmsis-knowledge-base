---
id: "dbgx-arm-cmsis-debugger-call-stack"
type: "concept"
domain: "debug"
title: "Arm CMSIS Debugger: Debugger User Interface / CALL STACK"
summary: "The CALL STACK section shows the function call tree that is currently on the stack. Threads are shown for applications that use an RTOS."
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@12cb62a:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/12cb62a/README.md#call-stack"
license: "Apache-2.0"
mode: "V"
---

_Part of: Debugger User Interface_

The **CALL STACK** section shows the function call tree that is currently on the stack. Threads are shown for applications
that use an RTOS. Each function call is associated to its location and when source code is available a _line number badge_ is shown. A click on this badge navigates to source file location.

The window content is updated whenever program execution stops.

(figure: CALL STACK section)

---
id: "dbgx-arm-cmsis-debugger-breakpoints"
type: "concept"
domain: "debug"
title: "Arm CMSIS Debugger: Debugger User Interface / BREAKPOINTS"
summary: "A breakpoint pauses the code execution at a specific point, so you can inspect the state of your application at that point. There are several breakpoint types."
status: "draft"
collection: "cmsis-debugger"
source: "Open-CMSIS-Pack/vscode-cmsis-debugger@28c1601:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger/blob/28c1601/README.md#breakpoints"
license: "Apache-2.0"
mode: "V"
---

_Part of: Debugger User Interface_

A breakpoint pauses the code execution at a specific point, so you can inspect the state of your
application at that point. There are several breakpoint types.

#### Setting breakpoints

To set or unset a breakpoint, click on the editor margin or use **F9** on the current line.

- Breakpoints in the editor margin are normally shown as red-filled circles.
- Disabled breakpoints have a filled grey circle.
- When a debugging session starts, breakpoints that can't be registered with the debugger change to a grey hollow
circle. The same might happen if the source is edited while a debug session without live-edit support is running.

(figure: Breakpoint in the editor margin)

For more control of breakpoints, use the **BREAKPOINTS** section that lists and manages all breakpoints.

(figure: BREAKPOINTS section)

> &#128221; **Note:**
>
> You can set breakpoints anytime during your debug session. However, when setting a breakpoint while running an
> application, the target stops for a short period of time.

#### Breakpoint types

Apart from the code breakpoint, there are other breakpoint types to satisfy specific use cases.

##### Function breakpoints

Instead of placing breakpoints directly in source code, a debugger can support creating breakpoints by specifying
a function name. This is useful in situations where the source is not available but a function name is known.

To create a function breakpoint, select the + button in the **BREAKPOINTS section** header and enter the function
name. Function breakpoints are shown with a red triangle in the **BREAKPOINTS section**.

##### Conditional breakpoints

Set breakpoint conditions based on expressions, hit counts, or a combination of both.

- Expression condition: The breakpoint is hit whenever the expression evaluates to true.
- Hit count: The hit count controls how many times a breakpoint needs to be hit before it interrupts execution.
- Wait for breakpoint: The breakpoint is activated when another breakpoint is hit ([triggered breakpoint](#triggered-breakpoints)).

To add a conditional breakpoint:

- Create a conditional breakpoint

    - Right-click in the editor margin and select Add Conditional Breakpoint.
    - Use the Add Conditional Breakpoint command in the Command Palette (⇧⌘P).

- Choose the type of condition you want to set (expression, hit count, or wait for a breakpoint).

(figure: Creating a conditional breakpoint)

To add a condition to an existing breakpoint:

- Edit an existing breakpoint

    - Right-click on the breakpoint in the editor margin and select Edit Breakpoint.
    - Select the pencil icon next for an existing breakpoint in the **BREAKPOINTS section** of the **Run and Debug view**.

- Edit the condition (expression, hit count, or wait for breakpoint).

> &#128221; **Note:**
>
> For checking the the breakpoint condition, the target is halted for a short period of time.

##### Data breakpoints

Data breakpoints can be set from the context menu of a variable in the **WATCH section**. The Break on Value
Change/Read/Access commands add a data breakpoint that is hit when the value of the underlying variable changes/is
read/is accessed. Data breakpoints are shown with a red hexagon in the **BREAKPOINTS section** and the type of
breakpoint is shown (Write/Read/Access).

(figure: Creating a data breakpoint)

> &#128221; **Note:**
>
> When hitting a data breakpoint, the program execution does not stop exactly on that line of code. Depending on the
> underlying CPU architecture, stopping can be delayed by up to 5 cycles. Use the
> [Call Stack](#call-stack) view to determine what caused the execution to stop.

##### Triggered breakpoints

A triggered breakpoint is type of conditional breakpoint that is enabled once another breakpoint is hit. They can
be useful when diagnosing failure cases in code that happen only after a certain precondition.

Triggered breakpoints can be set by right-clicking on the glyph margin, selecting **Add Triggered Breakpoint**, and
then, choose which other breakpoint enables the breakpoint.

(figure: Creating a triggered breakpoint)

<!--
##### Inline breakpoints

Inline breakpoints are only hit when the execution reaches the column associated with the inline breakpoint.
This is useful when debugging minified code, which contains multiple statements in a single line.

An inline breakpoint can be set using **Shift + F9** or through the context menu during a debug session.
Inline breakpoints are shown inline in the editor.

Inline breakpoints can also have conditions. Editing multiple breakpoints on a line is possible through the
context menu in the editor's left margin.
-->

##### Logpoints

A logpoint pauses the program execution for a short period of time, sends a message to the debug console, and then
continues with the application. Logpoints can help you save time by not having to add or remove logging statements in
your code.

A logpoint is represented by a diamond-shaped icon. Log messages are plain text, but can also include expressions to be
evaluated within curly braces (`{}`).

To add a logpoint, right-click in the editor left margin and select Add Logpoint, or use the
**Debug: Add Logpoint...** command in the Command Palette (**Ctrl/Cmd + Shift + p**).

(figure: Creating a logpoint)

Just like regular breakpoints, logpoints can be enabled or disabled and can also be controlled by a condition
and/or hit count.

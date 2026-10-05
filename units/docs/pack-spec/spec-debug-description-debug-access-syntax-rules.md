---
id: "spec-debug-description-debug-access-syntax-rules"
type: "concept"
domain: "pack"
title: "Debug Description: Writing debug access sequences / Debug access syntax rules"
summary: "Part of: Writing debug access sequences"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/debug_description.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html"
license: "Apache-2.0"
mode: "V"
---

_Part of: Writing debug access sequences_

Debug accesses are described in **block** elements (within a debug access **sequence** or **control** element).
The following syntax is used for this purpose:
- One or more statements have to be encapsulated in a **block** element.
- Each statement must begin in a new line and is terminated by a `;` character.
- A typical statement consists of variable, followed by a `=` character and an expression, where the
`=` character is an assignment of the expression result to the variable:
```
variable = expression;
```
- Alternatively, a statement can be a sole expression without storing its result
to a variable.
```
expression;
```
- Comments begin with two slashes (`//`) and end with a line break:
```
// Whole line is a comment
variable = expression;  // Comment appended to statement
```
- Variables must be defined using the keyword `__var`. The definition must include an initialization
  of the variable:
```
__var variable = 0;
```
- Variables can be defined only once within a scope. Scopes begin with entering a debug access
  sequence or a **control** element. They are extended to child **control** elements.
  Variables of a parent scope can be modified. Leaving a scope destroys all variables defined in it.

  ****block** elements do not begin a new scope.**
```
<sequence name="MySequence">
  
  <block info="Block 1">
    __var condvar = 1;
    __var myvar1  = 5;
    __var myvar2  = 0;
  </block>
  
  <control if="condvar">
    <block>
      // __var myvar1 = 2;      // Redefinition, not allowed!
      __var myvar3 = 2;
      myvar2 = myvar1 + myvar3; // Assign value (5+2) = 7
    </block>
  </control>
  
  <block info="Block 2">
    myvar1 = myvar2 + 1;  // Variable myvar1 holds the value '8' after this statement
    // myvar2 = myvar3;   // myvar3 does not exist in this scope, not allowed!
  </block>
  
</sequence>
```
- The debug access variables **__dp**, **__ap**, **__apid**, and **__errorcontrol** can be modified
  within a debug access sequence. An assigned value is held until leaving the sequence. Calling
  another sequence by the **Sequence** debug access function will push their values on a
  sequence execution stack. The values are restored when returning from such a call.
- The debug access variable **__Result** can be modified within a debug access sequence.
  Its value is held until the debug access sequence returns to the debugger. Hence its value is
  **not** pushed on a sequence execution stack when calling into another sequence by the **Sequence**
  debug access function.
- If the debug description contains access port elements
 - then the debug access variable **__ap** must **not** be used. Use **__apid** instead.
 - then the debug access variable **__dp** is only used for the **ReadDP()**, **WriteDP()**, and **DAP_WriteABORT()** debug access
   functions. All other debug access functions use the access port element that is referenced by **__apid** to determine the used debug port.

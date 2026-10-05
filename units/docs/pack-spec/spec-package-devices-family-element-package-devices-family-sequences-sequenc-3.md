---
id: "spec-package-devices-family-element-package-devices-family-sequences-sequenc-3"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../sequences/sequence/block"
summary: "Describes a block of debug accesses. See Debug Access Syntax Rules for details on the allowed syntax of the block contents."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Describes a block of debug accesses. See Debug Access Syntax Rules
for details on the allowed syntax of the block contents.

**Example**
```
<family Dfamily="Generic Family" Dvendor="Generic:5">
  ...
  <sequences>
    ...
    <sequence name="UserSequence">
      ...
      <block info="Define condition variales for later use in block elements.">
        // Variable definition by __var keyword
        __var doIfBlock      = 1;
        __var whileCondition = 1;
      </block>
      ...
    </sequence>
    ...
  </sequences>
  ...
</family>
```


 		



  | 
    Parents | 
    Element Chain | 
  

  | 
    sequence | 
    element_sequence | 
  

  | 
    control | 
    element_seq_control | 
  

  | 
    Attribute | 
    Description | 
    Type | 
    Use | 
  

  | 
    atomic | 
    
      Instruct the debugger to execute the block contents atomically; a debugger needs to
      download and buffer all debug accesses to the debug probe and finish the
      execution without further communication to the host PC. If a debugger cannot
      support an atomic block it must abort the execution of the debug access sequence.

       | 
    xs:boolean | 
    optional | 
  

  | 
    info | 
    Descriptive text to display for example for error diagnostics. | 
    xs:string | 
    optional | 
  



**Atomic Blocks:**
- Within an atomic block a variable must no longer be used as an r-value after a result from a target access has been assigned to it.
- Support for atomic blocks is highly debugger dependent. Keep them as short and simple as possible
to address a wide range of debuggers.
- **Query** and **Sequence** debug access functions must not be used in an atomic block.


 


**Debug Access Syntax Rules**

Debug accesses are described in **block** elements of a debug access sequence (**sequence** element).
The following syntax is used for this purpose:
- The contents of a **block** element is a series of statements.
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
- Comments begin with two slashes (`//`) and end with a linebreak:
```
// Whole line is a comment
variable = expression;  // Comment appended to statement
```
- Variables must be defined using the keyword `__var`. The definition must include an initalization
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
- Please refer to Debug Access Functions for how to use **__dp**, **__ap**,
  and **__apid** to select access ports for target accesses.
- The debug access variable **__Result** can be modified within a debug access sequence.
  Its value is held until the debug access sequence returns to the debugger. Hence its value is
  **not** pushed on a sequence execution stack when calling into another sequence by the **Sequence**
  debug access function.



**Expression Rules**

Expressions are used in various places to describe one of the following:
- A value as assigned in a debug access statement.
- A condition to use in the **if** attribute of a **control** element.
- A condition to use in the **while** attribute of a **control** element.
- A parameter to a debug access function as described below.

An expression may consist of the following:
- Constant numbers in decimal and hexadecimal representation (prefix `0x`).
- Arithmetic operators such as `+`, `-`, `*`, `/`, and `%`.
- Bit-arithmetic operators such as `&`, `|`, `~`, `^`, `>>`, and `<<`.
- Comparison-operators such as `==`, `!=`, `<`, `>`, `<=`, and `>=`.
- Logic operators such as `!`, `&&`, `||`, and `==`.
- Conditional expression operations like: \code (x < y) ? a : b \endcode
- Precedence of sub-expressions is indicated by brackets (`(`, `)`). C-like precedence applies 
  if brackets are omitted.
- References to debug access variables for evaluating debug settings.
- Calls to debug access functions.

**Note:**
- All values used in expressions resolve to 64-bit unsigned integer values.
- All logic-operations and comparisons resolve to the value `1` if true, to `0` otherwise.
- XML prohibits the use of the characters `&`, `<`, and `>`. Use the corresponding
  XML entity names instead: `&amp;amp;`, `&amp;lt;`, and `&amp;gt;`.

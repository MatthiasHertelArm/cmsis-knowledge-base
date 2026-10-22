---
id: "view-expressions-operators"
type: "concept"
domain: "trace"
title: "Expressions: Operators"
summary: "Operators combine and compare operands. Operators may be unary (requiring one operand) or binary (requiring two operands). The combination of an operator and its operands is an expression."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

Operators combine and compare operands. Operators may be unary (requiring one operand) or binary (requiring two operands).
The combination of an operator and its operands is an expression. Parentheses can be used in expressions with multiple
operators to specify the order of evaluation. If no parentheses are used in an expression, then the operator precedence
determines the evaluation order.

 Operators                          | Precedence | Description
------------------------------------|:----------:|---------------------------------------------------
 ( )                                |     1      | Parentheses can be used to specify the order of evaluation
 _.member_                     |     2      | Type member
 **typedef_name:member:enum**       |     2      | Enumerator value; refer to `<enum>`
 **typedef_name:member**            |     2      | Type-member selector for use in __Offset_of intrinsic; refer to `<member>`
 Unary +, Unary —             |     3      | Unary plus or minus applied to the following operand 
 \* / %                             |     4      | Multiplication, Division, or Modulo
 +  —                         |     5      | Addition, Subtraction
 <<  >>                             |     6      | Shift left, Shift right
 & \| ^                             |     7      | Binary AND, OR, XOR
 == != > >= < <=                    |     8      | Comparisons
 && \|\|                            |     9      | Logical AND, OR
 e ? e : e                          |    10      | Conditional operator
 = \|= &= ^= += -= *= /= %=         |    11      | Assignment operators

**Note:**
 - Because the character **&** is reserved in XML, it is required for logical operations to use **\&** instead.
 - Use **\"** whenever this quote is not part of an XML structure.

**Code** **Examples**
```
<item property="Wait" cond="TCB[i].p_blnk &amp;&amp; TCB[i].State == Thread_CB:State:WaitingSemaphore" value="%S[TCB[i].p_blnk]" />
 
<item property="Round Robin Timeout"                         value="%T[((float) (rrobin &amp; 0xFFFF) * (float) clockrate / 1000)] mSec" />
 
<item property="__Symbol_exists (&quot;os_active_TCB&quot;)" value="%t[__Symbol_exists (&quot;os_active_TCB&quot;) ? &quot;Yes&quot; : &quot;No&quot;]" />
```

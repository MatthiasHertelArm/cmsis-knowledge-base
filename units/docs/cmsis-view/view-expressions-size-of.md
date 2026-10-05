---
id: "view-expressions-size-of"
type: "concept"
domain: "trace"
title: "Expressions: __size_of"
summary: "Number of elements of an array defined by a symbol in user application - symbol_name: Reference to a symbol (examples: \"main\", \"os_active_TCB\", \"tasks.c/xSchedulerRunning\"). Returns: number of elements of an array defined in a user application"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

```
int32_t __size_of (symbol_name)
```
    Number of elements of an array defined by a symbol in user application
- `symbol_name`:       Reference to a symbol (examples: "main", "os_active_TCB", "tasks.c/xSchedulerRunning").
Returns:  number of elements of an array defined in a user application

The function searches for a debug symbol in the loaded user application. 
If the symbol is found it returns the number of elements of an array that is addressed by this symbol.
If the symbol is not found, an error message is displayed.

**Example:**

User application code (file MyTest.c):
```
struct {
  unsigned char   c0;
  unsigned char   c1;
  unsigned int     i;
} MyList [20];

static int MyVar[10];  
```

The following statements in the SCVD file output the number of elements of each variable. For 'MyList' the value is 20.  The value 20 for 'MyVar' is only displayed when the variable exists.

```
  <out name="MyTest">
    <item property="Elements of 'MyList'"   value="%d[__size_of(&quot;MyList&quot;)]"/>
    <item cond="__Symbol_exists(&quot;MyTest.c/MyVar&quot;)"  property="Elements of 'MyVar'"    value="%d[__size_of(&quot;MyTest.c/MyVar&quot;)]"/>
  </out>
```

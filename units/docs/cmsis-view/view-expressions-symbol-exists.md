---
id: "view-expressions-symbol-exists"
type: "concept"
domain: "trace"
title: "Expressions: __Symbol_exists"
summary: "Search for symbol - symbolname: Reference to a symbol (examples: \"main\", \"osactiveTCB\", \"tasks.c/xSchedulerRunning\"). Returns: - 1 for true - symbol present in user application - 0 for false - symbol not found"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

```
int32_t __Symbol_exists (symbol_name)
```
    Search for symbol
- `symbol_name`:       Reference to a symbol (examples: "main", "os_active_TCB", "tasks.c/xSchedulerRunning").
Returns:  
          - `1` for true - symbol present in user application
          - `0` for false - symbol not found

The function searches for a debug symbol in the loaded user application. 

 and returns `1` when the symbol was found, otherwise `0` for false.

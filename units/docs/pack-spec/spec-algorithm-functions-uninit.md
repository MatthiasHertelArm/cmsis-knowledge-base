---
id: "spec-algorithm-functions-uninit"
type: "concept"
domain: "pack"
title: "Algorithm Functions: UnInit"
summary: "The function UnInit de-initializes the microcontroller and is invoked at the end of an erasing, programming, or verifying step."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/flash_algorithms.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/algorithmFunc.html"
license: "Apache-2.0"
mode: "V"
---

```
int UnInit (unsigned long fnc);
```
- `fnc`: Function code
Returns: status information:
        - 0 on success.
        - 1 on failure.


The function **UnInit** de-initializes the microcontroller and is invoked at the end of an erasing, programming, or verifying
step.

The argument _fnc_ is a number:
- 1 stands for Erase.
- 2 stands for Program.
- 3 stands for Verify.

Thus, different de-initialization sections can be implemented for each individual Flash programming step.

**Code Example**
```
int UnInit (unsigned long fnc) {
 
  // Lock Flash
  FLASH->CR |=  FLASH_LOCK;
 
  return (0);
}
```

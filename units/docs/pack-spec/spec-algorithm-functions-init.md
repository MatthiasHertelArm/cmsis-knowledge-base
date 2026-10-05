---
id: "spec-algorithm-functions-init"
type: "concept"
domain: "pack"
title: "Algorithm Functions: Init"
summary: "The function Init initializes the microcontroller for Flash programming. It is invoked whenever an attempt is made to download the program to Flash."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/flash_algorithms.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/algorithmFunc.html"
license: "Apache-2.0"
mode: "V"
---

```
int Init (unsigned long adr, unsigned long clk, unsigned long fnc);
```
- `adr`: Device base address
- `clk`: Clock frequency (Hz)
- `fnc`: Function code
Returns: status information:
        - 0 on success.
        - 1 on failure.


The function **Init** initializes the microcontroller for Flash programming. It is invoked whenever an attempt is made to
download the program to Flash.

The argument _adr_ specifies the base address of the device.

The argument _clk_ specifies the clock frequency for prgramming the device.

The argument _fnc_ is a number:
- 1 stands for Erase.
- 2 stands for Program.
- 3 stands for Verify.

Thus, different initialization sections can be implemented for each individual Flash programming step.

**Code Example**
```
int Init (unsigned long adr, unsigned long clk, unsigned long fnc) {
 
  // Zero Wait State
  FLASH->ACR  = 0x00000000;
 
  // Unlock Flash
  FLASH->KEYR = FLASH_KEY1;
  FLASH->KEYR = FLASH_KEY2;
 
  // Test if IWDG is running (IWDG in HW mode)
  if ((FLASH->OBR & 0x04) == 0x00) {
    // Set IWDG time out to ~32.768 second
    IWDG->KR  = 0x5555; // Enable write access to IWDG_PR and IWDG_RLR
    IWDG->PR  = 0x06;   // Set prescaler to 256
    IWDG->RLR = 4095;   // Set reload value to 4095
  }
 
  return (0);
}
```

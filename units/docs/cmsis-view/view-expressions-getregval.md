---
id: "view-expressions-getregval"
type: "concept"
domain: "trace"
title: "Expressions: __GetRegVal"
summary: "GetRegVal | Read the value of processor register from the target processor."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/ref_scvd.txt"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/ref_scvd.txt"
license: "Apache-2.0"
mode: "V"
---

__GetRegVal     | Read the value of processor register from the target processor.


```
uint32_t __GetRegVal (char * RegisterName)
```
    Read CPU register value
- `RegisterName`:       Pointer to the name of a CPU register: "PSP", "MSP", ....
Returns:                     Value of the CPU register

The function reads the value of a CPU register.
 
 Register Name | Description
---------------|-------------------------------------------------------------
 R0 - R12      | General-purpose registers
 R13           | Stack pointer (SP)
 R14           | Link Register (LR)
 R15           | Program Counter (PC)
 XPSR          | Combined Program Status Register
 MSP           | Main Stack Pointer 
 PSP           | Process Stack Pointer
 BASEPRI       | Base Priority Mask Register
 PRIMASK       | Exception Mask Register
 FAULTMASK     | Fault Mask Register
 CONTROL       | Control Register
 
Domain specifier `x` is required on ARMv8-M architecture for some registers to specify
Non-Secure (`x=NS`) or Secure (`x=S`) access domain. Names of these registers then
become as follows:
 
 Register Name       | Description
---------------------|-------------------------------------------------------------
 MSP_`x`       | Main Stack Pointer 
 PSP_`x`       | Process Stack Pointer
 MSPLIM_`x`    | Main Stack Pointer Limit Register
 PSPLIM_`x`    | Process Stack Pointer Limit Register
 BASEPRI_`x`   | Base Priority Mask Register
 PRIMASK_`x`   | Exception Mask Register
 FAULTMASK_`x` | Fault Mask Register
 CONTROL_`x`   | Control Register 
 
**Example:**
```
  <objects>
    <object name="CPU Registers">
      <var name="R0"   type="uint32_t" value="0"/> 
      <var name="R1"   type="uint32_t" value="0"/> 
      <var name="R2"   type="uint32_t" value="0"/> 
      <var name="R3"   type="uint32_t" value="0"/> 
      <var name="XPSR" type="uint32_t" value="0"/> 
      
      <!-- ARMv8M registers -->
      <var name="PSP_NS"      type="uint32_t" value="0"/> 
      <var name="PSP_S"       type="uint32_t" value="0"/> 
      
      <!-- Read registers -->
      <calc>
        R0  = __GetRegVal ("R0");
        R1  = __GetRegVal ("R1");
        R2  = __GetRegVal ("R2");
        R3  = __GetRegVal ("R3");
        XPSR = __GetRegVal ("XPSR");
      </calc>
      
      <calc cond="NonSecure">
        PSP_NS = __GetRegVal ("PSP_NS");
      </calc>
      
      <calc cond="Secure">
        PSP_S = __GetRegVal ("PSP_S");
      </calc>
      
    </object>
  </objects>
```

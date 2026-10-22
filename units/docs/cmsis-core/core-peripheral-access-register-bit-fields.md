---
id: "core-peripheral-access-register-bit-fields"
type: "concept"
domain: "core"
title: "Peripheral Access: Register Bit Fields"
summary: "For Core Register, macros define the position and the mask value for a bit field. It is recommended to create such definitions also for other peripheral registers."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_peripheral.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_peripheral.txt"
license: "Apache-2.0"
mode: "V"
---

For Core Register, macros define the position and the mask value for a bit field. It is recommended to create such definitions also
for other peripheral registers.

**Example:**

Bit field definitions for register CPUID in SCB (System Control Block).


```
/* SCB CPUID Register Definitions */
#define SCB_CPUID_IMPLEMENTER_Pos      24U                                       /*!< SCB CPUID: IMPLEMENTER Position */
#define SCB_CPUID_IMPLEMENTER_Msk      (0xFFUL << SCB_CPUID_IMPLEMENTER_Pos)     /*!< SCB CPUID: IMPLEMENTER Mask */
                                                                                 
#define SCB_CPUID_VARIANT_Pos          20U                                       /*!< SCB CPUID: VARIANT Position */
#define SCB_CPUID_VARIANT_Msk          (0xFUL << SCB_CPUID_VARIANT_Pos)          /*!< SCB CPUID: VARIANT Mask */
                                                                                 
#define SCB_CPUID_ARCHITECTURE_Pos     16U                                       /*!< SCB CPUID: ARCHITECTURE Position */
#define SCB_CPUID_ARCHITECTURE_Msk     (0xFUL << SCB_CPUID_ARCHITECTURE_Pos)     /*!< SCB CPUID: ARCHITECTURE Mask */
                                                                                 
#define SCB_CPUID_PARTNO_Pos            4U                                       /*!< SCB CPUID: PARTNO Position */
#define SCB_CPUID_PARTNO_Msk           (0xFFFUL << SCB_CPUID_PARTNO_Pos)         /*!< SCB CPUID: PARTNO Mask */
                                                                                 
#define SCB_CPUID_REVISION_Pos          0U                                       /*!< SCB CPUID: REVISION Position */
#define SCB_CPUID_REVISION_Msk         (0xFUL /*<< SCB_CPUID_REVISION_Pos*/)     /*!< SCB CPUID: REVISION Mask */
```

The macros **_VAL2FLD(field, value)** and **_FLD2VAL(field, value)** enable access to bit fields.


### _VAL2FLD

```c
_VAL2FLD(field, value)
```

- `field`:        name of bit field.
- `value`:        value for the bit field. This parameter is interpreted as an uint32_t type.
 Mask and shift a bit field value for assigning the result to a peripheral register.

The macro _VAL2FLD uses the \#define's __Pos_ and __Msk_ of the related bit field to shift bit-field values for
assigning to a register.
 
**Example:**
```
  SCB->CPUID = _VAL2FLD(SCB_CPUID_REVISION, 0x3) | _VAL2FLD(SCB_CPUID_VARIANT, 0x3);
```


 

### _FLD2VAL

```c
_FLD2VAL(field, value)
```

- `field`:        name of bit field.
- `value`:        value of the register. This parameter is interpreted as an uint32_t type.
 Extract from a peripheral register value the a bit field value.

The macro _FLD2VAL uses the \#define's __Pos_ and __Msk_ of the related bit field to extract the value of a bit field from a register.
 
**Example:**
```
  id = _FLD2VAL(SCB_CPUID_REVISION, SCB->CPUID);
```

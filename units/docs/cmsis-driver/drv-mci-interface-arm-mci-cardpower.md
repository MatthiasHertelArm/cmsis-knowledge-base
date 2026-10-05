---
id: "drv-mci-interface-arm-mci-cardpower"
type: "concept"
domain: "drivers"
title: "MCI Interface: ARM_MCI_CardPower"
summary: "The function ARMMCICardPower operates the memory card power supply voltage."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_MCI_CardPower (uint32_t voltage)
```


The function **ARM_MCI_CardPower** operates the memory card power supply voltage. 

The parameter **voltage** sets the voltage. Not every voltage might be supported by the driver implementation.
The structure ARM_MCI_CAPABILITIES encodes the supported voltage. Retrieve the information with the function ARM_MCI_GetCapabilities and
verify the data fields.

The following values:

Parameter **voltage**                 | Description                   | supported when ARM_MCI_CAPABILITIES
:-------------------------------------|:------------------------------|-----------------------------------------
ARM_MCI_POWER_VDD_OFF            | VDD (VCC) turned off          | _always supported_
ARM_MCI_POWER_VDD_3V3            | VDD (VCC) = `3.3V`      | data field **vdd** = `1`
ARM_MCI_POWER_VDD_1V8            | VDD (VCC) = `1.8V`      | data field **vdd_1v8** = `1` 
ARM_MCI_POWER_VCCQ_OFF           | eMMC VCCQ turned off          | _always supported_
ARM_MCI_POWER_VCCQ_3V3           | eMMC VCCQ = `3.3V`      | data field **vccq** = `1`
ARM_MCI_POWER_VCCQ_1V8           | eMMC VCCQ = `1.8V`      | data field **vccq_1v8** = `1`
ARM_MCI_POWER_VCCQ_1V2           | eMMC VCCQ = `1.2V`      | data field **vccq_1v2** = `1`

******************************************************************************************************************

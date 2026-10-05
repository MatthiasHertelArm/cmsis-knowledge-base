---
id: "drv-ethernet-mac-interface-arm-eth-mac-controltimer"
type: "concept"
domain: "drivers"
title: "Ethernet MAC Interface: ARM_ETH_MAC_ControlTimer"
summary: "The function ARMETHMACControlTimer controls the timer required for PTP (Precision Time Protocol)."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_ETH_MAC_ControlTimer (uint32_t control, ARM_ETH_MAC_TIME *time)
```


The function **ARM_ETH_MAC_ControlTimer** controls the timer required for PTP (Precision Time Protocol).

The parameter **control** receives **ARM_ETH_MAC_TIMER_xxx** codes to manage the timer for a PTP enabled Ethernet MAC interface. \n
The parameter **time** is pointer to a structure that holds time information.

Mode Parameters: Timer Controls         | Description
:---------------------------------------|:--------------------------------------------
ARM_ETH_MAC_TIMER_GET_TIME         | Retrieve the current time and update the content ARM_ETH_MAC_TIME *time.
ARM_ETH_MAC_TIMER_SET_TIME         | Set the new time using the values provided with ARM_ETH_MAC_TIME *time.
ARM_ETH_MAC_TIMER_INC_TIME         | Increment the current time by using the values provided with ARM_ETH_MAC_TIME *time.
ARM_ETH_MAC_TIMER_DEC_TIME         | Decrement the current time by using the values provided with ARM_ETH_MAC_TIME *time.
ARM_ETH_MAC_TIMER_SET_ALARM        | Set the alarm time to the values provided with ARM_ETH_MAC_TIME *time.  
ARM_ETH_MAC_TIMER_ADJUST_CLOCK     | Set the clock frequency; the value in time->ns is the **correction factor** in fractional format q31.

******************************************************************************************************************

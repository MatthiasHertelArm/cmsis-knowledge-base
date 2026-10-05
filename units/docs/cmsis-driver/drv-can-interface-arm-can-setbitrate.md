---
id: "drv-can-interface-arm-can-setbitrate"
type: "concept"
domain: "drivers"
title: "CAN Interface: Remote Frame / ARM_CAN_SetBitrate"
summary: "The function ARM_CAN_SetBitrate sets the CAN communication bit rate."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: Remote Frame_

```c
int32_t ARM_CAN_SetBitrate (ARM_CAN_BITRATE_SELECT select, uint32_t bitrate, uint32_t bit_segments)
```

  
The function **ARM_CAN_SetBitrate** sets the CAN communication bit rate.

The parameter **select** selects the bit rate affected by function call as defined in ARM_CAN_BITRATE_SELECT and listed in the table below.

Parameter **select**                         | CAN Mode Bit Rate
:--------------------------------------------|:------------------------------
ARM_CAN_BITRATE_NOMINAL                 | Select nominal (flexible data-rate arbitration) bitrate (CAN 2.0B)
ARM_CAN_BITRATE_FD_DATA                 | Select flexible data-rate data bitrate (CAN_FD)

The parameter **bitrate** is the bit rate for the selected CAN mode.

The parameter **bit_segments** is used to setup the time quanta for sampling (see picture below).
The values listed in the table below are ORed and specify the various sampling segments.
The CAN controller samples each bit on the bus at the _Sample Point_.



| Parameter **bit_segments | Bit | for **select** = ARM_CAN_BITRATE_NOMINAL \n (CAN specification) | for **select** = ARM_CAN_BITRATE_NOMINAL \n (CAN FD specification) | for **select** = ARM_CAN_BITRATE_FD_DATA \n (CAN FD specification) |  |
|---|---|---|---|---|---|
| ARM_CAN_BIT_PROP_SEG( x ) \n Propagation Time Segment \n (PROP_SEG) | 0..7 | **x** = `[1..8]` | **x** = `[1..32] or more` | **x** = `[0..8]` |  |
| ARM_CAN_BIT_PHASE_SEG1( x ) \n Phase Buffer Segment 1 \n (PHASE_SEG1) | 8..15 | **x** = `[1..8]` | **x** = `[1..32] or more` | **x** = `[1..8]` |  |
| ARM_CAN_BIT_PHASE_SEG2( x ) \n Phase Buffer Segment 2 \n (PHASE_SEG2) | 16..23 | **x** = `[1..8]` | **x** = `[1..32] or more` | **x** = `[1..8]` | The maximum allowed value is `x = MAX (PHASE_SEG1, IPT)`. IPT = Information Processing Time. Usually, IPT = `2`. Exceptions apply. Read the specifications of your CAN controller. |
| ARM_CAN_BIT_SJW( x ) \n (Re-)Synchronization Jump Width \n (SJW). | 24..31 | **x** = `[1..4]` | **x** = `[1..4]` | **x** = `[1..4]` | The maximum allowed value is `x = MIN (MIN (PHASE_SEG1, PHASE_SEG2), 4)`. SJW is not allowed to be greater than either PHASE segment. |





The picture shows a Nominal Bit Time with 10 time quanta.
  "CAN Bit Timing"


The time quanta (N) per bit is:
```
  N = 1 + PROP_SEG + PHASE_SEG1 + PHASE_SEG2; // note SYNC_SEG is always 1
```

The driver uses this value and the CAN clock to calculate a suitable prescaler value (P).
If the driver cannot achieve the requested **bitrate** it returns with ARM_CAN_INVALID_BITRATE.
The formula for the **bitrate** is:
```
  bitrate = (CAN_Clock / P) / N;
```

**Example**:
```
status = ptrCAN->SetBitrate    (ARM_CAN_BITRATE_NOMINAL,              // Set nominal bitrate
                                125000U,                              // Set bitrate to 125 kbit/s
                                ARM_CAN_BIT_PROP_SEG(5U)   |          // Set propagation segment to 5 time quanta
                                ARM_CAN_BIT_PHASE_SEG1(1U) |          // Set phase segment 1 to 1 time quantum (sample point at 87.5% of bit time)
                                ARM_CAN_BIT_PHASE_SEG2(1U) |          // Set phase segment 2 to 1 time quantum (total bit is 8 time quanta long)
                                ARM_CAN_BIT_SJW(1U));                 // Resynchronization jump width is same as phase segment 2
```

In this example, N = 8 and with a CAN_Clock = 8MHz the prescaler (P) is calculated by the driver to 8.
*************************************************************************************************************************

---
id: "abi-semihosting-for-aarch32-and-aarch6-sys-clock-0x10"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting operations / `SYS_CLOCK (0x10)`"
summary: "Returns the number of centiseconds (hundredths of a second) since the execution started."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Semihosting operations_

Returns the number of centiseconds (hundredths of a second) since the execution started.

Values returned can be of limited use for some benchmarking purposes because of communication overhead or other agent-specific factors. For example, with a debug hardware unit the request is passed back to the host for execution. This can lead to unpredictable delays in transmission and process scheduling.

Use this function to calculate time intervals, by calculating differences between intervals with and without the code sequence to be timed.


#### Entry


The PARAMETER REGISTER must contain 0. There are no other parameters.


#### Return


On exit, the RETURN REGISTER contains:

* The number of centiseconds since some arbitrary start point, if the call is successful.

* –1 if the call is not successful. For example, because of a communications error.

- SYS_ELAPSED (0X30)

- SYS_TICKFREQ (0x31)

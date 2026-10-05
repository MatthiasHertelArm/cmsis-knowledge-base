---
id: "abi-semihosting-for-aarch32-and-aarch6-sys-time-0x11"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting operations / `SYS_TIME (0x11)`"
summary: "Returns the number of seconds since 00:00 January 1, 1970."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Semihosting operations_

Returns the number of seconds since 00:00 January 1, 1970.

This value is real-world time, regardless of any debug agent configuration.

The returned value should be interpreted as unsigned. There is no
representation for times before 1970. On 32-bit implementations, this
allows times after the year 2038 to be represented, by using values
greater than `0x80000000`.


#### Entry


There are no parameters.


#### Return


On exit, the RETURN REGISTER contains the number of seconds.

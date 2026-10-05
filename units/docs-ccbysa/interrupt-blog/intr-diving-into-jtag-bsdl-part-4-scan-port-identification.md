---
id: "intr-diving-into-jtag-bsdl-part-4-scan-port-identification"
type: "concept"
domain: "debug"
title: "Diving into JTAG — BSDL (Part 4): Scan Port Identification"
summary: "The scan port identification statements define the device's TAP. For example:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-29-diving-into-jtag-part-4.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-4#scan-port-identification"
license: "CC-BY-SA-4.0"
mode: "V"
---

The scan port identification statements define the device's TAP. For example:

```plaintext
attribute TAP_SCAN_CLOCK of TCK : signal is (10.0e6, BOTH);
attribute TAP_SCAN_IN of TDI : signal is TRUE;
attribute TAP_SCAN_OUT of TDO : signal is TRUE;
attribute TAP_SCAN_MODE of TMS : signal is TRUE;
```

`TAP_SCAN_CLOCK`, `TAP_SCAN_IN`, `TAP_SCAN_OUT`, and `TAP_SCAN_MODE` are
constants defining standard JTAG signals. `TCK`, `TDI`, `TDO`, `TMS` are the
port names defined in the **Pin Mapping(s)** section for a particular chip. The
value `TRUE` indicates active use of this port.

Additionally, the `TAP_SCAN_CLOCK` attribute specifies the maximum frequency of
the clock signal, in this example it is 10 MHz and that the signal is active on
both clock edges (rising and falling). Only the `BOTH` parameter is used for the
clock signal, but in general the following parameters can also be used for
signals: `RISING` or `FALLING`.

---
id: "view-eventlist-utility-usage-example"
type: "concept"
domain: "trace"
title: "eventlist Utility: Usage example"
summary: "eventlist functionality can be easily tested with the example project scvd_evt_stat."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Documentation/Doxygen/src/eventlist.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Documentation/Doxygen/src/eventlist.md#usage-example"
license: "Apache-2.0"
mode: "V"
---

eventlist functionality can be easily tested with the example project scvd_evt_stat.

Build and run the example. Then in the terminal run `eventlist -s EventRecorder.log` to obtain the following human readable output:

```text
   Start/Stop event statistic
   --------------------------

Event count      total       min         max         average     first       last
----- -----      -----       ---         ---         -------     -----       ----
A(0)  10000    31.44509s    1.69997ms   3.80041ms   3.14451ms   3.29962ms   3.59964ms
      Min: Start: 31.94980000 val1=0x000001f5, val2=0x00000000 Stop: 31.95149997 val1=0x10004d43, val2=0x0000003c
      Max: Start: 84.70757283 val1=0x000003a5, val2=0x00000000 Stop: 84.71137324 val1=0x10004d43, val2=0x00000038

A(15) 10000   169.75100s    2.49964ms  42.78648s   16.97510ms   3.99995ms   4.30004ms
      Min: Start: 81.87697318 val1=0x000001f8, val2=0x00000000 Stop: 81.87947282 val1=0x10004d43, val2=0x0000003c
      Max: Start: 37.41299154 val1=0x0000032f, val2=0x00000000 Stop: 80.19947314 val1=0x10004d43, val2=0x0000003c

B(0)  10000    10.83677s    0.00000s  169.29161ms   1.08368ms   1.60016ms   1.00010ms
      Min: Start: 1.76679986 val1=0x10004d43, val2=0x0000005c Stop: 1.76679986 val1=0x0000018e, val2=0x00000047
      Max: Start: 37.24369993 val1=0x10004d43, val2=0x0000005c Stop: 37.41299154 val1=0x000066bf, val2=0x00000487

C(0)      1   180.67372s  180.67372s  180.67372s  180.67372s  180.67372s  180.67372s
      Min: Start: 0.00000000 val1=0x10004d43, val2=0x00000057 Stop: 180.67371888 val1=0x10004d43, val2=0x00000062
      Max: Start: 0.00000000 val1=0x10004d43, val2=0x00000057 Stop: 180.67371888 val1=0x10004d43, val2=0x00000062
```

The output can be improved with extra context as explained in the next section.

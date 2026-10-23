---
id: "view-cmsis-view-readme-analyze-events"
type: "concept"
domain: "trace"
title: "cmsis-view README: Analyze Events"
summary: "This file can be analyzed using the eventlist utility with the following command:"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Examples/EventStatistic/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Examples/EventStatistic/README.md#analyze-events"
license: "Apache-2.0"
mode: "V"
---

This file can be analyzed using the `eventlist` utility with the following command:

```bash
eventlist -s EventRecorder.log

   Start/Stop event statistic
   --------------------------

Event count      total       min         max         average     first       last
----- -----      -----       ---         ---         -------     -----       ----
A(0)   1000     3.15054s    1.79081ms   3.84733ms   3.15054ms   3.28370ms   2.54044ms
      Min: Start: 1.06694371 val1=0x000001f5, val2=0x00000000 Stop: 1.06873452 val1=0x10004e5d, val2=0x0000003c
      Max: Start: 0.57401429 val1=0x000003d3, val2=0x00000000 Stop: 0.57786162 val1=0x10004e5d, val2=0x00000038

A(15)  1000     4.14074s    2.51858ms   5.83115ms   4.14074ms   4.01147ms   3.26821ms
      Min: Start: 1.06621594 val1=0x000001f5, val2=0x00000000 Stop: 1.06873452 val1=0x10004e5d, val2=0x0000003c
      Max: Start: 1.83631161 val1=0x000003e8, val2=0x00000000 Stop: 1.84214276 val1=0x10004e5d, val2=0x0000003c

B(0)   1000     1.02458s    9.44000µs   1.70736ms   1.02458ms   1.57731ms 707.89000µs
      Min: Start: 1.93540476 val1=0x10004e5d, val2=0x0000005c Stop: 1.93541420 val1=0x00000004, val2=0x00000003
      Max: Start: 3.49351979 val1=0x10004e5d, val2=0x0000005c Stop: 3.49522715 val1=0x00007fe5, val2=0x0000053d

C(0)      1     5.17924s    5.17924s    5.17924s    5.17924s    5.17924s    5.17924s
      Min: Start: 0.00001219 val1=0x10004e5d, val2=0x00000057 Stop: 5.17925291 val1=0x10004e5d, val2=0x00000067
      Max: Start: 0.00001219 val1=0x10004e5d, val2=0x00000057 Stop: 5.17925291 val1=0x10004e5d, val2=0x00000067
```

When adding the AXF file and the [SCVD file](https://arm-software.github.io/CMSIS-View/main/SCVD_Format.html) to the `eventlist`
command the context of the program is shown

```bash
eventlist -a out/EventStatistic/AVH/Debug/EventStatistic.axf -I $CMSIS_PACK_ROOT/ARM/CMSIS-View/1.0.0/EventRecorder/EventRecorder.scvd EventRecorder.log

  :

 5391 5.17525179 EvCtrl    StartAv(15)             v1=617 v2=0
 5392 5.17597956 EvCtrl    StartAv(0)              v1=617 v2=0
 5393 5.17852000 EvCtrl    StopA(15)               File=./EventStatistic/main.c(60)
 5394 5.17852488 EvCtrl    StartB(0)               File=./EventStatistic/main.c(92)
 5395 5.17923277 EvCtrl    StopBv(0)               v1=8659 v2=553
 5396 5.17925291 EvCtrl    StopC(0)                File=./EventStatistic/main.c(103)

   Start/Stop event statistic
   --------------------------

Event count      total       min         max         average     first       last
----- -----      -----       ---         ---         -------     -----       ----
A(0)   1000     3.15054s    1.79081ms   3.84733ms   3.15054ms   3.28370ms   2.54044ms
      Min: Start: 1.06694371 v1=501 v2=0 Stop: 1.06873452 File=./EventStatistic/main.c(60)
      Max: Start: 0.57401429 v1=979 v2=0 Stop: 0.57786162 File=./EventStatistic/main.c(56)

A(15)  1000     4.14074s    2.51858ms   5.83115ms   4.14074ms   4.01147ms   3.26821ms
      Min: Start: 1.06621594 v1=501 v2=0 Stop: 1.06873452 File=./EventStatistic/main.c(60)
      Max: Start: 1.83631161 v1=1000 v2=0 Stop: 1.84214276 File=./EventStatistic/main.c(60)

B(0)   1000     1.02458s    9.44000µs   1.70736ms   1.02458ms   1.57731ms 707.89000µs
      Min: Start: 1.93540476 File=./EventStatistic/main.c(92) Stop: 1.93541420 v1=4 v2=3
      Max: Start: 3.49351979 File=./EventStatistic/main.c(92) Stop: 3.49522715 v1=32741 v2=1341

C(0)      1     5.17924s    5.17924s    5.17924s    5.17924s    5.17924s    5.17924s
      Min: Start: 0.00001219 File=./EventStatistic/main.c(87) Stop: 5.17925291 File=./EventStatistic/main.c(103)
      Max: Start: 0.00001219 File=./EventStatistic/main.c(87) Stop: 5.17925291 File=./EventStatistic/main.c(103)
```

When using **Windows Command Prompt** use the following command:

```shell
eventlist -a out/EventStatistic/AVH/Debug/EventStatistic.axf -I %CMSIS_PACK_ROOT%/ARM/CMSIS-View/1.2.0/EventRecorder/EventRecorder.scvd EventRecorder.log
```

> **Note**  
> If `CMSIS-View v1.2.0` pack is not installed, in the previous command replace the corresponding path with the path of the latest installed pack
> (for example replace `%CMSIS_PACK_ROOT%/ARM/CMSIS-View/1.2.0/EventRecorder/` with `%CMSIS_PACK_ROOT%/ARM/CMSIS-View/1.2.1/EventRecorder/`)

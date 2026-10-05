---
id: "helium-introduction-fvp-avh-ipx-model-tarmac-trace-post-proc"
type: "concept"
domain: "optimization"
title: "Introduction: FVP/AVH/IPX model TARMAC Trace post-processing"
summary: "Most of the ARM simulation platforms support TARMAC execution trace generation which is a text time-annotated execution trace containing among others, instruction flow, memory accesses, register and flags update."
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:Performance_analysis/ml-dsp-front-end-optimization-with-helium.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/Performance_analysis/ml-dsp-front-end-optimization-with-helium.md#fvp-avh-ipx-model-tarmac-trace-post-processing"
license: "Apache-2.0"
mode: "V"
---

Most of the ARM simulation platforms support TARMAC execution trace
generation which is a text time-annotated execution trace containing
among others, instruction flow, memory accesses, register and flags
update.

FVP and AVH support generation of TARMAC trace via a dedicated TARMAC
plugin

[https://developer.arm.com/documentation/100964/1122/Plug-ins-for-Fast-Models/TARMACTrace](https://developer.arm.com/documentation/100964/1122/Plug-ins-for-Fast-Models/TarmacTrace)


*Note*: TARMAC plugin for the AVH/FVP models is part of the deliverable of the avh-fvp artifacts starting with version *11.22.39* (e.g. https://artifacts.keil.arm.com/avh/11.22.39/)



As an example:

```
VHT_MPS3_Corstone_SSE-300 -f config_sse300.txt VHT-Corstone-300/Release/audiomark_app.axf --plugin TARMACTrace.so -C TRACE.TarmacTrace.trace-file=audiomark_sse300.tarmac
```

Different trace filtering options are available to limit tracing scope.

*Note*: AVH platforms are **not cycle accurate**, but can still be used for an
initial crude complexity repartition.

Example of AVH TARMAC log content when execting Audiomark ABF:

```
72319080000 ps cpu0 R r8 200276e0
72319080000 ps cpu0 R cpsr 01000000
72319080000 ps cpu0 R VPR 0000ffff
72319080000 ps cpu0 R EXCEPTION_PC ffffffff
72319160000 ps cpu0 IT (1807979) 0006e1b4 f00fc809 T thread : LE LR, \#-0x9
72319160000 ps cpu0 R r14 00000040
72319200000 ps cpu0 IT (1807980) 0006e1a6 fe206f60 T thread : VQADD.U32 Q3, Q0, R0
72319200000 ps cpu0 R cpsr 01002000
72319200000 ps cpu0 R s12 4
72319200000 ps cpu0 R s13 5
72319200000 ps cpu0 R VPR 0000ffff
72319200000 ps cpu0 R EXCEPTION_PC 0006e1a6
72319200000 ps cpu0 R cpsr 01000000
72319200000 ps cpu0 R s14 6
72319200000 ps cpu0 R s15 7
72319200000 ps cpu0 R VPR 0000ffff
72319200000 ps cpu0 R EXCEPTION_PC ffffffff
72319280000 ps cpu0 IT (1807982) 0006e1aa 3004 T thread : ADDS r0,#4
72319280000 ps cpu0 R r0 8
72319280000 ps cpu0 R cpsr 01000000
72319320000 ps cpu0 IT (1807983) 0006e1ac fe630f87 T thread : VPT.U32 HI, Q1, Q3
72319320000 ps cpu0 R cpsr 01002000
72319320000 ps cpu0 R VPR 0008ffff
72319320000 ps cpu0 R EXCEPTION_PC 0006e1ac
72319360000 ps cpu0 IT (1807984) 0006e1b0 eca85f04 T thread : VSTRWT.32 Q2, \[R8\], \#0x10
```


Running ML application with TARMAC enabled all the time will
significantly slow down the simulation and is likely to generate
gigantic trace files. The entire Audiomark runs several Billions of
instructions, so it is wiser to capture only a few occurrences,
especially as the process is periodic.

If there is a need to capture processing peaks which could occur a long
time after boot period, it might be interesting to delay TARMAC capture
using the TRACE.TarmacTrace.start-instruction-count option

(Default is to trace from the beginning)

Cycle models and RTL simulators do support native TARMAC generation
support. Cloud simulations like IP explorer which allow to run RTL
simulations provide such tracing feature which can easily be enabled
though the graphical interface.

<https://www.arm.com/products/ip-explorer>

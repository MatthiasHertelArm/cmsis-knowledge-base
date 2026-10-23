---
id: "tfm-scheduling-for-a-hybrid-platform-s-system-architecture"
type: "concept"
domain: "security"
title: "Scheduling for a Hybrid Platform Solution: System Architecture"
summary: "A Hybrid Platform is a system topology where there is an instance of SPE and one or multiple instances of NSPE running at the same time."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/multi-cpu/hybrid_platform_solution.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/multi-cpu/hybrid_platform_solution.html#system-architecture"
license: "BSD-3-Clause"
mode: "V"
---

A Hybrid Platform is a system topology where there is an instance of SPE and one
or multiple instances of NSPE running at the same time.

A common layout is:

```output

    ┌──────────────────┐cpuN    ┌──────────────────┐cpu0
  ┌──────────────────┐cpu2      │┌────────────────┐│
┌──────────────────┐cpu1        ││                ││
│                  │ │ │        ││                ││
│                  │ │ │        ││      TF-M      ││
│                  │ │ │        ││      (SPE)     ││
│                  │ │ │        ││                ││
│                  │ │ │        │└────────────────┘│
│                  │ │ │        │                  │
│                  │ │ │ >MBOX< │ --TZ boundary--- │
│                  │ │ │        │                  │
│                  │ │ │        │┌────────────────┐│
│                  │ │ │        ││                ││
│  remote client   │ │ │        ││  local client  ││
│                  │ │ │        ││     (NSPE)     ││
│                  │ │ │        │└────────────────┘│
│                  │ │─┘        └──────────────────┘
│                  │─┘
└──────────────────┘
```
where `local client` refers to the NSPE running on the same core of SPE, while
`remote client` refers to the other instance(s) of NSPE running on other
separate cores (irrespective of whether, or not, the same type of core).

Typically, a Hybrid Platform would fall into two categories:

+---------------+--------------------------------------------------------------+
| Topology      | Description                                                  |
+===============+==============================================================+
| Heterogeneous | M-Class processor running TF-M and secure services.          |
| topology      |                                                              |
|               | Non-secure applications running in both the Normal World of  |
|               | the M-Class and in one or more other (non M-class) different |
|               | cores.                                                       |
+---------------+--------------------------------------------------------------+
| Homogeneous   | M-Class processor running TF-M and secure services.          |
| topology      |                                                              |
|               | Non-secure applications running in both the Normal World of  |
|               | the M-Class and in one or more other identical M-Class cores.|
+---------------+--------------------------------------------------------------+
| Remark:                                                                      |
| When the M-Class core hosting the Secure World does NOT have a Normal World, |
| then the solution is known as "Dual-CPU" System.                             |
+------------------------------------------------------------------------------+

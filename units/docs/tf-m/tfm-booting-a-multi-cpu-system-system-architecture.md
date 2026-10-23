---
id: "tfm-booting-a-multi-cpu-system-system-architecture"
type: "concept"
domain: "security"
title: "Booting a Multi CPU System: System Architecture"
summary: "There are many possibly ways to design a multi cpu system. Some important considerations from a boot perspective are:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/multi-cpu/booting_a_multi_cpu_system.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/multi-cpu/booting_a_multi_cpu_system.html#system-architecture"
license: "BSD-3-Clause"
mode: "V"
---

There are many possibly ways to design a multi cpu system. Some important
considerations from a boot perspective are:

- Which core has access to which areas of Flash?

    - It is possible that the secure core has no access to the Flash from which
      the non-secure core will boot, in which case the non-secure core will
      presumably have a separate root of trust and perform its own integrity
      checks on boot.

- How does the non-secure core behave on power-up? Is it held in reset,
  does it jump to a set address, …?

- What are the performance characteristics of the two core?

    - There could be a great disparity in performance


**Note:** Concept for multi-cpu are extended in the Hybrid Platform section.

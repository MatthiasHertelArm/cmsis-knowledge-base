---
id: "avh-user-benefits-continuous-testing"
type: "concept"
domain: "test"
title: "User Benefits: Continuous Testing"
summary: "Applying continuous integration work flows for embedded applications can be complicated by the specifics of development environments and the need of executing the program on target hardware."
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:DoxyGen/overview/src/benefits.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/overview/src/benefits.md#continuous-testing"
license: "Apache-2.0"
mode: "V"
---

Applying continuous integration work flows for embedded applications can be complicated by the specifics of development
environments and the need of executing the program on target hardware. Development teams are often reluctant to spend
initial effort setting up the continuous integration (CI) workflow even though the long-term benefits are undisputed as
shown on the figure below.

(figure: Comparison of test efforts in CI and no CI workflows)

[Arm FVP Infrastructure](https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/overview/src/../../infrastructure/html/index.html) with integration in tools such as Keil MDK and GitHub
Actions simplifies setup of CI workflows.

For unit and integration tests, virtual targets offer additional advantages over hardware, including:

- **Speed** - no overhead for flashing the application on physical hardware. This saves time on small and fast unit
  tests.
- **Scale** - virtual platforms can scale to run many tests in parallel. This makes virtual platforms more
  cost-effective than a farm of physical hardware.
- **Maintenance** – unlike physical hardware, virtual platforms do not overheat, wear out from overuse, break from
  misuse, or use physical space and resources.
- **Upgrades** – virtual platforms can be adapted and re-configured to match corresponding changes to the underlying
  hardware platform that is under development. These types of changes can be costly or impossible with physical
  hardware.

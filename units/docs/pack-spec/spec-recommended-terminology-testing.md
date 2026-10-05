---
id: "spec-recommended-terminology-testing"
type: "concept"
domain: "pack"
title: "Recommended terminology: Testing"
summary: "There are two major ways of categorising tests :"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doc/Glossary.md"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/Glossary.html"
license: "Apache-2.0"
mode: "V"
---

There are two major ways of categorising tests :

- By scope:
  - **Unit tests**
    Covers a specific piece of software isolating it from its environment for example by mocking its dependencies.
    In the case of Internal peripheral drivers that means mocking/simulating the hardware's behaviour and/or memory map.
  - **Integration tests**
    Verifies that multiple components can work together in the expected way.
  - [**System tests**](https://en.wikipedia.org/wiki/System_testing)
    Verifies that the components work together as expected and that the whole system also behaves as defined.
- By test objectives:
  - [**Functional tests**](https://en.wikipedia.org/wiki/Functional_testing)
  - [**API tests**](https://en.wikipedia.org/wiki/API_testing)
  - [**Stress tests**](https://en.wikipedia.org/wiki/Stress_testing)
  - **Memory tests**
    Checks the absence of leaks and buffer overflow.

The following terms are generally accepted and listed here as reminders :

- [**Acceptance test**](https://en.wikipedia.org/wiki/Acceptance_testing)
  Tests against design document(s) or specification(s).
- **Regression test**
  Tests that are repeatable and used to catch regressions as the code base evolves.
- **Test framework**
  Library used to help implement a test, e.g. CppUTest
- **Test harness**
  Combination of the Test framework and test data that allow automation of the tests.
- **Test infrastructure**
  Describes the environment where the tests are run. This includes CI and the required HW and SW tools down to the HW Platform boundaries.
- **Test tool**
  Includes the software tools as well as the physical tools such as the FPGA test shield.

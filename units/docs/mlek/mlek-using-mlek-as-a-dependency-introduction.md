---
id: "mlek-using-mlek-as-a-dependency-introduction"
type: "concept"
domain: "edge-ai"
title: "Using MLEK as a dependency: Introduction"
summary: "It may be desirable to wrap ML-Embedded-Evaluation-Kit (MLEK) as a source dependency to use the example pipelines."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/mlek_as_a_dependency.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/mlek_as_a_dependency.md#introduction"
license: "Apache-2.0"
mode: "V"
---

It may be desirable to wrap ML-Embedded-Evaluation-Kit (MLEK) as a source dependency to use the example pipelines.
The use cases have [reusable ML use-case libraries](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/../../source/lib/mlek/use_case/readme.md) that can be used as
a stand-alone CMake project, be consumed in CMSIS-Pack form, or pulled in as a [Zephyr module](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/../../source/lib/ports/zephyr/zephyr.md).
However, there may be scenarios where other parts of this project are required as dependencies. This guide provides
some general recommendations on wrapping MLEK sources.

Other useful readings:
* [Repository Structure](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/../../docs/documentation.md#repository-structure)
* [Reusable Software](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/../../README.md#reusable-software).
* [Zephyr port](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/../../source/lib/ports/zephyr/zephyr.md) if you want to consume MLEK libraries as a Zephyr module.

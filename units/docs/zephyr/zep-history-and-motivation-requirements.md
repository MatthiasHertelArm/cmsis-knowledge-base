---
id: "zep-history-and-motivation-requirements"
type: "concept"
domain: "project"
title: "History and Motivation: Requirements"
summary: "Although the motivation behind splitting the Zephyr codebase into multiple repositories is outside of the scope of this page, the fundamental requirements, along with a clear justification of the choice not to use existing tools and instead develop …"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/why.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/why.rst"
license: "Apache-2.0"
mode: "V"
---

Although the motivation behind splitting the Zephyr codebase into multiple
repositories is outside of the scope of this page, the fundamental requirements,
along with a clear justification of the choice not to use existing tools and
instead develop a new one, do belong here.

The basic requirements are:

* **R1**: Keep externally maintained code in separately maintained repositories
  outside of the main zephyr repository, without requiring users to manually
  clone each of the external repositories
* **R2**: Provide a tool that both Zephyr users and distributors can make use of
  to benefit from and extend
* **R3**: Allow users and downstream distributions to override or remove
  repositories without having to make changes to the zephyr repository
* **R4**: Support both continuous tracking and commit-based (bisectable) project
  updating

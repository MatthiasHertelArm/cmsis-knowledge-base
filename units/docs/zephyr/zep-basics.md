---
id: "zep-basics"
type: "concept"
domain: "project"
title: "Basics"
summary: "This page introduces west's basic concepts and provides references to further reading."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/basics.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/basics.rst"
license: "Apache-2.0"
mode: "V"
---

This page introduces west's basic concepts and provides references to further
reading.

West's built-in commands allow you to work with `projects <west project>`
(Git repositories) under a common `workspace <west workspace>` directory.

West works in the following manner: the `west init` command creates the
`west workspace`, and clones the :term:`manifest repo <west manifest
repository>`, while the `west update` command initially clones, and later updates, the
`projects <west project>` listed in the manifest in the workspace.

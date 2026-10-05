---
id: "pyocd-python-api"
type: "concept"
domain: "debug"
title: "python api"
summary: "Using pyOCD's Python API, you have extreme flexibility and precise control, and can do anything SWD allows, at the expense of more complexity compared to pyocd commander."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/python_api.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/python_api.md"
license: "Apache-2.0"
mode: "V"
---

Using pyOCD's Python API, you have extreme flexibility and precise control, and can do anything
SWD allows, at the expense of more complexity compared to `pyocd commander`. Using pyOCD like this is
particularly useful for situations where other debuggers become ineffective, such as device and
board bringup, or automated testing.

This document assumes familiarity with the Arm CoreSight debug architecture.

See the [architecture]({% link _docs/api/architecture.md %}) documentation for an overview of the classes and how
they are connected.

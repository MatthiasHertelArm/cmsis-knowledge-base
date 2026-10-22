---
id: "devt-ctrace-architecture-test-architecture"
type: "concept"
domain: "trace"
title: "ctrace Architecture: Test architecture"
summary: "Unit tests under test/unit/src mirror the production modules. Shared file, event, and diagnostic helpers live under test/unit/support. One CTest entry runs the complete GoogleTest executable and writes its XML report."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/ctrace/docs/architecture.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/architecture.md#test-architecture"
license: "Apache-2.0"
mode: "V"
---

Unit tests under `test/unit/src` mirror the production modules. Shared file, event, and diagnostic helpers live under
`test/unit/support`. One CTest entry runs the complete GoogleTest executable and writes its XML report.

Executable-level coverage and fixture ownership are documented next to the
[integration tests](https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/../test/integration/README.md) and [test data](https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/../test/data/README.md).

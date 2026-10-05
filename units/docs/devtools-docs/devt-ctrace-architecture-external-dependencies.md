---
id: "devt-ctrace-architecture-external-dependencies"
type: "concept"
domain: "trace"
title: "ctrace Architecture: External dependencies"
summary: "cxxopts provides command-line parsing, yaml-cpp is confined to the trace-run reader, OpenCSD is isolated behind the decode adapters, and GoogleTest is used only by test targets. Babeltrace and Trace Compass are acceptance consumers, not linked runtime dependencies."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/ctrace/docs/architecture.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/architecture.md#external-dependencies"
license: "Apache-2.0"
mode: "V"
---

`cxxopts` provides command-line parsing, `yaml-cpp` is confined to the trace-run reader, OpenCSD is isolated behind
the decode adapters, and GoogleTest is used only by test targets. Babeltrace and Trace Compass are acceptance
consumers, not linked runtime dependencies. Exact revisions, licenses, and build configuration for the packaged
dependencies are documented in the [third-party notices](https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/THIRD_PARTY_NOTICES.md).

The ITM adapter currently uses OpenCSD `common/` and `interfaces/` headers because the public OpenCSD 1.8.3 boundary
does not provide equivalent access: its installed headers omit the ITM configuration and packet types required by the
decoder callbacks, and its C API exposes only the last structured error rather than all errors from one data-path
operation. Moving the adapter to the public API therefore also requires resolving these two gaps.

A known decoder defect and its proposed upstream fix are recorded in the [OpenCSD issue notes](https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/opencsd-issues.md).

---
id: "devt-ctrace-architecture-build-and-ci-structure"
type: "concept"
domain: "trace"
title: "ctrace Architecture: Build and CI structure"
summary: "The source tree has seven static library targets: ctrace-model, ctrace-cli, ctrace-trace-run, ctrace-diagnostics, ctrace-decode, ctrace-output, and ctrace-control. Their ctrace:: aliases expose the shorter module names inside CMake."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/ctrace/docs/architecture.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/architecture.md#build-and-ci-structure"
license: "Apache-2.0"
mode: "V"
---

The source tree has seven static library targets: `ctrace-model`, `ctrace-cli`, `ctrace-trace-run`,
`ctrace-diagnostics`, `ctrace-decode`, `ctrace-output`, and `ctrace-control`. Their `ctrace::` aliases expose the
shorter module names inside CMake. The common `ctracelib` OBJECT target contains `CtraceMain`; the executable adds only the
platform trampoline and manifest where required. Dependencies form a directed, cycle-free graph with `control` as
the composition root.

The tool-specific GitHub workflow is triggered for matching pull requests and pushes to `main` and reacts to
published releases. Only its release job is selected by a `tools/ctrace/<version>` release tag. The build matrix
covers Windows AMD64 and Arm64, Linux AMD64 and Arm64, and macOS Arm64 binaries. Unit and
integration tests run on Windows AMD64, Linux AMD64, and macOS Arm64; Windows Arm64 and Linux Arm64 remain
compile-only. Native Linux additionally runs the exact Babeltrace 2.0.5 consumer gate on AMD64. CI enforces 100%
source-line coverage for `tools/ctrace/src`; branch coverage is retained for review but is not the merge gate. The
versioned manual Trace Compass Server/TSP acceptance record is documented beside the
[integration tests](https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/../test/integration/README.md).
The release version compiled into the executable is derived from the same tag.

`scripts/package-release.sh` packages the five platform binaries, the devtools license, third-party notices, and
dependency licenses into `ctrace.zip`. Its `SHA256SUMS` file covers the packaged binaries and license/notice files;
it is not a checksum of the zip archive itself or a signing/notarization statement. Dependency licensing is documented
in the [third-party notices](https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/THIRD_PARTY_NOTICES.md); unfinished release work remains in the
[TODO list](https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/todo.md).

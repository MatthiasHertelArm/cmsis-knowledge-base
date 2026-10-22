---
id: "devt-ctrace-build-and-test"
type: "concept"
domain: "trace"
title: "ctrace: Build and test"
summary: "Initialize all dependencies and configure the repository from its root:"
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/ctrace/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/README.md#build-and-test"
license: "Apache-2.0"
mode: "V"
---

Initialize all dependencies and configure the repository from its root:

```bash
git submodule update --init --recursive
cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
cmake --build build --target ctrace CtraceUnitTests CtraceIntegTests
```

Run the GoogleTest unit and integration suites plus the executable smoke tests:

```bash
ctest --test-dir build -C Debug -R '^(CtraceUnitTests|CtraceIntegTests|CtraceFixtureIntegrity|ctrace-)'
```

On native Linux, installing exactly Babeltrace `2.0.5` before configuration
also registers the external consumer gate:

```bash
ctest --test-dir build -C Debug --no-tests=error -L '^linux-consumer$'
```

CI installs the pinned consumer and treats a missing labelled test as a
failure. The separate versioned Trace Compass acceptance record is documented
with the [integration tests](https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/test/integration/README.md).

Editors using `clangd` should open the devtools repository root and configure into `build`. The tool-local
`.clangd` file points clangd at that compilation database.

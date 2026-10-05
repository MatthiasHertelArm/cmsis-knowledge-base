---
id: "tbx-theory-of-operation-west-integration"
type: "concept"
domain: "project"
title: "Theory of Operation: West Integration"
summary: "The west build system uses two environment variables to configure the toolchain. These variables are set when the .csolution.yml contains the west: node."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-operation.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/#west-integration"
license: "Apache-2.0"
mode: "V"
---

The west build system uses two environment variables to configure the toolchain. These variables are set when the `*.csolution.yml` contains the [`west:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/YML-Input-Format.md#west) node. The cbuild orchestration sets them when West is called during setup and build operations; the VS Code CMSIS Solution extension also provides them in its build environment.

The `west build` command is called for each `app-path:` that is specified in the [`west:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/YML-Input-Format.md#west) node.

Environment Variable         | Description
:----------------------------|:-------------------------------------------------------------------
`ZEPHYR_TOOLCHAIN_VARIANT`   | Toolchain selection depending on the selected [`compiler:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/YML-Input-Format.md#compiler) in `csolution.yml`. Values are: armclang (for AC6), gnuarmemb (for GCC), llvm (for CLANG), iar (for IAR).
`<TOOLCHAIN>_TOOLCHAIN_PATH` | Path to selected compiler executable. `<TOOLCHAIN>` is the capitalized string specified with `ZEPHYR_TOOLCHAIN_VARIANT`. The value is copied from the compiler registration [environment variable](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/installation.md#environment-variables). 

The various build operations of the `cbuild` tool map as shown below to the `west` tool.

Operation                     | Cbuild Invocation                   | West Invocation
:-----------------------------|:------------------------------------|:------------------------   
Build                         | `cbuild <name>.csolution.yml`       | `west build -p auto -d <dir> -b <board> <app>`
[Database](#cmake-invocation) | `cbuild setup <name>.csolution.yml` | `west build -p auto -d <dir> -b <board> --cmake-only <app> -- -DCMAKE_EXPORT_COMPILE_COMMANDS=ON`

The cbuild `Clean` operation is performed as usual by cleaning temporary and output files, and the cbuild `Rebuild` triggers a normal build after cleaning. No other `west build` option is required.

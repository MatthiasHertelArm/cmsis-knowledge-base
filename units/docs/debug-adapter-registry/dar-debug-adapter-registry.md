---
id: "dar-debug-adapter-registry"
type: "concept"
domain: "debug"
title: "debug-adapter-registry"
summary: "(figure: License) (figure: Test and release )"
status: "draft"
collection: "debug-adapter-registry"
source: "Open-CMSIS-Pack/debug-adapter-registry@2692b50:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/debug-adapter-registry/blob/2692b50/README.md"
license: "Apache-2.0"
mode: "V"
---

[(figure: License)](https://github.com/Open-CMSIS-Pack/debug-adapter-registry/blob/main/LICENSE)
[(figure: Test and release )](https://github.com/Open-CMSIS-Pack/debug-adapter-registry/tree/main/.github/workflows/ci.yml)

This repository contains the [debug adapter registry](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/#debug-adapter-integration)
and the CMSIS Solution extension specific adapter template files.

```txt
  📦
  ┣ 📂 registry               shared debug adapter registry
  ┃ ┗ 📄 debug-adapters.yml    yaml document listing all available debug adapters
  ┗ 📂 templates              command line tool source code
    ┣ 📄 *.adapter.json       json template for vscode launch and task definitions per debug adapter
    ┗ 📄 ...
```

The adapter registry is used by CMSIS-Toolbox starting version 2.9.0 to generate `<solution>+<target-type>.cbuild-run.yml`
files for the active target-set selected by

```sh
cbuild setup <solution> --active <target-type>[@<set>]
```

Available target-sets are listed by running

```sh
cbuild list target-sets <solution>
```

The `<solution>+<target-type>.cbuild-run.yml` file is then processed by the CMSIS Solution extension to generate
`launch.json` and `task.json` files from the debug adapter template files.

---

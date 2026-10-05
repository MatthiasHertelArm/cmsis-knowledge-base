---
id: "tbx-build-tools-setup-project-for-ide"
type: "concept"
domain: "project"
title: "Build Tools: Command Examples / Setup Project (for IDE)"
summary: "In an IDE environment, this command downloads missing packs creates build information files, and generates the file compilecommands.json for IntelliSense. Refer to cbuild setup command for more information."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#setup-project-for-ide"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Examples_

In an IDE environment, this command downloads missing packs creates [build information files](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/YML-CBuild-Format.md), and generates the file `compile_commands.json` for IntelliSense. Refer to [cbuild setup command](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/build-operation.md#details-of-the-setup-mode) for more information.

```shell
cbuild setup example.csolution.yml --active <target-type>[@<target-set>] --packs
```

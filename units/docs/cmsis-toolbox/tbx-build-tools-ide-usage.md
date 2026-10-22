---
id: "tbx-build-tools-ide-usage"
type: "concept"
domain: "project"
title: "Build Tools: IDE Usage"
summary: "An IDE may use the following cbuild setup command to set up the project outline view and get information about components and software layers."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#ide-usage"
license: "Apache-2.0"
mode: "V"
---

An IDE may use the following `cbuild setup` command to set up the project outline view and get information about components and software layers.

```shell
cbuild setup example.csolution.yml --active <target-type>[@<target-set>] [--packs] [--update-rte]
```

The command above is used when the IDE starts:

- The option `--active` uses one `target` in the format `<target-type>[@<target-set>]` that may specify multiple related projects.
- The option `--packs` can enable the download of missing software packs that are public.
- The option `--update-rte` is used when the IDE changes `device:`, `board:` or `component:` settings.

The `cbuild setup` command creates [build information files](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/YML-CBuild-Format.md), `compile_commands.json`, and `compile_macros.h` for IDE language services and [Static Code Analysis](#static-code-analysis). Refer to [cbuild setup command](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/build-operation.md#details-of-the-setup-mode) for more information.

### Project Outline View

The project outline view in an IDE may utilize the project files as described below:

- The file `*.csolution.yml` contains the overall structure of projects, `build-types`, and `target-types`.
- The file `*.cproject.yml` provides the source groups, source files, and the list of components (but without source files).
- The files `*.clayer.yml` or `*.cgen.yml` contain software layers with additional source groups, source files, and components. The `*.cbuild.<context>.yml` files provide the exact location of these files, for example, when variables are used.

Using the above information, it is possible to create an outline view, but without the file list for components. For software layers, the content may require the `*.cbuild.<context>.yml` files that are generated with the `cbuild setup` command.

The `cbuild-idx.yml` file provides the exact location of all `*.cbuild.<context>.yml` files that are used for the selected target. The `*.cbuild.<context>.yml` files contain for the components source files, configuration file information, API header files, user code templates, generator information, and links to documentation. The project outline view may provide access to this information.

### Build Process

An IDE may use the following `cbuild` command to build the overall application.

```shell
cbuild example.csolution.yml --active <target-type>[@<target-set>] [--packs] [--quite] [--rebuild]
```

- The option `--active` selects a target along with projects and debugger configuration.
- The option `--packs` can be enable the download missing software packs that are public.
- The option `--quite` suppresses details about the build process.
- The option `--rebuild` may be used to force a complete rebuild of the output files.

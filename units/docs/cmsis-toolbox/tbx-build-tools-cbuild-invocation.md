---
id: "tbx-build-tools-cbuild-invocation"
type: "concept"
domain: "project"
title: "Build Tools: `cbuild` Invocation"
summary: "Orchestrate the overall build steps utilizing the various tools of the CMSIS-Toolbox and a CMake-based compilation process."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#cbuild-invocation"
license: "Apache-2.0"
mode: "V"
---

Orchestrate the overall build steps utilizing the various tools of the CMSIS-Toolbox and a CMake-based compilation process.

```txt
cbuild: Build Invocation 2.15.0 (C) 2022-2026 Arm Ltd. and Contributors

Usage:
  cbuild [command] <name>.csolution.yml [options]

Commands:
  help        Help about any command
  list        List information about contexts, environment, targets and toolchains
  setup       Generate project data for IDE environment
  zephyr      Generate Zephyr module files from clayer input

Options:
  -a, --active arg         Select active target: <target-type>[@<target-set>]
      --cbuildgen          Generate legacy *.cprj files and use cbuildgen backend
  -C, --clean              Remove intermediate and output directories
  -c, --context arg [...]  Input context names [<project-name>][.<build-type>][+<target-type>]
  -S, --context-set        Select the context names from cbuild-set.yml for generating the target application
  -d, --debug              Enable debug messages of the cmsis build tools
      --frozen-packs       Pack list and versions from cbuild-pack.yml are fixed and raises errors if it changes
  -g, --generator arg      Select build system generator (default "Ninja")
  -h, --help               Print usage
  -j, --jobs int           Number of job slots for parallel execution (default 8)
  -l, --load arg           Set policy for packs loading [latest | all | required] (default "required")
      --log arg            Save output messages in a log file
  -n, --no-schema-check    Skip schema check
  -O, --output arg         Base folder for output files, 'outdir' and 'tmpdir' (default "Same as '*.csolution.yml'")
  -p, --packs              Download missing software packs with cpackget
  -q, --quiet              Suppress output messages except build invocations
  -r, --rebuild            Remove intermediate and output directories and rebuild
  -s, --schema             Validate project input file(s) against schema [deprecated]
      --skip-convert       Skip csolution convert step
  -t, --target arg         Optional CMake target name
      --toolchain arg      Input toolchain to be used
      --update-rte         Update the RTE directory and files
  -v, --verbose            Enable verbose messages from toolchain builds
  -V, --version            Print version

Use "cbuild [command] --help" for more information about a command.
```

!!! Note
    By default, the `cbuild` invocation does not update the [**RTE Directory**](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/build-overview.md#rte-directory-structure). If required, use the option `--update-rte`.

**Verbosity Levels**
| Mode | Description |
|------|-------------|
| quiet | Show only errors or fatal conditions |
| normal | Include build steps and warnings |
| verbose | Include command-line invocation and info messages |
| debug | Include internal process steps and debug messages |

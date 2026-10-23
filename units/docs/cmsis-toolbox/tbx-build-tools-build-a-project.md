---
id: "tbx-build-tools-build-a-project"
type: "concept"
domain: "project"
title: "Build Tools: Command Examples / Build a Project"
summary: "This command builds a project that is defined in the file example.csolution.yml:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#build-a-project"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Examples_

This command builds a project that is defined in the file `example.csolution.yml`:

```shell
cbuild example.csolution.yml
```

A *csolution project* that defines a [debugger](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/build-overview.md#run-and-debug-configuration) using `target-set:` should be build using the option `--active` that selects the target in the format `<target-type>[@<target-set>]`.

```shell
cbuild example.csolution.yml --active MyBoard
```

Options allow to rebuild and download missing software packs or to select specific context settings:

```shell
cbuild example.csolution.yml --rebuild --packs --context .Release
```

For reproducible builds in CI environments, fixed software pack versions are provided by the file `*.cbuild-pack.yml`. An error is reported if the file `*.cbuild-pack.yml` does not exist or packs are added/removed. Refer to [reproducible builds](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/build-overview.md#reproducible-builds) for more information.

```shell
cbuild example.csolution.yml --frozen-packs --packs --rebuild
```

It is also possible to overwrite the toolchain selection and use a different toolchain for translation:

```shell
cbuild example.csolution.yml --toolchain GCC
```

The `--toolchain` option is useful for:

- Test a new compiler or a different compiler version for the overall project.
- For unit test applications to allow the usage of different compilers.

In [DevOps systems](#devops-usage) that run CI test with a matrix build, it is sometimes required to separate the output of various builds. The option `--output` adds a prefix to the [output directory](https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/YML-Input-Format.md#output-dirs) for `outdir:`, `tmpdir:` and build information files. The following commands build the project with the AC6 and GCC compiler and separate the directories for output and temporary files.

```shell
cbuild example.csolution.yml --toolchain AC6 --output outAC6
cbuild example.csolution.yml --toolchain GCC --output outGCC
```

!!! Note
    The `--output` option may be used by an IDE environment to location build information files outside of the user space.

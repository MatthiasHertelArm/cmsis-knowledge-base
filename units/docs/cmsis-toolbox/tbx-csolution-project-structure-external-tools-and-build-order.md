---
id: "tbx-csolution-project-structure-external-tools-and-build-order"
type: "concept"
domain: "project"
title: "CSolution Project Structure: Project Examples / External Tools and Build Order"
summary: "The executes: node integrates CMake scripts and external tools. The input: and output: lists typically refer to files and therefore define the build order of projects:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#external-tools-and-build-order"
license: "Apache-2.0"
mode: "V"
---

_Part of: Project Examples_

The [`executes:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#executes) node integrates [CMake scripts](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/build-operation.md#cmake-script-integration-with-executes) and external tools. The `input:` and `output:` lists typically refer to files and therefore define the build order of projects:

- When `input:` contains files that are the [output](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#output) of a `cproject.yml`, this project part is built first.
- When `output:` contains files that are the input of a `cproject.yml`, the `execute:` node is built first.

**Example:**

The `KeyGenerator` tool builds the file `keys.c`, which is added as a source [file:](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#files) for other projects. Using `cbuild My.csolution.yml --active <target-type>[@<target-set>]` starts the build process of the application and runs the `KeyGenerator` before building projects that use the source file `keys.c` as input.

!!! Note
    Using `cbuild` with the option `--context` does not run `execute:` nodes as it triggers project builds only. Use an application build, optionally selected with `--active`.

```yml
solution:
    :
  executes:
    - execute: GenKeys                      # is a CMake target name
      run: KeyGenerator -k $input(0)$ -p $input(1)$ -o $output$
      input:
        - $SolutionDir()$/keyfile.txt       # input(0) contains key in text format
        - $SolutionDir()$/passcode.txt      # input(1) contains passcode in text format
      output:
        - $SolutionDir()$/keys.c            # output keys source file (input to other projects)
```

#### Project Dependency

An [access sequence](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#access-sequences) that refers to the output of another project also impacts the build order.

**Example:**

The [access sequence](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#access-sequences) `$cmse-lib(Project_S)$` includes the secure entry library of `Project_S`. Hence, `Project_S` is built before the non-secure project part of the application.

```yml
project:                                 # Non-secure project
    :
  groups:
    - group: CMSE Library
      files:
        - file: $cmse-lib(Project_S)$    # Secure part of an application
```

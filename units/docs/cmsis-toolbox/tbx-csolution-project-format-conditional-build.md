---
id: "tbx-csolution-project-format-conditional-build"
type: "concept"
domain: "project"
title: "CSolution Project Format: Conditional Build"
summary: "It is possible to include or exclude items of a list node in the build process."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#conditional-build"
license: "Apache-2.0"
mode: "V"
---

It is possible to include or exclude *items* of a [*list node*](#order-of-list-nodes) in the build process.

- [`for-compiler:`](#for-compiler) includes *items* only for a compiler toolchain.
- [`for-context:`](#for-context) includes *items* only for a [*context*](#context-name-conventions) list.
- [`not-for-context:`](#not-for-context) excludes *items* for a [*context*](#context-name-conventions) list.

!!! Note
    `for-context:` and `not-for-context:` are mutually exclusive, only one occurrence can be specified for a *list node*.

### `for-compiler:`

Depending on a [compiler](#compiler) toolchain it is possible to include *list nodes* in the build process.

**Examples:**

```yml
for-compiler: AC6@6.16               # add item for Arm Compiler version 6.16 only

for-compiler: GCC                    # for GCC Compiler (any version)
```

### `for-context:`

A [*context*](#context-name-conventions) list that adds a list-node for specific `target-type` and/or `build-type` names.

### `not-for-context:`

A [*context*](#context-name-conventions) list that removes a list-node for specific `target-types:` and/or `build-types:`.

### Context List

It is also possible to provide a [`context`](#context-name-conventions) list with:

```yml
  - [.build-type][+target-type]
  - [.build-type][+target-type]
```

**Examples:**

```yml
for-context:
  - .Test                            # add item for build-type: Test (any target-type)

for-context:                         # add item
  - .Debug                           # for build-type: Debug and
  - .Release+Production-HW           # build-type: Release / target-type: Production-HW

not-for-context:  +Virtual           # remove item for target-type: Virtual (any build-type)
not-for-context:  .Release+Virtual   # remove item for build-type: Release with target-type: Virtual
```

### Usage

The keyword `for-context:` and `not-for-context:` can be used for the following *list nodes*:

List Node                                  | Description
:------------------------------------------|:------------------------------------
[`- project:`](#projects)                  | At `projects:` level it is possible to control inclusion of project.
[`- layer:`](#layers)                      | At `layers:` level, it is possible to control the inclusion of a software layer.

The keyword `for-context:`, `not-for-context:`, and `for-compiler:` can be applied to the following *list nodes*:

List Node                                  | Description
:------------------------------------------|:------------------------------------
[`- component:`](#components)              | At `components:` level, control the inclusion of a software component.
[`- group:`](#groups)                      | At `groups:` level, control the inclusion of a file group.
[`- setup:`](#setups)                      | At `setups:` level, define toolchain-specific options that apply to the whole project.
[`- file:`](#files)                        | At `files:` level, control the inclusion of a file.

The inclusion of a *list node* is processed with this hierarchy from top to bottom:

`project` --> `layer` --> `component`/`group` --> `file`

In other words, the restrictions specified by `for-context:` or `not-for-context` for a *list node* are applied to it child nodes. Child *list nodes* inherit the restrictions from their parent.

!!! Note
    With `for-context:` and `not-for-context:` the `project-name` of a [context](#context-name-conventions) cannot be applied. The `context` name must, therefore, start with `.` to refer to the `build-type:` or `+` to refer to the `target-type:`.

#### Regular Expressions

With `for-context:` and `not-for-context:` a [regular expression](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap09.html#tag_09_03) can be used to refer to multiple context names. When a context name starts with the character `\` the [regular expression](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap09.html#tag_09_03) expansion is enabled. The character `\` itself is not part of the sequence.

**Example:**

The following project is only included when the `build-type:` of a context contains `Test`.

```yml
  build-types:
    - Debug-Test:         # Debug build with Test functionality
       :
    - Test-Release:       # Release build with Test functionality
       :
    - Debug:
       :
    - Release:
       :

  project: Test.cproject.yml
    - for-context: \.*Test*`
```

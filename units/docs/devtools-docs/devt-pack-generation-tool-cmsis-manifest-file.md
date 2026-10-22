---
id: "devt-pack-generation-tool-cmsis-manifest-file"
type: "concept"
domain: "pack"
title: "Pack Generation Tool: CMSIS Manifest File"
summary: "Pack Generation Tool: CMSIS Manifest File"
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packgen/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/packgen/README.md#cmsis-manifest-file"
license: "Apache-2.0"
mode: "V"
---

The YAML structure is described below.

```yml
build:
  - name: <value>
    options: <value>

packs:
  - name: <value>
    description: <value>
    vendor: <value>
    license: <value>
    url: <value>
    releases:
      - version: <value>
        date: <value>
        description: <value>

    requirements:
      packages:
        - attributes: {<key:value list>}
      compilers:
        - attributes: {<key:value list>}
      languages:
        - attributes: {<key:value list>}

    taxonomy:
      - attributes: {<key:value list>}
        description: <value>

    apis:
      - name: <value>
        attributes: {<key:value list>}
        description: <value>
        files:
          - name: <value>
            attributes: {<key:value list>}
        extensions: [<list>]

    components:
      - name: <value>
        target: [<list>]
        build: [<list>]
        operation: [<intersection|difference>]
        attributes: {<key:value list>}
        description: <value>
        dependencies: [<list>]
        conditions:
          - <require|accept|deny>: {<key:value list>}
        files:
          - name: <value>
            attributes: {<key:value list>}
            conditions:
              - <require|accept|deny>: {<key:value list>}
        extensions: [<list>]
```

### build

| Argument        | Description
|:----------------|:----------------------------------------
| name            | Name of a set of CMake options. Multiple sets are supported
| options         | List of CMake options

### packs

| Argument        | Description
|:----------------|:----------------------------------------
| name            | Unique name of the Software Pack
| description     | Description of the Software Pack
| vendor          | Name of the supplier or vendor of the Software Pack
| license         | Path to license document
| url             | HTTP URL or file URI location of the Software Pack
| requirements    | Lists of [requirements](#requirements)
| releases        | List of Software Pack [releases](#releases)
| components      | List of Software Pack [components](#components)

### requirements

| Argument        | Description
|:----------------|:----------------------------------------
| packages        | List of required package attributes
| compilers       | List of required compiler attributes
| languages       | List of required language attributes

### releases

| Argument        | Description
|:----------------|:----------------------------------------
| version         | Semantic version number, see [Version Type](https://arm-software.github.io/CMSIS_5/Pack/html/pdsc_package_pg.html#VersionType)
| date            | Release date in the format YYYY-MM-DD
| description     | Release notes

### taxonomy

| Argument        | Description
|:----------------|:----------------------------------------
| attributes      | Typically Cclass and Cgroup, see [taxonomy](https://arm-software.github.io/CMSIS_5/latest/Pack/html/element_taxonomy.html)
| description     | Taxonomy entry brief description

### apis

| Argument        | Description
|:----------------|:----------------------------------------
| name            | Unique name of the API
| description     | API brief description
| attributes      | List of API [attributes](#attributes)
| files           | List of API [files](#files)
| extensions      | List of header file extensions for recursive copy

### components

| Argument        | Description
|:----------------|:----------------------------------------
| name            | Unique name of the component
| target          | List of CMake targets associated with the component
| build           | List of build options sets associated with the component
| operation       | Obtain the `intersection` or the `difference` of build options sets
| description     | Component brief description
| dependencies    | List of component dependencies. Other components or CMake targets are accepted.
| attributes      | List of component [attributes](#attributes)
| conditions      | List of component [conditions](#conditions)
| files           | List of component [files](#files)
| extensions      | List of header file extensions for categorization and recursive copy

### attributes

| Argument        | Description
|:----------------|:----------------------------------------
| Cclass          | Component class
| Cgroup          | Component group
| Csubgroup       | Component subgroup
| Cvariant        | Component variant
| Cversion        | Component version

### files

| Argument          | Description
|:------------------|:----------------------------------------
| name              | File path relative to the pack root directory
| attributes        | List of [file attributes](#file-attributes)
| conditions        | List of file [conditions](#conditions)

### file attributes

| Argument        | Description
|:----------------|:----------------------------------------
| category        | Defines the purpose of the file.
| attr            | Defines the special use and handling of a file.
| version         | File-specific version information.

### conditions

| Argument          | Description
|:------------------|:----------------------------------------
| \`<rule>`           | It must be `require`, `accept` or `deny`
| \`<key:value list>` | Typically external component [attributes](#attributes), but not limited to it.

> For further info please consult the PDSC specification, for example:

- [components](https://arm-software.github.io/CMSIS_5/Pack/html/pdsc_components_pg.html#element_components)
- [conditions](https://arm-software.github.io/CMSIS_5/Pack/html/pdsc_conditions_pg.html#element_conditions)
- [file](https://arm-software.github.io/CMSIS_5/Pack/html/pdsc_components_pg.html#element_file)
- [requirements](https://arm-software.github.io/CMSIS_5/Pack/html/element_requirements_pg.html)

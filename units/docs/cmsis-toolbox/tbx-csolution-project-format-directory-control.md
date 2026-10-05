---
id: "tbx-csolution-project-format-directory-control"
type: "concept"
domain: "project"
title: "CSolution Project Format: Directory Control"
summary: "The following nodes control the application's directory structure."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#directory-control"
license: "Apache-2.0"
mode: "V"
---

The following nodes control the application's directory structure.

### `output-dirs:`

Allows control of the directory structure for building output files and temporary files.

!!! Note
    - This control is only possible at `csolution.yml` level.
    - With an active target selection, `tmpdir:` supports the access sequences [`$TargetType$`](#access-sequences) and [`$TargetSet$`](#access-sequences).

`output-dirs:`                     |              | Content
:----------------------------------|:-------------|:------------------------------------
&nbsp;&nbsp;&nbsp; `outdir:`       |  Optional    | Specifies the directory for the build output files (ELF, binary, MAP files).
&nbsp;&nbsp;&nbsp; `tmpdir:`       |  Optional    | Specifies the directory for the interim temporary files.
&nbsp;&nbsp;&nbsp; `intdir:`       |  Optional    | Legacy node, applied instead of `tmpdir:` when using `cbuild` with option `--cbuildgen`.

Without an active target selection, the default settings for `output-dirs:` are:

```yml
  tmpdir:  tmp                          # All projects use the same temporary directory
  outdir:  $SolutionDir()$/out/$TargetType$/$BuildType$
```

With `--active`, the default temporary directory separates the selected target type and target-set. `$TargetSet$` expands to the value of `set:` or to `default` for an unnamed target-set:

```yml
  tmpdir:  tmp/$TargetType$/$TargetSet$
```

With the tool option `--output`, a top-level prefix directory can be added. The effective `outdir:` with the command below is: `MyOut/out/$TargetType$/$BuildType$`.

```bash
cbuild <name>.csolution.yml --output MyOut
```

**Example:**

```yml
output-dirs:
  tmpdir: ./tmp2/$TargetType$/$TargetSet$ # relative path to csolution.yml file
  outdir: ./out/$Project$/$TargetType$    # $BuildType$ no longer part of the outdir
```

### `generators:`

Allows control of the directory structure for generator output files.

When no explicit `generators:` is specified, the **`csolution` Project Manager** uses as path:

- The `workingDir` defined in the [generators element](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_generators_pg.html#element_generator) of the PDSC file.
- When no `workingDir` is defined the default directory `$ProjectDir()$/generated/<generator-id>` is used; `<generator-id>` is defined by the `id` in the generators element of the PDSC file.

The `generators:` node can be added at various levels of the `*.yml` input files. The following order is used:

1. Use `generators:` specification of the `*.clayer.yml` input file, if not exist:
2. Use `generators:` specification of the `*.cproject.yml` input file, if not exist:
3. Use `generators:` specification of the `*.csolution.yml` input file.

!!! Note
    - Only relative paths are permitted to support the portability of projects.
    - The location of the `*.yml` file that contains the `generators:` node is the reference for relative paths.

`generators:`                  |            | Content
:------------------------------|:-----------|:------------------------------------
&nbsp;&nbsp;&nbsp; `base-dir:` |  Optional  | Base directory for unspecified generators; default: `$ProjectDir()$/generated`.
&nbsp;&nbsp;&nbsp; `options:`  |  Optional  | Specific generator options; allows explicit directory configuration for a generator.

!!! Note
    The base directory is extended for each generator with `/<generator-id>`; `<generator-id>` is defined by the `id` in the generator element of the PDSC file.

#### `generators:` `options:`

`options:`                     |            | Content
:------------------------------|:-----------|:------------------------------------
`- generator:`                 |  Optional  | Identifier of the generator tool, specified with `id` in the [generators element](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_generators_pg.html#element_generator) of the PDSC file.
&nbsp;&nbsp;&nbsp; `path:`     |  Optional  | Specifies the directory for generated files. Relative paths used the location of the `*.cproject.yml` or `*.clayer.yml` file as the base directory.
&nbsp;&nbsp;&nbsp; `name:`     |  Optional  | Specifies the base name of the [generator import file](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/YML-CBuild-Format.md#generator-import-file) (added in CMSIS-Toolbox 2.4.0); typically used for a board layer.
&nbsp;&nbsp;&nbsp; `map:`      |  Optional  | Mapping of the *csolution project* to a generator-specific run-time context name (added in CMSIS-Toolbox 2.4.0).

**Example:**

```yml
generators:
  base-dir: $SolutionDir()$/MyGenerators      # Path for all generators extended by '/<generator-id>'

  options:
  - generator: CubeMX                         # for the generator id `CubeMX` use this path
    path:  ./CubeFiles                        # relative path to generated files and the generator import file
    name: MyConf                              # results in generator import file ./CubeFiles/MyConf.cgen.yml
    map: Boot                                 # Map this project part to the CubeMX run-time context Boot
```

### `rte:`

Allows to control the directory structure for [RTE (run-time environment)](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/build-overview.md#rte-directory-structure) files.

!!! Note
    - This control is only possible at `*.cproject.yml` level.
    - Only relative paths are permitted to support the portability of projects.
    - The location of the `*.cproject.yml` file is the reference for relative paths.

`rte:`                         |            | Content
:------------------------------|:-----------|:------------------------------------
&nbsp;&nbsp;&nbsp; `base-dir:` |  Optional  | Base directory for unspecified generators; default: `$ProjectDir()$/RTE`.

```yml
rte:
  base-dir: $TargetType$/RTE      # Path extended with target-type, results in `$ProjectDir()$/$TargetType$/RTE`
```

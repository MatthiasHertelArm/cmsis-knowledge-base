---
id: "ceed-mixins-options-for-loading-mixins"
type: "concept"
domain: "test"
title: "Mixins: Options for loading Mixins"
summary: "You have three options for telling Ceedling what mixins to load. These options are ordered below according to their precedence."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/mixins.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/mixins/#options-for-loading-mixins"
license: "MIT"
mode: "V"
---

You have three options for telling Ceedling what mixins to load. These
options are ordered below according to their precedence. A Mixin higher
in the list is merged **later** and therefore its content takes priority 
over lower-listed options in two ways:

- **Single values** (a path string, a number, true/false): The higher-priority
  mixin’s value replaces any lower-priority mixin’s value for the same setting.
- **Lists** (e.g. search paths, plugin names): The higher-priority mixin’s
  entries appear **before** lower-priority entries in the combined list.
  For example, if a command line mixin adds the search path `vendor/include`
  and the project configuration mixin adds `src/include`, the merged include
  path list will be `[vendor/include, src/include]` — the command line path
  is searched first.

In addition, options higher in the list force duplicate mixin filepaths in
lower-listed options to be ignored (i.e. deduplicated).

Unlike project file loading that resolves to a single filepath
to load your base configuration, multiple mixins can be specified using 
any or all of these options.

1. Command line option flags
1. Environment variables
1. Base project configuration file entries

### `--mixin` command line flags

As already discussed above, many of Ceedling’s application commands 
include an optional `--project` flag. Most of these same commands 
also recognize optional `--mixin` flags.

Note that `--mixin` can be used multiple times in a single command line 
and the rightmost instance is merged last (i.e. highest priority).

When provided, Ceedling merges the specified mixin into the base 
project configuration. A `--mixin` value accepts three forms 
distinguished by an optional sigil prefix:

!!! note "Sigil definition"
    A _sigil_ is a non-alphabetic symbol (e.g. `$`, `@`, `%`) that 
    serves as a visual prefix or suffix that instantly tells an 
    interpreter and the developer a data type, scope, or structure.

#### File or named mixin (optional `@` sigil)

The value is treated as a file path or named mixin lookup. Two 
equivalent syntaxes are accepted:

```sh
--mixin my_compiler         # simple name lookup (no sigil)
--mixin @my_compiler        # simple name lookup (no sigil)
--mixin bar/mixin.yaml      # filepath (no sigil)
--mixin @bar/mixin.yaml     # filepath (explicit @ sigil — same result)
```

- A **simple name** (no extension, no path separator) is looked up 
  among Ceedling’s configured mixin load paths.
- A **filename or filepath** (with extension or path separator) loads 
  the specified YAML file directly.
- The `@` sigil is optional and makes the file/name intent explicit; 
  it is otherwise identical to providing the value without a sigil
  (primarily for backwards compatibility pre-inline YAML).

#### Inline YAML (`=` sigil)

The value is treated as a YAML string merged directly into 
configuration — no file needed.

!!! note "Flow-style versus block YAML"
    Ceedling can parse both flow-style and block YAML in the 
    configuration files it loads. The inline YAML command line 
    option must use [flow-style](https://www.educative.io/answers/what-is-flow-style-in-yaml).
    Block-style YAML supports a leading optional colon for key names,
    and Ceedling uses this internally. Flow-style does not support
    this YAML notation style. So, `:foo: 'bar'` is illegal in 
    inline YAML; `foo: 'bar'` must be used instead.

Prefix the value with `=` and quote the argument to protect 
YAML special characters (colons, brackets, spaces) from shell 
interpretation:

```sh
--mixin "=defines: {release: ['MY_SYMBOL']}"
```

The YAML content must evaluate to a Hash at the top level (matching 
the structure of a project configuration file). Arrays, scalars, and 
empty strings are rejected with an error.

#### Combining forms

All three forms can be mixed freely in a single command line and are 
processed in the order they appear, left-to-right:

```sh
ceedling release \
  --mixin @mixins/base_compiler.yml \
  --mixin "=defines: {release: ['CIPHER_ROT13']}" \
  --mixin ci_overrides
```

In this example: `mixins/base_compiler.yml` is merged first as a
loaded file, then the inline YAML, and finally a `ci_overrides` file 
found among mixin paths specified in the base configuration file
(not shown).

Later entries (on the right side of a command line) win on conflicts,
so the content of `ci_overrides.yml` has the highest priority.

Simple mixin names are resolved by searching load paths in this order:

1. User-configured `:load_paths` from the base project file (if any)
1. The directory containing the base project file
1. Ceedling's built-in Unity toolchain targets

User-specified load paths are configured through the `:mixins` section
of the base project file. See the [documentation for the `:mixins`
section of your project configuration][mixins-config-section] for
more details. See [Built-in toolchain targets](#built-in-toolchain-targets)
for details on what names are available without any load path configuration.

Filepaths may be relative (to the working directory) or absolute.

[mixins-config-section]: #base-configuration-mixins-entries

#### Error behavior

If the `--mixin` filename or filepath does not exist, Ceedling
terminates with an error. If Ceedling cannot find a mixin name in
any load paths, it terminates with an error. If an inline YAML
string cannot be parsed or does not evaluate to a Hash, Ceedling
terminates with an error.

### Environment variables

Mixins can also be loaded through environment variables. Ceedling
recognizes environment variables with a naming scheme of 
`CEEDLING_MIXIN_#`, where `#` is any number greater than 0.

Precedence among the environment variables follows a simple ascending
sort of the trailing numeric value in the environment variable name.
Lower-numbered variables are merged first (lower priority); higher-numbered
variables are merged last (higher priority). For example,
`CEEDLING_MIXIN_5` is merged before `CEEDLING_MIXIN_99`, so
`CEEDLING_MIXIN_99` takes priority.

Mixin environment variables only hold filepaths. Filepaths may be 
relative (in relation to the working directory) or absolute.

If the filepath specified by an environment variable does not exist,
Ceedling terminates with an error.

### Base configuration `:mixins` entries

!!! note
    Ceedling only recognizes a `:mixins` section in your base project
    configuration file. A `:mixins` section nested in a mixin is ignored.

The `:mixins` section of a base project configuration file is filtered
out of the resulting merged configuration and will be absent in 
`ceedling dumpconfig` output.

The `:mixins` configuration section can contain up to two subsections.
Each subsection is optional.

* `:enabled`

    An optional array comprising (A) mixin filenames/filepaths and/or 
    (B) simple mixin names.

    1. A filename contains a file extension. A filepath includes a 
       directory path. The file content is YAML.
    1. A simple name (no file extension and no path) is used
       as a file lookup among any configured load paths (see next
       section) and as a lookup name among Ceedling’s built-in mixins
       (currently none).

    Enabled entries support [inline Ruby string expansion][inline-ruby-string-expansion].

    **Default**: `[]`

* `:load_paths`

    Paths containing mixin files to be searched via mixin names. A mixin
    filename in a load path has the form _<name>.yml_ by default. If
    alternate filename extensions have been specified in your project
    configuration (`:extension` ↳ `:yaml`, a single extension or a list)
    they will be used for file lookups in the mixin load paths instead of
    _.yml_. Each load path is searched for every extension before the next.

    Searches start in the path at the top of the list.

    Both mixin names in the `:enabled` list (above) and on the command
    line via `--mixin` flag use this list of load paths for searches.

    If a mixin name is not found in any user-configured load path,
    Ceedling automatically searches two additional locations in order:

    1. **Project directory** — the directory containing your base project
       configuration file. This lets you drop a YAML file alongside
       _project.yml_ and reference it by name with no extra configuration.
    1. **Built-in toolchain targets** — Ceedling's bundled Unity `targets/`
       folder. See [Built-in toolchain targets](#built-in-toolchain-targets).

    User-configured load paths always take priority over these fallbacks.
    The project directory takes priority over the built-in targets.

    Load paths entries support [inline Ruby string expansion][inline-ruby-string-expansion].

    **Default**: `[]`

Example `:mixins` YAML blurb:

```yaml
:mixins:
  :enabled:
    - foo            # Search for foo.yml in proj/mixins & support/ and 'foo' among built-in mixins
    - path/bar.yaml  # Merge this file with base project conig
  :load_paths:
    - proj/mixins
    - support
```

Relating the above example to command line `--mixin` flag handling:

* A command line flag of `--mixin=foo` is equivalent to the `foo` 
  entry in the `:enabled` mixin configuration.
* A command line flag of `--mixin=path/bar.yaml` is equivalent to the 
  `path/bar.yaml` entry in the `:enabled` mixin configuration.
* Note that while command line `--mixin` flags work identically to
  entries in `:mixins` ↳ `:enabled`, they are merged **last** and therefore
  have the highest priority. The `:enabled` list is merged **first** (because
  it resides in the base configuration and has the lowest priority).

[inline-ruby-string-expansion]: project-file.md#inline-ruby-string-expansion

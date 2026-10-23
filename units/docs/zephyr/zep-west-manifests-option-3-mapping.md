---
id: "zep-west-manifests-option-3-mapping"
type: "concept"
domain: "project"
title: "West Manifests: Manifest Imports / Option 3: Mapping"
summary: "The import key can also contain a mapping with the following keys:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/manifest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/manifest.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Manifest Imports_

The `import` key can also contain a mapping with the following keys:

- `file`: Optional. The name of the manifest file or directory to import.
  This defaults to `west.yml` if not present.
- `name-allowlist`: Optional. If present, a name or sequence of project names
  to include.
- `path-allowlist`: Optional. If present, a path or sequence of project paths
  to match against. This is a shell-style globbing pattern, currently
  implemented with pathlib. Note that this means case sensitivity is
  platform specific.
- `name-blocklist`: Optional. Like `name-allowlist`, but contains project
  names to exclude rather than include.
- `path-blocklist`: Optional. Like `path-allowlist`, but contains project
  paths to exclude rather than include.
- `path-prefix`: Optional (new in v0.8.0). If given, this will be prepended
  to the project's path in the workspace, as well as the paths of any imported
  projects. This can be used to place these projects in a subdirectory of the
  workspace.

Allowlists override blocklists if both are given. For example, if a project is
blocked by path, then allowed by name, it will still be imported.

.. _west-manifest-ex3.1:


#### Example 3.1: Downstream with name allowlist


Here is a pair of manifest files, representing a mainline and a
downstream. The downstream doesn't want to use all the mainline
projects, however. We'll assume the mainline `west.yml` is
hosted at `https://git.example.com/mainline/manifest`.

```yaml

# mainline west.yml:
manifest:
  projects:
    - name: mainline-app                # included
      path: examples/app
      url: https://git.example.com/mainline/app
    - name: lib
      path: libraries/lib
      url: https://git.example.com/mainline/lib
    - name: lib2                        # included
      path: libraries/lib2
      url: https://git.example.com/mainline/lib2

# downstream west.yml:
manifest:
  projects:
    - name: mainline
      url: https://git.example.com/mainline/manifest
      import:
        name-allowlist:
          - mainline-app
          - lib2
    - name: downstream-app
      url: https://git.example.com/downstream/app
    - name: lib3
      path: libraries/lib3
      url: https://git.example.com/downstream/lib3
```
An equivalent manifest in a single file would be:

```yaml

manifest:
  projects:
    - name: mainline
      url: https://git.example.com/mainline/manifest
    - name: downstream-app
      url: https://git.example.com/downstream/app
    - name: lib3
      path: libraries/lib3
      url: https://git.example.com/downstream/lib3
    - name: mainline-app                   # imported
      path: examples/app
      url: https://git.example.com/mainline/app
    - name: lib2                           # imported
      path: libraries/lib2
      url: https://git.example.com/mainline/lib2
```
If an allowlist had not been used, the `lib` project from the mainline
manifest would have been imported.

.. _west-manifest-ex3.2:


#### Example 3.2: Downstream with path allowlist


Here is an example showing how to allowlist mainline's libraries only,
using `path-allowlist`.

```yaml

# mainline west.yml:
manifest:
  projects:
    - name: app
      path: examples/app
      url: https://git.example.com/mainline/app
    - name: lib
      path: libraries/lib                  # included
      url: https://git.example.com/mainline/lib
    - name: lib2
      path: libraries/lib2                 # included
      url: https://git.example.com/mainline/lib2

# downstream west.yml:
manifest:
  projects:
    - name: mainline
      url: https://git.example.com/mainline/manifest
      import:
        path-allowlist: libraries/*
    - name: app
      url: https://git.example.com/downstream/app
    - name: lib3
      path: libraries/lib3
      url: https://git.example.com/downstream/lib3
```
An equivalent manifest in a single file would be:

```yaml

manifest:
  projects:
    - name: lib                          # imported
      path: libraries/lib
      url: https://git.example.com/mainline/lib
    - name: lib2                         # imported
      path: libraries/lib2
      url: https://git.example.com/mainline/lib2
    - name: mainline
      url: https://git.example.com/mainline/manifest
    - name: app
      url: https://git.example.com/downstream/app
    - name: lib3
      path: libraries/lib3
      url: https://git.example.com/downstream/lib3
```
.. _west-manifest-ex3.3:


#### Example 3.3: Downstream with path blocklist


Here's an example showing how to block all vendor HALs from mainline by
common path prefix in the workspace, add your own version for the chip
you're targeting, and keep everything else.

```yaml

# mainline west.yml:
manifest:
  defaults:
    remote: mainline
  remotes:
    - name: mainline
      url-base: https://git.example.com/mainline
  projects:
    - name: app
    - name: lib
      path: libraries/lib
    - name: lib2
      path: libraries/lib2
    - name: hal_foo
      path: modules/hals/foo     # excluded
    - name: hal_bar
      path: modules/hals/bar     # excluded
    - name: hal_baz
      path: modules/hals/baz     # excluded

# downstream west.yml:
manifest:
  projects:
    - name: mainline
      url: https://git.example.com/mainline/manifest
      import:
        path-blocklist: modules/hals/*
    - name: hal_foo
      path: modules/hals/foo
      url: https://git.example.com/downstream/hal_foo
```
An equivalent manifest in a single file would be:

```yaml

manifest:
  defaults:
    remote: mainline
  remotes:
    - name: mainline
      url-base: https://git.example.com/mainline
  projects:
    - name: app                  # imported
    - name: lib                  # imported
      path: libraries/lib
    - name: lib2                 # imported
      path: libraries/lib2
    - name: mainline
      repo-path: https://git.example.com/mainline/manifest
    - name: hal_foo
      path: modules/hals/foo
      url: https://git.example.com/downstream/hal_foo
```
.. _west-manifest-ex3.4:


#### Example 3.4: Import into a subdirectory


You want to import a manifest and its projects, placing everything into a
subdirectory of your `west workspace`.

For example, suppose you want to import this manifest from project `foo`,
adding this project and its projects `bar` and `baz` to your workspace:

```yaml

# foo/west.yml:
manifest:
  defaults:
    remote: example
  remotes:
    - name: example
      url-base: https://git.example.com
  projects:
    - name: bar
    - name: baz
```
Instead of importing these into the top level workspace, you want to place all
three project repositories in an `external-code` subdirectory, like this:

```none

workspace/
└── external-code/
    ├── foo/
    ├── bar/
    └── baz/
```
You can do this using this manifest:

```yaml

manifest:
  projects:
    - name: foo
      url: https://git.example.com/foo
      import:
        path-prefix: external-code
```
An equivalent manifest in a single file would be:

```yaml

# foo/west.yml:
manifest:
  defaults:
    remote: example
  remotes:
    - name: example
      url-base: https://git.example.com
  projects:
    - name: foo
      path: external-code/foo
    - name: bar
      path: external-code/bar
    - name: baz
      path: external-code/baz
```

---
id: "zep-west-manifests-group-filters-and-imports"
type: "concept"
domain: "project"
title: "West Manifests: Project Groups / Group Filters and Imports"
summary: "This section provides a simplified description of how the manifest: group-filter: value behaves when combined with west-manifest-import. For complete details, see west-manifest-formal."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/manifest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/manifest.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Project Groups_

This section provides a simplified description of how the ``manifest:
group-filter:`` value behaves when combined with west-manifest-import.
For complete details, see west-manifest-formal.


**Warning:** The below semantics apply to west v0.10.0 and later. West v0.9.x semantics are different, and combining `group-filter` with `import` in west v0.9.x is discouraged.

In short:

- if you only import one manifest, any groups it disables in its
  `group-filter` are also disabled in your manifest
- you can override this in your manifest file's `manifest: group-filter:`
  value, your workspace's `manifest.group-filter` configuration option, or
  both

Here are some examples.


#### Example 1: no overrides


You are using this `parent/west.yml` manifest:

```yaml

# parent/west.yml:
manifest:
  projects:
    - name: child
      url: https://git.example.com/child
      import: true
    - name: project-1
      url: https://git.example.com/project-1
      groups:
        - unstable
```
And `child/west.yml` contains:

```yaml

# child/west.yml:
manifest:
  group-filter: [-unstable]
  projects:
    - name: project-2
      url: https://git.example.com/project-2
    - name: project-3
      url: https://git.example.com/project-3
      groups:
        - unstable
```
Only `child` and `project-2` are active in the resolved manifest.

The `unstable` group is disabled in `child/west.yml`, and that is not
overridden in `parent/west.yml`. Therefore, the final `group-filter`
for the resolved manifest is `[-unstable]`.

Since `project-1` and `project-3` are in the `unstable` group and are not
in any other group, they are inactive.


#### Example 2: overriding an imported `group-filter` via manifest


You are using this `parent/west.yml` manifest:

```yaml

# parent/west.yml:
manifest:
  group-filter: [+unstable,-optional]
  projects:
    - name: child
      url: https://git.example.com/child
      import: true
    - name: project-1
      url: https://git.example.com/project-1
      groups:
        - unstable
```
And `child/west.yml` contains:

```yaml

# child/west.yml:
manifest:
  group-filter: [-unstable]
  projects:
    - name: project-2
      url: https://git.example.com/project-2
      groups:
        - optional
    - name: project-3
      url: https://git.example.com/project-3
      groups:
        - unstable
```
Only the `child`, `project-1`, and `project-3` projects are active.

The `[-unstable]` group filter in `child/west.yml` is overridden in
`parent/west.yml`, so the `unstable` group is enabled. Since
`project-1` and `project-3` are in the `unstable` group, they are active.

The same `parent/west.yml` file disables the `optional` group, so
`project-2` is inactive.

The final group filter specified by `parent/west.yml` is
`[+unstable,-optional]`.


#### Example 3: overriding an imported `group-filter` via configuration


You are using this `parent/west.yml` manifest:

```yaml

# parent/west.yml:
manifest:
  projects:
    - name: child
      url: https://git.example.com/child
      import: true
    - name: project-1
      url: https://git.example.com/project-1
      groups:
        - unstable
```
And `child/west.yml` contains:

```yaml

# child/west.yml:
manifest:
  group-filter: [-unstable]
  projects:
    - name: project-2
      url: https://git.example.com/project-2
      groups:
        - optional
    - name: project-3
      url: https://git.example.com/project-3
      groups:
        - unstable
```
If you run:

```shell

west config manifest.group-filter +unstable,-optional
```
Then only the `child`, `project-1`, and `project-3` projects are active.

The `-unstable` group filter in `child/west.yml` is overridden in the
`manifest.group-filter` configuration option, so the `unstable` group is
enabled. Since `project-1` and `project-3` are in the `unstable` group,
they are active.

The same configuration option disables the `optional` group, so `project-2`
is inactive.

The final group filter specified by `parent/west.yml` and the
`manifest.group-filter` configuration option is `[+unstable,-optional]`.

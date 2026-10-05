---
id: "zep-west-manifests-project-group-examples"
type: "concept"
domain: "project"
title: "West Manifests: Project Groups / Project Group Examples"
summary: "This section contains example situations involving project groups and active projects. The examples use both manifest: group-filter: YAML lists and manifest.group-filter configuration lists, to show how they work together."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/manifest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/manifest.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Project Groups_

This section contains example situations involving project groups and active
projects. The examples use both `manifest: group-filter:` YAML lists and
`manifest.group-filter` configuration lists, to show how they work together.

Note that the `defaults` and `remotes` data in the following manifests
isn't relevant except to make the examples complete and self-contained.


**Note:** In all of the examples that follow, the `manifest.project-filter` option is assumed to be unset.


#### Example 1: no disabled groups


The entire manifest file is:

```yaml

manifest:
  projects:
    - name: foo
      groups:
        - groupA
    - name: bar
      groups:
        - groupA
        - groupB
    - name: baz

  defaults:
    remote: example-remote
  remotes:
    - name: example-remote
      url-base: https://git.example.com
```
The `manifest.group-filter` configuration option is not set (you can ensure
this by running `west config -D manifest.group-filter`).

No groups are disabled, because all groups are enabled by default. Therefore,
all three projects (`foo`, `bar`, and `baz`) are active. Note that there
is no way to make project `baz` inactive, since it has no groups.


#### Example 2: Disabling one group via manifest


The entire manifest file is:

```yaml

manifest:
  projects:
    - name: foo
      groups:
        - groupA
    - name: bar
      groups:
        - groupA
        - groupB

  group-filter: [-groupA]

  defaults:
    remote: example-remote
  remotes:
    - name: example-remote
      url-base: https://git.example.com
```
The `manifest.group-filter` configuration option is not set (you can ensure
this by running `west config -D manifest.group-filter`).

Since `groupA` is disabled, project `foo` is inactive. Project `bar` is
active, because `groupB` is enabled.


#### Example 3: Disabling multiple groups via manifest


The entire manifest file is:

```yaml

manifest:
  projects:
    - name: foo
      groups:
        - groupA
    - name: bar
      groups:
        - groupA
        - groupB

  group-filter: [-groupA,-groupB]

  defaults:
    remote: example-remote
  remotes:
    - name: example-remote
      url-base: https://git.example.com
```
The `manifest.group-filter` configuration option is not set (you can ensure
this by running `west config -D manifest.group-filter`).

Both `foo` and `bar` are inactive, because all of their groups are
disabled.


#### Example 4: Disabling a group via configuration


The entire manifest file is:

```yaml

manifest:
  projects:
    - name: foo
      groups:
        - groupA
    - name: bar
      groups:
        - groupA
        - groupB

  defaults:
    remote: example-remote
  remotes:
    - name: example-remote
      url-base: https://git.example.com
```
The `manifest.group-filter` configuration option is set to `-groupA` (you
can ensure this by running `west config manifest.group-filter -- -groupA`;
the extra `--` is required so the argument parser does not treat `-groupA`
as a command line option `-g` with value `roupA`).

Project `foo` is inactive because `groupA` has been disabled by the
`manifest.group-filter` configuration option. Project `bar` is active
because `groupB` is enabled.


#### Example 5: Overriding a disabled group via configuration


The entire manifest file is:

```yaml

manifest:
  projects:
    - name: foo
    - name: bar
      groups:
        - groupA
    - name: baz
      groups:
        - groupA
        - groupB

  group-filter: [-groupA]

  defaults:
    remote: example-remote
  remotes:
    - name: example-remote
      url-base: https://git.example.com
```
The `manifest.group-filter` configuration option is set to `+groupA` (you
can ensure this by running `west config manifest.group-filter +groupA`).

In this case, `groupA` is enabled: the `manifest.group-filter`
configuration option has higher precedence than the ``manifest: group-filter:
[-groupA]`` content in the manifest file.

Therefore, projects `foo` and `bar` are both active.


#### Example 6: Overriding multiple disabled groups via configuration


The entire manifest file is:

```yaml

manifest:
  projects:
    - name: foo
    - name: bar
      groups:
        - groupA
    - name: baz
      groups:
        - groupA
        - groupB

  group-filter: [-groupA,-groupB]

  defaults:
    remote: example-remote
  remotes:
    - name: example-remote
      url-base: https://git.example.com
```
The `manifest.group-filter` configuration option is set to
`+groupA,+groupB` (you can ensure this by running ``west config
manifest.group-filter "+groupA,+groupB"``).

In this case, both `groupA` and `groupB` are enabled, because the
configuration value overrides the manifest file for both groups.

Therefore, projects `foo` and `bar` are both active.


#### Example 7: Disabling multiple groups via configuration


The entire manifest file is:

```yaml

manifest:
  projects:
    - name: foo
    - name: bar
      groups:
        - groupA
    - name: baz
      groups:
        - groupA
        - groupB

  defaults:
    remote: example-remote
  remotes:
    - name: example-remote
      url-base: https://git.example.com
```
The `manifest.group-filter` configuration option is set to
`-groupA,-groupB` (you can ensure this by running ``west config
manifest.group-filter -- "-groupA,-groupB"``).

In this case, both `groupA` and `groupB` are disabled.

Therefore, projects `foo` and `bar` are both inactive.

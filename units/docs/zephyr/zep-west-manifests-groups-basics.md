---
id: "zep-west-manifests-groups-basics"
type: "concept"
domain: "project"
title: "West Manifests: Project Groups / Groups Basics"
summary: "The groups: and group-filter: keys appear in the manifest like this:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/manifest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/manifest.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Project Groups_

The `groups:` and `group-filter:` keys appear in the manifest like this:

```yaml

manifest:
  projects:
    - name: some-project
      groups: ...
  group-filter: ...
```
The `groups` key's value is a list of group names. Group names are strings.

You can enable or disable project groups using `group-filter`. Projects whose
groups are all disabled, and which are not otherwise made active by a
`manifest.project-filter` configuration option, are inactive.

For example, in this manifest fragment:

```yaml

manifest:
  projects:
    - name: project-1
      groups:
        - groupA
    - name: project-2
      groups:
        - groupB
        - groupC
    - name: project-3
```
The projects are in these groups:

- `project-1`: one group, named `groupA`
- `project-2`: two groups, named `groupB` and `groupC`
- `project-3`: no groups

Project group names must not contain commas (,), colons (:), or whitespace.

Group names must not begin with a dash (-) or the plus sign (+), but they may
contain these characters elsewhere in their names. For example, `foo-bar` and
`foo+bar` are valid groups, but `-foobar` and `+foobar` are not.

Group names are otherwise arbitrary strings. Group names are case sensitive.

As a restriction, no project may use both `import:` and `groups:`. (This
is necessary to avoid some pathological edge cases.)

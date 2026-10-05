---
id: "zep-west-manifests-manifest-import-details"
type: "concept"
domain: "project"
title: "West Manifests: Manifest Imports / Manifest Import Details"
summary: "This section describes how west resolves a manifest file that uses import a bit more formally."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/manifest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/manifest.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Manifest Imports_

This section describes how west resolves a manifest file that uses `import` a
bit more formally.


#### Overview


The `import` key can appear in a west manifest's `projects` and `self`
sections. The general case looks like this:

```yaml

# Top-level manifest file.
manifest:
  projects:
    - name: foo
      import:
        ... # import-1
    - name: bar
      import:
        ... # import-2
    # ...
    - name: baz
      import:
        ... # import-N
  self:
    import:
      ... # self-import
```
Import keys are optional. If any of `import-1, ..., import-N` are missing,
west will not import additional manifest data from that project. If
`self-import` is missing, no additional files in the manifest repository
(beyond the top-level file) are imported.

The ultimate outcomes of resolving manifest imports are:

- a `projects` list, which is produced by combining the `projects` defined
  in the top-level file with those defined in imported files

- a set of extension commands, which are drawn from the `west-commands`
  keys in the top-level file and any imported files

- a `group-filter` list, which is produced by combining the top-level and any
  imported filters

Importing is done in this order:

#. Manifests from `self-import` are imported first.
#. The top-level manifest file's definitions are handled next.
#. Manifests from `import-1`, ..., `import-N`, are imported in that order.

When an individual `import` key refers to multiple manifest files, they are
processed in this order:

- If the value is a relative path naming a directory (or a map whose `file`
  is a directory), the manifest files it contains are processed in
  lexicographic order -- i.e., sorted by file name.
- If the value is a sequence, its elements are recursively imported in the
  order they appear.

This process recurses if necessary. E.g., if `import-1` produces a manifest
file that contains an `import` key, it is resolved recursively using the same
rules before its contents are processed further.

The following sections describe these outcomes.


#### Projects


This section describes how the final `projects` list is created.

Projects are identified by name. If the same name occurs in multiple manifests,
the first definition is used, and subsequent definitions are ignored. For
example, if `import-1` contains a project named `bar`, that is ignored,
because the top-level `west.yml` has already defined a project by that
name.

The contents of files named by `import-1` through `import-N` are imported
from Git at the latest `manifest-rev` revisions in their projects. These
revisions can be updated to the values `rev-1` through `rev-N` by running
`west update`. If any `manifest-rev` reference is missing or out of date,
`west update` also fetches project data from the remote fetch URL and updates
the reference.

Also note that all imported manifests, from the root manifest to the repository
which defines a project `P`, must be up to date in order for west to update
`P` itself. For example, this means `west update P` would update
`manifest-rev` in the `baz` project if `baz/west.yml` defines `P`,
as well as updating the `manifest-rev` branch in the local git clone of
`P`. Confusingly, updating `baz` may result in the removal of `P`
from `baz/west.yml`, which "should" cause `west update P` to fail with an
unrecognized project!

For this reason, it's not possible to run `west update P` if `P` is defined
in an imported manifest; you must update this project along with all the others
with a plain `west update`.

By default, west won't fetch any project data over the network if a project's
revision is a SHA or tag which is already available locally, so updating the
extra projects shouldn't take too much time unless it's really needed. See the
documentation for the update.fetch configuration
option for more information.


#### Extensions


All extension commands defined using `west-commands` keys discovered while
handling imports are available in the resolved manifest.

If an imported manifest file has a `west-commands:` definition in its
`self:` section, the extension commands defined there are added to the set of
available extensions at the time the manifest is imported. They will thus take
precedence over any extension commands with the same names added later on.


#### Group filters


The resolved manifest has a `group-filter` value which is the result of
concatenating the `group-filter` values in the top-level manifest and any
imported manifests.

Manifest files which appear earlier in the import order have higher precedence
and are therefore concatenated later into the final `group-filter`.

In other words, let:

- the submanifest resolved from `self-import` have group filter `self-filter`
- the top-level manifest file have group filter `top-filter`
- the submanifests resolved from `import-1` through `import-N` have group
  filters `filter-1` through `filter-N` respectively

The final resolved `group-filter` value is then ``filterN + ... + filter-2 +
filter-1 + top-filter + self-filter`, where `+`` here refers to list
concatenation.


**Important:** The order that filters appear in the above list matters. The last filter element in the final concatenated list "wins" and determines if the group is enabled or disabled.

For example, in `[-foo] + [+foo]`, group `foo` is *enabled*.
However, in `[+foo] + [-foo]`, group `foo` is *disabled*.

For simplicity, west and this documentation may elide concatenated group filter
elements which are redundant using these rules. For example, ``[+foo] +
[-foo]` could be written more simply as `[-foo]``, for the reasons given
above. As another example, `[-foo] + [+foo]` could be written as the empty
list `[]`, since all groups are enabled by default.

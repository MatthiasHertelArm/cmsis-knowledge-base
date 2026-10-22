---
id: "zep-west-manifests-manifest-imports"
type: "concept"
domain: "project"
title: "West Manifests: Manifest Imports"
summary: "You can use the import key briefly described above to include projects from other manifest files in your west.yml. This key can be either a project or self section attribute:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/manifest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/manifest.rst"
license: "Apache-2.0"
mode: "V"
---

You can use the `import` key briefly described above to include projects from
other manifest files in your `west.yml`. This key can be either a
`project` or `self` section attribute:

```yaml

manifest:
  projects:
    - name: some-project
      import: ...
  self:
    import: ...
```
You can use a "self: import:" to load additional files from the repository
containing your `west.yml`. You can use a "project: ... import:" to load
additional files defined in that project's Git history.

West resolves the final manifest from individual manifest files in this order:

#. imported files in `self`
#. your `west.yml` file
#. imported files in `projects`

During resolution, west ignores projects which have already been defined in
other files. For example, a project named `foo` in your `west.yml`
makes west ignore other projects named `foo` imported from your `projects`
list.

The `import` key can be a boolean, path, mapping, or sequence. We'll describe
these in order, using examples:

- Boolean

  - west-manifest-ex1.1
  - west-manifest-ex1.2
  - west-manifest-ex1.3

- Relative path

  - west-manifest-ex2.1
  - west-manifest-ex2.2
  - west-manifest-ex2.3

- Mapping with additional configuration

  - west-manifest-ex3.1
  - west-manifest-ex3.2
  - west-manifest-ex3.3
  - west-manifest-ex3.4

- Sequence of paths and mappings

  - west-manifest-ex4.1
  - west-manifest-ex4.2

A more formal description of how this works is
last, after the examples.

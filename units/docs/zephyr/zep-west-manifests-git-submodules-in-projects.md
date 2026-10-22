---
id: "zep-west-manifests-git-submodules-in-projects"
type: "concept"
domain: "project"
title: "West Manifests: Git Submodules in Projects"
summary: "You can use the submodules keys briefly described :ref:above <west-manifest-files> to force west update to also handle any Git submodules configured in project's git repository. The submodules key can appear inside projects, like this:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/manifest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/manifest.rst"
license: "Apache-2.0"
mode: "V"
---

You can use the `submodules` keys briefly described :ref:`above
<west-manifest-files>` to force `west update` to also handle any `Git
submodules`_ configured in project's git repository. The `submodules` key can
appear inside `projects`, like this:

```YAML

manifest:
  projects:
    - name: some-project
      submodules: ...
```
The `submodules` key can be a boolean or a list of mappings. We'll describe
these in order.


### Option 1: Boolean


This is the easiest way to use `submodules`.

If `submodules` is `true` as a `projects` attribute, `west update` will
recursively update the project's Git submodules whenever it updates the project
itself. If it's `false` or missing, it has no effect.

For example, let's say you have a source code repository `foo`, which has
some submodules, and you want `west update` to keep all of them in sync,
along with another project named `bar` in the same workspace.

You can do that with this manifest file:

```yaml

manifest:
  projects:
    - name: foo
      submodules: true
    - name: bar
```
Here, `west update` will initialize and update all submodules in `foo`. If
`bar` has any submodules, they are ignored, because `bar` does not have a
`submodules` value.


### Option 2: List of mappings


The `submodules` key may be a list of mappings, one list element for
each desired submodule. Each submodule listed is updated recursively.
You can still track and update unlisted submodules with `git` commands
manually; present or not they will be completely ignored by `west`.

The `path` key must match exactly the path of one submodule relative
to its parent west project, as shown in the output of ``git submodule
status`. The `name`` key is optional and not used by west for now;
it's not passed to `git submodule` commands either. The `name` key
was briefly mandatory in west version 0.9.0, but was made optional in 0.9.1.

For example, let's say you have a source code repository `foo`, which has
many submodules, and you want `west update` to keep some but not all of them
in sync, along with another project named `bar` in the same workspace.

You can do that with this manifest file:

```yaml

manifest:
  projects:
    - name: foo
      submodules:
        - path: path/to/foo-first-sub
        - name: foo-second-sub
          path: path/to/foo-second-sub
    - name: bar
```
Here, `west update` will recursively initialize and update just the
submodules in `foo` with paths `path/to/foo-first-sub` and
`path/to/foo-second-sub`. Any submodules in `bar` are still ignored.

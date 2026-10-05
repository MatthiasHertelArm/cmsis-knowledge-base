---
id: "zep-west-manifests-manifest-files"
type: "concept"
domain: "project"
title: "West Manifests: Manifest Files"
summary: "West manifests are YAML files. Manifests have a top-level manifest section with some subsections, like this:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/manifest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/manifest.rst"
license: "Apache-2.0"
mode: "V"
---

West manifests are YAML files. Manifests have a top-level `manifest` section
with some subsections, like this:

```yaml

manifest:
  remotes:
    # short names for project URLs
  projects:
    # a list of projects managed by west
  defaults:
    # default project attributes
  self:
    # configuration related to the manifest repository itself,
    # i.e. the repository containing west.yml
  version: "<schema-version>"
  group-filter:
    # a list of project groups to enable or disable
```
In YAML terms, the manifest file contains a mapping, with a `manifest`
key. Any other keys and their contents are ignored (west v0.5 also required a
`west` key, but this is ignored starting with v0.6).

The manifest contains subsections, like `defaults`, `remotes`,
`projects`, and `self`. In YAML terms, the value of the `manifest` key is
also a mapping, with these "subsections" as keys. As of west v0.10, all of
these "subsection" keys are optional.

The `projects` value is a list of repositories managed by west and associated
metadata. We'll discuss it soon, but first we will describe the `remotes`
section, which can be used to save typing in the `projects` list.

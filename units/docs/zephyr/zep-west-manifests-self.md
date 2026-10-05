---
id: "zep-west-manifests-self"
type: "concept"
domain: "project"
title: "West Manifests: Manifest Files / Self"
summary: "The self subsection can be used to control the manifest repository itself."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/manifest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/manifest.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Manifest Files_

The `self` subsection can be used to control the manifest repository itself.

As an example, let's consider this snippet from the zephyr repository's
`west.yml`:

```yaml

manifest:
  # ...
  self:
    path: zephyr
    west-commands: scripts/west-commands.yml
```
This ensures that the zephyr repository is cloned into path `zephyr`, though
as explained above that would have happened anyway if cloning from the default
manifest URL, `https://github.com/zephyrproject-rtos/zephyr`. Since the
zephyr repository does contain extension commands, its `self` entry declares
the location of the corresponding `west-commands.yml` relative to the
repository root.

The available `self` keys and their usage are in the following table.


* - Key
  - Description

* - `path`
  - Optional. The path `west init` should clone the manifest repository
    into, relative to the west workspace topdir.

    If not given, the basename of the path component in the manifest
    repository URL will be used by default. For example, if the URL is
    `https://git.example.com/project-repo`, the manifest repository would
    be cloned to the directory `project-repo`.

* - `west-commands`
  - Optional. This is analogous to the same key in a project sequence
    element.

* - `import`
  - Optional. This is also analogous to the `projects` key, but allows
    importing projects from other files in the manifest repository. See

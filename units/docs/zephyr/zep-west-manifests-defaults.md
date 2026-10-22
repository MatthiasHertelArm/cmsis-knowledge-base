---
id: "zep-west-manifests-defaults"
type: "concept"
domain: "project"
title: "West Manifests: Manifest Files / Defaults"
summary: "The defaults subsection can provide default values for project attributes. In particular, the default remote name and revision can be specified here. Another way to write the same manifest we have been describing so far using defaults is:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/manifest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/manifest.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Manifest Files_

The `defaults` subsection can provide default values for project
attributes. In particular, the default remote name and revision can be
specified here. Another way to write the same manifest we have been describing
so far using `defaults` is:

```yaml

manifest:
  defaults:
    remote: remote1
    revision: v1.3

  remotes:
    - name: remote1
      url-base: https://git.example.com/base1
    - name: remote2
      url-base: https://git.example.com/base2

  projects:
    - name: proj1
      description: the first example project
      path: extra/project-1
      revision: master
    - name: proj2
      description: |
        A multi-line description of the second example
        project.
      repo-path: my-path
      remote: remote2
    - name: proj3
      url: https://github.com/user/project-three
      revision: abcde413a111
```
The available `defaults` keys and their usage are in the following table.


* - Key
  - Description

* - `remote`
  - Optional. This will be used for a project's `remote` if it does not
    have a `url` or `remote` key set.

* - `revision`
  - Optional. This will be used for a project's `revision` if it does
    not have one set. If not given, the default is `master`.

---
id: "zep-west-manifests-remotes"
type: "concept"
domain: "project"
title: "West Manifests: Manifest Files / Remotes"
summary: "The remotes subsection contains a sequence which specifies the base URLs where projects can be fetched from."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/manifest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/manifest.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Manifest Files_

The `remotes` subsection contains a sequence which specifies the base URLs
where projects can be fetched from.

Each `remotes` element has a name and a "URL base". These are used to form
the complete Git fetch URL for each project. A project's fetch URL can be set
by appending a project-specific path onto a remote URL base. (As we'll see
below, projects can also specify their complete fetch URLs.)

For example:

```yaml

manifest:
  # ...
  remotes:
    - name: remote1
      url-base: https://git.example.com/base1
    - name: remote2
      url-base: https://git.example.com/base2
```
The `remotes` keys and their usage are in the following table.


* - Key
  - Description

* - `name`
  - Mandatory; a unique name for the remote.

* - `url-base`
  - A prefix that is prepended to the fetch URL for each
    project with this remote.
Above, two remotes are given, with names `remote1` and `remote2`. Their URL
bases are respectively `https://git.example.com/base1` and
`https://git.example.com/base2`. You can use SSH URL bases as well; for
example, you might use `git@example.com:base1` if `remote1` supported Git
over SSH as well. Anything acceptable to Git will work.

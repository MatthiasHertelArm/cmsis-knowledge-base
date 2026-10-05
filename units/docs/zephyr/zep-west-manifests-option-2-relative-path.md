---
id: "zep-west-manifests-option-2-relative-path"
type: "concept"
domain: "project"
title: "West Manifests: Manifest Imports / Option 2: Relative path"
summary: "The import value can also be a relative path to a manifest file or a directory containing manifest files. The path is relative to the root directory of the projects or self repository the import key appears in."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/manifest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/manifest.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Manifest Imports_

The `import` value can also be a relative path to a manifest file or a
directory containing manifest files. The path is relative to the root directory
of the `projects` or `self` repository the `import` key appears in.

Here is an example:

```yaml

manifest:
  projects:
    - name: project-1
      revision: v1.0
      import: west.yml
    - name: project-2
      revision: main
      import: p2-manifests
  self:
    import: submanifests
```
This will import the following:

- the contents of `project-1/west.yml` at `manifest-rev`, which points
  at tag `v1.0` after running `west update`
- any YAML files in the directory tree `project-2/p2-manifests`
  at the latest commit in the `main` branch, as fetched by `west update`,
  sorted by file name
- YAML files in `submanifests` in your manifest repository,
  as they appear on your file system, sorted by file name

Notice how `projects` imports get data from Git using `manifest-rev`, while
`self` imports get data from your file system. This is because as usual, west
leaves version control for your manifest repository up to you.

.. _west-manifest-ex2.1:


#### Example 2.1: Downstream of a Zephyr release with explicit path


This is an explicit way to write an equivalent manifest to the one in
west-manifest-ex1.1.

```yaml

manifest:
  remotes:
    - name: zephyrproject-rtos
      url-base: https://github.com/zephyrproject-rtos
  projects:
    - name: zephyr
      remote: zephyrproject-rtos
      revision: v1.14.1
      import: west.yml
```
The setting `import: west.yml` means to use the file `west.yml` inside
the `zephyr` project. This example is contrived, but shows the idea.

This can be useful in practice when the name of the manifest file you want to
import is not `west.yml`.

.. _west-manifest-ex2.2:


#### Example 2.2: Downstream with directory of manifest files


Your Zephyr downstream has a lot of additional repositories. So many, in fact,
that you want to split them up into multiple manifest files, but keep track of
them all in a single manifest repository, like this:

```none

my-repo/
├── submanifests
│   ├── 01-libraries.yml
│   ├── 02-vendor-hals.yml
│   └── 03-applications.yml
└── west.yml
```
You want to add all the files in `my-repo/submanifests` to the main
manifest file, `my-repo/west.yml`, in addition to projects in
`zephyr/west.yml`. You want to track the latest development code
in the Zephyr repository's `main` branch instead of using a fixed revision.

Here's how:

```yaml

# my-repo/west.yml:
manifest:
  remotes:
    - name: zephyrproject-rtos
      url-base: https://github.com/zephyrproject-rtos
  projects:
    - name: zephyr
      remote: zephyrproject-rtos
      revision: main
      import: true
  self:
    import: submanifests
```
Manifest files are imported in this order during resolution:

#. `my-repo/submanifests/01-libraries.yml`
#. `my-repo/submanifests/02-vendor-hals.yml`
#. `my-repo/submanifests/03-applications.yml`
#. `my-repo/west.yml`
#. `zephyr/west.yml`


**Note:** The `.yml` file names are prefixed with numbers in this example to make sure they are imported in the specified order. You can pick arbitrary names. West sorts files in a directory by name before importing.

Notice how the manifests in `submanifests` are imported *before*
`my-repo/west.yml` and `zephyr/west.yml`. In general, an `import`
in the `self` section is processed before the manifest files in `projects`
and the main manifest file.

This means projects defined in `my-repo/submanifests` take highest
precedence. For example, if `01-libraries.yml` defines `hal_nordic`,
the project by the same name in `zephyr/west.yml` is simply ignored. As
usual, see west-manifest-resolve for troubleshooting advice.

This may seem strange, but it allows you to redefine projects "after the fact",
as we'll see in the next example.

.. _west-manifest-ex2.3:


#### Example 2.3: Continuous Integration overrides


Your continuous integration system needs to fetch and test multiple
repositories in your west workspace from a developer's forks instead of your
mainline development trees, to see if the changes all work well together.

Starting with west-manifest-ex2.2, the CI scripts add a
file `00-ci.yml` in `my-repo/submanifests`, with these contents:

```yaml

# my-repo/submanifests/00-ci.yml:
manifest:
  projects:
    - name: a-vendor-hal
      url: https://github.com/a-developer/hal
      revision: a-pull-request-branch
    - name: an-application
      url: https://github.com/a-developer/application
      revision: another-pull-request-branch
```
The CI scripts run `west update` after generating this file in
`my-repo/submanifests`. The projects defined in `00-ci.yml` have
higher precedence than other definitions in `my-repo/submanifests`,
because the name `00-ci.yml` comes before the other file names.

Thus, `west update` always checks out the developer's branches in the
projects named `a-vendor-hal` and `an-application`, even if those same
projects are also defined elsewhere.

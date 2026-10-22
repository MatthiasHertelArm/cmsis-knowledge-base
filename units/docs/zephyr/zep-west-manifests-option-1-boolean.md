---
id: "zep-west-manifests-option-1-boolean"
type: "concept"
domain: "project"
title: "West Manifests: Manifest Imports / Option 1: Boolean"
summary: "This is the easiest way to use import."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/manifest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/manifest.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Manifest Imports_

This is the easiest way to use `import`.

If `import` is `true` as a `projects` attribute, west imports projects
from the `west.yml` file in that project's root directory. If it's
`false` or missing, it has no effect. For example, this manifest would import
`west.yml` from the `p1` git repository at revision `v1.0`:

```yaml

manifest:
  # ...
  projects:
    - name: p1
      revision: v1.0
      import: true    # Import west.yml from p1's v1.0 git tag
    - name: p2
      import: false   # Nothing is imported from p2.
    - name: p3        # Nothing is imported from p3 either.
```
It's an error to set `import` to either `true` or `false` inside
`self`, like this:

```yaml

manifest:
  # ...
  self:
    import: true  # Error
```
.. _west-manifest-ex1.1:


#### Example 1.1: Downstream of a Zephyr release


You have a source code repository you want to use with Zephyr v1.14.1 LTS.  You
want to maintain the whole thing using west. You don't want to modify any of
the mainline repositories.

In other words, the west workspace you want looks like this:

```none

my-downstream/
├── .west/                     # west directory
├── zephyr/                    # mainline zephyr repository
│   └── west.yml               # the v1.14.1 version of this file is imported
├── modules/                   # modules from mainline zephyr
│   ├── hal/
│   └── [...other directories..]
├── [ ... other projects ...]  # other mainline repositories
└── my-repo/                   # your downstream repository
    ├── west.yml               # main manifest importing zephyr/west.yml v1.14.1
    └── [...other files..]
```
You can do this with the following `my-repo/west.yml`:

```yaml

# my-repo/west.yml:
manifest:
  remotes:
    - name: zephyrproject-rtos
      url-base: https://github.com/zephyrproject-rtos
  projects:
    - name: zephyr
      remote: zephyrproject-rtos
      revision: v1.14.1
      import: true
```
You can then create the workspace on your computer like this, assuming
`my-repo` is hosted at `https://git.example.com/my-repo`:

```console

west init -m https://git.example.com/my-repo my-downstream
cd my-downstream
west update
```
After `west init`, `my-downstream/my-repo` will be cloned.

After `west update`, all of the projects defined in the `zephyr`
repository's `west.yml` at revision `v1.14.1` will be cloned into
`my-downstream` as well.

You can add and commit any code to `my-repo` you please at this point,
including your own Zephyr applications, drivers, etc. See application.

.. _west-manifest-ex1.2:


#### Example 1.2: "Rolling release" Zephyr downstream


This is similar to west-manifest-ex1.1, except we'll use ``revision:
main`` for the zephyr repository:

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
```
You can create the workspace in the same way:

```console

west init -m https://git.example.com/my-repo my-downstream
cd my-downstream
west update
```
This time, whenever you run `west update`, the special :ref:`manifest-rev
<west-manifest-rev>` branch in the `zephyr` repository will be updated to
point at a newly fetched `main` branch tip from the URL
https://github.com/zephyrproject-rtos/zephyr.

The contents of `zephyr/west.yml` at the new `manifest-rev` will then
be used to import projects from Zephyr. This lets you stay up to date with the
latest changes in the Zephyr project. The cost is that running `west update`
will not produce reproducible results, since the remote `main` branch can
change every time you run it.

It's also important to understand that west **ignores your working tree's**
`zephyr/west.yml` entirely when resolving imports. West always uses the
contents of imported manifests as they were committed to the latest
`manifest-rev` when importing from a project.

You can only import manifest from the file system if they are in your manifest
repository's working tree. See west-manifest-ex2.2 for an example.

.. _west-manifest-ex1.3:


#### Example 1.3: Downstream of a Zephyr release, with module fork


This manifest is similar to the one in west-manifest-ex1.1, except it:

- is a downstream of Zephyr 2.0
- includes a downstream fork of the `modules/hal/nordic`
  module which was included in that release

```yaml

# my-repo/west.yml:
manifest:
  remotes:
    - name: zephyrproject-rtos
      url-base: https://github.com/zephyrproject-rtos
    - name: my-remote
      url-base: https://git.example.com
  projects:
    - name: hal_nordic         # higher precedence
      remote: my-remote
      revision: my-sha
      path: modules/hal/nordic
    - name: zephyr
      remote: zephyrproject-rtos
      revision: v2.0.0
      import: true             # imported projects have lower precedence

# subset of zephyr/west.yml contents at v2.0.0:
manifest:
  defaults:
    remote: zephyrproject-rtos
  remotes:
    - name: zephyrproject-rtos
      url-base: https://github.com/zephyrproject-rtos
  projects:
  # ...
  - name: hal_nordic           # lower precedence, values ignored
    path: modules/hal/nordic
    revision: another-sha
```
With this manifest file, the project named `hal_nordic`:

- is cloned from `https://git.example.com/hal_nordic` instead of
  `https://github.com/zephyrproject-rtos/hal_nordic`.
- is updated to commit `my-sha` by `west update`, instead of
  the mainline commit `another-sha`

In other words, when your top-level manifest defines a project, like
`hal_nordic`, west will ignore any other definition it finds later on while
resolving imports.

This does mean you have to copy the `path: modules/hal/nordic` value into
`my-repo/west.yml` when defining `hal_nordic` there. The value from
`zephyr/west.yml` is ignored entirely. See west-manifest-resolve
for troubleshooting advice if this gets confusing in practice.

When you run `west update`, west will:

- update zephyr's `manifest-rev` to point at the `v2.0.0` tag
- import `zephyr/west.yml` at that `manifest-rev`
- locally check out the `v2.0.0` revisions for all zephyr projects except
  `hal_nordic`
- update `hal_nordic` to `my-sha` instead of `another-sha`

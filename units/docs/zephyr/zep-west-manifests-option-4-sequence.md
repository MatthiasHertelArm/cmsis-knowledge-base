---
id: "zep-west-manifests-option-4-sequence"
type: "concept"
domain: "project"
title: "West Manifests: Manifest Imports / Option 4: Sequence"
summary: "The import key can also contain a sequence of files, directories, and mappings."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/west/manifest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/west/manifest.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Manifest Imports_

The `import` key can also contain a sequence of files, directories,
and mappings.

.. _west-manifest-ex4.1:


#### Example 4.1: Downstream with sequence of manifest files


This example manifest is equivalent to the manifest in
west-manifest-ex2.2, with a sequence of explicitly named files.

```yaml

# my-repo/west.yml:
manifest:
  projects:
    - name: zephyr
      url: https://github.com/zephyrproject-rtos/zephyr
      import: west.yml
  self:
    import:
      - submanifests/01-libraries.yml
      - submanifests/02-vendor-hals.yml
      - submanifests/03-applications.yml
```
.. _west-manifest-ex4.2:


#### Example 4.2: Import order illustration


This more complicated example shows the order that west imports manifest files:

```yaml

# my-repo/west.yml
manifest:
  # ...
  projects:
    - name: my-library
    - name: my-app
    - name: zephyr
      import: true
    - name: another-manifest-repo
      import: submanifests
  self:
    import:
      - submanifests/libraries.yml
      - submanifests/vendor-hals.yml
      - submanifests/applications.yml
  defaults:
    remote: my-remote
```
For this example, west resolves imports in this order:

#. the listed files in `my-repo/submanifests` are first, in the order
   they occur (e.g. `libraries.yml` comes before
   `applications.yml`, since this is a sequence of files), since the
   `self: import:` is always imported first
#. `my-repo/west.yml` is next (with projects `my-library` etc. as long
   as they weren't already defined somewhere in `submanifests`)
#. `zephyr/west.yml` is after that, since that's the first `import` key
   in the `projects` list in `my-repo/west.yml`
#. files in `another-manifest-repo/submanifests` are last (sorted by file
   name), since that's the final project `import`

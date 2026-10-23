---
id: "zep-west-manifests-version"
type: "concept"
domain: "project"
title: "West Manifests: Manifest Files / Version"
summary: "The version subsection declares that the manifest file uses features which were introduced in some version of west."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/west/manifest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/west/manifest.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Manifest Files_

The `version` subsection declares that the manifest file uses features which
were introduced in some version of west. Attempts to load the manifest with
older versions of west will fail with an error message that explains the
minimum required version of west which is needed.

Here is an example:

```yaml

manifest:
  # Marks that this file uses version 0.10 of the west manifest
  # file format.
  #
  # An attempt to load this manifest file with west v0.8.0 will
  # fail with an error message saying that west v0.10.0 or
  # later is required.
  version: "0.10"
```
The pykwalify schema `manifest-schema.yml` in the `west source code
repository`_ is used to validate the manifest section.

Here is a table with the valid `version` values, along with information
about the manifest file features that were introduced in that version.


* - `version`
  - New features

* - `"0.7"`
  - Initial support for the `version` feature. All manifest file features
    that are not otherwise mentioned in this table were introduced in
    west v0.7.0 or earlier.

* - `"0.8"`
  - Support for `import: path-prefix:` (west-manifest-import-map)

* - `"0.9"`
  - **Use of west v0.9.x is discouraged**.

    This schema version is provided to allow users to explicitly request
    compatibility with west west_0_9_0. However, west
    that were introduced in west v0.9.0. You should ignore version "0.9" if
    possible.

* - `"0.10"`

  - Support for:

    - `submodules:` in `projects:` (west-manifest-submodules)
    - `manifest: group-filter:`, and `groups:` in `projects:`
      (west-manifest-groups)
    - The `import:` feature now supports `allowlist:` and
      `blocklist:`; these are respectively recommended as replacements for
      older names as part of a general Zephyr-wide inclusive language
      change. The older key names are still supported for backwards
      compatibility. (west-manifest-import,

* - `"0.12"`
  - Support for `userdata:` in `projects:` (west-project-userdata)

* - `"0.13"`
  - Support for `self: userdata:` (west-project-userdata)

* - `"1.0"`
  - Identical to `"0.13"`, but available for use by users that
    do not wish to use a `"0.x"` version field.

* - `"1.2"`
  - Support for `description:` in `projects:`
    (west-manifests-projects)

**Note:** Versions of west without any new features in the manifest file format do not change the list of valid `version` values. For example, `version: "0.11"` is **not** valid, because west v0.11.x did not introduce new manifest file format features.

Quoting the `version` value as shown above forces the YAML parser to treat it
as a string. Without quotes, `0.10` in YAML is just the floating point value
`0.1`. You can omit the quotes if the value is the same when cast to string,
but it's best to include them. Always use quotes if you're not sure.

If you do not include a `version` in your manifest, each new release of west
assumes that it should try to load it using the features that were available in
that release. This may result in error messages that are harder to understand
if that version of west is too old to load the manifest.

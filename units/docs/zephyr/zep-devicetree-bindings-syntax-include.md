---
id: "zep-devicetree-bindings-syntax-include"
type: "concept"
domain: "project"
title: "Devicetree bindings syntax: Include"
summary: "Bindings can include other files, which can be used to share common property definitions between bindings. Use the include: key for this. Its value is either a string or a list."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/dts/bindings-syntax.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/dts/bindings-syntax.rst"
license: "Apache-2.0"
mode: "V"
---

Bindings can include other files, which can be used to share common property
definitions between bindings. Use the `include:` key for this. Its value is
either a string or a list.

In the simplest case, you can include another file by giving its name as a
string, like this:

```YAML

include: foo.yaml
```
If any file named `foo.yaml` is found (see
dt-where-bindings-are-located for the search process), it will be
included into this binding.

Included files are merged into bindings with a simple recursive dictionary
merge. The build system will check that the resulting merged binding is
well-formed. It is allowed to include at any level, including `child-binding`,
like this:

```YAML

# foo.yaml will be merged with content at this level
include: foo.yaml

child-binding:
  # bar.yaml will be merged with content at this level
  include: bar.yaml
```
It is an error if a key appears with a different value in a binding and in a
file it includes, with two exceptions: a binding can have `required: true`
for a property definition for which the
included file has `required: false` (the `required: true` takes
precedence, allowing bindings to strengthen requirements from included
files), and `class:` values are unioned as described in
dt-bindings-class.

Note that weakening requirements by having `required: false` where the
included file has `required: true` is an error. This is meant to keep the
organization clean.

The file `base.yaml <dts/bindings/base/base.yaml>` contains
definitions for many common properties. When writing a new binding, it is a
good idea to check if `base.yaml` already defines some of the needed
properties, and include it if it does.

Note that you can make a property defined in base.yaml obligatory like this,
taking reg as an example:

```YAML

reg:
  required: true
```
This relies on the dictionary merge to fill in the other keys for `reg`, like
`type`.

To include multiple files, you can use a list of strings:

```YAML

include:
  - foo.yaml
  - bar.yaml
```
This includes the files `foo.yaml` and `bar.yaml`. (You can
write this list in a single line of YAML as `include: [foo.yaml, bar.yaml]`.)

When including multiple files, any overlapping `required` keys on properties
in the included files are ORed together. This makes sure that a ``required:
true`` is always respected.

In some cases, you may want to include some property definitions from a file,
but not all of them. In this case, `include:` should be a list, and you can
filter out just the definitions you want by putting a mapping in the list, like
this:

```YAML

include:
  - name: foo.yaml
    property-allowlist:
      - i-want-this-one
      - and-this-one
  - name: bar.yaml
    property-blocklist:
      - do-not-include-this-one
      - or-this-one
```
Each map element must have a `name` key which is the filename to include, and
may have `property-allowlist` and `property-blocklist` keys that filter
which properties are included.

You cannot have a single map element with both `property-allowlist` and
`property-blocklist` keys. A map element with neither `property-allowlist`
nor `property-blocklist` is valid; no additional filtering is done.

You can freely intermix strings and mappings in a single `include:` list:

```YAML

include:
  - foo.yaml
  - name: bar.yaml
    property-blocklist:
      - do-not-include-this-one
      - or-this-one
```
Finally, you can filter from a child binding like this:

```YAML

include:
  - name: bar.yaml
    child-binding:
      property-allowlist:
        - child-prop-to-allow
```

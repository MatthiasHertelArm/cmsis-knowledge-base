---
id: "ceed-paths"
type: "concept"
domain: "test"
title: "`:paths`"
summary: "Ceedling relies on various path and file collections to do its work. File collections are automagically assembled from paths, matching globs / wildcards, and file extensions. See project configuration :extension."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/paths.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/paths/"
license: "MIT"
mode: "V"
---

**Paths for build tools and building file collections**

Ceedling relies on various path and file collections to do its work. File
collections are automagically assembled from paths, matching globs / wildcards,
and file extensions. See [project configuration `:extension`](https://throwtheswitch.github.io/Ceedling/configuration/reference/paths/extension.md).

Entries in `:paths` help create directory-based bulk file collections. The
`:files` configuration section is available for filepath-oriented tailoring of
these bulk file collections.

Entries in `:paths` ↳ `:include` also specify search paths for header files.

All of the configuration subsections that follow default to empty lists. In
YAML, list items can be comma separated within brackets or organized per line
with a dash. An empty list can only be denoted as `[]`. Typically, you will see
Ceedling project files use lists broken up per line.

```yaml
:paths:
  :support: []    # Empty list (internal default)
  :source:
    - files/code  # Typical list format

```

!!! warning "Mixin order controls path list order"
    If you use Mixins to build up path lists in your project configuration,
    the merge order of those Mixins will dictate the ordering of your path
    lists. Particularly given that the search path list built with
    `:paths` ↳ `:include` you will want to pay attention to ordering issues
    involved in specifying path lists in Mixins.

---
id: "ceed-mixins-notes"
type: "concept"
domain: "test"
title: "`:mixins`: Notes"
summary: "[mixins-config-section]: ../mixins.md [inline-ruby-string-expansion]: ../project-file.md#inline-ruby-string-expansion"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/reference/mixins.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/mixins/#notes"
license: "MIT"
mode: "V"
---

* A `:mixins` section is only recognized within a base project configuration 
  file. Any `:mixins` sections within mixin files are ignored.
* A `:mixins` section in a Ceedling configuration is entirely filtered out of
  the resulting configuration. That is, it is unavailable for use by plugins
  and will not be present in any output from `ceedling dumpconfig`.
* A `:mixins` section supports [inline Ruby string expansion][inline-ruby-string-expansion].
  See the full documetation on Mixins for details.

[mixins-config-section]: ../mixins.md
[inline-ruby-string-expansion]: ../project-file.md#inline-ruby-string-expansion

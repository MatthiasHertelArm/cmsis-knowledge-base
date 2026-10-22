---
id: "ceed-project-global-project-settings-release-build"
type: "concept"
domain: "test"
title: "`:project`: Global project settings: `:release_build`"
summary: "When enabled, a release Rake task is exposed. This configuration option requires a corresponding release compiler and linker to be defined (gcc is used as the default)."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/project.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/project/#release-build"
license: "MIT"
mode: "V"
---

When enabled, a release Rake task is exposed. This configuration option requires
a corresponding release compiler and linker to be defined (`gcc` is used as the
default).

Ceedling is primarily concerned with facilitating the complicated mechanics of
automating unit tests. The same mechanisms are easily capable of building a
final release binary artifact (i.e. non test code — the thing that is your
final working software that you execute on target hardware). That said, if you
have complicated release builds, you should consider a traditional build tool
for these. Ceedling shines at executing test suites.

More release configuration options are available in the `:release_build` section.

**Default**: FALSE

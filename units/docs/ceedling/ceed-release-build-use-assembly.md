---
id: "ceed-release-build-use-assembly"
type: "concept"
domain: "test"
title: "`:release_build`: `:use_assembly`"
summary: "This option causes Ceedling to enable an assembler tool and add any assembly code present in the project to the release artifact's build."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/release-build.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/release-build/#use-assembly"
license: "MIT"
mode: "V"
---

This option causes Ceedling to enable an assembler tool and add any
assembly code present in the project to the release artifact's build.

The default assembler is the GNU tool `as`; it may be overridden
in the `:tools` section.

The assembly files must be visible to Ceedling by way of `:paths` and
`:extension` settings for assembly files.

**Default**: FALSE

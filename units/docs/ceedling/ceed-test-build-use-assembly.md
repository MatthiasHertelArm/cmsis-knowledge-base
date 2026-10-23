---
id: "ceed-test-build-use-assembly"
type: "concept"
domain: "test"
title: "`:test_build`: `:use_assembly`"
summary: "This option causes Ceedling to enable an assembler tool and collect a list of assembly file sources for use in a test suite build."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/reference/test-build.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/test-build/#use-assembly"
license: "MIT"
mode: "V"
---

This option causes Ceedling to enable an assembler tool and collect a
list of assembly file sources for use in a test suite build.

The default assembler is the GNU tool `as`; like all other tools, it
may be overridden in the `:tools` section.

After enabling this feature, two conditions must be true in order to
inject assembly code into the build of a test executable:

1. The assembly files must be visible to Ceedling by way of `:paths` and
   `:extension` settings for assembly files. Here, assembly files would be
   equivalent to C code files handled in the same ways.
1. Ceedling must be told into which test executable build to insert a
   given assembly file. The easiest way to do so is with the
   [`TEST_SOURCE_FILE()` build directive macro](https://throwtheswitch.github.io/Ceedling/configuration/reference/test-build/../../testing-guide/build-directives.md).

**Default**: FALSE

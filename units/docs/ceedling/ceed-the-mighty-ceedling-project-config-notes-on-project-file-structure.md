---
id: "ceed-the-mighty-ceedling-project-config-notes-on-project-file-structure"
type: "concept"
domain: "test"
title: "The Mighty Ceedling Project Configuration File: Notes on Project File Structure"
summary: "The Mighty Ceedling Project Configuration File: Notes on Project File Structure"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/project-file.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/project-file/#notes-on-project-file-structure"
license: "MIT"
mode: "V"
---

* Each of the following sections represent top-level entries
  in the YAML configuration file. Top-level means the named entries
  are furthest to the left in the hierarchical configuration file 
  (not at the literal top of the file).

* Unless explicitly specified in the configuration file by you, 
  Ceedling uses default values for settings.

* At minimum, these settings must be specified for a test suite:
    * `:project` ↳ `:build_root`
    * `:paths` ↳ `:source`
    * `:paths` ↳ `:test`
    * `:paths` ↳ `:include` and/or use of `TEST_INCLUDE_PATH(...)` 
      build directive macro within your test files

* At minimum, these settings must be specified for a release build:
    * `:project` ↳ `:build_root`
    * `:paths` ↳ `:source`

* As much as is possible, Ceedling validates your settings in
  properly formed YAML.

* Improperly formed YAML will cause a Ruby error when the YAML
  is parsed. This is usually accompanied by a complaint with
  line and column number pointing into the project file.

* Certain advanced features rely on `gcc` and `cpp` as preprocessing
  tools. In most Linux systems, these tools are already available.
  For Windows environments, we recommend the [MinGW] project
  (Minimalist GNU for Windows).

* Ceedling is primarily meant as a build tool to support automated
  unit testing. All the heavy lifting is involved there. Creating
  a simple binary release build artifact is quite trivial in
  comparison. Consequently, most default options and the construction
  of Ceedling itself is skewed towards supporting testing, though
  Ceedling can, of course, build your binary release artifact
  as well. Note that some complex binary release builds are beyond
  Ceedling's abilities. See the [`dependencies`](https://throwtheswitch.github.io/Ceedling/configuration/project-file/../plugins/dependencies.md)
  plugin for extending release build abilities.

[MinGW]: http://www.mingw.org/

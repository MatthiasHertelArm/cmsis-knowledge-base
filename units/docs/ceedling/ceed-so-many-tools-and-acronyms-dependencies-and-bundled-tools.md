---
id: "ceed-so-many-tools-and-acronyms-dependencies-and-bundled-tools"
type: "concept"
domain: "test"
title: "So Many Tools and Acronyms: Dependencies and Bundled Tools"
summary: "So Many Tools and Acronyms: Dependencies and Bundled Tools"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/overview/tools-and-frameworks.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/overview/tools-and-frameworks/#dependencies-and-bundled-tools"
license: "MIT"
mode: "V"
---

* By using the preferred installation options of the Ruby Ceedling gem or 
  the prepackaged Docker images, all Ceedling dependencies will be installed 
  for you. (See [installation section](https://throwtheswitch.github.io/Ceedling/overview/tools-and-frameworks/../getting-started/installation.md).)

* Regardless of installation method, Unity, CMock, and CException are bundled 
  with Ceedling. Ceedling is designed to glue them all together for your 
  project as seamlessly as possible.

* YAML support is included with Ruby. It requires no special installation
  or configuration. If your project file contains properly formatted YAML
  with the recognized names and options (see later sections), you are good 
  to go.

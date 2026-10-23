---
id: "ceed-loading-a-project-configuration-loading-smooshing-overview"
type: "concept"
domain: "test"
title: "Loading a Project Configuration: Loading & Smooshing Overview"
summary: "Ceedling has a certain pipeline for loading and manipulating the configuration it uses to build your projects. It goes something like this:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/loading.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/loading/#loading-smooshing-overview"
license: "MIT"
mode: "V"
---

Ceedling has a certain pipeline for loading and manipulating the 
configuration it uses to build your projects. It goes something like
this:

1. Load the base project configuration from a YAML file.
1. Merge the base configuration with zero or more Mixins from YAML files.
1. Load zero or more plugins that provide default configuration values
   or alter the base project configuration.
1. Populate the configuration with default values if anything was left
   unset to ensure all configuration needed to run is present.

Ceedling provides reasonably verbose logging at startup telling you which
configuration file and Mixins were used and in what order they were merged.
Similarly, it provides fairly robust validation and warning messages to
help you catch a broken configuration and problematic combinations of
settings.

For nitty-gritty details on plugin configuration behavior, see the
_[Plugin Development Guide](https://throwtheswitch.github.io/Ceedling/configuration/loading/../development/plugins/index.md)_

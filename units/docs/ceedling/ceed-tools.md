---
id: "ceed-tools"
type: "concept"
domain: "test"
title: "`:tools`"
summary: "Ceedling requires a variety of tools to work its magic. By default, the GNU toolchain (gcc, cpp, as — and gcov via plugin) are configured and ready for use with no additions to your project configuration YAML file."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/reference/tools.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/tools/"
license: "MIT"
mode: "V"
---

**Configuring command line tools used for build steps**

Ceedling requires a variety of tools to work its magic. By default, the GNU
toolchain (`gcc`, `cpp`, `as` — and `gcov` via plugin) are configured and ready
for use with no additions to your project configuration YAML file.

!!! tip "Mechanisms to configure tools without redefining them"
    Sometimes Ceedling’s built-in tool configurations are _nearly_ what you need 
    but not quite. 

    1. If you only need to add some arguments to all uses of a tool’s command
      line, Ceedling offers a shortcut to do so. See the
      [shortcuts section of `:tools`][tool-definition-shortcuts] documentation for
      details.
    1. If you need fine-grained control of the arguments Ceedling uses in the build
      steps for test executables, see the documentation for [`:flags`][flags].
      Ceedling allows you to control the command line arguments for each test
      executable build — with a variety of pattern matching options.
    1. If you need to link libraries — your own or standard options — please see the
      [top-level `:libraries` section][libraries] available for your project 
      configuration. Ceedling supports a number of useful options for working with
      pre-compiled libraries. If your library linking needs are super simple, the
      shortcut in (1) might be the simplest option.

[flags]: flags.md
[tool-definition-shortcuts]: #ceedling-tool-modification-shortcuts
[libraries]: libraries.md

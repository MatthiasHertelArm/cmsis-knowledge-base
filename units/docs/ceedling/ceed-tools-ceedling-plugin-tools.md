---
id: "ceed-tools-ceedling-plugin-tools"
type: "concept"
domain: "test"
title: "`:tools`: Ceedling plugin tools"
summary: "Ceedling plugins are free to define their own tools that are loaded into your project configuration at startup. Plugin tools are defined using the same mechanisms as Ceedling’s built-in tools and are called the same way."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/tools.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/tools/#ceedling-plugin-tools"
license: "MIT"
mode: "V"
---

Ceedling plugins are free to define their own tools that are loaded into your
project configuration at startup. Plugin tools are defined using the same
mechanisms as Ceedling’s built-in tools and are called the same way. That is,
all features available to you for working with tools as an end user are
generally available for working with plugin-based tools. This presumes a plugin
author followed guidance and convention in creating any command line actions.

---
id: "ceed-dependencies"
type: "concept"
domain: "test"
title: "Dependencies"
summary: "Plugin for supporting release dependencies. It’s rare for an embedded project to be built completely free of other libraries and modules. Some of these may be standard internal libraries. Some of these may be 3rd party libraries."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/dependencies.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/dependencies/"
license: "MIT"
mode: "V"
---

Plugin for supporting release dependencies. It’s rare for an embedded project to
be built completely free of other libraries and modules. Some of these may be
standard internal libraries. Some of these may be 3rd party libraries. In either
case, they become part of the project’s ecosystem.

This plugin is intended to make that relationship easier. It allows you to specify
a source for dependencies. If required, it will automatically grab the appropriate
version of that dependency.

Most 3rd party libraries have a method of building already in place. While we’d
love to convert the world to a place where everything downloads with a test suite
in Ceedling, that’s not likely to happen anytime soon. Until then, this plugin
will allow the developer to specify what calls Ceedling should make to oversee
the build process of those third party utilities. Are they using Make? CMake? A
custom series of scripts that only a mad scientist could possibly understand? No
matter. Ceedling has you covered. Just specify what should be called, and Ceedling
will make it happen whenever it notices that the output artifacts are missing.

Output artifacts? Sure! Things like static and dynamic libraries, or folders
containing header files that might want to be included by your release project.

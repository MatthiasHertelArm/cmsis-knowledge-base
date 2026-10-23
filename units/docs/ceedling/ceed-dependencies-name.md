---
id: "ceed-dependencies-name"
type: "concept"
domain: "test"
title: "Dependencies: Name"
summary: "As a YAML array of objects, each dependency begins with a dash, followed by its fields. By convention, :name comes first, which makes each dependency easy to spot."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/dependencies.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/dependencies/#name"
license: "MIT"
mode: "V"
---

As a YAML array of objects, each dependency begins with a dash, followed by its fields.
By convention, `:name` comes first, which makes each dependency easy to spot.

The name appears in Ceedling’s progress messages. Its letters, digits, and underscores
also name the dependency’s own tasks, so `Worker Bees` gets `dependencies:make:WorkerBees`.
A name therefore needs at least one letter or digit. Two dependencies whose names reduce
to the same task name stop the build with an error.

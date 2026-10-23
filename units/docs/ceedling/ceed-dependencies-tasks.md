---
id: "ceed-dependencies-tasks"
type: "concept"
domain: "test"
title: "Dependencies: Tasks"
summary: "Once configured, the plugin works on its own: a release or test build fetches and builds any dependency whose outputs are missing. These tasks let you act on dependencies directly."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/dependencies.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/dependencies/#tasks"
license: "MIT"
mode: "V"
---

Once configured, the plugin works on its own: a release or test build fetches and builds
any dependency whose outputs are missing. These tasks let you act on dependencies
directly. Each also works on a single dependency by its task name, such as
`dependencies:make:WorkerBees`.

### `ceedling dependencies:fetch`

Fetches each dependency that is not fetched yet. Dependencies without fetch settings, or
fetched by `:none`, are left alone.

### `ceedling dependencies:make`

Fetches each dependency if needed, then builds any whose outputs are missing. This
happens automatically in a release build, but is handy while you are configuring a
dependency.

### `ceedling dependencies:clean`

Removes a fetched dependency entirely, every one of its working paths, so the next build
fetches and builds it from scratch. A dependency fetched by `:none` keeps its source and
loses only its artifact path. A dependency without fetch settings is left alone.

### `ceedling dependencies:deploy`

Copies every dynamic library and executable of each dependency to its
[`:deploy` path](#working-paths), by default beside your release executable. An artifact
that has not been built is built first.

### `files:dependencies`

Lists every static library, dynamic library, and executable your dependencies provide.

### `paths:include`

Lists every header search path Ceedling uses, including those from dependencies.

### `files:include`

Lists every header file Ceedling has found, including those from dependencies.

---
id: "ceed-dependencies-tasks"
type: "concept"
domain: "test"
title: "Dependencies: Tasks"
summary: "Once configured correctly, the :dependencies plugin should integrate seamlessly into your workflow and you shouldn't have to think about it. In the real world, that doesn't always happen."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/dependencies.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/dependencies/#tasks"
license: "MIT"
mode: "V"
---

Once configured correctly, the `:dependencies` plugin should integrate seamlessly into your
workflow and you shouldn't have to think about it. In the real world, that doesn't always happen.
Here are a number of tasks that are added or modified by this plugin.

### `ceedling dependencies:clean`

This can be issued in order to completely remove the dependency from its source path. On the
next build, it will be refetched and rebuilt from scratch. This can also apply to a particular
dependency. For example, by specifying `dependencies:clean:DepName`.

### `ceedling dependencies:fetch`

This can be issued in order to fetch each dependency from its origin. This will have no effect on
dependencies that don't have fetch instructions specified. This can also apply to a particular
dependency. For example, by specifying `dependencies:fetch:DepName`.

### `ceedling dependencies:make`

This will force the dependencies to all build. This should happen automatically when a release
has been triggered... but if you're just getting your dependency configured at this moment, you
may want to just use this feature instead. A single dependency can also be built by specifying its
name, like `dependencies:make:MyTunaBoat`.

### `ceedling dependencies:deploy`

This will force any dynamic libraries produced by your dependencies to be copied to your release
build directory... just in case you clobbered them.

### `paths:include`

Maybe you want to verify that all the include paths are correct. If you query Ceedling with this
request, it will list all the header file paths that it’s found, including those produced by
dependencies.

### `files:include`

Maybe you want to take that query further and actually get a list of ALL the header files
Ceedling has found, including those belonging to your dependencies.

---
id: "ceed-dependencies-working-paths"
type: "concept"
domain: "test"
title: "Dependencies: Working Paths"
summary: "All paths are collected under :dependencies ↳ :paths. The :source field allows us to specify where the source code for each of our dependencies is stored."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/dependencies.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/dependencies/#working-paths"
license: "MIT"
mode: "V"
---

All paths are collected under `:dependencies` ↳ `:paths`. The `:source` field allows us 
to specify where the source code for each of our dependencies is stored. By default, it’s
the same as the `:fetch` path, which is where source will be fetched TO when fetching the 
dependency from elsewhere. All commands to build this dependency will be executed from
the `:source` location. Temporary data will be placed in the `:build` location. Unless you're
using one of Ceedling’s built-in builders, you'll need to learn where the tool you're using to
build places it’s built artifacts , and list that here. Finally, the output
artifacts will be referenced to this location. You override this by specifying a `:artifact`
path. In summary:

- `:paths`
    - `:fetch` -- where things are fetched to (defaults to `build/deps/depname/`)
    - `:source` -- where we trigger builds (defaults to `:fetch`)
    - `:build` -- where we have the produced build files (defaults to `<:fetch>/build`)
    - `:deploy` -- where any produced library files should be copied (defaults to same as release executable)
    - `:artifact` -- where output libraries can be found (defaults to `:build`)

If the dependency is directly included in your project (you've specified `:none` as the
`:method` for fetching), then `:source` should be where your Ceedling can find the
source for your dependency in you repo.

All artifacts are relative to the appropriate `:artifact` path. So if there are multiple 
include dirs, choose the highest level and make the rest relative from there.

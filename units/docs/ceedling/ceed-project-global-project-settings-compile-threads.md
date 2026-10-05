---
id: "ceed-project-global-project-settings-compile-threads"
type: "concept"
domain: "test"
title: "`:project`: Global project settings: `:compile_threads`"
summary: "A value greater than one enables parallelized build steps. Ceedling creates a number of threads up to :compile_threads for build steps. These build steps execute batched operations including but not limited to mock generation, code compilation, and running test executables."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/project.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/project/#compile-threads"
license: "MIT"
mode: "V"
---

A value greater than one enables parallelized build steps. Ceedling creates a
number of threads up to `:compile_threads` for build steps. These build steps
execute batched operations including but not limited to mock generation, code
compilation, and running test executables.

Particularly if your build system includes multiple cores, overall build time
will drop considerably as compared to running a build with a single thread.

Tuning the number of threads for peak performance is an art more than a
science. A special value of `:auto` instructs Ceedling to query the host
system's number of virtual cores. To this value it adds a constant of 4. This
is often a good value sufficient to "max out" available resources without
overloading available resources.

`:compile_threads` is used for all release build steps and all test suite build
steps except for running the test executables that make up a test suite. See
next section for more.

**Default**: 1

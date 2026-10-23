---
id: "ceed-ceedling-plugins-understanding-plugin-build-duplication"
type: "concept"
domain: "test"
title: "Ceedling Plugins: Understanding plugin build duplication"
summary: "Plugins including Gcov, Bullseye, Valgrind, and Sanitize recreate test build tasks. That is, the command line build task test:foo also exists as gcov:foo, bullseye:foo, valgrind:foo, and/or sanitize:foo if these plugins are enabled."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/index.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/#understanding-plugin-build-duplication"
license: "MIT"
mode: "V"
---

!!! warning
    Build-related plugins intentionally execute duplicated builds.

Plugins including [Gcov](https://throwtheswitch.github.io/Ceedling/plugins/gcov/index.md), [Bullseye](https://throwtheswitch.github.io/Ceedling/plugins/bullseye/index.md), [Valgrind](https://throwtheswitch.github.io/Ceedling/plugins/valgrind.md),
and [Sanitize](https://throwtheswitch.github.io/Ceedling/plugins/sanitize.md) recreate test build tasks. That is, the command line build task
`test:foo` also exists as `gcov:foo`, `bullseye:foo`, `valgrind:foo`, and/or `sanitize:foo`
if these plugins are enabled. Each of these triggers a full rebuild of the named test with 
instrumentation activated. **This duplication is intentional and very necessary.**

These plugins modify executable code or the environment in which a test suite 
executable runs. Duplicating and segregating the build tasks addresses several 
important issues:

1. **Conflicting interactions**. Enabling multiple plugins without 
   duplicated tasks (i.e. integrated build tasks) can bring about conflicts and
   undefined behavior. For instance, Gcov’s instrumentation does not
   necessarily play nice with Valgrind’s memory-instrumented emulation
   runtime, and the two should be kept entirely segregated. Likewise, a
   sanitizer-instrumented test executable cannot run under Valgrind at all.
2. **Unforeseen effects**. These plugins can directly alter the functioning of
   the code under test. For instance, coverage instrumentation inserted into
   your compiled code can alter its function or timing. As such, it is vital
   to maintain distinct builds to compare them. Your vanilla test suite build
   may function slightly differently than the coverage-instrumented build.
3. **Optional instrumentation**. The `<plugin>:` command line task convention
   also provides a very simple opt-in scheme. Plugins automatically enabled 
   for every build drives the desire to optional disable them. Valgrind testing
   can require 25-50x the execution time of a test suite, and you likely will
   want the option to easily disable it. While Ceedling could certainly provide
   that option at the command line for otherwise always-on plugins, this
   plugin task namespacing scheme naturally accomplished this along with the
   needs of (1) and (2).

!!! note
    A duplicated build task is a [delta build](https://throwtheswitch.github.io/Ceedling/plugins/../getting-started/builds.md).
    Ceedling skips unneeded work in a `gcov:`, `bullseye:`, `valgrind:`, or
    `sanitize:` build in the same way it does in a standard `test:` build.

Each of these plugins maintains its own separate delta build cache, apart from
plain test builds and from each other. A file with no role specific to a
given plugin will still be rebuilt the first you run that plugin’s build.
This happens because each build tracks state in its own dependency cache, 
not because of the file itself.

---

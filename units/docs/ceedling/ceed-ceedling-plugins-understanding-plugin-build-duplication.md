---
id: "ceed-ceedling-plugins-understanding-plugin-build-duplication"
type: "concept"
domain: "test"
title: "Ceedling Plugins: Understanding plugin build duplication"
summary: "Plugins including Gcov, Bullseye, and Valgrind recreate test build tasks. That is, the command line build task test:foo also exists as gcov:foo, bullseye:foo, and/or valgrind:foo if these plugins are enabled."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/index.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/#understanding-plugin-build-duplication"
license: "MIT"
mode: "V"
---

!!! warning
    Build-related plugins intentionally execute duplicated builds.

Plugins including [Gcov](https://throwtheswitch.github.io/Ceedling/plugins/gcov/index.md), [Bullseye](https://throwtheswitch.github.io/Ceedling/plugins/bullseye.md), and [Valgrind](https://throwtheswitch.github.io/Ceedling/plugins/valgrind.md)
recreate test build tasks. That is, the command line build task `test:foo` also exists 
as `gcov:foo`, `bullseye:foo`, and/or `valgrind:foo` if these plugins are enabled.
Each of these triggers a full rebuild of the named test with instrumentation 
activated. **This duplication is intentional and very necessary.**

These plugins modify executable code or the environment in which a test suite 
executable runs. Duplicating and segregating the build tasks addresses several 
important issues:

1. **Conflicting interactions**. Enabling multiple plugins without 
   duplicated tasks (i.e. integrated build tasks) can bring about conflicts and
   undefined behavior. For instance, Gcov’s instrumentation does not
   necessarily play nice with Valgrind’s memory-instrumented emulation
   runtime, and the two should be kept entirely segregated.
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

---

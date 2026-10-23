---
id: "ceed-sanitize-set-up"
type: "concept"
domain: "test"
title: "Sanitize: Set up"
summary: "The sanitizers are part of GCC and Clang. No separate installation is needed where your compiler provides them."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/sanitize.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/sanitize/#set-up"
license: "MIT"
mode: "V"
---

### Toolchain

The sanitizers are part of GCC and Clang. No separate installation is needed
where your compiler provides them.

- **Linux**: GCC or Clang with their sanitizer runtimes. Some distributions
  package these separately (e.g. `libasan` and `libubsan`).
- **macOS**: The Clang that ships with Xcode or the Command Line Tools.

The plugin runs each test executable through `env`, which sets the sanitizers’
runtime options. `env` is standard on Linux and macOS.

The `-plugins` variants of the [_MadScienceLab_ Docker images][docker-hub]
come with a ready toolchain.

[docker-hub]: https://hub.docker.com/repository/docker/throwtheswitch/

### Enable the plugin

Enable the plugin by adding `sanitize` to the enabled plugins list in your
project configuration:

```yaml
:plugins:
  :enabled:
    - sanitize
```

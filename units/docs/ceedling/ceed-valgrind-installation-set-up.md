---
id: "ceed-valgrind-installation-set-up"
type: "concept"
domain: "test"
title: "Valgrind: Installation & set up"
summary: "You have at least 3 options for getting the valgrind tool working on your system, including one readymade option."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/valgrind.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/valgrind/#installation-set-up"
license: "MIT"
mode: "V"
---

### Installation

You have at least 3 options for getting the `valgrind` tool working on your
system, including one readymade option.

#### Linux package manager

Install Valgrind from your Linux distribution’s package manager:

```shell
sudo apt-get install valgrind   # Debian / Ubuntu
sudo dnf install valgrind       # Fedora / RHEL
```

#### Build from source

Or build from source from [valgrind.org/downloads/](https://valgrind.org/downloads/).

#### _MadScienceLab_ Docker images

Fully packaged [_MadScienceLab_ Docker images][docker-hub] containing Ruby, 
Ceedling, the GCC toolchain, and more are available. The `-plugins` variants 
of the images come with all of Ceedling’s plugin tools preinstalled.

[docker-hub]: https://hub.docker.com/repository/docker/throwtheswitch/

### Enable the plugin

Enable the plugin by adding `valgrind` to the enabled plugins list in your
project configuration:

```yaml
:plugins:
  :enabled:
    - valgrind
```

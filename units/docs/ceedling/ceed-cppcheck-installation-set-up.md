---
id: "ceed-cppcheck-installation-set-up"
type: "concept"
domain: "test"
title: "Cppcheck: Installation & set up"
summary: "You have several options for getting the cppcheck tool working on your system, including one readymade option."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/cppcheck.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/cppcheck/#installation-set-up"
license: "MIT"
mode: "V"
---

### Installation

You have several options for getting the `cppcheck` tool working on your
system, including one readymade option.

#### Linux package manager

```shell
sudo apt-get install cppcheck   # Debian / Ubuntu
sudo dnf install cppcheck       # Fedora / RHEL
```

#### macOS

```shell
brew install cppcheck
```

#### Windows

```shell
choco install cppcheck
```

Alternatively, use the installer from [Cppcheck's site][cppcheck-download].

#### Build from source

Source releases are available from [Cppcheck's GitHub releases][cppcheck-releases].

#### _MadScienceLab_ Docker images

Fully packaged [_MadScienceLab_ Docker images][docker-hub] containing Ruby,
Ceedling, the GCC toolchain, and more are available. The `-plugins` variants
of the images come with all of Ceedling's plugin tools preinstalled.

!!! note "HTML reports need a second tool"
    The [`html`](#reports) report is produced by `cppcheck-htmlreport`, which
    ships alongside Cppcheck in most distributions. It is optional. Every other
    report format needs only `cppcheck` itself.

### Enable the plugin

Enable the plugin by adding `cppcheck` to the enabled plugins list in your
project configuration:

```yaml
:plugins:
  :enabled:
    - cppcheck
```

Enabling the plugin alone requires no Cppcheck installation. The executable is
only needed when a `cppcheck:` task actually runs.

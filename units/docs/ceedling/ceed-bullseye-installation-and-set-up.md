---
id: "ceed-bullseye-installation-and-set-up"
type: "concept"
domain: "test"
title: "Bullseye: Installation and set up"
summary: "Obtain an installer from [Bullseye's download page][bullseye-download]. Install and activate it following Licensing."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/bullseye/index.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/bullseye/#installation-and-set-up"
license: "MIT"
mode: "V"
---

### Install Bullseye

Obtain an installer from [Bullseye's download page][bullseye-download]. Install
and activate it following [Licensing](https://throwtheswitch.github.io/Ceedling/plugins/bullseye/licensing.md).

Bullseye's tools must be on your `PATH`. Ceedling's
[`:environment`](https://throwtheswitch.github.io/Ceedling/plugins/bullseye/../../configuration/reference/environment.md) settings can
also supply the path.

!!! note "Docker images"
    Ceedling's `madsciencelab-plugins` Docker image variants do not include
    Bullseye. This requires a license that a freely available image cannot carry. 
    Download Bullseye and then either extend the image or install into a running 
    container.
    See [Using Bullseye in a container](https://throwtheswitch.github.io/Ceedling/plugins/bullseye/licensing.md#using-bullseye-in-a-container).

### Enable the plugin

Add the plugin to your Ceedling project file.

```yaml
:plugins:
  :enabled:
    - bullseye
```

This alone creates the `bullseye:` tasks and prints console coverage summaries.
No further configuration is required.

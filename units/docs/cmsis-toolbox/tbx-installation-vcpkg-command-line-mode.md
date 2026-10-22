---
id: "tbx-installation-vcpkg-command-line-mode"
type: "concept"
domain: "project"
title: "Installation: vcpkg Command Line Mode"
summary: "Using vcpkg in Continuous Integration (CI) environments is basically like using it in a CLI environment."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/installation.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/installation/#vcpkg-command-line-mode"
license: "Apache-2.0"
mode: "V"
---

Using vcpkg in Continuous Integration (CI) environments is basically like [using it in a CLI environment](#vcpkg-setup-using-cli).

The way how `vcpkg artifacts` updates the current shell environment needs to be taken into account when creating CI
pipelines. The command `vcpkg-shell activate` updates the current environment variables by extending `PATH` and adding
additional variables required by installed artifacts. These modifications are only visible in the currently running
shell and spawned subprocesses.

This also enables manual usage on a local prompt, given a typical user runs subsequent commands from the same
parent shell process. In contrast, typical CI systems such as GitHub Actions or Jenkins spawn a new sub-shell for each
step of a pipeline. Hence, modifications made to the environment in one sub-shell by running the `vcpkg-shell activate`
command, does not persist in the subsequent steps.

Another aspect to consider is about handling the local vcpkg cache (e.g., `~/.vcpkg`). Common practice on CI systems is
to recreate a clean environment for each run. Hence, vcpkg and all required artifacts are re-downloaded on every run.
This may cause massive bandwidth requirements for downloading the same (huge) archives all the time. Instead, consider preserving the local vcpkg cache between runs.

### GitHub Actions

GitHub Actions allow you to preserve environment settings via the files
exposed in `$GITHUB_PATH` and `$GITHUB_ENV`. Refer to the custom action provided in [github.com/ARM-software/cmsis-actions - Action: vcpkg](https://github.com/ARM-software/cmsis-actions) for more information.

Preserving the runners between runs `vcpkg cache` is achieved with an `actions/cache` step preceding the
first `vcpkg-shell activate` command. The above custom action uses this `actions/cache` step.

### Other CI Systems

In CI Systems without a vcpkg integration:

- Keep all tool installations depending on an activated environment within the same shell block, or
- Repeat activation for each new shell block before running any dependent command.

```sh
. ~/.vcpkg/vcpkg-init
vcpkg-shell activate
```

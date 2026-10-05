---
id: "ethu-zephyr-build-in-arm-keil-studio-for-vs-code"
type: "concept"
domain: "edge-ai"
title: "Zephyr: Build in Arm Keil Studio for VS Code"
summary: "The CMSIS Solution extension can display, build, and debug a Zephyr application that uses the west build system. Install Zephyr in a central workspace, then set these entries under the CMSIS Solution Environment Variables user or workspace setting:"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/zephyr/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/zephyr/src/main.md#build-in-arm-keil-studio-for-vs-code"
license: "Apache-2.0"
mode: "V"
---

The CMSIS Solution extension can display, build, and debug a Zephyr application
that uses the `west` build system. Install Zephyr in a central workspace, then
set these entries under the CMSIS Solution **Environment Variables** user or
workspace setting:

| Variable | Typical Linux/macOS value |
|---|---|
| `ZEPHYR_BASE` | `$HOME/zephyrproject/zephyr` |
| `PATH` | `$HOME/zephyrproject/.venv/bin` |
| `VIRTUAL_ENV` | `$HOME/zephyrproject/.venv` |

On Windows, use `$HOME/zephyrproject/.venv/Scripts` for the virtual-environment
`PATH`. Adjust every path to the actual Zephyr workspace. The corresponding VS
Code setting is:

```json
"cmsis-csolution.environmentVariables": {
    "ZEPHYR_BASE": "$HOME/zephyrproject/zephyr",
    "PATH": "$HOME/zephyrproject/.venv/bin",
    "VIRTUAL_ENV": "$HOME/zephyrproject/.venv"
}
```

Copy or clone the application into the CMSIS solution workspace. In
`csolution.yml`, point a west project entry at the application directory:

```yaml
projects:
  - west:
      app-path: ./my-zephyr-application
```

Do not add a `cproject.yml` for the Zephyr application. The `west` entry owns
that build. See
[Work with Zephyr applications](https://mdk-packs.github.io/vscode-cmsis-solution-docs/zephyr.html)
for the current extension setup and build/debug workflow.

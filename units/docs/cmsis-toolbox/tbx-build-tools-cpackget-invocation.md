---
id: "tbx-build-tools-cpackget-invocation"
type: "concept"
domain: "project"
title: "Build Tools: `cpackget` Invocation"
summary: "Manage the installation of software packs on the host computer."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-tools.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-tools/#cpackget-invocation"
license: "Apache-2.0"
mode: "V"
---

Manage the installation of *software packs* on the host computer.

``` txt
cpackget version 2.2.1 (C) 2021-2023 Linaro, 2024-2026 Arm Ltd.

Usage:
  cpackget [command] [flags]

Available Commands:
  add              Add Open-CMSIS-Pack packages
  checksum-create  Generates a .checksum file containing the digests of a pack
  checksum-verify  Verifies the integrity of a pack using its .checksum file
  completion       Generate the autocompletion script for the specified shell
  connection       Check online connection to default or given URL
  help             Help about any command
  init             Initializes a pack root folder
  list             List installed packs
  rm               Remove Open-CMSIS-Pack packages
  signature-create Digitally signs a pack with a X.509 certificate or PGP key
  signature-verify Verifies a signed pack
  update           Update Open-CMSIS-Pack packages to latest
  update-index     Update the public index

Flags:
  -C, --concurrent-downloads uint   Number of concurrent batch downloads. Set to 0 to disable concurrency (default 20)
  -h, --help                        help for cpackget
  -R, --pack-root string            Specifies pack root folder. Defaults to CMSIS_PACK_ROOT environment variable.
  -q, --quiet                       Run cpackget silently, printing only error messages
  -T, --timeout uint                Set maximum duration (in seconds) of a download. Disabled by default
  -v, --verbose                     Sets verboseness level: None (Errors + Info + Warnings), -v (all + Debugging). Specify "-q" for no messages
  -V, --version                     Prints the version number of cpackget and exit

Use "cpackget [command] --help" for more information about a command and command-specific flags.
```

By default, `cpackget` reports warnings, errors, and a concise summary of operations and progress. Use `--verbose` to include debugging details or `--quiet` to print only error messages.

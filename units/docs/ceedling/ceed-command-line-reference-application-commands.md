---
id: "ceed-command-line-reference-application-commands"
type: "concept"
domain: "test"
title: "Command Line Reference: Application commands"
summary: "Because the built-in command line help is thorough, the following reference includes brief entries."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/reference/command-line.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/reference/command-line/#application-commands"
license: "MIT"
mode: "V"
---

!!! tip "Detailed command line help at the, well, command line"
    Ceedling provides robust help for application commands.
    Execute `ceedling help` for a summary view of all application commands.
    Execute `ceedling help <command>` for detailed help.

    Because the built-in command line help is thorough, the following 
    reference includes brief entries.

---

### [`ceedling [no arguments]`](../getting-started/command-line.md#ceedling-no-arguments)

Runs the default build tasks. Unless set in the project file, Ceedling 
uses a default task of `test:all`. To override this behavior, set your 
own default tasks in the project file (see later section). 

---

### [`ceedling <tasks...>`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-tasks)

Runs the named build tasks (i.e. `ceedling test:all`). Various option flags
exist to control project configuration loading, verbosity levels, 
logging, test task filters, etc.

See [next section](#build-plugin-tasks) to understand the build & plugin 
tasks this application command is able to execute. Run `ceedling help build` 
to understand all the command line flags that work with build & plugin tasks.

---

### [`ceedling build <tasks...>`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-build-tasks)

`ceedling build` is a verbose alias for the preceding. `build` is optional 
(i.e. `ceedling test:all` is equivalent to `ceedling build test:all`).

---

### [`ceedling check`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-check)

Process project configuration for validity and to check for any warnings
or automated overrides. No builds occur. Various option flags exist to 
control project configuration loading and configuration manipulation.

---

### [`ceedling dumpconfig`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-dumpconfig-filepath-sections)

Process project configuration and write final result to a YAML file. 
Various option flags exist to control project configuration loading,
configuration manipulation, and configuration sub-section extraction.

---

### [`ceedling environment`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-environment)

Lists project related environment variables:

* All environment variable names and string values added to your 
  environment from within Ceedling and through the `environment`
  section of your configuration. This is especially helpful in 
  verifying the evaluation of any string replacement expressions in
  your `environment` config entries.
* All existing Ceedling-related environment variables set before you
  ran Ceedling from the command line.

---

### [`ceedling example`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-example-name-dest)

Extracts an example project from within Ceedling to your local 
filesystem. The available examples are listed with 
`ceedling examples`. Various option flags control whether the example
contains vendored Ceedling and/or a documentation bundle.

---

### [`ceedling examples`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-examples)

Lists the available examples within Ceedling. To extract an example,
use `ceedling example`.

---

### [`ceedling help`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-help-command)

  Displays summary help for all application commands and detailed help 
  for each command. `ceedling help` also loads your project 
  configuration (if available) and lists all build tasks from it. 
  Various option flags control what project configuration is loaded.

---

### [`ceedling new`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-new-dest)

  Creates a new project structure. Various option flags control whether 
  the new project contains vendored Ceedling, a documentation bundle,
  and/or a starter project configuration file.

---

### [`ceedling upgrade`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-upgrade-path)

  Upgrade vendored installation of Ceedling for an existing project 
  along with any locally installed documentation bundles.

---

### [`ceedling version`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-version)

Displays version information for Ceedling and its components. Version 
output for Ceedling includes the Git Commit short SHA in Ceedling’s 
build identifier and Ceedling’s path of origin.

```
🌱 Welcome to Ceedling!

  Ceedling => #.#.#-<Short SHA>
  ----------------------
  <Ceedling install path>

  Build Frameworks
  ----------------------
       CMock => #.#.#
       Unity => #.#.#
  CException => #.#.#
```

If the short SHA information is unavailable such as in local 
development, the SHA is omitted. The source for this string is 
generated and captured in the Ruby Gem at the time of Ceedling’s 
automated build in CI.

---
id: "ceed-module-generator-overview"
type: "concept"
domain: "test"
title: "Module Generator: Overview"
summary: "Enable the plugin by adding module_generator to the enabled [plugins][plugins] list in your project configuration:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/module-generator.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/module-generator/#overview"
license: "MIT"
mode: "V"
---

Enable the plugin by adding `module_generator` to the enabled [plugins][plugins] list in
your project configuration:

```yaml
:plugins:
  :enabled:
    - module_generator
```

Then a single call creates a new module:

```sh
ceedling "module:create[MadScience]"
```

This creates `MadScience.c`, `MadScience.h`, and `test_MadScience.c`. The test file
carries your project’s [`:test_file_prefix`][test-file-prefix]. Names keep the case you type unless you
configure a [naming convention](#naming-convention).

Several modules can be named in one call, separated by commas. Leave no spaces between
the brackets or rely on surrounding quotes; your shell would otherwise split the command.

```sh
ceedling "module:create[MadScience,EvilGenius,SecretLair]"
```

The plugin’s three commands take the same arguments:

| Command | Does |
|---|---|
| `module:create[...]` | Creates each module’s files, skipping any that already exist and stopping when all of them do |
| `module:destroy[...]` | Removes each module’s files |
| `module:stub[...]` | Writes a source file of function stubs from each module’s header |
| `module:test[...]` | Writes a test file with a test for each function in each module’s header |

A name that begins with your test file prefix asks for a test file alone.
`"module:create[test_MadScience]"` creates only `test_MadScience.c`. When the prefix ends
in a letter or digit, as a prefix of `Test` does, the character after the prefix must
not be a lowercase letter or digit. An uppercase letter starts the module name, so
`TestMadScience` is a test file for `MadScience`, while `Testimony` and `Test2Widget`
are modules. A prefix ending in a separator, like the default `test_`,
needs no such check.

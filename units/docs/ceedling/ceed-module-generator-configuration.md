---
id: "ceed-module-generator-configuration"
type: "concept"
domain: "test"
title: "Module Generator: Configuration"
summary: "The module generator runs as-is with its defaults. Every setting lives under :module_generator in your project file:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/module-generator.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/module-generator/#configuration"
license: "MIT"
mode: "V"
---

The module generator runs as-is with its defaults. Every setting lives under
`:module_generator` in your project file:

| Setting | Purpose | Default |
|---|---|---|
| `:naming` | File [naming convention](#naming-convention) | none (names keep their case) |
| `:path_src`, `:path_inc`, `:path_tst` | [Default locations when no hint is given](#default-paths) | first path of each `:paths` list |
| `:includes` | [Headers every generated file includes](#includes) | none |
| `:boilerplates` | [Text at the top of every generated file](#boilerplates) | none |
| `:boilerplate_files` | [Files holding that text instead](#boilerplate-files) | none |
| `:test_define` | [Symbol guarding each test file](#test-defines) | `TEST` |
| `:test_guard` | [`#ifdef` or `#if` around each test file](#test-guards) | `:ifdef` |

### Naming convention

A naming convention keeps everyone’s file names consistent, whatever case a name is
typed in. Words are found at underscores, spaces, and changes of case, so
`mad_science` and `MadScience` name the same module.

```yaml
:module_generator:
  :naming: :bumpy
```

The options for `:naming`, and the source file each creates for this command:

```sh
ceedling "module:create[mad_science]"
```

| `:naming` | Style | Source file |
|---|---|---|
| `:bumpy` | BumpyFilesLookLikeSo | `MadScience.c` |
| `:camel` | camelFilesAreSimilarButStartLow | `madScience.c` |
| `:snake` | snake_case_is_all_lower_and_uses_underscores | `mad_science.c` |
| `:caps` | CAPS_FEELS_LIKE_YOU_ARE_SCREAMING | `MAD_SCIENCE.c` |

The header and test file follow the same convention, as do a pattern’s module names.
Without `:naming`, names keep the case you type.

### Default paths

`:path_src`, `:path_inc`, and `:path_tst` choose where files go when a command gives no
[hint](#path-hints). A hint still matches against your `:paths` and ignores these
settings.

```yaml
:module_generator:
  :path_src: src/
  :path_inc: include/
  :path_tst: test/
```

With these settings, this command:

```sh
ceedling "module:create[Widget]"
```

creates `src/Widget.c`, `include/Widget.h`, and `test/test_Widget.c`.

### Includes

Every generated file of a kind can include a standard list of headers. `:src` lists
those for source files, `:inc` for headers, and `:tst` for tests:

```yaml
:module_generator:
  :includes:
    :src:
      - board.h
    :inc:
      - types.h
    :tst:
      - defs.h
      - board.h
```

With these settings, this command:

```sh
ceedling "module:create[Widget]"
```

creates `Widget.c` including `board.h`, `Widget.h` including `types.h`, and
`test_Widget.c` including `defs.h` and `board.h`, each ahead of the module’s own
includes.

### Boilerplates

A boilerplate is text placed at the top of each generated file, the handy place for a
copyright notice. Each kind of file has its own. A boilerplate may contain `%1$s`, which
is replaced with the module name.

```yaml
:module_generator:
  :boilerplates:
    :src: |
      /***************************
      * %1$s
      * This file is Awesome.
      * That is All.
      ***************************/
    :inc: |
      /***************************
      * Header. Woo.             *
      ***************************/
    :tst: |
      /***************************
      * My Awesome Test For %1$s
      ***************************/
```

With these settings, this command:

```sh
ceedling "module:create[Widget]"
```

creates `Widget.c` beginning with the source boilerplate, its second line reading
`* Widget`, and `test_Widget.c` beginning with `* My Awesome Test For Widget`.

### Boilerplate files

A boilerplate can instead live in a file, which keeps long notices out of your project
file. `:boilerplate_files` names a file for any kind, and that file’s contents replace
the kind’s `:boilerplates` text. A named file that does not exist stops the command.

```yaml
:module_generator:
  :boilerplate_files:
    :src: config/boilerplate_source.txt
    :tst: config/boilerplate_test.txt
```

With these settings, this command:

```sh
ceedling "module:create[Widget]"
```

creates `Widget.c` beginning with the contents of `config/boilerplate_source.txt` and
`test_Widget.c` beginning with the contents of `config/boilerplate_test.txt`. `Widget.h`
uses the `:inc` boilerplate, if any.

### Test defines

Each generated test file is wrapped in `#ifdef TEST`. `:test_define` names a
different symbol.

```yaml
:module_generator:
  :test_define: CEEDLING_TEST
```

With this setting, this command:

```sh
ceedling "module:create[Widget]"
```

creates `test_Widget.c` wrapped in `#ifdef CEEDLING_TEST` and `#endif // CEEDLING_TEST`.

The symbol must be defined for your test builds, or every generated test compiles to
nothing. Add it under [`:defines`][defines] ↳ `:test`:

```yaml
:defines:
  :test:
    - CEEDLING_TEST
```

`module:create` and `module:test` warn about each generated test file whose build would
not define the symbol. Each file is checked as a test build would compile it, so a symbol
under a per-test matcher counts only for the test files that matcher matches.

### Test guards

Each generated test file is guarded with `#ifdef`. Some coding standards forbid `#ifdef`
in favor of `#if`, and `:test_guard` set to `:if` uses `#if` instead. The options are
`:ifdef` (the default) and `:if`.

```yaml
:defines:
  :test:
    - UNIT_TEST

:module_generator:
  :test_define: UNIT_TEST
  :test_guard: :if
```

With these settings, this command:

```sh
ceedling "module:create[Widget]"
```

creates `test_Widget.c` wrapped in `#if UNIT_TEST` and `#endif // UNIT_TEST`. With
`#if`, the symbol must be defined to a nonzero value. A bare `UNIT_TEST` under `:defines`
is defined as `1`.

[plugins]: ../configuration/reference/plugins.md
[paths]: ../configuration/reference/paths.md
[test-file-prefix]: ../configuration/reference/project.md#test_file_prefix
[cmock]: ../configuration/reference/cmock.md
[defines]: ../configuration/reference/defines.md

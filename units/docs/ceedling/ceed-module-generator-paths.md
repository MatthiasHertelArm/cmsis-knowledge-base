---
id: "ceed-module-generator-paths"
type: "concept"
domain: "test"
title: "Module Generator: Paths"
summary: "Without any hint, each kind of file goes to the first path listed for it under [:paths][paths]. Source files go to the first :source path, headers to the first :include path, and tests to the first :test path."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/module-generator.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/module-generator/#paths"
license: "MIT"
mode: "V"
---

Without any hint, each kind of file goes to the first path listed for it under
[`:paths`][paths]. Source files go to the first `:source` path, headers to the first `:include`
path, and tests to the first `:test` path. Headers go with the source when your project
lists no include paths. To choose other default locations, configure them:

```yaml
:module_generator:
  :path_src: src/
  :path_inc: include/
  :path_tst: test/
```

### Path hints

A hint before a colon steers a module toward matching paths:

```sh
ceedling "module:create[lab:SecretLair,mch]"
```

The hint is matched separately against your source, include, and test paths, and each
kind of file goes to the path the hint matches best. A path matches best when its
trailing folders match the hint. When the hint matches nothing among one kind of path,
those files go to the first path of that kind. When it matches nothing at all, the
command stops with an error and creates nothing.

Say your project lists these paths:

```yaml
:paths:
  :source:
    - lab/src
    - lair/src
    - other/src
  :test:
    - lab/test
    - lair/test
    - other/test
```

The `lab:` hint places files here:

- source files: `lab/src` (a close match)
- include files: `lab/src` (no include paths are listed, so headers go with the source)
- test files: `lab/test` (a close match)

Instead, say your paths look like this:

```yaml
:paths:
  :source:
    - src/**   # might contain subfolders lab, lair, and other
  :include:
    - inc/**   # might contain subfolders lab, lair, other, and shared
  :test:
    - test
```

Now the `lab:` hint places files here:

- source files: `src/lab` (a close match)
- include files: `inc/lab` (a close match)
- test files: `test` (no close match, so the first test path)

A few more notes about hints:

1. Several hints narrow the match through nested folders. `lab:secret:lair` places
   `lair.c` in a folder like `my/lab/secret/`.
2. Among equally good matches, and without any hint, the order of your paths in the
   project file decides.
3. With a `**` glob under `:paths`, the parent folder comes first, then its
   subfolders alphabetically, and so on.
4. A hint may be an absolute path, including one with a Windows drive letter, as in
   `C:/project/lab:SecretLair`.

More complicated structures will sometimes place a file in the wrong folder, and you
can move it afterward. A project with a consistent structure gets good placement.

### Adding to paths

A slash in the name, rather than a colon, names a subdirectory to use as given. The
module generator creates it if it does not exist. With the second set of paths above,
this call:

```sh
ceedling "module:create[newlab/SecretLair]"
```

creates these files:

- `src/newlab/SecretLair.c`
- `inc/newlab/SecretLair.h`
- `test/newlab/test_SecretLair.c`

A hint and a slash can combine, as in `lab:newlab/SecretLair`. A hint picks among
existing paths, and the slash then adds a subdirectory below the chosen path.

The module generator does not check whether a new subdirectory is covered by your
`:paths`. You can create files before updating your project file. You might also create
a file Ceedling does not see until you add its folder to `:paths`.

### Same-named files

`module:create` warns about each existing source, header, or test file elsewhere in your
project that shares a name with a file it is about to create, then creates the module.
Ceedling distinguishes same-named files by their paths, so this is allowed. The warning
catches the case where you meant to work with the existing module instead.

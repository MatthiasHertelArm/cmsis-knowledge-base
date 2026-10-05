---
id: "intr-automatically-format-and-lint-code-additional-hooks"
type: "concept"
domain: "debug"
title: "Automatically format and lint code with pre-commit: Additional hooks"
summary: "There are a few more hooks that are application-specific but provide a lot of value."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-10-27-pre-commit.md"
doc_source: "https://interrupt.memfault.com/blog/pre-commit#additional-hooks"
license: "CC-BY-SA-4.0"
mode: "V"
---

There are a few more hooks that are application-specific but provide a _lot_ of
value.

### clang-tidy

[clang-tidy](https://clang.llvm.org/extra/clang-tidy/) is a powerful C/C++
linter that can catch a lot of straightforward errors (ex: forgetting to
`close()` an open file descriptor). While not as sophisticated as full static
analysis checkers, such as [Code Checker](https://interrupt.memfault.com/blog/static-analysis-with-codechecker), it's quite useful.

Using it is a little complicated, depending on how your project is set up.
Generally, you'll need the following steps:

1. get your C/C++ sources compiling with Clang
2. generate a `compile_commands.json` file
3. run `clang-tidy` on the source files in question (with `pre-commit`!)

To drive steps 2 + 3 from `pre-commit`, here's an example
`.pre-commit-config.yaml` section:

```yaml
- repo: local
  hooks:
    # keep this before clang-tidy, it generates compile_commands.json for it.
    # requires the 'compiledb' tool, 'pip install compiledb'
    - id: compiledb
      name: compiledb
      entry: compiledb
      language: system
      args: [--overwrite, make, -n, -B]
      always_run: true
      require_serial: true
      pass_filenames: false

- repo: https://github.com/pocc/pre-commit-hooks
  rev: v1.3.5
  hooks:
    - id: clang-tidy
      args: [-checks=clang-diagnostic-return-type]
      files: src/.*\.c
```

Setting up and configuring `clang-tidy` can be difficult (you'll almost
certainly want a `.clang-tidy` configuration file). Here are some articles that
talk through the process:

- <https://developers.redhat.com/blog/2021/04/06/get-started-with-clang-tidy-in-red-hat-enterprise-linux#>
- <https://www.kdab.com/clang-tidy-part-1-modernize-source-code-using-c11c14/>
- <https://www.kdab.com/clang-tidy-part-1-modernize-source-code-using-c11c14/>

### cppcheck

```yaml
- repo: local
  hooks:
    - id: cppcheck
      name: cppcheck
      entry: cppcheck
      language: system
      args:
        [
          --enable=all,
          --suppress=unusedFunction,
          --suppress=unmatchedSuppression,
          --suppress=missingIncludeSystem,
          --suppress=toomanyconfigs,
          --error-exitcode=1,
        ]
      files: \.(c|h|cpp)$
```

The `cppcheck` hook relies on the `cppcheck` binary being available on the host
system (`sudo apt install cppcheck` on Ubuntu) - note the `- repo: local` and
`language: system` specifiers for the hook.

### Dockerfiles

If you're using Docker (eg for [reproducible builds](https://interrupt.memfault.com/blog/reproducible-firmware-builds) or CI), this provides a lot of nice
recommendations for Dockerfiles:

```yaml
- repo: https://github.com/pryorda/dockerfilelint-precommit-hooks
  rev: v0.1.0
  hooks:
    - id: dockerfilelint
```

### GitHub Actions

If you're using GitHub Actions for CI, these hooks do some validation on the
config files that can save some churn when testing new actions:

```yaml
- repo: https://github.com/sirosen/check-jsonschema
  rev: 0.28.2
  hooks:
    - id: check-github-actions
    - id: check-github-workflows
```

### Shellcheck

Some useful and quality-of-life checks for shell scripts:

```yaml
- repo: https://github.com/shellcheck-py/shellcheck-py
  rev: v0.10.0.1
  hooks:
    - id: shellcheck
```

### Mypy

If you're using Python type annotations, you can have mypy run in `pre-commit`:

```yaml
- repo: https://github.com/pre-commit/mirrors-mypy
  rev: "v0.931"
  hooks:
    - id: mypy
```

> Note: take a look at `dmypy` for a way to speed up mypy on larger projects,
> but be sure to test that it's working correctly for you:
> <https://mypy.readthedocs.io/en/stable/mypy_daemon.html>

---
id: "mlek-coding-standards-and-guidelines-static-analysis"
type: "concept"
domain: "edge-ai"
title: "Coding standards and guidelines: Static Analysis"
summary: "This repository uses pre-commit to run static-analysis and file-hygiene checks before each commit. The configured hooks currently cover:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/coding_guidelines.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/coding_guidelines.md#static-analysis"
license: "Apache-2.0"
mode: "V"
---

This repository uses [pre-commit](https://pre-commit.com/) to run static-analysis
and file-hygiene checks before each commit. The configured hooks currently cover:

- general file hygiene checks such as trailing whitespace, end-of-file, YAML, JSON,
  and merge-conflict validation
- `clang-format` for C and C++ formatting
- `cppcheck` for C and C++ static analysis
- `pylint` for Python linting

### Installing the pre-commit hook

Install `pre-commit` and register the repository hook:

```sh
python3 -m pip install pre-commit
pre-commit install
```

You can also install `pre-commit` using your system package manager
(for example `apt`, `dnf`, or `brew`) if you prefer.

This installs a Git `pre-commit` hook in `.git/hooks/`. Once installed, the checks
run automatically on the files staged for every `git commit`.

The first run may take longer because `pre-commit` creates isolated environments
for the configured tools and installs the hook dependencies automatically.

### Running the checks manually

You can run the checks independently of `git commit` at any time.

To run all configured hooks on all tracked files:

```sh
pre-commit run --all-files
```

To run the hooks only on the files currently staged for commit:

```sh
pre-commit run
```

To run a specific hook:

```sh
pre-commit run clang-format --all-files
pre-commit run cppcheck --all-files
pre-commit run pylint --all-files
```

To run hooks on a specific file:

```sh
pre-commit run --files path/to/file
```

### Working with hook failures

If a hook fails during `git commit`, the commit is aborted and the hook output
describes what needs to be fixed.

Some hooks may modify files automatically. For example, `clang-format` applies the
format defined in the repository's `.clang-format` file. If a hook updates a file,
review the changes, stage them, and rerun the commit.

You can still run `clang-format` directly if needed:

```sh
clang-format -style=file -i path/to/file
```

For `cppcheck` and `pylint`, address the reported issues and rerun `pre-commit`
until the checks pass cleanly.

---
id: "intr-automatically-format-and-lint-code-using-pre-commit"
type: "concept"
domain: "debug"
title: "Automatically format and lint code with pre-commit: Using `pre-commit`"
summary: "There are some wonderful instructions provided here:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-10-27-pre-commit.md"
doc_source: "https://interrupt.memfault.com/blog/pre-commit#using-pre-commit"
license: "CC-BY-SA-4.0"
mode: "V"
---

There are some wonderful instructions provided here:

> <https://pre-commit.com/#quick-start>

Briefly, here's how to set up and use the tool:

```bash
# install it with pip
python -m pip install pre-commit

# generate a sample config (you'll want to modify it)
pre-commit sample-config > .pre-commit-config.yaml

# activate pre-commit in a repository
pre-commit install

# pre-commit will now run on future `git commit` operations!

# optionally, the tool can be run standalone too:
# manually run pre-commit on the current checked-in files (git add'd).
pre-commit run

# run pre-commit on all files selected in the config
pre-commit run --all-files
```

See `pre-commit --help` for information on running the tool. A useful command is
`pre-commit autoupdate`, which will update all the checks to the latest tag!

Example run:

[(figure: img/pre-commit/pre-commit-example.png)](https://interrupt.memfault.com/img/pre-commit/pre-commit-example.png)

### Setup

`pre-commit` is configured with a file name `.pre-commit-config.yaml` at the
root of your repository.

This file selects the hooks to be installed + used, and contains other
configuration values such as paths to exclude from linting, etc. The
documentation here is the reference for config values:

> <https://pre-commit.com/index.html#adding-pre-commit-plugins-to-your-project>

For adding plugins, there's a registry of existing hooks maintained here:

> <https://pre-commit.com/hooks.html>

There are a _lot_ of existing hooks!

Note that individual tools will honor their normal configuration files (eg
`.prettierrc.yml`), so if you have some tools already set up, running them from
`pre-commit` will be the same.

### Example configuration

➡️ A configuration file with **all** the discussed checkers can be found
[here](https://github.com/memfault/interrupt/blob/master/example/pre-commit/.pre-commit-config.yaml).

For a C-and-python firmware repo, here's the config I typically start with:

```yaml
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks

# Don't run pre-commit on files under third-party/
exclude: "^\
  (third-party/.*)\
  "

repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: check-added-large-files # prevents giant files from being committed.
      - id: check-case-conflict # checks for files that would conflict in case-insensitive filesystems.
      - id: check-merge-conflict # checks for files that contain merge conflict strings.
      - id: check-yaml # checks yaml files for parseable syntax.
      - id: detect-private-key # detects the presence of private keys.
      - id: end-of-file-fixer # ensures that a file is either empty, or ends with one newline.
      - id: fix-byte-order-marker # removes utf-8 byte order marker.
      - id: mixed-line-ending # replaces or checks mixed line ending.
      - id: requirements-txt-fixer # sorts entries in requirements.txt.
      - id: trailing-whitespace # trims trailing whitespace.

  - repo: https://github.com/pre-commit/mirrors-prettier
    rev: v2.5.1
    hooks:
      - id: prettier
        files: \.(js|ts|jsx|tsx|css|less|html|json|markdown|md|yaml|yml)$

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.1
    hooks:
      - id: ruff
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-clang-format
    rev: v18.1.4
    hooks:
      - id: clang-format
```

The next subsections describe each check above.

#### Basic checks

From the `pre-commit-hooks` repo, these are basic text checks. Most are pretty
self-explanatory- I'm particularly fond of `trim-trailing-whitespace`, since my
editor is set up to do that when saving a file by default 😅.

If your repo has standalone scripts (`chmod +x`), the following additional
checks are quite useful (I've often goofed this up accidentally):

```yaml
- id: check-executables-have-shebangs # ensures that (non-binary) executables have a shebang.
- id: check-shebang-scripts-are-executable # ensures that (non-binary) files with a shebang are executable.
```

The `requirements-txt-fixer` hook only applies if your repository has a
`requirements.txt` file for Python packages.

Some other quite useful ones that are more situation-specific:

- `check-json` - if you have JSON files in your repo
- `check-merge-conflict` - useful if you often rebase/merge
- `check-symlinks` and `destroyed-symlinks` - very helpful if there's symlinks
  checked in to the index
- `check-vcs-permalinks` - particularly useful if there's a lot of documentation
  files tracked
- `file-contents-sorter` - if there are files that benefit from a reliable
  ordering, this is a handy hook

#### Prettier

`prettier` is a Javascript tool that can format many different language types. I
find it does a nice job on Markdown, Javascript, JSON, and YAML files in
particular.

Installing `prettier` can be a bit of a pain if you don't have `node` etc
already available; `pre-commit` manages the tool itself here, which is ✨
amazing ✨!

#### Python checks

- `ruff` - a Python linter that can catch a lot of common issues, and also
  formats and sorts imports. Replaces `flake8` and `isort` and `black` in one
  go!

Another very useful check is `pylint`:

```yaml
- repo: https://github.com/PyCQA/pylint
  rev: v3.1.0
  hooks:
    - id: pylint
```

However, you'll want to spend some quality time with your `.pylintrc` file to
tune to your needs. Out of the box pylint is very strict (but 100% compliance
often leads to nice code!).

There are a lot of other nice checkers available for python projects (eg
`bandit`), definitely worth looking through them.

#### clang-format

This runs the clang-format formatting tool over your C/C++ source files. You'll
probably want to add a `.clang-format` file to the base of your repo to
configure the tool; for example, here's what I usually use for my personal
projects:

```config
---
BasedOnStyle:  Google
---
Language: Cpp
...
```

That config is just selecting the Google C++ style built in to `clang-format`.

The hook provides its own copy of the `clang-format` binary, which means there's
no required setup outside of `pre-commit`! If you're managing your own
`clang-format` tools for your repo, you could instead call `clang-format` as a
`repo: local` + `language: system` hook.

To configure `clang-format`, either add a `.clang-format` file to the repo (the
[default](https://github.com/pre-commit/mirrors-clang-format/blob/ca42fca/.pre-commit-hooks.yaml#L6)),
or specify command-line options in the hook config (eg `args: ["-style=Google", "-i"]`).

Note that `clang-format` has a lot of configuration options. Recommendations for
how to tune a config is outside the scope of this article, but here's some
starting guidance:

- documentation: <https://releases.llvm.org/15.0.0/tools/clang/docs/ClangFormatStyleOptions.html>
- interactive configurator: <https://zed0.co.uk/clang-format-configurator/>
- generate a stub config with ex:
  `clang-format --style=Google --dump-config > .clang-format` (this will dump
  out _all_ the options set by that config. Optionally, the `BasedOnStyle:`
  option will set all of them to those values.

There's also a community-provided
[`clang-format-diff`](https://github.com/jlebar/pre-commit-hooks), which uses
the `git-clang-format` tool to only apply formatting to lines modified in the
current patch (if you're not ready to run a format pass across your entire
repo).

> Extra note: if you do run a whitespace or formatting pass over the entire
> repository, I recommend setting up a `.git-blame-ignore-revs` file, see here
> for more information:
 <https://michaelheap.com/git-ignore-rev/>

---
id: "intr-automatically-format-and-lint-code-why-format-lint-your-source-code"
type: "concept"
domain: "debug"
title: "Automatically format and lint code with pre-commit: Why format/lint your source code"
summary: "A lot of digital ink has been spilt on this topic, but to me, these are the reasons for performing automated styling (formatting) and linting-"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-10-27-pre-commit.md"
doc_source: "https://interrupt.memfault.com/blog/pre-commit#why-format-lint-your-source-code"
license: "CC-BY-SA-4.0"
mode: "V"
---

A lot of digital ink has been spilt on this topic, but to me, these are the
reasons for performing automated styling (formatting) and linting-

### 1. ♻️ Reduce churn in pull request reviews!

The **best** way to document a project's style is to have a tool automate it. If
a pull request has any style violations, we only need a single comment asking:

> Nit: could you run the formatter before merging?

Rather than commenting/suggesting changes on each violation.

It also reduces frustration and simplifies new developer onboarding (no
gatekeeping based on mysterious style choices in the repository).

Codebases should **prioritize** adding automated styling if there's a style
guide that is enforced. For example, Linux has the
["checkpatch.pl"](https://www.kernel.org/doc/html/latest/dev-tools/checkpatch.html)
tool that should always be run before submitting a patch.

### 2. 😪 Remove manual overhead for styling code

I think it's generally preferable to have a consistent style throughout a
codebase- automated styling makes it easy!

Most editors/IDE's will support a way to run styling (eg VSCode has the
`editor.formatOnSave` option, including supporting formatting
[only modified lines](https://code.visualstudio.com/updates/v1_49#_only-format-modified-text)).

### 3. 🐛 Catch bugs or typos

Aside from styling/formatting code, other tools provide checks such as:

- common security checks
- ensure parseable syntax in configuration files
- linting (static analysis checks)

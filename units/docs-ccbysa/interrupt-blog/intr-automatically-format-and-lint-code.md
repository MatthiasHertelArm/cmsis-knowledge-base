---
id: "intr-automatically-format-and-lint-code"
type: "concept"
domain: "debug"
title: "Automatically format and lint code with pre-commit"
summary: "I love clean and tidy codebases. I love them even more if I don't have to manually spend hours doing it myself."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-10-27-pre-commit.md"
doc_source: "https://interrupt.memfault.com/blog/pre-commit"
license: "CC-BY-SA-4.0"
mode: "V"
---

I love clean and tidy codebases. I love them even more if I don't have to
manually spend hours doing it myself. The problem is not everyone shares the
same love and passion for tidy codebases, especially when we're pressed for time
trying to get a new firmware build released.

This is where automated formatting and linting tools come in. These tools are
generally run in [continuous integration](https://interrupt.memfault.com/blog/continuous-integration-for-firmware) to make sure that all code
committed to the main branch follows the team's agreed-upon format and
structure. We can do one better and hook up these tools to run locally on any
commit or update to a version-controlled branch by using git hooks.

I'm here to talk about one of my favorite tools that is built upon git hooks,
[pre-commit](https://pre-commit.com/), and specifically to detail how you can
use it to format and lint firmware code as you program.



This article provides some background and guidelines for using `pre-commit` to
automatically format and lint C-language firmware codebases. We'll cover general
guidelines and go over an example set of checks that can be helpful when working
on firmware code.







> Note: jump to [Using `pre-commit`](#using-pre-commit) for the TLDR!

[(figure: img/pre-commit/pre-commit-pass.png)](https://interrupt.memfault.com/img/pre-commit/pre-commit-pass.png)

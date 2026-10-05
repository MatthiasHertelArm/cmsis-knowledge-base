---
id: "intr-automatically-format-and-lint-code-why-pre-commit"
type: "concept"
domain: "debug"
title: "Automatically format and lint code with pre-commit: Why `pre-commit`"
summary: "A typical software workflow might look like this:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-10-27-pre-commit.md"
doc_source: "https://interrupt.memfault.com/blog/pre-commit#why-pre-commit"
license: "CC-BY-SA-4.0"
mode: "V"
---

A typical software workflow might look like this:

1. **modify** source code
2. **commit changes** to version control (git)
3. **submit** changes to a remote repository (github PR, email list, etc)

A nice "neutral ground" point for running styling/linting is at step #2; there
are countless different methods for modifying source code, which makes it
complicated to integrate with any developer's particular setup (though there are
efforts in this space, eg [EditorConfig](https://editorconfig.org/)).

### git hooks

`git` has a notion of "hooks", which are scripts that run at specific points in
the `git` workflow, including just before committing:

> <https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks>

There are a couple of different tools that provide ways of adding checks at the
pre-commit stage, some examples:

- [husky](https://github.com/typicode/husky) and
  [lint-staged](https://github.com/okonet/lint-staged) (primarily js-focused)
- [Arcanist](https://secure.phabricator.com/book/phabricator/article/arcanist_lint/)
  (PHP-based, very powerful and customizable, can be difficult to configure)
- [overcommit](https://github.com/sds/overcommit) (Ruby-based, can be difficult
  to customize)

These all do the job, but have some complexities in setup and configuration that
make them a little difficult to install and use ☹️. The whole point is to
_reduce_ friction, after all!

### The `pre-commit` tool

I was in the process of adding Arcanist to a repo at one of my previous jobs
when my coworker (thanks Patrick!) pointed me to `pre-commit`:

> <https://pre-commit.com/>

I was immediately impressed. `pre-commit` really stands out in these areas:

- super simple setup
- easy and flexible configuration
- can be installed in a Python virtual environment, which our team was already
  using

It took about 10 minutes to add `pre-commit` to our repo, and it helped me keep
my patches clean and tidy!

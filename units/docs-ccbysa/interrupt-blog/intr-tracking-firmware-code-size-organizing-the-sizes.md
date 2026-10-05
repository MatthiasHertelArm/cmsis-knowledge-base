---
id: "intr-tracking-firmware-code-size-organizing-the-sizes"
type: "concept"
domain: "debug"
title: "Tracking Firmware Code Size: How to Track Code Size / Organizing the Sizes"
summary: "Our goal is to keep track of the sizes of the text, data, and bss regions for every commit and every build."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-18-code-size-deltas.md"
doc_source: "https://interrupt.memfault.com/blog/code-size-deltas#organizing-the-sizes"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: How to Track Code Size_

Our goal is to keep track of the sizes of the `text`, `data`, and `bss`
**regions** for every **commit** and every **build**. By storing the commit
revision and the build type, we can perform code size deltas between any
revisions built with the same configuration.

To ensure that we can calculate the deltas between commits properly, we also
need to keep track of the "parent" commit, since the commit that comes before it
in the `git log` is not necessarily the parent.

A commit's parent can be found using the following git command:

```
$ git rev-parse a2bc514653^1
c1fdf98ba5eb393a7646775921630bf4323ed832
```

To summarize, for every commit, we will store the following information for each
**commit and build** combination:

- `revision`: `a2bc51465395057e3830614b20ceea10976204bb`
- `parent_revision`: `c1fdf98ba5eb393a7646775921630bf4323ed832`
- `build`: `lwm2m_client`
- `text`: 130,780 B
- `data`: 3,356 B
- `bss`: 21,167 B

One thing to also be aware of is that if we want our code size deltas between
commits and pull request builds to always work, we need to ensure that **every
single commit** in the master branch that a developer could branch from has its
code size calculated and stored.

For better or worse, the Zehpyr Project has chosen the "Rebase and Merge"
strategy. This means that a pull-request can have many commits that don't
successfully build in CI. It also means that to successfully store code size
about every commit, we'll need to build
`count of pull requests * count of commits in each pull request` times in our CI
system.

> I've come around to Phabricator's
> ["One Idea is One Commit"](https://secure.phabricator.com/book/phabflavor/article/recommendations_on_revision_control/)
> philosophy, especially in large projects. It greatly simplifies release
> management and
> [reverts](https://github.com/zephyrproject-rtos/zephyr/commits/9b9436dfbe40a162b41ce6418839c5c1fd3d8d65).
> If this strategy is too heavy of a hammer, I suggest using merge commits.

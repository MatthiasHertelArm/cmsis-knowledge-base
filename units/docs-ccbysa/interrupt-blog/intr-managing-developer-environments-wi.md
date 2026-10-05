---
id: "intr-managing-developer-environments-wi"
type: "concept"
domain: "debug"
title: "Managing Developer Environments with Conda"
summary: "We've all had the experience of checking out an old release branch to debug an issue, only to find out that it depends on toolchains and packages that are no longer installed."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-01-07-conda-developer-environments.md"
doc_source: "https://interrupt.memfault.com/blog/conda-developer-environments"
license: "CC-BY-SA-4.0"
mode: "V"
---

We've all had the experience of checking out an old release branch to debug an
issue, only to find out that it depends on toolchains and packages that are no
longer installed. This can be a major pain, and people have come up with several
ways around it.

In previous posts,
[we have used virtualenv](https://interrupt.memfault.com/blog/using-pypi-packages-with-GDB#virtual-environment)
to manage our Python packages. What if you would like to easily manage non
Python dependencies? This is where Conda comes into play.



This post gives an introduction to what Conda is, explains why you should care
about keeping your developer environments in sync, and finally provides a
walk-through on getting started with Conda to set up a GCC based developer
environment.

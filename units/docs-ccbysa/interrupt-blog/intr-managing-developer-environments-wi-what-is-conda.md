---
id: "intr-managing-developer-environments-wi-what-is-conda"
type: "concept"
domain: "debug"
title: "Managing Developer Environments with Conda: What is Conda?"
summary: "Conda is a \"package, dependency and environment management for any language\"[^1]. It is most popular in the world of data science, but it can easily be used in any field, including firmware development!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-01-07-conda-developer-environments.md"
doc_source: "https://interrupt.memfault.com/blog/conda-developer-environments#what-is-conda"
license: "CC-BY-SA-4.0"
mode: "V"
---

(figure: Conda)

Conda is a "package, dependency and environment management for any
language"[^1]. It is most popular in the world of data science, but it can
easily be used in any field, including firmware development! Conda has become my
favorite way to manage the developer and continuous integration environments for
my firmware projects.

Conda is primarily used to manage Python distributions and environments. It can
either be used as a replacement for virtualenv[^2] or used alongside it if
necessary. It also provides `pip` so that PyPi packages can be installed as
well.

The primary benefit of using Conda over Virtualenv is its ability to install and
manage system binary packages that one may need in a developer environment, such
as the `arm-none-eabi-gcc` toolchain, `wget`, or Make.

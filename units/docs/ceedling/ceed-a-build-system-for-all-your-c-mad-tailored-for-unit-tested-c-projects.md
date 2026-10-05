---
id: "ceed-a-build-system-for-all-your-c-mad-tailored-for-unit-tested-c-projects"
type: "concept"
domain: "test"
title: "A Build System for All Your C Mad Scientisting Needs: “Tailored for unit-tested C projects”?"
summary: "Well, we like to write unit tests for our C code to make it lean and mean — that whole [Test-Driven Development][tdd] thing."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/overview/build-system.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/overview/build-system/#tailored-for-unit-tested-c-projects"
license: "MIT"
mode: "V"
---

Well, we like to write unit tests for our C code to make it lean and
mean — that whole [Test-Driven Development][tdd] thing.

Along the way, this style of writing C code spawned two
tools to make the job easier:

1. A unit test framework for C called _Unity_
1. A mocking library called _CMock_

And, though it's not directly related to testing, a C framework for 
exception handling called _CException_ also came along.

[tdd]: http://en.wikipedia.org/wiki/Test-driven_development

These tools and frameworks are great, but they require quite
a bit of environment support to pull them all together in a convenient,
usable fashion. We started off with Rakefiles to assemble everything.
These ended up being quite complicated and had to be hand-edited
or created anew for each new project. Ceedling replaces all that
tedium and rework with a configuration file that ties everything
together.

Though Ceedling is tailored for unit testing, it can also go right 
ahead and build your final binary release artifact for you as well. 
That said, Ceedling is more powerful as a unit test build environment 
than it is a general purpose release build environment. Complicated 
projects including separate bootloaders or multiple library builds, 
etc. are not necessarily its strong suit (but the 
[`dependencies`](https://throwtheswitch.github.io/Ceedling/overview/build-system/../plugins/dependencies.md) plugin can 
accomplish quite a bit here).

It's quite common and entirely workable to host Ceedling and your 
test suite alongside your existing release build setup. That is, you 
can use make, Visual Studio, SCons, Meson, etc. for your release build
and Ceedling for your test build. Your two build systems will simply
"point" to the same project code.

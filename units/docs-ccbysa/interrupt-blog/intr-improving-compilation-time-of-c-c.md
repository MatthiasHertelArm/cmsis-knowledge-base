---
id: "intr-improving-compilation-time-of-c-c"
type: "concept"
domain: "debug"
title: "Improving Compilation Time of C/C++ Projects"
summary: "We've all likely worked on a software or firmware project where the build takes a \"coffee break\" amount of time to complete. It's become such a common occurrence that there is an infamous xkcd comic related to the matter."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-02-11-improving-compilation-times-c-cpp-projects.md"
doc_source: "https://interrupt.memfault.com/blog/improving-compilation-times-c-cpp-projects"
license: "CC-BY-SA-4.0"
mode: "V"
---

We've all likely worked on a software or firmware project where the build takes
a "coffee break" amount of time to complete. It's become such a common
occurrence that there is an infamous [xkcd comic](https://xkcd.com/303/) related
to the matter.



Build times don't have to be long, even yours! However, many factors play a
role. In this post, we'll dive into which factors contribute to slower builds,
compare and contrast options, and also go over some easy wins which you can
immediately contribute to your project and share with your teammates. The
techniques discussed apply to most C/C++ compilers and projects, and there are a
couple extra tips for those using the GNU GCC compiler.



Hold on tight, as there is a lot to talk about.

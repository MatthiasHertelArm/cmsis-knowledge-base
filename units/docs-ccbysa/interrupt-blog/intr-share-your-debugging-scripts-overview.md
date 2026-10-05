---
id: "intr-share-your-debugging-scripts-overview"
type: "concept"
domain: "debug"
title: "Share Your Debugging Scripts: Overview"
summary: "Enabling the sharing of debugging techniques and scripts amongst the team is a 1 man-hour (and at max 1 day if you have a sad IDE or environment) effort to improve the productivity of every engineer on the team."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-04-21-sharing-gdb-scripts.md"
doc_source: "https://interrupt.memfault.com/blog/sharing-gdb-scripts#overview"
license: "CC-BY-SA-4.0"
mode: "V"
---

Enabling the sharing of debugging techniques and scripts amongst the team is a 1 man-hour (and at max 1 day if you have a sad IDE or environment) effort to improve the productivity of every engineer on the team. The best way to do this is to share a project-level `gdbinit` script that is loaded automatically when GDB is launched. It's even more powerful if the newly defined functions and commands have help menus and instructions about how to use them!

I won't go into how to define custom GDB commands because we've written about it in [a few posts](). This post is about how to share custom commands easily with your team.

It all starts with a single `project.gdbinit` file that is committed into the project's repository. When a debugger is launched with the project as its working directory, it can easily load the `project.gdbinit` on launch.

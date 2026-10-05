---
id: "intr-a-shallow-dive-into-gnu-make-recommendations"
type: "concept"
domain: "debug"
title: "A Shallow Dive into GNU Make: Recommendations"
summary: "A list of recommendations for getting the most of Make:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-03-gnu-make-guidelines.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-make-guidelines#recommendations"
license: "CC-BY-SA-4.0"
mode: "V"
---

A list of recommendations for getting the most of Make:

1. Targets should usually be real files.
2. Always use `$(MAKE)` when issuing sub-make commands.
3. Try to avoid using `.PHONY` targets. If the rule generates any file artifact,
   consider using that as the target instead of a phony name!
4. Try to avoid using implicit rules.
5. For C files, make sure to use `.d` automatic include tracking!
6. Use metaprogramming with caution.
7. Use automatic variables in rules. _Always_ try to use `$@` for a recipe
   output path, so your rule and Make have the exact same path.
8. Use comments liberally in Makefiles, especially if there is complicated
   behavior or subtle syntax used. Your co-workers (and future self) will thank
   you.
9. Use the `-j` or `-l` options to run Make in parallel!
10. Try to avoid using the `touch` command to track rule completion

---
id: "intr-zephyr-west-tips-and-tricks-aliases"
type: "concept"
domain: "debug"
title: "Zephyr West tips and tricks: Aliases"
summary: "West supports user-defined command aliases, similar to git aliases. These are great for shortening workflows you run constantly. From the docs:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2026-04-10-west-tips-and-tricks.md"
doc_source: "https://interrupt.memfault.com/blog/west-tips-and-tricks#aliases"
license: "CC-BY-SA-4.0"
mode: "V"
---

West supports user-defined command aliases, similar to `git` aliases. These are
great for shortening workflows you run constantly. From the docs:

```bash
west config --global alias.run "build --pristine=never --target run"
west config --global alias.menuconfig "build --pristine=never --target menuconfig"
```

After that, `west run` and `west menuconfig` just work. The alias docs have more
examples:
<https://docs.zephyrproject.org/latest/develop/west/alias.html#examples>

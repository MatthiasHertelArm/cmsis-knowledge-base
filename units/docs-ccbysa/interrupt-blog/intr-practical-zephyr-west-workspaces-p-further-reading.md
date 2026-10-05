---
id: "intr-practical-zephyr-west-workspaces-p-further-reading"
type: "concept"
domain: "debug"
title: "Practical Zephyr - West workspaces (Part 6): Further reading"
summary: "We've only covered the surface of what West can do for you. I very warmly recommend at least skimming through the following resources:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-16-practical_zephyr_west.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_west#further-reading"
license: "CC-BY-SA-4.0"
mode: "V"
---

We've only covered the surface of what _West_ can do for you. I very warmly recommend at least skimming through the following resources:

- Watch Mike Szczys' talk ["Manifests: Project Sanity in the Ever-Changing Zephyr World"](https://www.youtube.com/watch?v=PVhu5rg_SGY) from the 2022 Zephyr Developer Summit, lots of what you've read here comes from this presentation!
- If you like the `app` and `deps` separation, have a look at [Golioth's Zephyr training repository](https://github.com/golioth/zephyr-training) to see how it is applied in practice.
- Jonathan Beri also has a great [example `.vscode` configuration](https://github.com/beriberikix/zephyr-vscode-example) in case you're working with Visual Studio Code.
- Zephyr's own [example workspace application](https://github.com/zephyrproject-rtos/example-application) is of course also a great resource - and should be much more understandable now that you've read through this article.

Finally, have a look at the files in the example repositories used throughout this article:
- [practical-zephyr-t2-empty-ws](https://github.com/lmapii/practical-zephyr-t2-empty-ws) contains an empty _manifest_ repository for creating a dummy _West_ workspace that we'll use to explore _West_ without Zephyr.
- [practical-zephyr-manifest-repository](https://github.com/lmapii/practical-zephyr-manifest-repository) contains the _manifest repository_ of the Zephyr application that we're building in this article.

---
id: "intr-zephyr-west-tips-and-tricks-caching-west-update-fetches"
type: "concept"
domain: "debug"
title: "Zephyr West tips and tricks: Caching west update fetches"
summary: "If you clone west workspaces frequently (e.g., when testing unfamiliar projects), git fetch traffic can add up quickly. West supports a reference cache to share object storage across workspaces:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2026-04-10-west-tips-and-tricks.md"
doc_source: "https://interrupt.memfault.com/blog/west-tips-and-tricks#caching-west-update-fetches"
license: "CC-BY-SA-4.0"
mode: "V"
---

If you clone west workspaces frequently (e.g., when testing unfamiliar
projects), git fetch traffic can add up quickly. West supports a reference cache
to share object storage across workspaces:

```bash
west config --global update.auto-cache ~/.cache/west
```

With `auto-cache`, west will automatically populate and use a cache directory,
so subsequent `west update` calls in new workspaces can resolve most objects
locally instead of hitting the network.

There are a few other useful `update.*` config options worth looking at in the
reference:
<https://docs.zephyrproject.org/latest/develop/west/config.html#built-in-configuration-options>

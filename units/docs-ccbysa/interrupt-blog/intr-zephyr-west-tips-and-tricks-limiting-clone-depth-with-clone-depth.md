---
id: "intr-zephyr-west-tips-and-tricks-limiting-clone-depth-with-clone-depth"
type: "concept"
domain: "debug"
title: "Zephyr West tips and tricks: Limiting clone depth with `clone-depth`"
summary: "If you're working with large repositories or frequently initializing new workspaces, you can add clone-depth to projects in your west manifest to speed things up considerably:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2026-04-10-west-tips-and-tricks.md"
doc_source: "https://interrupt.memfault.com/blog/west-tips-and-tricks#limiting-clone-depth-with-clone-depth"
license: "CC-BY-SA-4.0"
mode: "V"
---

If you're working with large repositories or frequently initializing new
workspaces, you can add `clone-depth` to projects in your west manifest to speed
things up considerably:

```yaml
# west.yml
manifest:
  projects:
    - name: some-large-repo
      url: https://github.com/example/some-large-repo
      clone-depth: 1
```

Full manifest reference:
<https://docs.zephyrproject.org/latest/develop/west/manifest.html#projects>

> **Note:** I'm not sure whether `clone-depth` is respected for projects that
> are pulled in transitively via `import`. Worth verifying for your particular
> workspace setup.

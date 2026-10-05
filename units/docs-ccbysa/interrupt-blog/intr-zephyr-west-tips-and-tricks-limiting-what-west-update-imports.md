---
id: "intr-zephyr-west-tips-and-tricks-limiting-what-west-update-imports"
type: "concept"
domain: "debug"
title: "Zephyr West tips and tricks: Limiting what `west update` imports"
summary: "By default, if you import a project's manifest (e.g., Zephyr's west.yml), west will clone all of its listed dependencies recursively."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2026-04-10-west-tips-and-tricks.md"
doc_source: "https://interrupt.memfault.com/blog/west-tips-and-tricks#limiting-what-west-update-imports"
license: "CC-BY-SA-4.0"
mode: "V"
---

By default, if you import a project's manifest (e.g., Zephyr's `west.yml`), west
will clone _all_ of its listed dependencies recursively. Zephyr has a lot of
them, and a naive `west update` can easily pull down gigabytes worth of repos
you don't need.

Two manifest options that help a lot here:

**`name-allowlist`** - Only import the named projects from the upstream
manifest:

```yaml
# west.yml
manifest:
  projects:
    - name: zephyr
      url: https://github.com/zephyrproject-rtos/zephyr
      revision: v4.3.0
      import:
        name-allowlist:
          - cmsis
          - hal_nordic
          - mbedtls
```

This is
[Option 3 in the manifest docs](https://docs.zephyrproject.org/latest/develop/west/manifest.html#option-3-mapping)
and is probably the most useful thing you can do to keep workspace
initialization fast.

**`path-prefix`** - Put all imported projects under a common subdirectory
instead of the workspace root. Keeps things tidy:

```yaml
import:
  path-prefix: deps
  name-allowlist:
    - cmsis
    - hal_nordic
```

With the above, imported repos land under `deps/` rather than scattered at the
top level. The [Practical Zephyr - West
workspaces](https://interrupt.memfault.com/blog/practical_zephyr_west) article walks
through a full working example of both of these together.

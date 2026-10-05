---
id: "intr-zephyr-west-tips-and-tricks-resolving-the-manifest-to-exact-shas"
type: "concept"
domain: "debug"
title: "Zephyr West tips and tricks: Resolving the manifest to exact SHAs"
summary: "West manifests typically reference branches or tags, which can drift over time. To capture a fully-resolved snapshot with exact commit SHAs - useful for reproducible builds or auditing - use:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2026-04-10-west-tips-and-tricks.md"
doc_source: "https://interrupt.memfault.com/blog/west-tips-and-tricks#resolving-the-manifest-to-exact-shas"
license: "CC-BY-SA-4.0"
mode: "V"
---

West manifests typically reference branches or tags, which can drift over time.
To capture a fully-resolved snapshot with exact commit SHAs - useful for
reproducible builds or auditing - use:

```bash
west manifest --resolve
```

The output is a valid west manifest with every project pinned to a specific
revision:

```yaml
manifest:
  group-filter:
    - -babblesim
    - -optional
    - -testing
  projects:
    - name: canopennode
      url: https://github.com/zephyrproject-rtos/canopennode
      revision: dec12fa3f0d790cafa8414a4c2930ea71ab72ffd
      path: modules/lib/canopennode
      groups:
        - optional
    - name: chre
      url: https://github.com/zephyrproject-rtos/chre
      revision: c4c2f49fdcaa2fed49eb1db027696a5734a010d2
      path: modules/lib/chre
      groups:
        - optional
  # ...
```

You can redirect this into a `west.lock.yml` (or similar) and commit it
alongside your manifest so that anyone cloning the workspace gets exactly the
same tree.









{:.no_toc}

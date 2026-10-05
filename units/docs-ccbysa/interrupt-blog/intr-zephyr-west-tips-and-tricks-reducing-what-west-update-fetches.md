---
id: "intr-zephyr-west-tips-and-tricks-reducing-what-west-update-fetches"
type: "concept"
domain: "debug"
title: "Zephyr West tips and tricks: Reducing what `west update` fetches"
summary: "For day-to-day development you often don't need the full history of every dependency. You can speed up west update significantly with a couple of flags:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2026-04-10-west-tips-and-tricks.md"
doc_source: "https://interrupt.memfault.com/blog/west-tips-and-tricks#reducing-what-west-update-fetches"
license: "CC-BY-SA-4.0"
mode: "V"
---

For day-to-day development you often don't need the full history of every
dependency. You can speed up `west update` significantly with a couple of flags:

```bash
west update --narrow --fetch-opt=--depth=1
```

- `--narrow` tells west to only fetch the specific revision referenced in the
  manifest, rather than fetching all refs from the remote.
- `--fetch-opt=--depth=1` passes `--depth=1` to the underlying `git fetch`,
  giving you a shallow clone with just the tip commit.

Together these can dramatically cut down network traffic and disk usage,
especially on first initialization of a large workspace.

Use `git fetch --unshallow` on a module to convert a shallow clone to a full one
later- this is useful if you need the full history (eg bisecting) or want to
make a contribution upstream!

---
id: "intr-dealing-with-large-symbol-files-summary"
type: "concept"
domain: "debug"
title: "Dealing with Large Symbol Files: Summary"
summary: "In general, I think the best option to use is:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-03-30-dealing-with-large-symbol-files.md"
doc_source: "https://interrupt.memfault.com/blog/dealing-with-large-symbol-files#summary"
license: "CC-BY-SA-4.0"
mode: "V"
---

In general, I think the best option to use is:

```bash
objcopy --compress-debug-sections
```

This requires no changes when using the file- debuggers and binutils are all
good about unpacking the data, and worst case it can be reversed with
`--decompress-debug-sections`.

The `dwz` tool definitely performs nice optimizations on larger binaries, but it
seems to be very dependent on the specific file. In some cases it provides
_superb_ optimization.

The remaining strategies covered in this article are more situation-specific.

Hope you enjoyed reading this! I certainly learned a lot investigating these
tools.









{:.no_toc}

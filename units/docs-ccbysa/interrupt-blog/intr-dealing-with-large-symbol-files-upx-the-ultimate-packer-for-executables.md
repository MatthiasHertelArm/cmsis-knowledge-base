---
id: "intr-dealing-with-large-symbol-files-upx-the-ultimate-packer-for-executables"
type: "concept"
domain: "debug"
title: "Dealing with Large Symbol Files: `upx`: the \"Ultimate Packer for eXecutables\""
summary: "This tool compresses a binary file, adds a wrapper that's capable of unpacking it into memory at runtime, and bundles that into a standalone executable that when run behaves like the original binary."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-03-30-dealing-with-large-symbol-files.md"
doc_source: "https://interrupt.memfault.com/blog/dealing-with-large-symbol-files#upx-the-ultimate-packer-for-executables"
license: "CC-BY-SA-4.0"
mode: "V"
---

This tool compresses a binary file, adds a wrapper that's capable of unpacking
it into memory at runtime, and bundles that into a standalone executable that
when run behaves like the original binary.

It achieves great compression ratios:

```bash
❯ upx --preserve-build-id -o cmake.upx bin/cmake
❯ ls -lh bin/cmake cmake.upx*
-rwxrwxr-x 1 noah noah 179M Mar  2 14:46 bin/cmake
-rwxrwxr-x 1 noah noah  42M Mar  2 14:46 cmake.upx
```

It also preserves debug information (you have to decompress the file with
`upx -d` first though), what's not to love! (it does require certain features of
the host runtime environment so the executable can unpack itself into memory on
launch and before executing the compressed binary 😅).

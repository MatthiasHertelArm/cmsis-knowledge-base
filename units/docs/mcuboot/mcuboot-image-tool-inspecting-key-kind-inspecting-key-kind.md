---
id: "mcuboot-image-tool-inspecting-key-kind-inspecting-key-kind"
type: "concept"
domain: "boot-update"
title: "Image tool: [Inspecting key kind](#inspecting-key-kind)"
summary: "For build-system use, imgtool keyinfo reports whether a PEM contains private material (private) or only public material (public):"
status: "draft"
collection: "mcuboot"
source: "mcu-tools/mcuboot@ba2099f:docs/imgtool.md"
doc_source: "https://github.com/mcu-tools/mcuboot/blob/ba2099f/docs/imgtool.md#inspecting-key-kind-inspecting-key-kind"
license: "Apache-2.0"
mode: "V"
---

For build-system use, `imgtool keyinfo` reports whether a PEM contains
private material (`private`) or only public material (`public`):

    ./scripts/imgtool.py keyinfo -k some-key.pem

Pair with `--require private` or `--require public` to exit non-zero
when the kind does not match. The Zephyr port uses this to enforce that
every verification-only key passed via `CONFIG_BOOT_SIGNATURE_KEY_FILE`
past the first entry is a public-only PEM.

---
id: "x-validate-pdsc-sequence-xml-2"
type: "pattern"
domain: "pack"
title: "C-like block layout in PDSC sequences and its rg checks"
status: "draft"
extracted_from: "proc-validate-pdsc-sequence-xml"
source: "pack/validate-pdsc-sequence-xml/SKILL.md"
license: "Apache-2.0"
---

Require matching XML-tag alignment. Require C-like content to start after `<block>`, be indented one level inside it, use one semicolon-terminated statement per line, and preserve XML entities.

Run and inspect every relevant match from `rg -n '<block>.*;</block>' <target.pdsc>` and `rg -n '^[[:space:]]*[^<].*;.*;' <target.pdsc>`. Resolve each C-like match; one-line block bodies and multiple statements on one line fail validation.

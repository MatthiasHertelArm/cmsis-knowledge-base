---
id: "devt-pack-checking-tool-categories"
type: "concept"
domain: "pack"
title: "Pack Checking Tool: Error and Warning Messages / Categories"
summary: "Pack Checking Tool: Error and Warning Messages / Categories"
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/packchk/README.md#categories"
license: "Apache-2.0"
mode: "V"
---

_Part of: Error and Warning Messages_

<!-- markdownlint-capture -->
<!-- markdownlint-disable MD013 -->

| Code           | Category            | Description
|:---------------|:--------------------|:-----------------------------------
| M0xx           | Info messages       | Help and Progress messages. No action required.
| M1xx           | Internal errors     | Internal execution errors
| M2xx           | Invocation Errors   | Errors in the command line input.
| M3xx, M4xx     | Validation Messages | Errors and Warnings from the pack validation.
| M5xx           | Model Errors        | Errors in RTE model creation

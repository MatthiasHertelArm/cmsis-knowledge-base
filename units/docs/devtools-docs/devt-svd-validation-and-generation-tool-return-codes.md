---
id: "devt-svd-validation-and-generation-tool-return-codes"
type: "concept"
domain: "pack"
title: "SVD Validation and Generation Tool: Return Codes"
summary: "SVD Validation and Generation Tool: Return Codes"
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/svdconv/SVDConv/README.md#return-codes"
license: "Apache-2.0"
mode: "V"
---

SVDConv returns the following codes:

| Code |  Description |  Action |
|------|--------------|---------|
| 0 |  OK |  No action required. Validation and conversion performed without errors. |
| 1 |  WARNINGS |  Warnings should be checked an possibly removed. The header file is created and could be used. |
| 2 |  ERRORS |  Errors during validation or output generation. Check diagnostics and correct input or output options. |
| 3 |  Error in command line |  Check and correct the command line arguments. |

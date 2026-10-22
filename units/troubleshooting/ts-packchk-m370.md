---
id: "ts-packchk-m370"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M370: URL is not conformant: '…': Backslashes are not allowed in URL, use forward slashes."
status: "draft"
tool: "packchk"
severity: "warning"
code: "M370"
symptoms: ["M370", "URL is not conformant: '%URL%':   Backslashes are not allowed in URL, use forward slashes."]
symptom_regex: "^URL is not conformant: '.+?':   Backslashes are not allowed in URL, use forward slashes\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Use standard URL notation using forward slashes (/)."
summary: "The packchk tool found a URL in the PDSC (for example a release, license or other URL attribute) that contains a backslash character, which is not allowed in URL notation."
cause_origin: "source-analysis"
confidence: "medium"
---

## Symptom

`M370`
`URL is not conformant: '%URL%':   Backslashes are not allowed in URL, use forward slashes.`

## Cause

The packchk tool found a URL in the PDSC (for example a release, license or other URL attribute) that contains a backslash character, which is not allowed in URL notation. The variable %URL% is the offending URL string as written in the pack description.

## Fix

Open the PDSC file and replace every backslash in the reported URL with a forward slash, for example change https://example.com\docs\file.html to https://example.com/docs/file.html, then rerun packchk.

## Note

Source lines were not available, so the trigger and handling are taken from the message text and the README only. The README cause matches the message text. The exact PDSC attribute that carries the URL is not confirmed.

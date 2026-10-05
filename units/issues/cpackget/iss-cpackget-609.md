---
id: "iss-cpackget-609"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add: 'certificate signed by unknown authority' on old Debian image"
summary: "The pack server's certificate chain ends in a root CA that is missing from the CA store of that Debian 12 image (wget fails too; Debian 13 and Ubuntu work)."
status: "draft"
tool: "cpackget"
symptoms: ["E: Get \"https://itools.infineon.com/cmsis_packs/T2G-B-H/Infineon.T2G-B-H_DFP.1.2.1.pack\": tls: failed to verify certificate: x509: certificate signed by unknown authority"]
symptom_regex: "E:\\s+Get\\s+\".*?\":\\s+tls:\\s+failed\\s+to\\s+verify\\s+certificate:\\s+x509:\\s+certificate\\s+signed\\s+by\\s+unknown\\s+authority"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/609"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/609"
resolution: "workaround"
versions: "--insecure-skip-verify added in 2025/2026 releases"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: Get "https://itools.infineon.com/cmsis_packs/T2G-B-H/Infineon.T2G-B-H_DFP.1.2.1.pack": tls: failed to verify certificate: x509: certificate signed by unknown authority`

## Cause

The pack server's certificate chain ends in a root CA that is missing from the CA store of that Debian 12 image (wget fails too; Debian 13 and Ubuntu work). It is a host trust-store problem, not a pack problem.

## Fix

Update ca-certificates or the OS image so the issuing root is trusted. If that is impossible, use a cpackget/CMSIS-Toolbox build that has the --insecure-skip-verify option and accept the risk: cpackget add <pack> --insecure-skip-verify.

## Source

Resolution: workaround

Versions: --insecure-skip-verify added in 2025/2026 releases

From [Open-CMSIS-Pack/cpackget #609](https://github.com/Open-CMSIS-Pack/cpackget/issues/609), summarized in own words; confidence high, not reviewed yet.

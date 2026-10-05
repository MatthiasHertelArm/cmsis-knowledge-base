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
versions: "Debian 12 (bookworm) affected; Debian 13 and Ubuntu Server 24.04 work; --insecure-skip-verify verified with a CMSIS-Toolbox nightly build"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: Get "https://itools.infineon.com/cmsis_packs/T2G-B-H/Infineon.T2G-B-H_DFP.1.2.1.pack": tls: failed to verify certificate: x509: certificate signed by unknown authority`

## Cause

The pack server's certificate chain ends in a root CA that is missing from the CA store of that Debian 12 image (wget fails too; Debian 13 and Ubuntu work). It is a host trust-store problem, not a pack problem.

## Fix

Use an OS image whose CA store trusts the issuing root (the error did not occur on Debian 13 or Ubuntu Server 24.04). Otherwise use a cpackget with the --insecure-skip-verify option, at your own risk: cpackget add <pack> --insecure-skip-verify (verified with a CMSIS-Toolbox nightly build; the CMSIS-Toolbox release tested before lacked the option).

## Source

Resolution: workaround

Versions: Debian 12 (bookworm) affected; Debian 13 and Ubuntu Server 24.04 work; --insecure-skip-verify verified with a CMSIS-Toolbox nightly build

From [Open-CMSIS-Pack/cpackget #609](https://github.com/Open-CMSIS-Pack/cpackget/issues/609), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.

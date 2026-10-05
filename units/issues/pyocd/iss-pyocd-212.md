---
id: "iss-pyocd-212"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: gdbserver 'Errno 10013' socket access forbidden on Windows"
summary: "The GDB port (3333) could not be bound, typically because another service such as a VPN client already uses it."
status: "draft"
tool: "pyocd"
symptoms: ["ERROR:root:Unexpected exception: [Errno 10013] An attempt was made to access a socket in a way forbidden by its access permissions"]
symptom_regex: "Unexpected\\s+exception:\\s+\\[Errno\\s+\\S+\\]\\s+An\\s+attempt\\s+was\\s+made\\s+to\\s+access\\s+a\\s+socket\\s+in\\s+a\\s+way\\s+forbidden\\s+by\\s+its\\s+access\\s+permissions"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/212"
doc_source: "https://github.com/pyocd/pyOCD/issues/212"
resolution: "configuration"
versions: "0.8"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ERROR:root:Unexpected exception: [Errno 10013] An attempt was made to access a socket in a way forbidden by its access permissions`

## Cause

The GDB port (3333) could not be bound, typically because another service such as a VPN client already uses it.

## Fix

Choose another port with `-p`; the server then waits for gdb to connect, which is normal.

## Source

Resolution: configuration

Versions: 0.8

From [pyocd/pyOCD #212](https://github.com/pyocd/pyOCD/issues/212), summarized in own words; confidence low, not reviewed yet.

---
id: "iss-pyocd-212"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: gdbserver 'Errno 10013' socket access forbidden on Windows"
summary: "pyOCD could not bind the GDB port 3333, which points to another service holding that port (a maintainer saw this with a VPN client); for the reporter the problem later disappeared and its origin stayed unclear."
status: "draft"
tool: "pyocd"
symptoms: ["ERROR:root:Unexpected exception: [Errno 10013] An attempt was made to access a socket in a way forbidden by its access permissions"]
symptom_regex: "Unexpected\\s+exception:\\s+\\[Errno\\s+\\S+\\]\\s+An\\s+attempt\\s+was\\s+made\\s+to\\s+access\\s+a\\s+socket\\s+in\\s+a\\s+way\\s+forbidden\\s+by\\s+its\\s+access\\s+permissions"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/212"
doc_source: "https://github.com/pyocd/pyOCD/issues/212"
resolution: "configuration"
confidence: "low"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ERROR:root:Unexpected exception: [Errno 10013] An attempt was made to access a socket in a way forbidden by its access permissions`

## Cause

pyOCD could not bind the GDB port 3333, which points to another service holding that port (a maintainer saw this with a VPN client); for the reporter the problem later disappeared and its origin stayed unclear.

## Fix

Start the server on another port with -p (for example 3334); a server that then sits silently is just waiting for gdb to connect.

## Source

Resolution: configuration

From [pyocd/pyOCD #212](https://github.com/pyocd/pyOCD/issues/212), summarized in own words; confidence low, corrected against the thread, not reviewed yet.

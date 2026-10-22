---
id: "pyocd-debug-probes-unique-ids"
type: "concept"
domain: "debug"
title: "Debug probes: Unique IDs"
summary: "Every debug probe has a unique ID. For debug probes that connect with USB, this is nominally the same as its USB serial number. However, every debug probe plugin determines for itself what the unique ID means."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@a743211:docs/debug_probes.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/a743211/docs/debug_probes.md#unique-ids"
license: "Apache-2.0"
mode: "V"
---

Every debug probe has a **unique ID**. For debug probes that connect with USB, this is nominally the same as
its USB serial number. However, every debug probe plugin determines for itself what the unique ID means. Some
debug probes types are not connected with USB but are accessed across the network. In this case, the unique ID
is the probe's network address.

The unique ID parameter is actually a simple form of URL. It can be prefixed with the name of a debug probe plugin
followed by a colon, e.g. `cmsisdap:`, to restrict the type of debug probe that will match. This form is also a
requirement for certain probe types, such as the remote probe client, where the unique ID is a host address rather than
serial number.

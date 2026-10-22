---
id: "vela-vela-debug-database-ordering"
type: "concept"
domain: "edge-ai"
title: "Vela Debug Database: Ordering"
summary: "Note that the source, cmdstream and optimised tables are not ordered in any particular way. The insertion order of entries in the source and optimised tables is due to Vela's internal operation and does not represent a graph structure."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:DEBUG_DB.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/DEBUG_DB.md#ordering"
license: "Apache-2.0"
mode: "V"
---

Note that the `source`, `cmdstream` and `optimised` tables are not ordered in
any particular way.  The insertion order of entries in the `source` and
`optimised` tables is due to Vela's internal operation and does not represent a
graph structure.  The only ordered table is the `queue`; which is ordered by its
queue offset.  This table describes the execution order of the hardware
commands, and they can be mapped back to the optimised and source operators in
order to determine their execution order.

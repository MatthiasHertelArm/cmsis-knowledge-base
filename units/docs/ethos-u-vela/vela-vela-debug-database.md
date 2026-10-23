---
id: "vela-vela-debug-database"
type: "concept"
domain: "edge-ai"
title: "Vela Debug Database"
summary: "The purpose of the debug database is to track operator transformations during the optimisation process of Vela. This is later correlated with the trace output of the model, externally, to determine the runtime of the original layer operators."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:DEBUG_DB.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/DEBUG_DB.md"
license: "Apache-2.0"
mode: "V"
---

The purpose of the debug database is to track operator transformations during
the optimisation process of Vela.  This is later correlated with the trace
output of the model, externally, to determine the runtime of the original layer
operators.  Standalone, the debug database can be used in order to give a brief
overview of how the operators in the network change throughout the optimisation
process.  This document gives an overview of the structure of the database and
its outputs, to help parsing of the generated data in a debug procedure.

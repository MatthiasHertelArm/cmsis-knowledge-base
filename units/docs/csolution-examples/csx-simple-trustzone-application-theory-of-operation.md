---
id: "csx-simple-trustzone-application-theory-of-operation"
type: "concept"
domain: "project"
title: "Simple TrustZone Application: Theory of operation"
summary: "The output shows the transition from secure to non-secure execution followed by the function calls and their results in the non-secure application."
status: "draft"
collection: "csolution-examples"
source: "Open-CMSIS-Pack/csolution-examples@02f71b2:SimpleTrustZone/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/SimpleTrustZone/README.md#theory-of-operation"
license: "Apache-2.0"
mode: "V"
---

### Secure application

- Sets up and starts the non-secure application.

### Non-secure application

- Calls a secure function from the non-secure state.
- Calls a secure function that calls back to a non-secure function.

### Output

The output shows the transition from secure to non-secure execution followed by the function calls and their results in the non-secure application.

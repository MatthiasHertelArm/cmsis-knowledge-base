---
id: "mlek-deployment-semihosting"
type: "concept"
domain: "edge-ai"
title: "Deployment: Fixed Virtual Platform / Semihosting"
summary: "FVPs allow semihosting support which can be enabled by passing in additional command line arguments. Note that this needs to be enabled for the application being deployed too."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/deployment.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/deployment.md#semihosting"
license: "Apache-2.0"
mode: "V"
---

_Part of: Fixed Virtual Platform_

FVPs allow semihosting support which can be enabled by passing in additional command line arguments. Note that this
needs to be enabled for the application being deployed too.

* For `MPS3` based targets: `-C cpu0.semihosting-enable=1`
* For `MPS4` based targets: `-C mps4_board.subsystem.cpu0.semihosting-enable=1`

> **NOTE**: For some toolchains (e.g.: the GNU Arm Embedded Toolchain) it may be necessary to set these values too:
> * `MPS3`: `-C cpu0.semihosting-stack_base=0 -C cpu0.semihosting-stack_limit=0`
> * `MPS4`: `-C mps4_board.subsystem.cpu0.semihosting-stack_base=0 -C mps4_board.subsystem.cpu0.semihosting-stack_limit=0`
>
> Read more on this [here](https://developer.arm.com/documentation/ka005824/latest/).

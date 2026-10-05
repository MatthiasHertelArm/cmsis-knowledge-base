---
id: "threadx-appendix-e-threadx-smp-misra-c-com-building-threadx-smp-without-tx-misra-en"
type: "concept"
domain: "rtos"
title: "Appendix E - ThreadX SMP MISRA C compliance: MISRA C Overview / Building ThreadX SMP Without TX_MISRA_ENABLE"
summary: "Building ThreadX SMP without TX_MISRA_ENABLE has significant run-time performance advantages and is the default (and recommended) configuration for ThreadX SMP. When building in this manner, there are several mandatory MISRA C rules that are not met, including the following:"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/appendix-e.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/appendix-e.md#building-threadx-smp-without-tx-misra-enable"
license: "MIT"
mode: "V"
---

_Part of: MISRA C Overview_

Building ThreadX SMP without **_TX_MISRA_ENABLE_** has significant
run-time performance advantages and is the default (and recommended)
configuration for ThreadX SMP. When building in this manner, there are
several mandatory MISRA C rules that are not met, including the
following:

- **MISRA-C:2004** - 8.5a, 10.1a, 11.3, 12.13, 13.2d, 14.7, 17.4a
- **MISRA C:2012** - 10.3, 11.4, 13.3, 14.4d, 15.5, 17.7

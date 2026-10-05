---
id: "threadx-appendix-e-threadx-smp-misra-c-com-misra-c-overview"
type: "concept"
domain: "rtos"
title: "Appendix E - ThreadX SMP MISRA C compliance: MISRA C Overview"
summary: "MISRA C is a set of programming guidelines for critical systems using the C programming language."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/appendix-e.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/appendix-e.md#misra-c-overview"
license: "MIT"
mode: "V"
---

MISRA C is a set of programming guidelines for critical systems using
the C programming language. The original MISRA C guidelines were
primarily targeted toward automotive applications, however, MISRA C is
now widely recognized as being applicable to any safety critical
application. MISRA-C:2004 consists of 142 rules (122 are "required"
while 20 are "advisory"). MISRA C:2012 consists of 143 rules of varying
importance and 16 directives. ThreadX is compliant with all "required"
and "mandatory" rules of MISRA-C:2004 and MISRA C:2012. ThreadX is also
compliant with all but two "advisory" rules.

ThreadX SMP has nearly the same compliance, however, there are a two
"required" rule exceptions specific to ThreadX SMP implementation. These
are of low priority and are necessary for the reuse of the standard
ThreadX code base.

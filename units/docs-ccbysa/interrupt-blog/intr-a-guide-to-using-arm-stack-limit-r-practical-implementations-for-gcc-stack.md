---
id: "intr-a-guide-to-using-arm-stack-limit-r-practical-implementations-for-gcc-stack"
type: "concept"
domain: "debug"
title: "A Guide to Using ARM Stack Limit Registers: Practical implementations for GCC stack Canaries"
summary: "Implementing the ssp library does provide additional overhead in execution time and code space. A function will add 7 additional instructions to make use of this feature."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-02-14-using-psp-msp-limit-registers-for-stack-overflow.md"
doc_source: "https://interrupt.memfault.com/blog/using-psp-msp-limit-registers-for-stack-overflow#practical-implementations-for-gcc-stack-canaries"
license: "CC-BY-SA-4.0"
mode: "V"
---

Implementing the ssp library does provide additional overhead in execution time
and code space. A function will add 7 additional instructions to make use of
this feature. The developer should weigh these factors when choosing which
setting to use in GCC.

My preference would be to develop and test with a stricter setting and more
coverage and move to a more relaxed setting when getting closer to production.
For example, you could start your development process with
-fstack-protector-all, and later relax this to -fstack-protector-strong or
-fstack-protector as the code matures.

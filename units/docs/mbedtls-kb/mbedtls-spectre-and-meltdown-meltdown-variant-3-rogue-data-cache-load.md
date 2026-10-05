---
id: "mbedtls-spectre-and-meltdown-meltdown-variant-3-rogue-data-cache-load"
type: "concept"
domain: "security"
title: "Spectre and Meltdown: Meltdown (Variant 3: Rogue Data Cache Load)"
summary: "The Meltdown attack exploits microarchitectural data leaks in the processor's out-of-order execution machinery."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/attacks/spectre_and_meltdown.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/attacks/spectre_and_meltdown.md#meltdown-variant-3-rogue-data-cache-load"
license: "Apache-2.0"
mode: "V"
---

The Meltdown attack exploits microarchitectural data leaks in the processor's
out-of-order execution machinery. To mount the attack, the attacker needs a covert channel
where the sender end triggers a cache load at an address constructed using a
value from kernel memory. The code sequence provided in the Meltdown paper is
as follows [[1]]:

```
1 ; rcx = kernel address
2 ; rbx = probe array
3 retry:
4 mov al, byte [rcx]
5 shl rax, 0xc
6 jz retry
7 mov rbx, qword [rbx + rax]
```

In this code, the register `rcx` holds a kernel address, which is then used to
load a byte of kernel memory into the least significant byte of the `rax`
register in line 4. In line 5, the kernel data byte in `rax` is used to
construct an index into the `probe` array by performing a 12 bit shift left
(equivalent to multiplying by 4096 bytes, the page size), and the result is
written back to `rax`. Finally, a load from the `probe` array at the index in
`rax` is executed in line 7. Due to out-of-order execution, it is likely that
the transient instructions between lines 5-7 are executed before an exception
is raised, as a result of the invalid address in line 4. This small time window,
between the memory being accessed and the exception being raised, is all that is
needed to leak information.

To recover the secret data from the microarchitectural state into an
architectural one, the receiver end of the covert channel simply needs to run
the Flush+Reload cache timing side-channel attack to find out which cache line
from the `probe` array was loaded. The process is repeated to recover more
inaccessible data from an unprivileged process, yet the attacker must have a
mechanism to either catch or suppress the exception raised by the processor.

Unlike Spectre, the Meltdown attack can only recover protected data that is
mapped into the attacker process's memory space.
This means Meltdown can only be used to recover data
from the kernel pages mapped into the user's virtual memory.  However, in many
modern systems, a subset of the kernel addresses map to physical memory, in which
case, Meltdown can recover the contents of most (if not all) of the
physical memory. Given that other processes' data will reside in physical
memory, Meltdown can bypass the memory isolation between processes.

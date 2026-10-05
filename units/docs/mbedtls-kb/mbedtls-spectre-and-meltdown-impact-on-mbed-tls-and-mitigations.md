---
id: "mbedtls-spectre-and-meltdown-impact-on-mbed-tls-and-mitigations"
type: "concept"
domain: "security"
title: "Spectre and Meltdown: Impact on Mbed TLS and Mitigations"
summary: "At this time, there are no reports of Spectre and Meltdown-style attacks that have been successfully deployed on production systems, although proof-of-concept attacks have been created by researchers."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/attacks/spectre_and_meltdown.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/attacks/spectre_and_meltdown.md#impact-on-mbed-tls-and-mitigations"
license: "Apache-2.0"
mode: "V"
---

At this time, there are no reports of Spectre and Meltdown-style
attacks that have been successfully deployed on production systems, although
proof-of-concept attacks have been created by researchers. As a security
library, Mbed TLS could be a prime target for Spectre and Meltdown attacks attempting to
retrieve sensitive information, such as keys, passwords, decrypted data, etc.

It is important to highlight that the attacks discussed only impact processors
that implement out-of-order execution, in the case of Meltdown, and
branch prediction, in the case of Spectre. However, the microarchitecture of processors
varies significantly between vendors and even product lines. Therefore, we
recommend that you consult your vendor's documentation to confirm whether your
hardware is affected. The References section below has links to several
processor vendors' information pages: Arm [[5]], AMD [[8]] and Intel [[7]].

The remainder of this section analyzes the impact of Meltdown and Spectre on
affected systems and provides information on how to mitigate it.

### Spectre: Variants 1

This attack has been demonstrated using a JIT engine within the Linux kernel.
However, in practice, the attacker must manually inspect the victim's code that
is usable for the attack. The code should load a value using an untrusted
offset and use the result to form a second address, so that meaningful
information is leaked [[6]]. The most effective mitigation is to entirely avoid
such sequences of instruction, when possible. Depending on the architecture, 
you might also be able to implement instruction sequences, so
that data is not leaked by speculative execution. For example, in the case of
Arm, this can be achieved by using conditional selection or conditional move
instruction based on the condition that is used to determine the outcome of the
branch [[6]].

When it is not possible to use the above mitigation, the processor can
implement barrier instructions that prevent the speculation from taking place.
In the case of Intel x86, the Spectre paper suggests that the lfence and mfence
instructions prevent the attack [[2]]. It is also possible to use tools, such
as compilers, to insert these instructions where they are relevant. For example,
compiler support is being introduced into GCC and LLVM to mitigate this variant 
(for more information refer to [[10]]).

In the case of Mbed TLS, we have not yet found usable pieces of code for the
Spectre variant 1 of the attack.

### Spectre: Variant 2

As with Variant 1, the attacker must manually inspect the victim's code to
find usable pieces of transient instructions that can be connected in a
return-oriented programming fashion to leak information via the processor's
microarchitecture. The attacker must also train the branch predictor to predict
the wrong destination address for the selected branch instructions. This can be
achieved by a separate, unprivileged process, as access to the branch
predictor is generally not filtered. For the training to succeed, some
understanding of the branch prediction algorithm is required.  While this is a
closely guarded secret by many processor vendors, researchers have reverse
engineered enough information to successfully mount the attack.

Security updates for the major operating systems have been issued, and even
microcode updates for specific hardware have been released. Yet, these mitigations 
might only be partial, as in some cases, microarchitectural changes are required. 
From a software point of view, there are no definitive solutions to mitigating 
this attack. This is partially because branch predictors vary
significantly across architectures and even product lines. For example, Arm
recommends invalidating branch predictors when switching from privileged to
unprivileged processes, whenever possible, or disabling branch prediction
altogether [[6]]. However, both of these solutions are likely have a significant
impact on performance, and this feature is not always present in the underlying
system. We recommended consulting the vendor's documentation directly for
information specific to your processor. In some cases, it may be possible to
avoid indirect branches, but this is largely unfeasible, as these
branches are constructed by the compiler, and important steps in the toolchain,
such as linking, heavily depend on the capabilities of indirect branches.

### Meltdown: Variant 3

In many affected systems, the attackers can use Meltdown to read (but not
modify) the full contents held in physical RAM, including data that belongs to
other privileged or unprivileged processes. In the case of a system running
Mbed TLS, either as a client or as a server, the attacker can retrieve
confidential information in main memory, such as the TLS session keys. It
is also possible for the attacker to stimulate another application to load pages stored
in lower layers of the memory hierarchy (e.g the swap partition in a hard
drive) into the main memory, and then run the Meltdown attack to recover the
information. Once the attacker has recovered the confidential information, they
can use it in any way they please. For example, an attacker can use recovered
TLS sessions keys to spy on an open TLS connection, or AES keys to decrypt a
file. The attack is also independent of any software vulnerabilities, so that
conventional operating system security practices, such as address space
layout randomization, do not prevent Meltdown.

In practice, for Meltdown to work, the attacker must be given remote access 
and permission to execute an unprivileged program in the target computer.
Therefore, we recommended that Mbed TLS users maintain security best
practices, such as avoiding executing applications or code from untrusted
sources. The Meltdown attack also affects paravirtualized environments
(e.g Xen) and containers (e.g Docker), but not fully virtualized environments.
When running Mbed TLS in shared systems, such as is common in web hosting
services, we recommended ensuring that the underlying operating
system/environment has the latest security updates.

All major operating system vendors have released security updates to prevent the attack. 
Broadly speaking, the idea is to only map a small subset of the kernel address space into other processes'
virtual address space, so that the unprivileged processes cannot attempt to
access physical memory and leak its contents through the microarchitecture.
KAISER is a proof-of-concept of this idea, but unfortunately, this can have
a high impact on performance. KAISER enforces strict kernel and user space
isolation, so that user processes cannot access any kernel information, as this
is not held by the hardware [[4]].

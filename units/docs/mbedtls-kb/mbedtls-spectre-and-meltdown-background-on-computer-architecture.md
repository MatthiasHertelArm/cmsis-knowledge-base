---
id: "mbedtls-spectre-and-meltdown-background-on-computer-architecture"
type: "concept"
domain: "security"
title: "Spectre and Meltdown: Background on Computer Architecture"
summary: "Spectre and Meltdown exploit vulnerabilities in the hardware and some knowledge of processor optimization techniques is necessary for understanding the attacks."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/attacks/spectre_and_meltdown.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/attacks/spectre_and_meltdown.md#background-on-computer-architecture"
license: "Apache-2.0"
mode: "V"
---

Spectre and Meltdown exploit vulnerabilities in the hardware and some
knowledge of processor optimization techniques is necessary for understanding
the attacks. The following section provides this background
information, but can be safely skipped if you are already familiar with these concepts.

### Architecture vs Microarchitecture

Most software developers are familiar with the concept of an architecture, which
refers to the contract between a programmer and the underlying hardware in a
system. The architecture includes the Instruction Set Architecture (ISA) and
other important information, such as the memory consistency and input/output
models. However, there are usually many different implementations (or
microarchitectures) of an architecture. For example, the Arm Cortex-A53 and
Cortex-A57 processors are different microarchitectures of the ARMv8-A
architecture. While programmers can monitor aspects of the architecture, they 
cannot directly observe many aspects of a microarchitecture, such as caching, speculative
execution and branch prediction. These will be discussed below.

### Out-of-Order and Speculative Execution

In many architectures, such as Arm and x86, we expect processors to execute
instructions in sequential order as they appear in the execution path.  In
practice, however, advanced processors only give the illusion of sequential
execution. Internally, out-of-order execution techniques are used to reorder
operations whenever possible, to maximize the utilization of execution units,
and ultimately, the throughput of the processor.

It is common for out-of-order processors to also support speculative execution.
If the processor encounters a branch instruction, then before it can be fully
resolved, the processor guesses what execution path will be taken and
speculatively processes instructions along that path. When the branch is fully
resolved, the processor either continues executing as normal, if the guess was
correct, or reverts to the correct architectural state just after the execution
of the branch. However, side effects of the incorrect execution path remain
observable in the microarchitectural state, as this is not fully reverted, and this makes 
the Meltdown and Spectre attacks possible.

### Branch Prediction

Speculative execution requires the processor to guess the outcome of branch
instructions. Accurate predictions are desirable, as they improve
performance, and branch prediction techniques are used to increase said
accuracy.

In a simple scenario, branch predictors always predict the same outcome. For
example, if they always predict that branches to lower and higher addresses are
taken and not taken respectively, this may improve the performance of loops.
However, high-end processors typically have complex prediction schemes and
special purpose hardware that constitutes a significant portion of the
processor core. The following two components of branch predictors are the most
relevant for understanding the Meltdown and Spectre attacks:

* Branch Target Buffer (BTB): When the branch is indirect (there is more than
  one possible target address), it is necessary to maintain a BTB, a buffer
  that maps the source to target address of branch instructions.
* Branch History: The target of a branch instruction can change depending on a
  condition. In this case, the processor records the conditional outcomes of
  the last N executions of the branch, and uses this information to make an
  educated guess about the resolution of the condition when the instruction is
  executed again.

### Address Spaces

Virtual memory is a technique that is widely used in modern computers for a
variety of reasons. One of its aims is to isolate processes from each other,
that is, to give the illusion that every process is executing on its own
address space and unable to directly access another process's memory.

Virtual memory is generally divided in 4KB pages, and virtual
addresses are translated to physical ones with the help of a page table (often
by a hardware memory management unit). As the supervisor of the system, the
kernel performs operations on behalf of user processes, as well as many other
managerial operations. For performance reasons, it is common to map kernel
addresses into the user process's virtual address space. In turn, a subset of
the kernel addresses maps to physical memory. However, pages have associated
access permissions stored in the page table to restrict the process's access,
and the kernel manages these permissions.

### The Memory Hierarchy

Due to the disparity in speed between the memory and the processor, computer
architects use various types of memory devices within a single system. This
structure of the memory subsystem is known as the "memory hierarchy," where the
memory technologies that are fastest, most expensive and with less capacity
(e.g registers and caches) are closer to the processor, while slower, cheaper
and larger memories (e.g DRAM, flash, disk) are further away.

When the processor accesses an address, the memory closer to the processor is
searched first. If the data is not found there, then the next component further
down the memory hierarchy is searched, and so on, until the data is found.
However, the access latency of memory devices increases dramatically as each
level down the hierarchy is accessed. For example, according to the
Performance Analysis Guide [[9]], in an Intel Core i7 processor, the latency of
accessing the L3 cache is as low as ~40 cycles, while accessing local DRAM costs
~60 nanoseconds (or ~200 cycles with a 3.4GHz clock). It is partly this
disparity that techniques, such as speculative execution, aim to mitigate. For
example, while a branch based on a memory access is resolved, the processor
might be speculatively executing tens of instructions in the meantime.

As previously discussed, when a branch prediction is incorrect, the processor
will revert to its last correct architectural state (just after executing the
mispredicted branch). However, side effects of the invalid state can still be
observed in the microarchitecture, potentially leaking sensitive data. The
Meltdown and Spectre attacks rely on the state of the cache not being rolled
back when a misprediction occurs. Well understood cache timing side-channel
attacks can be used to recover the leaked data to an architecturally valid
state (e.g a general-purpose register), as applications cannot directly observe
changes in the microarchitectural state of the cache.

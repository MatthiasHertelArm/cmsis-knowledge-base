---
id: "mbedtls-random-generator-cloning-what-is-cloning"
type: "concept"
domain: "security"
title: "random generator cloning: What is cloning?"
summary: "On Unix-like systems, a process (application instance) can be cloned with the fork() system call), or with similar methods such as clone() on Linux."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/random_generator_cloning.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/random_generator_cloning.md#what-is-cloning"
license: "Apache-2.0"
mode: "V"
---

**Cloning** means that the state of the application has been copied, and there are multiple instances of the same application that initially have the same state. In this section, we discuss some common cases where cloning can happen. This is not an exhaustive list.

### Process forking

On Unix-like systems, a process (application instance) can be cloned with the [`fork()` system call](https://en.wikipedia.org/wiki/Fork_(system_call)), or with similar methods such as `clone()` on Linux. Often, `fork()` is only used to run a separate program (the child calls `execve()`), in which case any RNG state in the child is wiped before it is used. However, applications that use `fork()` with an active RNG that is used in the child process must pay attention to the RNG state.

### Virtual machine cloning

Virtual machine (VM) technology often allows freezing the state of a VM, then resuming it multiple times. This may be done, for example, to deploy it quickly to multiple hardware instances (concurrent clones), or to respond quickly to similar requests (serial clones).

When the system inside the VM resumes after cloning, the operating system running inside the VM must reseed its random generator. Additionally, any application that has its own random generator instance must also reseed.

Some environments broadcast VM cloning events. For example, some hypervisors gives each VM instance a unique [ACPI Virtual Machine Generation ID](https://download.microsoft.com/download/3/1/C/31CFC307-98CA-4CA5-914C-D9772691E214/VirtualMachineGenerationID.docx), and guest operating systems can respond to the ACPI `VM_GEN_COUNTER` event.
<!-- Linux had a proposal for propagating this event to userspace (https://lwn.net/Articles/887207/) but it has not gone through as of 6.18.0. -->

There is no cloning concern if a VM instance is merely migrated, i.e. only one copy of the VM instance is made and the original is destroyed.

### Resuming from hibernation

Some systems can hibernate, i.e. the system state is saved to persistent storage, then the system resumes later. This is fine if resuming destroys the hibernation image. However, in some environments, it is possible to resume multiple times from the same hibernation image. In such environments, the operating system must reseed its random generator after resuming from hibernation. Additionally, any application that has its own random generator instance must also reseed.

### Why is cloning a problem?

A cryptographic random generator consists of two parts: a seeding process which requires a non-deterministic source, and an algorithmic part which produces cryptographically strong random output from the seed.

If the state of a random generator is cloned, both instances will produce the same output until the random generator reseeds. This can be very bad for security since both instances will produce the same keys, the same nonces, etc. An adversary could even interact with one instance to obtain random generator outputs that are public (e.g. a protocol nonce), and use that knowledge to attack the other instance (e.g. a victim's session key).

As a consequence, if the application state is cloned, the random generator must not be used until each instance has a unique state, preferably obtained by reseeding from an entropy source.

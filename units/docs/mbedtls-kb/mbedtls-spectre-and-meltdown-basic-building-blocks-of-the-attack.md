---
id: "mbedtls-spectre-and-meltdown-basic-building-blocks-of-the-attack"
type: "concept"
domain: "security"
title: "Spectre and Meltdown: Basic Building Blocks of the Attack"
summary: "This section describes the main building blocks of the Spectre and Meltdown attacks."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/attacks/spectre_and_meltdown.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/attacks/spectre_and_meltdown.md#basic-building-blocks-of-the-attack"
license: "Apache-2.0"
mode: "V"
---

This section describes the main building blocks of the Spectre and Meltdown
attacks.

### Transient Instructions

Transient instructions are those that would never be executed in a program's
strict execution path, but are executed early by an out-of-order pipeline. For
example, consider the following instruction sequence:

```
1 if (a < length)
2     b = mem[a]
3 else
4     b = 0
```

If, on reaching this fragment of code, the processor is unable to resolve the
branch in line 1, it might speculate that the correct execution path is the
statement in line 2, which could cause a buffer over-read if `a >= length`.
However, when the branch condition is resolved, the processor will recover from
this incorrect state and start executing from line 4.

While the architectural effects of transient instructions are rolled back, the
microarchitectural state of the processor is changed in noticeable ways,
potentially leaking data to an architectural state. For example, in the case of
the trivial code above, a new line could have been inserted in the cache.  This
can be checked by simply measuring the time of the next memory access and
comparing it to the access time of a location that is known to be in the cache.

### Covert Channel

The covert channel is a means to transfer leaked information by transient
instructions from the microarchitectural state to an architectural one. In the
case of both Meltdown and Spectre, the covert channel is constructed using well
known cache timing side-channels. For example, the Flush+Reload timing
side-channel attack detects whether a memory location is cached [[1]].

The covert channel can be thought of as having sender and receiver ends. The
sender has access to an array, and the receiver simply needs to be aware of the
array's location. For example, consider a program with the following array:

```
uint8_t probe[256 * <cache_line_size>]
```

To send a byte of data `b` using the covert channel, the sender executes a
memory load of the form `probe[b * <cache_line_size>]`. This will load exactly
1 cache line out of 256 (assuming that it was not already cached). Then, at the
receiving end, the attacker simply uses the Flush+Reload technique on each of
the 256 possible cache lines to check which one is loaded, thus retrieving the
byte value `b`. Note that the array is of length:

```
2^n * <cache_line_size>
```

where `n` is the number of bits transferred per exchange and
`<cache_line_size>` is the size (in bytes) of a cache line.

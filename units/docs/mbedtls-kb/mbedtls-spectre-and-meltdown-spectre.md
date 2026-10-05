---
id: "mbedtls-spectre-and-meltdown-spectre"
type: "concept"
domain: "security"
title: "Spectre and Meltdown: Spectre"
summary: "Spectre bypasses the process's memory isolation mechanisms. It exploits information leaks by taking advantage of the branch predictor and out-of-order execution to recover secret information via microarchitectural covert channels. The remainder of this section describes two variants of this attack."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/attacks/spectre_and_meltdown.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/attacks/spectre_and_meltdown.md#spectre"
license: "Apache-2.0"
mode: "V"
---

Spectre bypasses the process's memory isolation mechanisms. It exploits
information leaks by taking advantage of the branch predictor and out-of-order
execution to recover secret information via microarchitectural covert channels.
The remainder of this section describes two variants of this attack.

### Variant 1: Bounds Check Bypass

As discussed above, branch predictors often maintain the history of executed
branches to make an educated guess about the next resolution of a branch before
the condition itself is evaluated. Variant 1 of the Spectre attack relies on
training the branch predictor to incorrectly speculate on a branch, so that
data is leaked via the covert channel. For example, consider the following
fragment of code from the Spectre paper [[2]]:

    1 if (x < array1_size)
    2     y = array2[array1[x] * 256];

If, upon reaching line 1, the value of `array1_size` is not cached, then the
processor might speculate incorrectly when `x >= array1_size` and execute line
2. Before the misprediction is confirmed, the loads from `array1` and `array2`
succeed. Later, the processor rolls back its architectural state, but changes
to the cache still linger. Thus, the attacker simply needs to run the receiving
end of the covert channel to recover the secret value of the byte `array1[x]`.

### Variant 2: Branch Target Injection

Indirect branches are those that have more than two destination addresses. As
discussed above, branch predictors are equipped with a Branch Target
Buffer (BTB) that maps the branch source to target addresses. Variant 2 of the
Spectre attack relies on training the branch predictor to predict an incorrect
target address. Before the correct target address is resolved, transient
instructions are executed leaking secret information via a covert channel.

For this attack to work, the attacker must first identify two pieces of code
in the victim's source code:

1. A sequence of instructions that uses registers, whose values can be
   manipulated by the attacker. These are typically functions that receive user
   inputs. Furthermore, the code must have an indirect branch.
2. A sequence of instructions that uses the registers from (1), so that
   sensitive data is leaked. The start of this sequence will be the target
   address of the misprediction.

The attacker must also train the branch predictor to map the source to the
chosen destination address in the BTB. Note that, due to the lack of isolation
between processes in the BTB, it is feasible to train the branch predictor from
a different unprivileged process to the one being attacked. The attacker then
needs to stimulate the victim into executing the code path in point (1) above.
Finally, the attacker uses the covert channel to recover the data.

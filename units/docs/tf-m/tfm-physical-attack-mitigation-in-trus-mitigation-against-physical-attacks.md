---
id: "tfm-physical-attack-mitigation-in-trus-mitigation-against-physical-attacks"
type: "concept"
domain: "security"
title: "Physical attack mitigation in Trusted Firmware-M: Mitigation against physical attacks"
summary: "The applicability of these attacks highly depends on the device. Some devices are more sensitive than others. Protection is possible at hardware and software levels as well."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/tfm_physical_attack_mitigation.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/tfm_physical_attack_mitigation.html#mitigation-against-physical-attacks"
license: "BSD-3-Clause"
mode: "V"
---

The applicability of these attacks highly depends on the device. Some
devices are more sensitive than others. Protection is possible at hardware and
software levels as well.

On the hardware level, there are chip design principles and system IPs that are
resistant to fault injection attacks. These can make it harder to perform a
successful attack and as a result the chip might reset or erase sensitive
content. The device maker needs to consider what level of physical attack is in
scope and choose a SoC accordingly.

On top of hardware-level protection, a secondary protection layer can be
implemented in software. This approach is known as "defence in depth".

Neither hardware nor software level protection is perfect because both can be
bypassed. The combination of them provides the maximum level of protection.
However, even when both are in place, it is not certain that they provide 100%
protection against physical attacks. The best of what is to achievable to harden
the system to increase the cost of a successful attack (in terms of time and
equipment), thereby making it non profitable to perform them.


### Software countermeasures against physical attacks

There are practical coding techniques which can be applied to harden software
against fault injection attacks. They significantly decrease the probability of
a successful attack:

  - Control flow monitor

    To catch malicious modification of the expected control flow. When an
    important portion of a program is executed, a flow monitor counter is
    incremented. The program moves to the next stage only if the accumulated
    flow monitor counter is equal to an expected value.

  - Default failure

    The return value variable should always contain a value indicating
    failure. Changing its value to success is done only under one protected
    flow (preferably protected by double checks).

  - Complex constant

    It is hard to change a memory region or register to a pre-defined value, but
    usual boolean values (0 or 1) are easier to manipulate.

  - Redundant variables and condition checks

    To make branch condition attack harder it is recommended to check the
    relevant condition twice (it is better to have a random delay between the
    two comparisons).

  - Random delay

    Successful fault injection attacks require very precise timing. Adding
    random delay to the code execution makes the timing of an attack much
    harder.

  - Loop integrity check

    To avoid to skip critical loop iterations. It can weaken the cryptographic
    algorithms. After a loop has executed, check the loop counter whether it
    indeed has the expected value.

  - Duplicated execution

    Execute a critical step multiple times to prevent fault injection from
    skipping the step. To mitigate multiple consecutive fault injections, random
    delay can be inserted between duplicated executions.

These techniques should be applied in a thoughtful way. If it is applied
everywhere then it can result in messy code that makes the maintenance harder.
Code must be analysed and sensitive parts and critical call path must be
identified. Furthermore, these techniques increase the overall code size which
might be an issue on the constrained devices.

Currently, compilers are not providing any support to implement these
countermeasures automatically. On the contrary, they can eliminate the
protection code during optimization. As a result, the C level protection does
not add any guarantee about the final behavior of the system. The effectiveness
of these protections highly depends on the actual compiler and the optimization
level. The compiled assembly code must be visually inspected and tested to make
sure that proper countermeasures are in-place and perform as expected.

---
id: "mbedtls-providing-diffie-hellman-merkle-dh-custom-and-standard-parameters"
type: "concept"
domain: "security"
title: "Providing Diffie-Hellman-Merkle (DHM) parameters in versions before 4.0: Custom and standard parameters"
summary: "We used to recommend using standard parameters rather than generating your own. However, the team of researchers behind the Logjam attack also showed that a risk associated is with that if the parameters are not large enough."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/cryptography/providing-diffie-hellman-or-dhm-parameters.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/cryptography/providing-diffie-hellman-or-dhm-parameters.md#custom-and-standard-parameters"
license: "Apache-2.0"
mode: "V"
---

We used to recommend using standard parameters rather than generating your own. However, the team of researchers behind the [Logjam attack](https://weakdh.org/) also showed that a risk associated is with that if the parameters are not large enough. More precisely, they showed that the amount of computation required to break any number of MODP DHM key exchanges is close to the amount required to break just one of them, as long as they all use the same parameters. So if your parameter size is just at the limit of what an adversary can break, using standard parameters allows the adversary to amortize the cost of the initial computation, which is not what you want.

1,024 bits is considered within reach of the most powerful adversaries, and 2,048 bits safe according to public knowledge. If you absolutely must use 1,024 bit parameters for compatibility with old clients, it is highly desirable to generate your own rather than use the standard parameters, as long as you take into consideration [backdoor vulnerabilities](https://github.com/tech-updates/blog/dh-backdoors). If you can use parameters of 2,048 bits or more, then you are safe either way.

An alternative is to switch to Elliptic Curve Diffie-Hellman (ECDH ciphersuite), which does not have this security issue and also improves the performance, as [this article](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/cryptography/ephemeral-diffie-hellman.md) describes.

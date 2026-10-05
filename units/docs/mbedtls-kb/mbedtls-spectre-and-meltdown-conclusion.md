---
id: "mbedtls-spectre-and-meltdown-conclusion"
type: "concept"
domain: "security"
title: "Spectre and Meltdown: Conclusion"
summary: "The Meltdown and Spectre attacks are vulnerabilities in architecturally correct hardware. The attacks rely on processor optimization techniques, such as out-of-order execution and branch prediction, to leak information through the microarchitecture while executing transient instructions."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/attacks/spectre_and_meltdown.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/attacks/spectre_and_meltdown.md#conclusion"
license: "Apache-2.0"
mode: "V"
---

The Meltdown and Spectre attacks are vulnerabilities in architecturally correct
hardware. The attacks rely on processor optimization techniques, such as
out-of-order execution and branch prediction, to leak information through the
microarchitecture while executing transient instructions. They then recover
the data through cache timing side-channel attacks. The attacks do not rely on
vulnerabilies in the software, but there are mitigations that can be implemented 
into the software to prevent them. It is important to highlight that not all 
hardware platforms are affected by these attacks. For more information on which 
processors are vulnerable, refer to your vendor's documentation (see [References](#references)).

Like other attacks on the application code, system, or hardware that is
hosting Mbed TLS as a security library, Mbed TLS cannot fully defend against
these attacks by itself. It is built on the assumption that the underlying
hardware provides some basic building blocks for security, such as process
isolation, which is violated by Meltdown and Spectre. The following is a
comprehensive list of advice and actions that Mbed TLS users can implement to more
effectively prevent these attacks:

* Review the processor vendor's security information to find out if your
  system is affected, and apply the vendor's security guidelines where
  appropriate.
* Maintain up-to-date systems with the latest security updates from the
  operating system vendor, and if necessary, any microcode updates issued by
  the processor vendor.
* Ensure you are using the most recent version of Mbed TLS, and that you can
  update your system as new versions become available.
* Ensure you follow security best practices and guidelines. For example, do not
  run any unstrusted software.
* Identify and patch any source code in your software that may be
  vulnerable to a variant of the Spectre attack. Remember that these attacks
  might not be fully prevented by operating system updates, and changes to
  vulnerable software might be necessary. 
* Check for upcoming compiler and tool updates to defend against Spectre.

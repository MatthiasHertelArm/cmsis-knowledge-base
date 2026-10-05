---
id: "mbedtls-alternative-cryptography-engines-i"
type: "concept"
domain: "security"
title: "Alternative cryptography engines implementation"
summary: "As mentioned in the Mbed TLS Abstraction layers article, Mbed TLS supports alternative implementation for most of its cryptography modules. A common use case is for hardware accelerated cryptography engines."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/hw_acc_guidelines.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/hw_acc_guidelines.md"
license: "Apache-2.0"
mode: "V"
---

As mentioned in the [Mbed TLS Abstraction layers article](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/../generic/abstraction-layers.md), Mbed TLS supports alternative implementation for most of its cryptography modules. A common use case is for hardware accelerated cryptography engines. There are a couple of methods for alternative implementations: specific function replacement and full module replacement. The latter is the more common one.

The [configuration file (`mbedtls_config.h`)](https://github.com/Mbed-TLS/mbedtls/blob/development/include/mbedtls/mbedtls_config.h) lists the cryptography modules, which you can replace with alternative implementation. An alternative implementation of a module is effectively a driver for a piece of cryptographic hardware. These are named `MBEDTLS_<MODULE NAME>_ALT`. In order to support an alternative implementation for a module, uncomment the corresponding `*_ALT` definition. Function replacement is based on the function name, upper-cased, with the suffix `_ALT`. To support a hardware entropy source, enable `MBEDTLS_ENTROPY_HARDWARE_ALT` in the configuration file.  

**Note: For RSA and ECP function replacement, the behavior is different. Refer to the [ECP internal header](https://github.com/Mbed-TLS/mbedtls/blob/development/library/ecp_internal_alt.h) for more information.**  

Note: for more information about the configuration file, see [How do I configure Mbed TLS](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/../compiling-and-building/how-do-i-configure-mbedtls.md).

Some hardware acceleration engines require an initial setup to be done on the platform, before they can work, such as enabling cache, or initializing the cryptographic engine. Such setup should be implemented in the function `mbedtls_platform_setup()` and terminated in the function `mbedtls_platform_teardown()`, as shown in the example in [this article](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/../how-to/how-do-i-port-mbed-tls-to-a-new-environment-OS.md).

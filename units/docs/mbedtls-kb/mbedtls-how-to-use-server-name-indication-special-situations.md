---
id: "mbedtls-how-to-use-server-name-indication-special-situations"
type: "concept"
domain: "security"
title: "How to use Server Name Indication: Special situations"
summary: "Sometimes certificates are issued for IP addresses and not DNS names. Unfortunately, Mbed TLS doesn't yet support using such certificates while SNI is turned on."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/use-sni.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/use-sni.md#special-situations"
license: "Apache-2.0"
mode: "V"
---

Sometimes certificates are issued for IP addresses and not DNS names. Unfortunately, Mbed TLS doesn't yet support using such certificates while SNI is turned on. This means that you may be able to set IP addresses with the `mbedtls_ssl_set_hostname` function, but it will result in non-compliant behavior and limited functionality.

As mentioned above, Mbed TLS uses the same function to set the name for the certificate verification and to set the name for the SNI. The standard does not allow sending IP addresses in the SNI extension, and using an IP address when the SNI is turned on means that a compliant server can't possibly find the matching certificate, and some servers may terminate the connection immediately.

**Note:** When SNI is turned off, Mbed TLS can handle certificates that have IP addresses as their subject name or subject alternative name.

<!---",use-sni,"sni, server name indication, virtual host, rfc 6066, tls extension",,,published,"2016-07-05 14:55:00",2,4773,"2016-07-06 12:55:00","Janos Follath"--->

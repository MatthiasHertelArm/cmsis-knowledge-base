---
id: "mbedtls-debugging-tls-sessions-use-sample-applications"
type: "concept"
domain: "security"
title: "Debugging TLS sessions: Use Sample applications"
summary: "Mbed TLS comes with a variety of sample applications that run on your desktop machine in the programs folder."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/debugging-tls.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/debugging-tls.md#use-sample-applications"
license: "Apache-2.0"
mode: "V"
---

Mbed TLS comes with a variety of sample applications that run on your desktop machine in the `programs` folder. We recommended that you first try using one of these sample applications in the `ssl` programs sub-folder to eliminate issues unrelated to your platform, such as certificate handling and configuration setup. Most of the ssl sample applications have a `debug_level` application parameter to show TLS logs.  
You should use the sample application to eliminate issues related to the peer, and use a known server \ client for your porting process.  
For example, if you are porting a TLS client and have issues connecting to a server, then you should run the following setups with debug logs enabled:

1. Run `ssl_client2` and `ssl_server2` to first understand the basic TLS connection.
1. Run `ssl_client2` with the server you are trying to connect to. This will help you understand what CA root certificate you need to set in `mbedtls_ssl_conf_ca_chain()`.
1. Run `ssl_server2` with your client application. This will have you working with a known server, and help you test your specific porting setup.
1. Run your client application with the server you are trying to connect to. Once the previous steps have been completed, you should test the final setup, to get past all the TLS related issues.

If you still encounter problems after trying these steps, then it is likely that your issue is platform specific, such as a memory related issue.

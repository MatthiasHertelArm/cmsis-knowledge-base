---
id: "mbedtls-compiling-mbed-tls-in-mingw-use-mbed-tls"
type: "concept"
domain: "security"
title: "Compiling Mbed TLS in MinGW: Use Mbed TLS"
summary: "You can now use some of the utility programs that come with Mbed TLS, like:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/compiling-and-building/compiling-mbedtls-in-mingw.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/compiling-and-building/compiling-mbedtls-in-mingw.md#use-mbed-tls"
license: "Apache-2.0"
mode: "V"
---

You can now use some of the utility programs that come with Mbed TLS, like:

```
programs\ssl\ssl_client2 server_name=www.google.nl server_port=443

programs\test\selftest
```
    
You should see some HTML output for the first program, and something like this for the selftest program:

(figure: Selftest output)

If your client application fails, it is probably because you need to set the CA certificate file or path of `www.google.nl`, as `ca_file` or `ca_path` parameter.
If you installed Perl and built the tests, you can run any of the executables in the `tests` directory to run the individual test suites.

Enter:

```
test_suite_aes.cbc
```

To link Mbed TLS to your own programs, you can add the paths to the `mbedtls\include and mbedtls\library` directories to your project.

<!---compiling-mbedtls-in-mingw,"Walkthrough for compiling Mbed TLS under MinGW under Windows","MinGW, compiling under Windows, compiling with MinGW","mingw, compile, perl, windows, make",published,"2012-10-09 00:00:00",6,10344,"2017-04-25 08:12:00","Paul Bakker"--->

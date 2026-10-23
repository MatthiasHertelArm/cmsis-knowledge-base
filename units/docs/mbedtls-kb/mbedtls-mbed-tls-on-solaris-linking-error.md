---
id: "mbedtls-mbed-tls-on-solaris-linking-error"
type: "concept"
domain: "security"
title: "Mbed TLS on Solaris: Linking error"
summary: "If you run make, you may get an error during linking similar to:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/compiling-and-building/mbedtls-on-solaris.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/compiling-and-building/mbedtls-on-solaris.md#linking-error"
license: "Apache-2.0"
mode: "V"
---

If you run `make`, you may get an error during linking similar to:

```
$ make
...
  CC    pkey/dh_client.c
Undefined                       first referenced
 symbol                             in file
bind                                ../library/libmbedtls.a(net.o)
accept                              ../library/libmbedtls.a(net.o)
listen                              ../library/libmbedtls.a(net.o)
gethostbyname                       ../library/libmbedtls.a(net.o)
socket                              ../library/libmbedtls.a(net.o)
setsockopt                          ../library/libmbedtls.a(net.o)
connect                             ../library/libmbedtls.a(net.o)
shutdown                            ../library/libmbedtls.a(net.o)
ld: fatal: symbol referencing errors. No output written to pkey/dh_client
collect2: ld returned 1 exit status
make[1]: *** [pkey/dh_client] Error 1
make: *** [all] Error 2
```

This is because under Solaris, you must to instruct GCC to include `libsocket` and `libnsl` during linking.

Define `LDFLAGS` to include `-lsocket -lnsl` when running `make` on Solaris 10.

---
id: "mbedtls-mbed-tls-on-solaris-ar-error"
type: "concept"
domain: "security"
title: "Mbed TLS on Solaris: Ar error"
summary: "If you run make and receive the following error:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/compiling-and-building/mbedtls-on-solaris.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/compiling-and-building/mbedtls-on-solaris.md#ar-error"
license: "Apache-2.0"
mode: "V"
---

If you run `make` and receive the following error:

```
$ make
....
  AR    libmbedtls.a
ar: creating libmbedtls.a
  RL    libmbedtls.a
ar: one of [drqtpmx] must be specified
make[1]: *** [libmbedtls.a] Error 1
make: *** [all] Error 2
```

### Workaround

Install the package `SUNWbinutils`, then run:

```
export AR=gar
```


<!--- mbedtls-on-solaris,"When compiling Mbed TLS on Solaris some modifications might be needed in the Makefile or a package must be installed","Solaris, Makefile, undefined symbol, linking, bind, accept, listen, socket, connect, ar, make, gar","Solaris, build, compile,, Makefile, undefined symbol, linking, bind, accept, listen, socket, connect, ar, make, gar, setsockopt, gethostbyname, shutdown, libsocket, libnsl, ldflags",published,"2013-06-27 11:43:00",6,3122,"2015-07-24 11:39:00","Paul Bakker" --->

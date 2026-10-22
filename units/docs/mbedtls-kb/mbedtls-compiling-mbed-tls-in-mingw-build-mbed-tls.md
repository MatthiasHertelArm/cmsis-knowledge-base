---
id: "mbedtls-compiling-mbed-tls-in-mingw-build-mbed-tls"
type: "concept"
domain: "security"
title: "Compiling Mbed TLS in MinGW: Build Mbed TLS"
summary: "Now we are ready to build Mbed TLS. Go back to the command window where you set the mingw-64\\mingw64\\bin path."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/compiling-and-building/compiling-mbedtls-in-mingw.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/compiling-and-building/compiling-mbedtls-in-mingw.md#build-mbed-tls"
license: "Apache-2.0"
mode: "V"
---

Now we are ready to build Mbed TLS. Go back to the command window where you set the `mingw-64\mingw64\bin` path.

Change directory to the `c:\mingw-64\projects\mbedtls-x.y.z` folder.

```
cd c:\mingw-64\projects\mbedtls-x.y.z
```

MinGW uses a slightly different `make` command. Also, the Mbed TLS makefiles need to know you are building for Windows, so it can adjust the linker flags:

```
set WINDOWS=1
mingw32-make CC=gcc
```

Alternatively, you can type `mingw32-make CC=gcc WINDOWS=1`, but you will need to re-type `WINDOWS=1` with every single invocation of `mingw32-make`, while the above version works for an entire shell session.

You can optionally check that Mbed TLS works correctly by entering:
    
```
mingw32-make CC=gcc check
```
Note: in order to run the tests, you will need to [install cygwin](https://cygwin.com/install.html) and set it in the path, since the tests rely on `cygwin1.dll`:

```
set PATH=C:\cygwin64\bin;%PATH%
```

If you chose not to install Perl or Python, then you can skip building the full suite of unit tests by using the following build command:

```
mingw32-make CC=gcc no_test
```

You can then run a much more minimal set of unit tests with:

```
programs\test\selftest
```

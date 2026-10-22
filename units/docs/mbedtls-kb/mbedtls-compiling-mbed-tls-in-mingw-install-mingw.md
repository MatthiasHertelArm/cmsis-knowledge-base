---
id: "mbedtls-compiling-mbed-tls-in-mingw-install-mingw"
type: "concept"
domain: "security"
title: "Compiling Mbed TLS in MinGW: Install MinGW"
summary: "Install MinGW64 by downloading and running the installer mingw-w64-install.exe from Sourceforge."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/compiling-and-building/compiling-mbedtls-in-mingw.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/compiling-and-building/compiling-mbedtls-in-mingw.md#install-mingw"
license: "Apache-2.0"
mode: "V"
---

Install MinGW64 by downloading and running the installer `mingw-w64-install.exe` from [Sourceforge](https://sourceforge.net/projects/mingw-w64/).

Choose latest mingw64 version, for x86_64 architecture and win32 threads:
(figure: MingW installer)

This tutorial uses the install location: `c:\mingw-64`. (The default install location of Mingw64 is different and dependent on the parameters chosen in the installer. With the described parameters, it would be `C:\Program Files\mingw-w64\x86_64-8.1.0-win32-seh-rt_v6-rev0`.)

Before using the MinGW environment, you must set the path to the `mingw-64\mingw64\bin` directory.

For Windows 10, you can set this permanently through:
 * **Control Panel** > **User Accounts** > **Change my environment variables**.

Add `C:\mingw-w64\mingw64\bin` to the **path** variable. You need administrator privileges to do this.

To set the path for each session you can start a command prompt and type:

```
set PATH=C:\mingw-64\mingw64\bin;%PATH%"
```

**Keep the command window open.**

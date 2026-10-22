---
id: "mbedtls-arm-mbed-tls-in-microsoft-visual-s-build"
type: "concept"
domain: "security"
title: "Arm Mbed TLS in Microsoft Visual Studio 2015: Use the solution file supplied with the Mbed TLS source code / Build"
summary: "Part of: Use the solution file supplied with the Mbed TLS source code"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/compiling-and-building/using-mbedtls-in-microsoft-visual-studio-2015.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/compiling-and-building/using-mbedtls-in-microsoft-visual-studio-2015.md#build"
license: "Apache-2.0"
mode: "V"
---

_Part of: Use the solution file supplied with the Mbed TLS source code_

When Visual Studio opens, it shows all the components of the Mbed TLS source code. For this step, you only need the `mbedTLS` project (shown in bold to indicate that it is the default project), which builds the `mbedTLS` library file. Later, you will link to this library file from the sample application.

Now you can build the library. Because you won't be debugging Mbed TLS, build the `Release` version. To do this, select the `release` configuration in the icon bar. Then press **ctrl+shift+b** to start the building process.





Not all components may have built successfully. This does not matter as long as the `mbedTLS` project built. Check this by looking in this folder: My Documents\Visual Studio 2015\Projects\mbedtls-<version\>\visualc\VS2010\Release. The file `mbedTLS.lib` msut be present.



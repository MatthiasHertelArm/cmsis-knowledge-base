---
id: "mbedtls-arm-mbed-tls-in-microsoft-visual-s-use-cmake-to-generate-a-visual-studio-so"
type: "concept"
domain: "security"
title: "Arm Mbed TLS in Microsoft Visual Studio 2015: Use `cmake` to generate a Visual Studio solution file"
summary: "You can use cmake to generate Visual Studio."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/compiling-and-building/using-mbedtls-in-microsoft-visual-studio-2015.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/compiling-and-building/using-mbedtls-in-microsoft-visual-studio-2015.md#use-cmake-to-generate-a-visual-studio-solution-file"
license: "Apache-2.0"
mode: "V"
---

You can use `cmake` to generate Visual Studio.

In a command prompt, change directory to the root folder of your Mbed TLS folder.

Type: `cmake -G "Visual Studio 14 2015 Win64"`



You have now generated a solution file in the root of your Mbed TLS folder.



You can now continue as described previously for the supplied Visual Studio solution file.

Note that the generated solution file created the library for `Win64` architecture(`x64`) (or `ARM`, depending on the parameters). You can also build the supplied solution file for Win32. When you write your sample application, build it with the same architecture that the library was built for.

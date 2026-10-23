---
id: "mbedtls-compile-mbed-tls-to-a-static-libra-create-the-project"
type: "concept"
domain: "security"
title: "Compile Mbed TLS to a static library in Eclipse CDT: Create the project"
summary: "Compile Mbed TLS to a static library in Eclipse CDT: Create the project"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/compiling-and-building/compile-mbedtls-to-a-static-library-in-eclipse-cdt.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/compiling-and-building/compile-mbedtls-to-a-static-library-in-eclipse-cdt.md#create-the-project"
license: "Apache-2.0"
mode: "V"
---

* Start your Eclipse CDT environment by running `eclipse.exe` in the Eclipse installed directory.
* Choose an appropriate directory for the workspace you would like to save your project.
* You can close the **Welcome** screen if it pops up.
* Create your new C project by choosing  **File** > **New C Project**.
* The **C Project** dialog pops up:

(figure: Eclipse new project popup)

* In the **Project name** field, enter your project name (for example, "Mbedtls").

**Note:** Be aware that the compiler will automatically prefix your compiled static library name with `lib` in front of the project name. A project named ``Mbedtls`` will produce a `libmbedtls.a` library.

* Leave **Use default location** checked.
* In the **Project Types** box, select **Static Library** > **Empty Project**.
*  In the **Toolchains** box, choose your compiler (such as **Cygwin GCC** or **MinGW GCC**) and click **Next**.
* The **Select Configurations** dialog appears.
* Select both **Debug** and **Release**, then click **Finish**.
* Your C project is now created.

---
id: "mbedtls-compile-mbed-tls-to-a-static-libra-import-mbed-tls-code-into-your-project"
type: "concept"
domain: "security"
title: "Compile Mbed TLS to a static library in Eclipse CDT: Import Mbed TLS code into your project"
summary: "In this step, you import the Mbed TLS code into the project and make it ready for compilation."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/compiling-and-building/compile-mbedtls-to-a-static-library-in-eclipse-cdt.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/compiling-and-building/compile-mbedtls-to-a-static-library-in-eclipse-cdt.md#import-mbed-tls-code-into-your-project"
license: "Apache-2.0"
mode: "V"
---

In this step, you import the Mbed TLS code into the project and make it ready for compilation.

* Inside the **Project Explorer tree** on the left side, right click on your **project folder** and click **Properties**.
* A **project properties window** pops up.
* Go to **C/C++** > **General Paths and Symbols** and choose the **includes** tab.
* Under **Languages**, select **GNU C**.
* Add the Mbed `include` location and click **Apply**, then **OK**.

Since we are using a mixture of Windows- and Unix-based tools, we will encounter our first problem:

**Option 1:** Windows-style path:
(figure: Windows-style path)

If you add a Windows-style path like `C:/mbed/include`, project rebuilds will fail and `make` returns a `multiple target` error caused by the ``:`` character in your path.
One solution is to always clean the project before a new rebuild.

**Option 2:** Cygwin-style path:
(figure: Cygwin-style path)

If you add a Cygwin-style path like `/cygdrive/c/mbed/include` Eclipse will warn you that the directory cannot be found, and all your includes get an unresolved warning.
**The project will compile anyway.**

* Right click on your project and click **Import**.
* Choose **General** > **Filesystem** and  **Next**.

(figure: Import Code)

* Navigate to the **MbedTLS** library folder
* Select all the `.c` files
* Click **Finish**.

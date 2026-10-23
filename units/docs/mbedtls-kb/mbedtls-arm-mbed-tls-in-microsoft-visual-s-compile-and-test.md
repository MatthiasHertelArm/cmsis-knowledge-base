---
id: "mbedtls-arm-mbed-tls-in-microsoft-visual-s-compile-and-test"
type: "concept"
domain: "security"
title: "Arm Mbed TLS in Microsoft Visual Studio 2015: Use the solution file supplied with the Mbed TLS source code / Compile and test"
summary: "Part of: Use the solution file supplied with the Mbed TLS source code"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/compiling-and-building/using-mbedtls-in-microsoft-visual-studio-2015.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/compiling-and-building/using-mbedtls-in-microsoft-visual-studio-2015.md#compile-and-test"
license: "Apache-2.0"
mode: "V"
---

_Part of: Use the solution file supplied with the Mbed TLS source code_

Before building the new project, you need to add one project setting. In the solution explorer, right click on the project name, in this case **Mbed\_client\_demo**. Select **Properties**.



In the properties dialog, select **Linker / Input**. Select **Additional dependencies**. Click on the down arrow, and choose **edit**.



Type `wsock32.lib` in the dialog, and click on **OK** twice. You need to add this library to the project because line 4 of the source code includes the `winsock` header file. Visual Studio needs to know where to find the executable code for this file.



You can now build the sample application. Press **ctrl+shift+b**. Visual Studio shows `Build: 1 succeeded` in the output screen.



Start the application by pressing the **F5** key. Note that line 16 of the source code states that the application loads the home page of a well-known search engine.

The application shows a command screen, stating that a connection has been made to the server and shows the server's response. Press **enter** to close the application.



To connect to the server using HTTPS, change line 15 to:

```
#define SERVER_PORT 443
```

Build (**ctrl+shift+b**), and run (**F5**) the application again. The application shows an error. You first need to set up a TLS connection. That is what Mbed TLS is for.



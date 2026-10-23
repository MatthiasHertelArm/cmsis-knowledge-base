---
id: "mbedtls-setting-up-the-eclipse-cdt-environ-install-eclipse-c-c-development-tool-cdt"
type: "concept"
domain: "security"
title: "Setting up the Eclipse CDT environment on Windows: Install Eclipse C/C++ Development Tool (CDT)"
summary: "You can either download and install a new version of Eclipse CDT, or extend the existing Eclipse for Java Developers on your system with a CDT plugin."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/compiling-and-building/setup-eclipse-cdt-environment-on-windows.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/compiling-and-building/setup-eclipse-cdt-environment-on-windows.md#install-eclipse-c-c-development-tool-cdt"
license: "Apache-2.0"
mode: "V"
---

You can either download and install a new version of Eclipse CDT, or extend the existing **Eclipse for Java Developers** on your system with a CDT plugin.

**Option 1:** Clean Eclipse CDT install:
  * [Download](http://www.eclipse.org/downloads) **Eclipse IDE for C/C++ Developers** and unzip the downloaded file into a directory of your choice.
  * Run `eclipse.exe` inside the directory.

**Option 2:** Extend an existing **Eclipse for Java Developers** installation:
 * Launch Eclipse.
 * Go to **Help** > **Install New Software**.
 * In "Work with", enter the CDT update site `http://download.eclipse.org/tools/cdt/releases/juno` (for Eclipse Juno only) > **Add** > Enter a name (such as CDT 8.1.0) > Select **all the "CDT main features"**.
 * You may select optional features.
 * Click **Finish**.
 * Restart Eclipse after the plugin installation is finished.

<!--- "This quickstart manual is intended for C/C++ developers who are interesting in developing Mbed TLS based projects in Eclipse C/C++ Development Tool (CDT) on Windows.","Eclipse CDT, Cygwin, Eclipse installation","eclipse, cygwin, tutorial",published,"2013-01-04 15:39:00",6,47375,"2015-07-24 11:51:00","Paul Bakker"--->

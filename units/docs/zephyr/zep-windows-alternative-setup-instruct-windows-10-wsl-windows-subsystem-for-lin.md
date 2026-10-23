---
id: "zep-windows-alternative-setup-instruct-windows-10-wsl-windows-subsystem-for-lin"
type: "concept"
domain: "project"
title: "Windows alternative setup instructions: Windows 10 WSL (Windows Subsystem for Linux)"
summary: "If you are running a recent version of Windows 10 you can make use of the built-in functionality to natively run Ubuntu binaries directly on a standard command-prompt."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/getting_started/installation_win.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/getting_started/installation_win.rst"
license: "Apache-2.0"
mode: "V"
---

If you are running a recent version of Windows 10 you can make use of the
built-in functionality to natively run Ubuntu binaries directly on a standard
command-prompt. This allows you to use software such as the :ref:`Zephyr SDK
<toolchain_zephyr_sdk>` without setting up a virtual machine.


**Warning:** Windows 10 version 1803 has an issue that will cause CMake to not work properly and is fixed in version 1809 (and later). More information can be found in `Zephyr Issue 10420 <10420>`.

#. Install the Windows Subsystem for Linux (WSL).


**Note:** For the Zephyr SDK to function properly you will need Windows 10 build 15002 or greater. You can check which Windows 10 build you are running in the "About your PC" section of the System Settings. If you are running an older Windows 10 build you might need to install the Creator's Update.

#. Follow the Ubuntu instructions in the installation_linux document.

.. NOTE FOR DOCS AUTHORS: as a reminder, do *NOT* put dependencies for building
   the documentation itself here.

.. _Install the Windows Subsystem for Linux (WSL): https://msdn.microsoft.com/en-us/commandline/wsl/install_guide

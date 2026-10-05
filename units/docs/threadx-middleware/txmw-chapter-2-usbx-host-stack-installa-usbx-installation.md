---
id: "txmw-chapter-2-usbx-host-stack-installa-usbx-installation"
type: "concept"
domain: "rtos"
title: "Chapter 2 - USBX Host Stack Installation: USBX Installation"
summary: "USBX is installed by cloning the GitHub repository to your local machine. The following is typical syntax for creating a clone of the USBX repository on your PC:"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/usbx-host-stack-2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-host-stack-2.md#usbx-installation"
license: "MIT"
mode: "V"
---

USBX is installed by cloning the GitHub repository to your local machine. The following is typical syntax for creating a clone of the USBX repository on your PC:

```powershell
    git clone https://github.com/eclipse-threadx/usbx
```

Alternatively you can download a copy of the repository using the download button on the GitHub main page.

You will also find instructions for building the USBX library on the front page of the online repository.

The following general instructions apply to virtually any installation:

1. Use the same directory in which you previously installed ThreadX on the host hard drive. All USBX names are unique and will not interfere with the previous USBX installation.
2. Add a call to ***ux_system_initialize*** at or near the beginning of ***tx_application_define*.** This is where the USBX resources are initialized.
3. Add a call to ***ux_host_stack_initialize*.**
4. Add one or more calls to initialize the required USBX.
5. Add one or more calls to initialize the host controllers available in the system.
6. It may be required to modify the tx_low_level_initialize.c file to add low-level hardware initialization and interrupt vector routing. This is specific to the hardware platform and will not be discussed here.
7. Compile application source code and link with the USBX and ThreadX run time libraries (FileX and/or Netx Duo may also be required if the USB storage class and/or USB network classes are to be compiled in), ux.a (or ux.lib) and tx.a (or tx.lib). The resulting can be downloaded to the target and executed.

---
id: "zepb-kit-xmc72-evk-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "kit_xmc72_evk: Programming and Debugging"
summary: "The KIT_XMC72_EVK includes an onboard programmer/debugger (KitProg3) which can be used to program and debug the XMC 7200 cores."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/infineon/kit_xmc72_evk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/infineon/kit_xmc72_evk/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

The KIT_XMC72_EVK includes an onboard programmer/debugger (KitProg3)
which can be used to program and debug the XMC 7200 cores.


### Infineon OpenOCD Installation


The ModusToolbox™ Programming Tools package includes Infineon OpenOCD.
Alternatively, a standalone installation can be done by downloading the
Infineon OpenOCD release for your system and extracting the files to a
location of your choice.


**Note:** Linux requires device access rights to be set up for KitProg3. This is handled automatically by the ModusToolbox™ Programming Tools installation. When doing a standalone OpenOCD installation, this can be done manually by executing the script `openocd/udev_rules/install_rules.sh`.


### Configuring a Console


Connect a USB cable from your PC to the KitProg3 micro-B USB connector (J7)
on the KIT_XMC72_EVK.Use the serial terminal of your choice (minicom, PuTTY,
etc.) with the following settings:

- **Speed:** 115200
- **Data:** 8 bits
- **Parity:** None
- **Stop bits:** 1


### Flashing


You should see the following message on the console:

```console

*** Booting Zephyr OS build vX.Y.Z ***
Hello World! kit_xmc72_evk
```

### Debugging


Once the GDB console starts, you may set breakpoints and perform standard
GDB debugging on the XMC 7200 cores.

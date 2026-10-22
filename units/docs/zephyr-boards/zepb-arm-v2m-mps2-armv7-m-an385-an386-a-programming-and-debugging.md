---
id: "zepb-arm-v2m-mps2-armv7-m-an385-an386-a-programming-and-debugging"
type: "concept"
domain: "bring-up"
title: "ARM V2M MPS2 Armv7-m (AN385/AN386/AN500): Programming and Debugging"
summary: "Here is an example for the hello_world application with AN385."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/arm/mps2/doc/mps2_armv7m.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/arm/mps2/doc/index.html#programming-and-debugging"
license: "Apache-2.0"
mode: "V"
---

### Flashing


V2M MPS2 provides:

- A USB connection to the host computer, which exposes a Mass Storage and an
  USB Serial Port.
- A Serial Flash device, which implements the USB flash disk file storage.
- A physical UART connection which is relayed over interface USB Serial port.


#### Flashing an application to V2M MPS2


Here is an example for the hello_world application with AN385.

Connect the V2M MPS2 to your host computer using the USB port and you should
see a USB connection which exposes a Mass Storage and a USB Serial Port.
Copy the generated zephyr.bin in the exposed drive.
Reset the board and you should be able to see on the corresponding Serial Port
the following message:

```console

Hello World! arm
```

#### Running an applicatoin with FVP


Here is the same example for running with FVP.
Set the `ARMFVP_BIN_PATH` environment variable to the location of your FVP you have downloaded from here <FVP_>

```console

export ARMFVP_BIN_PATH=/home/../FVP_MPS2/
```
Then build with the same command you would use normally, and run with `west build -t run_armfvp`.

.. _MPS2 Technical Reference Manual (TRM):
   https://developer.arm.com/documentation/100112/0200/

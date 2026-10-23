---
id: "mlek-deployment-mps3-mps4-fpga-board"
type: "concept"
domain: "edge-ai"
title: "Deployment: MPS3 + MPS4 FPGA board"
summary: "Once the board has booted, the micro SD card is enumerated as a mass storage device. On most systems, this is automatically mounted. However, manual mounting is sometimes required."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/deployment.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/deployment.md#mps3-mps4-fpga-board"
license: "Apache-2.0"
mode: "V"
---

> **Note:**  Before proceeding, make sure that you have the MPS3/MPS4 board powered on, and a USB cable connected
> between your machine and the board (USB-A to USB-B for MPS3, USB-A to USB-C for MPS4).
> The connector on the board is marked as "Debug USB".

(figure: MPS3)

### MPS3/MPS4 board top-view

Once the board has booted, the micro SD card is enumerated as a mass storage device. On most systems, this is
automatically mounted. However, manual mounting is sometimes required.

Also, check for four serial-over-USB ports that are available for use through this connection. 
* On Linux-based machines, these would typically be */dev/ttyUSB`<n>`* to */dev/ttyUSB\<n+3\>*.
* On macOS® machines, these would typically be */dev/tty.usbserial-`<n>`* to */dev/tty.usbserial-\<n+3\>*.

The default configuration for all of them is `115200`, `8/N/1`. So, 15200 Baud, 8 bits, no parity, and one stop bit,
with no flow control.

> **Note:** For Windows machines, extra FTDI drivers may be required for these serial ports to be available.

For more information on getting started with an MPS3 board, please refer to:
[MPS3 Getting Started](https://developer.arm.com/-/media/Arm%20Developer%20Community/PDF/MPS3GettingStarted.pdf).

### Deployment on MPS3/MPS4 board

To run the application on MPS3 platform, you must first ensure that the platform has been set up using the correct
configuration.

> **Note:**: These instructions are valid only if the evaluation is being done using the MPS3 FPGA platform using
> an Arm® Corstone™-300 (AN552) or Corstone™-310 (AN555) implementations, or MPS4 FPGA using Corstone™-320 implementation.

For details on platform set-up, please see the relevant documentation.

- Arm® Corstone™-300 implementation `AN552`: [Arm Developer - AN552](https://developer.arm.com/documentation/dai0552/).
- Arm® Corstone™-310 implementation `AN555`: [Arm Developer - AN555](https://developer.arm.com/documentation/107642/B/?lang=en)

For the MPS3/MPS4 FPGA board, instead of loading the `axf` file directly, copy the executable blobs generated under the
`sectors/<use_case>` subdirectory to the microSD card located on the board. Also, the `sectors/images.txt` file is
used by the MPS3 to understand which memory regions the blobs must be loaded into.

Once the USB cable between the board and the development machine is connected, and the board powered on,
the board enumerates as a mass storage device over this USB connection.
The MPS3 board has a USB-B for its debug USB interface, and the MPS4 board has USB-C.

Depending on the version of the board you are using, there might be two devices listed.
One of the devices will be the microSD card on the board, which will likely be named:
- `V2M-MPS3` for MPS3
- `MPS4` for MPS4

+Note that if `V2M-MPS3` or `MPS4` device is not listed, you may need to enable USB
connection from the board. You can do this by opening a serial connection to the first serial port (as specified in
point 3 in the instructions below) and issuing a `usb_on` command at the prompt:

```commandline
Cmd> usb_on
Enabling debug USB...
USB Serial Number = 5000123456789
```

If the `axf` or `elf` file is within the ITCM/BRAM load size limit, it can be copied into the FPGA memory directly
without having to break it down into separate load region-specific blobs. However, if the neural network models exceed
this size, you must use the approach described below.

1. For example, the image classification use-case produces the following for Corstone™-300:

    ```tree
    ./bin/sectors/
        └── img_class
            ├── ddr.bin
            └── itcm.bin
    ```
    For Corstone™-310, the tree should have:
    ```tree
    ./bin/sectors/
        └── img_class
            ├── bram.bin
            └── ddr.bin
    ```
    For Corstone™-320, the tree should have:
    ```tree
    ./bin/sectors/
        └── img_class
            ├── boot.bin
            ├── bram.bin
            └── ddr.bin
    ```
    As reflected in the names above, the primary code memory for Arm® Corstone™-300 is the ITCM.
    For Arm® Corstone™-310 however, this is the FPGA SRAM (or BRAM) region instead.
    This is because the ITCM is only 32kB which cannot accommodate the code footprint for our applications.
    For Arm® Corstone™-320, there is a read-only boot region where our boot code must be placed.

    Copy these binaries to the connected MPS3 board as follows:

    ```commandline
    # MPS3
    cp -av ./bin/sectors/img_class/* /media/user/V2M-MPS3/SOFTWARE/ && sync
    ```

    or for MPS4:

    ```commandline
   # MPS4
    cp -av ./bin/sectors/img_class/* /media/user/MPS4/SOFTWARE/ && sync
    ```

    For macOS®, the micro SD card is likely mounted at `/Volumes/V2M-MPS3` or `/Volumes/MPS4`.

    Note that the `boot.bin`, `itcm.bin`, `bram.bin` and `ddr.bin` files correspond to the part of the application
    residing in different load regions, as defined in the
    [scatter file for sse-300](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/../../scripts/cmake/platforms/mps3/sse-300/mps3-sse-300.armclang.sct),
    [scatter file for sse-310](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/../../scripts/cmake/platforms/mps3/sse-310/mps3-sse-310.armclang.sct) and
    [scatter file for sse-320](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/../../scripts/cmake/platforms/mps4/sse-320/mps4-sse-320.armclang.sct).


2. The `./bin/sectors/images.txt` file must be copied over to the MPS3. The exact location for the destination depends
   on the version of the MPS3 board and the application note for the bit file in use.

   For example, with revision `C` of the MPS3 board hardware, using an application note directory named `AN552`, we can
   replace the `images.txt` file by:
    ```commandline
    # MPS3
    cp ./bin/sectors/images.txt /media/$USER/V2M-MPS3/MB/HBI0309C/AN552/images.txt && sync
    ```
   With revision `B` of the MPS4 board hardware, using the Corstone™-320 image, use the following:
    ```commandline
    # MPS4
    cp ./bin/sectors/images.txt /media/$USER/MPS4/MB/HBI0376B/FI101/images.txt && sync
    ```

    > **NOTE**: Make sure the SD card is unmounted correctly after all the files have been copied. For example:

    > On Linux:
    > ```commandline
    > # MPS3
    > umount /media/user/V2M-MPS3
    > # MPS4
    > umount /media/user/MPS4
    > ```
    > On macOS®:
    > ```commandline
    > # MPS3
    > diskutil eject /Volumes/V2M-MPS3
    > # MPS4
    > diskutil eject /Volumes/MPS4
    > ```


3. Open the first serial port available from MPS3. For example, `/dev/ttyUSB0` or `/dev/tty.usbserial-000000`. This can be typically done using
   `minicom`, `screen`, or `Putty` applications. Make sure the configuration is set to 115200 8/N/1 and that the
   flow control setting is switched off:

    ```commandline
    minicom --D /dev/ttyUSB0
    ```

    You should see an output similar to:

    ```log
    Welcome to minicom 2.7.1
    OPTIONS: I18n
    Compiled on Aug 13 2017, 15:25:34.
    Port /dev/ttyUSB0, 16:05:34
    Press CTRL-A Z for help on special keys
    Cmd>
    ```

4. In another terminal, open the second serial port. For example: `/dev/ttyUSB1` or `/dev/tty.usbserial-000001`:

    ```commandline
    minicom --D /dev/ttyUSB1
    ```

5. On the first serial port, issue a "reboot" command and then press the return key:

    ```commandline
    $ Cmd> reboot
    ```

    ```log
    Rebooting...
    Disabling debug USB..
    Board rebooting...

    ARM V2M-MPS3 Firmware v1.5.1
    Build Date: Jun  2 2021

    Powering up system...
    Switching on main power...
    Configuring motherboard (rev C, var A)...
    ```

    This goes on to reboot the board and prime the application to run by flashing the binaries into their respective
    FPGA memory locations. For example:

    ```log
    Reading images file \MB\HBI0309C\AN552\images.txt
    Writing File \SOFTWARE\itcm.bin to Address 0x00000000
    ......
    File \SOFTWARE\itcm.bin written to memory address 0x00000000
    Image loaded from \SOFTWARE\itcm.bin
    Writing File \SOFTWARE\ddr.bin to Address 0x0C000000
    .......................................................................................................................................................................
    File \SOFTWARE\ddr.bin written to memory address 0x0C000000
    Image loaded from \SOFTWARE\ddr.bin
    ```

6. If the reboot from previous step completes without starting the application, issue a reset command:

    ``` commandline
    $ Cmd> reset
    ```

    This should trigger the application to start, and the output should be visible on the second serial
    connection. By default, the FPGA configuration should start the application as soon as it is loaded
    into the memory and the above command should not be required.

7. On the second serial port the output should show the standard output and error streams from the
   application deployed. For example:

    ```log
    INFO - V2M-MPS3 revision C
    INFO - Application Note AN552, Revision B
    INFO - MPS3 build 2
    INFO - MPS3 core clock has been set to: 32000000Hz
    INFO - CPU ID: 0x411fd220
    INFO - CPU: Cortex-M55 r1p0
    ...
    ```

The next section of the documentation details: [Implementing custom ML application](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/customizing.md).

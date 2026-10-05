---
id: "ocp-readme-board-configuration"
type: "concept"
domain: "project"
title: "README: Board configuration"
summary: "README: Board configuration"
status: "draft"
collection: "ocp-tools-readmes"
source: "Open-CMSIS-Pack/RefApp-Framework@54fba8b:layer/Board/B-U585I-IOT02A/IoT/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/RefApp-Framework/blob/54fba8b/layer/Board/B-U585I-IOT02A/IoT/README.md#board-configuration"
license: "Apache-2.0"
mode: "V"
---

**Board setup**

  - Insure that the **5V_USB_STLK** and **JP3** jumpers are bridged and the remaining jumpers are not bridged
  - Check that the **BOOT0** DIP switch is in the **0** / right position (closest to the ST-LINK STLK CN8 USB connector)
  - Connect a **USB micro-B cable** between the **STLK** connector and your **Personal Computer**

**WiFi module firmware update** (required for older board revision C01)

  - Download the [EMW3080 update tool](https://www.st.com/content/ccc/resource/technical/software/firmware/group1/48/a2/e8/27/7f/ae/4b/26/x-wifi-emw3080b/files/x-wifi-emw3080b.zip/jcr:content/translations/en.x-wifi-emw3080b.zip) archive from the STMicroelectronics website
  - Extract the downloaded archive
  - Connect a **USB micro-B cable** between the **STLK** connector and your **Personal Computer**
  - Start the serial terminal application on the PC and connect via the **Virtual COM Port** of the **ST-LINK**
  - Drag and drop the **EMW3080updateV2.1.11RevC.bin** binary from the subfolder **V2.1.11\\SPI\\** of the previously 
    extracted **MW3080 update tool** package to the **DIS_U585AI** USB mass storage device
  - Flip the **SW2 - BOOT** DIP switch (**not the main BOOT0** DIP switch) to the **0** position instead of **NC 1** position
  - Press the **RST** (black) button to reset the STM32U5 microcontroller that will display a menu in the serial terminal
  - Press the **USER** (blue) button to start the firmware update
  - Wait for programming to finish, serial terminal display should look like below:
    ```
    Boot done successfully
    STM32>Waiting EMW3080 ready for programming (you should wait for more than 20 seconds before getting any message)
    Transferring packet ...
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
    ...
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
    STM32>Programming successful, move back switch to original position, reset the device to get back to prompt
    ```  
  - Return the **SW2 - BOOT** DIP switch to the **NC 1** position
  - Press the **RST** (black) button to reset the STM32U5 microcontroller thus concluding the firmware update

  > Note: When TrustZone is enabled the USB device does not show mass storage device as **DIS_U585AI** but as **NOD_U585AI** which 
    cannot be used for firmware update. To update the EMW3080 firmware the TrustZone needs to be disabled.

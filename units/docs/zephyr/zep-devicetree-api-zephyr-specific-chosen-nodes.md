---
id: "zep-devicetree-api-zephyr-specific-chosen-nodes"
type: "concept"
domain: "project"
title: "Devicetree API: Zephyr-specific chosen nodes"
summary: "The following table documents some commonly used Zephyr-specific chosen nodes."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/build/dts/api/api.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/build/dts/api/api.rst"
license: "Apache-2.0"
mode: "V"
---

The following table documents some commonly used Zephyr-specific chosen nodes.

Sometimes, a chosen node's label property will be used to set the default value
of a Kconfig option which in turn configures a hardware-specific device. This
is usually for backwards compatibility in cases when the Kconfig option
predates devicetree support in Zephyr. In other cases, there is no Kconfig
option, and the devicetree node is used directly in the source code to select a
device.

.. Keep list sorted by property name:
.. zephyr-keep-sorted-start re(^\s+\* - \w+,\w+)


* - Property
  - Purpose
* - mcuboot,ram-load-dev
  - When a Zephyr application is built to be loaded to RAM by MCUboot, with
    this property is used to tell MCUboot the load address of the image, which
    will be the `reg` of the chosen node.
* - zephyr,boot-mode
  - Used for boot_mode_api selection, part of retention_api, which specifies
    what image on a device should be booted.
* - zephyr,bootloader-info
  - Selects the retention_api area used to share information with the bootloader.
* - zephyr,bt-c2h-uart
  - Selects the UART used for host communication in the
* - zephyr,bt-hci
  - Selects the HCI device used by the Bluetooth host stack
* - zephyr,bt-hci-ipc
  - Selects the IPC device used to expose a Bluetooth controller to another
    device or CPU in the bluetooth_hci_ipc sample.
* - zephyr,bt-mon-uart
  - Sets UART device used for the Bluetooth monitor logging
* - zephyr,camera
  - Video input device, typically a camera.
* - zephyr,canbus
  - Sets the default CAN controller
* - zephyr,code-partition
  - Flash partition that the Zephyr image's text section should be linked
    into
* - zephyr,console
  - Sets UART device used by console driver
* - zephyr,cpu-load-counter
  - Selects the counter_api device used to track CPU idle time.
* - zephyr,crc
  - Selects the CRC device used as an accelerator by the CRC subsystem
* - zephyr,display
  - Sets the default display controller
* - zephyr,dtcm
  - Data Tightly Coupled Memory node on some Arm SoCs
* - zephyr,edac
  - Selects the edac_api device used by the EDAC subsystem.
* - zephyr,entropy
  - A device which can be used as a system-wide entropy source
* - zephyr,flash
  - A node whose `reg` is sometimes used to set the defaults for
* - zephyr,flash-controller
  - The node corresponding to the flash controller device for
    the `zephyr,flash` node
* - zephyr,gdbstub-uart
  - Sets UART device used by the gdbstub subsystem
* - zephyr,hdlc-rcp-if
  - Selects the radio device used by the OpenThread HDLC RCP interface.
    This device must have `hdlc_api` as its `api`.
* - zephyr,host-cmd-espi-backend
  - Refer to ec_host_cmd_backend_api API documentation.
* - zephyr,host-cmd-shi-backend
  - Refer to ec_host_cmd_backend_api API documentation.
* - zephyr,host-cmd-spi-backend
  - Refer to ec_host_cmd_backend_api API documentation.
* - zephyr,host-cmd-uart-backend
  - Refer to ec_host_cmd_backend_api API documentation.
* - zephyr,ieee802154
  - Used by the networking subsystem to set the IEEE 802.15.4 device
* - zephyr,ipc
  - Used by the OpenAMP subsystem to specify the inter-process communication
    (IPC) device
* - zephyr,ipc_rsc_table
  - Specifies a memory region that will be used for the OpenAMP resource table.
    Only needed if `CONFIG_OPENAMP_COPY_RSC_TABLE` is enabled.
* - zephyr,ipc_rx
  - Alternative to `zephyr,ipc`. Selects the IPC device to use for reception
    when separate devices are used for TX and RX. `zephyr,ipc_tx` must also
    be provided alongside this chosen, and selects the IPC device to use for
    transmission. When this chosen and `zephyr,ipc_tx` are provided, the
    single-device `zephyr,ipc` compatible **must not** be provided.
* - zephyr,ipc_shm
  - A node whose `reg` is used by the OpenAMP subsystem to determine the
    base address and size of the shared memory (SHM) usable for
    interprocess-communication (IPC)
* - zephyr,ipc_tx
  - See description of `zephyr,ipc_rx`.
* - zephyr,itcm
  - Instruction Tightly Coupled Memory node on some Arm SoCs
* - zephyr,led-strip
  - A LED-strip node which is used to determine the timings of the
    WS2812 GPIO driver
* - zephyr,log-ipc
  - Selects the IPC device used by the logging subsystem's IPC service backend.
* - zephyr,log-uart
  - Sets the UART device(s) used by the logging subsystem's UART backend.
    If defined, the UART log backend would output to the devices listed in this node.
* - zephyr,modem-uart
  - Selects the modem UART used by the at_client sample.
* - zephyr,ocm
  - On-chip memory node on Xilinx Zynq-7000 and ZynqMP SoCs
* - zephyr,openthread-counter
  - Selects the counter device used by the OpenThread platform for microsecond alarm
    timers when `CONFIG_OPENTHREAD_ALARM_COUNTER` is enabled.
* - zephyr,osdp-uart
  - Sets UART device used by OSDP subsystem
* - zephyr,ot-uart
  - Used by the OpenThread to specify UART device for Spinel protocol
* - zephyr,pcie-controller
  - The node corresponding to the PCIe Controller
* - zephyr,ppp-uart
  - Sets UART device used by PPP
* - zephyr,ram-console
  - Selects the `RAM section <zephyr,memory-region>` in which
    the console subsystem's RAM backend should place its buffer.
* - zephyr,rtc
  - Sets the default RTC device (used for example by the SNTP library to
    set the system time when `CONFIG_NET_CONFIG_CLOCK_SNTP_SET_RTC` is enabled)
* - zephyr,rtk-serial
  - Selects the uart_api device used by the Serial GNSS RTK client.
* - zephyr,secure-storage-its-partition
  - Fixed partition node. This selects the partition used by the Secure Storage ZMS backend.
* - zephyr,sensor-clock
  - Selects the counter_api device used as sensor time source.
* - zephyr,settings-partition
  - Fixed partition node. If defined this selects the partition used
    by the NVS and FCB settings backends.
* - zephyr,shell-uart
  - Sets UART device used by serial shell backend
* - zephyr,sram
  - A node whose `reg` sets the base address and size of SRAM memory
    available to the Zephyr image, used during linking
* - zephyr,system-timer
  - Selects the hardware timer instance used as the Zephyr system timer,
    which is a singleton system-wide function. This chosen is needed when the
    selected system timer driver corresponds to timer hardware for which multiple
    instances may exist: it selects one instance as the system timer and allows
    using the other instances with other APIs. This chosen is ignored when the
    selected system timer driver corresponds to timer hardware for which only one
    instance may ever exist, such as the Cortex-M SysTick timer; otherwise, it
    must corresponds to a node that the selected system timer driver can operate.
    (Note: the Zephyr system timer *driver* is selected using Kconfig options such
    as `CONFIG_CORTEX_M_SYSTICK` - not Devicetree!)
* - zephyr,system-timer-companion
  - Selects the device used to keep time while the primary system timer is
    inactive in low-power states. It must implement the counter_api API.
* - zephyr,tflm-storage
  - Selects the `memory region <zephyr,memory-region>`
    used by the tflite-ethosu sample.
* - zephyr,touch
  - Touchscreen controller device node. When LVGL is used, if
    pointer input device is created using the touchscreen controller
    as its input source.
* - zephyr,tracing-uart
  - Sets UART device used by tracing subsystem
* - zephyr,uart-mcumgr
  - UART used for device_mgmt
* - zephyr,uart-pipe
  - Sets UART device used by serial pipe driver
* - zephyr,videoenc
  - Video encoder device, typically an H264 or MJPEG video encoder.
.. zephyr-keep-sorted-stop

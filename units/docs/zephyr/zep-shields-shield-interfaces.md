---
id: "zep-shields-shield-interfaces"
type: "concept"
domain: "bring-up"
title: "Shields: Shield interfaces"
summary: "A shield is defined by two key characteristics:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/porting/shields.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/porting/shields.rst"
license: "Apache-2.0"
mode: "V"
---

A shield is defined by two key characteristics:

#. **Physical connectors** - the mechanical interface
#. **Electrical signals** - what each pin actually does

The connection between a shield and a board happens through Devicetree files:

- Board side: The board's devicetree file uses a GPIO nexus node to map
  connector pins to the microcontroller's actual GPIO pins. It also defines labels for buses exposed
  through the connector (like `arduino_i2c`, `arduino_spi`, `arduino_uart`).

- Shield side: The shield's .overlay file references these same labels to describe how its
  components connect to the board.

At build time, the board's devicetree and the shield's overlay are combined to create a complete
picture of the hardware setup.

For example, let's say you have a board with an Arduino connector but no built-in accelerometer.
You can add one using an Arduino shield:

#. The board's Devicetree defines an `arduino_i2c` label: it is the I2C bus made available on the
   Arduino connector

#. The accelerometer shield's overlay file also references `arduino_i2c` to indicate it uses that
   same I2C bus. If it needs to use GPIO pins from the connector, it references the GPIO nexus node
   defined by the board's Devicetree (e.g. `arduino_header`).

When you then build for this board with this shield, Zephyr automatically "wires them" together.


**Note:** Some boards and shields may only support a limited set of features of a shield hardware interface. Refer to their documentation for more details.


### Arduino MKR


This is the form factor of the Arduino MKR boards.

Relevant devicetree node labels:

- `arduino_mkr_header` See `arduino-mkr-header` for details on GPIO pin definitions
  and includes for use in devicetree files.
- `arduino_mkr_i2c`
- `arduino_mkr_spi`
- `arduino_mkr_serial`



### Arduino Nano


This is the form factor of the Arduino Nano boards.

Relevant devicetree node labels:

- `arduino_nano_header` See `arduino-nano-header` for details on GPIO pin definitions
  and includes for use in devicetree files.
- `arduino_nano_i2c`
- `arduino_nano_spi`
- `arduino_nano_serial`



### Arduino Uno R3


This is the form factor of the Arduino Uno R3 board.

Relevant devicetree node labels:

- `arduino_header` See `arduino-header-r3` for details on GPIO pin definitions
  and includes for use in devicetree files.
- `arduino_adc` See `arduino,uno-adc`
- `arduino_pwm` See `arduino-header-pwm`
- `arduino_serial`
- `arduino_i2c`
- `arduino_spi`

For technical details, see Arduino Uno R3 pinout.



### Camera and display connectors


These describe connections to cameras and displays (strictly speaking not shields).

- `arducam,dvp-20pin-connector`
- `nxp,cam-44pins-connector`
- `nxp,parallel-lcd-connector`
- `raspberrypi,csi-connector`
- `st,dsi-lcd-qsh-030-connector`
- `st,dvp-cam-zif-30-connector`
- `weact,dcmi-camera-connector`



### ESP-01


This is an 8-pin header for ESP-01 Wi-Fi modules.

Relevant devicetree node labels:

- `esp_01_header` See `esp-01-header` for details on GPIO pin
  definitions and includes for use in devicetree files.
- `esp_01_serial`



### Feather


This is the form factor of the Adafruit Feather series of boards.
Shields intended for Feather boards are called Featherwings.

Relevant devicetree node labels:

- `feather_header` See `adafruit-feather-header` for GPIO pin definitions.
- `feather_adc`
- `feather_i2c`
- `feather_serial`
- `feather_spi`



### Microbit


This is for the edge connector of the Microbit boards.

See `microbit,edge-connector` for GPIO pin definitions and
links to technical requirements.



### mikroBUS™


This is an interface standard for add-on boards, developed by Mikroe.

Relevant devicetree node labels:

- `mikrobus_header` See `mikro-bus` for GPIO pin definitions and links to
  technical specifications.
- `mikrobus_adc`
- `mikrobus_i2c`
- `mikrobus_pwm`
- `mikrobus_spi`
- `mikrobus_serial`

Note that boards with several mikroBUS™ connectors might define for
example `mikrobus_2_spi`.



### Pico


This is the form factor of the Raspberry Pi Pico boards.

Relevant devicetree node labels:

- `pico_header` See `raspberrypi,pico-header` for GPIO pin definitions.
- `pico_i2c` A node label that refers to the same node as either the node label
  `pico_i2c0` or `pico_i2c1`. It references the node that should be used with
  priority or as default.
- `pico_i2c0`
- `pico_i2c1`
- `pico_serial`
- `pico_spi`



### ST Morpho


Development boards from ST Microelectronics often uses the ST Morpho shield interface.

Relevant devicetree node labels:

- `st_morpho_header`  See `st-morpho-header` for details on GPIO pin definitions
  and includes for use in devicetree files.
- `st_morpho_lcd_spi`
- `st_morpho_flash_spi`



### ST Zio


STM32 Nucleo-144 development boards from ST Microelectronics expose the ST Zio
connector, an extension of the Arduino Uno V3 connector that gives access to
more of the STM32 I/Os through four headers (CN7, CN8, CN9 and CN10).

Relevant devicetree node labels:

- `st_zio_header`  See `st-zio-header` for details on GPIO pin definitions
  and includes for use in devicetree files.



### STMod+


This is a 20-pin expansion connector found on some STMicroelectronics Discovery
and Evaluation boards.

Relevant devicetree node labels:

- `stmod_plus_connector` See `st,stmod-plus-connector` for
  details on GPIO pin definitions and includes for use in devicetree files.
- `stmod_adc`
- `stmod_i2c`
- `stmod_pwm`
- `stmod_serial`
- `stmod_spi`

Boards may expose additional interface labels when a peripheral is wired to the
STMod+ connector and enabled in the board devicetree.



### WisBlock


This is a modular interface standard for add-on boards, developed by RAKwireless.
It defines Core, Sensor, I/O and Power Slots, each accepting a module of the
matching class through a 24-pin or 40-pin WisConnector.

Relevant devicetree node labels:

- `wisblock_io` See `wisblock-io-slot` for GPIO pin definitions.
- `wisblock_sensor_a` See `wisblock-sensor-slot` for GPIO pin definitions.
- `wisblock_adc`
- `wisblock_pwm`
- `wisblock_i2c1`
- `wisblock_i2c2`
- `wisblock_i2s`
- `wisblock_pdm`
- `wisblock_spi`
- `wisblock_uart0`
- `wisblock_uart1`

Note that Sensor Slots are labeled `wisblock_sensor_a` through
`wisblock_sensor_f` after the Slot they implement.



### Xiao


This is the form factor of the Seeeduino XIAO boards.

Relevant devicetree node labels:

- `xiao_d` See `seeed,xiao-gpio` for GPIO pin definitions.
- `xiao_spi`
- `xiao_i2c`
- `xiao_serial`
- `xiao_adc`
- `xiao_dac`



### zephyr_i2c / Stemma QT / Quiic


These are four-pin I2C connectors. SparkFun calls these connectors "Qwiic", and Adafruit
calls them "Stemma QT". The I2C connectors have four pins; GND, +3.3 Volt, I2C data and I2C
clock. The most common physical connector is the 1.0 mm pitch JST-SH.

Due to the different brand names, the interface is labeled "zephyr_i2c".

See `stemma-qt-connector` and `grove-header` for descriptions
and links to further details.

Relevant devicetree node labels:

- `zephyr_i2c`


### ST M.2 serial memory connector


Some STMicroelectronics Nucleo-144 development boards expose an ST-specific
M.2 serial memory connector used to interface with external serial memories
through XSPI, together with auxiliary signals such as I2C and connector GPIOs.

Relevant devicetree node labels:

- `m2mem_connector`  See `st,m2-memory-connector` for details on GPIO pin definitions
  and includes for use in devicetree files.
- `m2mem_i2c`
- `m2mem_xspi`

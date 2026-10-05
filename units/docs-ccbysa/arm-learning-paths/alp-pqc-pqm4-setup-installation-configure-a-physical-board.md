---
id: "alp-pqc-pqm4-setup-installation-configure-a-physical-board"
type: "concept"
domain: "core"
title: "Implement post-quantum cryptography on Arm Cortex-M4: Set up the pqm4 development environment: Configure a physical board"
summary: "If you're using a physical development board, follow these steps to configure it."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/pqc_pqm4/setup-installation.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/pqc_pqm4/setup-installation/#configure-a-physical-board"
license: "CC-BY-SA-4.0"
mode: "V"
---

If you're using a physical development board, follow these steps to configure it.

### Install stlink 

Install stlink using your package manager.

On Linux:

```bash
sudo apt-get install stlink-tools
```

On macOS:

```bash
brew install stlink
```

If you need to build from source on Linux:

```bash
sudo apt-get install libusb-1.0-0-dev -y
git clone https://github.com/stlink-org/stlink.git
cd stlink
make release
```

Verify the connection to your board:

```bash
st-info --probe
```

The output is similar to:

```output
Found 1 stlink programmers
```

### (Optional) Install OpenOCD 

If you are using a physical board and stlink does not support it, install OpenOCD as an alternative.

On Linux:

```bash
sudo apt-get install openocd -y
```

On macOS:

```bash
brew install openocd
```

If your package manager provides an older version that doesn't support your board, you can build from source instead:

```bash
sudo apt install libjim-dev libtool-bin -y
git clone https://github.com/openocd-org/openocd.git
cd openocd
./bootstrap
./configure
make
sudo make install
```

### (Optional) Install ChipWhisperer 

ChipWhisperer is required only if you're using the `cw308t-stm32f3` platform. If you're using another board such as NUCLEO or STM32 Discovery, skip this section.

Install it using pip:

```bash
python3 -m pip install chipwhisperer
```


### Build for a target platform

Build pqm4 by specifying the platform identifier for your board using the `PLATFORM` variable.

For NUCLEO-L4R5ZI (the pqm4 default):

```bash
make -j4 PLATFORM=nucleo-l4r5zi
```

For NUCLEO-L476RG:

```bash
make -j4 PLATFORM=nucleo-l476rg
```

For STM32F4 Discovery:

```bash
make -j4 PLATFORM=stm32f4discovery
```
For a full list of supported platforms, see the [pqm4 README](https://github.com/mupq/pqm4).

### Configure the serial port 

The script `host_unidirectional.py` uses a default serial port (often `/dev/ttyUSB0`) which might not match your system. Update it to match your board's serial port.

On macOS:

```bash
ls /dev/tty.*
```

On Linux:

```bash
ls /dev/ttyACM* /dev/ttyUSB*
```

Open the script:

```bash
nano hostside/host_unidirectional.py
```

Update this line with your actual port:

```python
dev = serial.Serial("/dev/tty.usbmodemXXXX", 38400)
```

### Flash and verify communication

Connect the board to your host machine using the mini-USB port to provide power and enable flashing.

Flash a test binary:

```bash
st-flash write bin/boardtest.bin 0x8000000
```

Read the output from the board:

```bash
python3 hostside/host_unidirectional.py
```

Press the RESET button on the board. The output is similar to:

```output
Hello world
Stack Size
Random number
```

If you see this output, your board is flashed, communicating over serial, and ready to run pqm4.

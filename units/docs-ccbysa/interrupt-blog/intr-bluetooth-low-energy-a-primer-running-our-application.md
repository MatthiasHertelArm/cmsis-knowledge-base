---
id: "intr-bluetooth-low-energy-a-primer-running-our-application"
type: "concept"
domain: "debug"
title: "Bluetooth Low Energy: A Primer: Implementation of a BLE Peripheral (nRF52 example) / Running our Application"
summary: "Part of: Implementation of a BLE Peripheral (nRF52 example)"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-07-30-bluetooth-low-energy-a-primer.md"
doc_source: "https://interrupt.memfault.com/blog/bluetooth-low-energy-a-primer#running-our-application"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Implementation of a BLE Peripheral (nRF52 example)_

As we mentioned earlier, we'll be using command line for almost everything in this post. For compiling the application, we'll be using ARM GCC and GNU Make. For flashing the application to the board, we'll be using the Nordic Command Line Tools (specifically, the `nrfjprog` command).

#### 1. Compiling the Application
Before we can compile the application, we need to make a couple of modifications:

- Add the new Simple Service source code file to `Makefile`.
	We add `$(PROJ_DIR)/simple_service.c` to the `Makefile` file which is located at `ble_peripheral/ble_app_template/pca10056/s140/armgcc/Makefile`:

	```bash
	  $(PROJ_DIR)/main.c \
	  $(PROJ_DIR)/simple_service.c \
	  $(SDK_ROOT)/external/segger_rtt/SEGGER_RTT.c \
	```

- Update the `Makefile.posix` file to point to the correct location and version of the armgcc compiler. Edit the file located at `<nRF5 SDK Folder>/components/toolchain/gcc/Makefile.posix`:

	```bash
	GNU_INSTALL_ROOT ?= <Toolchain Folder>/gcc-arm-none-eabi-7-2017-q4-major/bin/
	GNU_VERSION ?= 7.2.1
	GNU_PREFIX ?= arm-none-eabi
	``` 
	
	Make sure you replace `<Toolchain Folder>` with the appropriate path based on where you installed the armgcc toolchain.
	
Now that we've made these changes, we're ready to compile our application and flash it to the development board.

In the same folder where `Makefile` is located (`ble_peripheral/ble_app_template/pca10056/s140/armgcc/`), run the following command.

```terminal
$ make
```

Sometimes, it's a good idea to run `make clean` before running `make` just to make sure you are starting from a clean state. You should see an output similar to this when it finishes:



#### 2. Hardware Setup
The second step is to get the hardware set up to run the example.

Here are the steps to accomplish this:

- Connect the development kit to your computer (via the micro-USB to USB-A cable)
- Make sure the development kit jumpers are in the right settings:
	- **SW6** set to "Default" (**not** "nRF ONLY")
	- **SW9** (nRF power source) set to "VDD"
	- **Power** set to "ON"
	
	

	
	
- Erase the development kit by running the following command. This will erase the chipset on the board, just to make sure we are starting from a clean slate.

	```terminal
	$ nrfjprog -f NRF52 --eraseall
	```

- Next, we will flash the chipset with Nordic's SoftDevice which acts as both the BLE stack and RTOS (Real-Time Operating System) for the nRF52 chipset. This is crucial before flashing our application (since the binaries compile separately).

	To do this, run the following command:

	```terminal
	$ nrfjprog -f NRF52 --program <nRF5 SDK Folder>/components/softdevice/s140/hex/s140_nrf52_6.1.1_softdevice.hex --chiperase --verify
	```
	
	Don't forget to change the `<nRF5 SDK Folder>` portion to match the location where you installed/unzipped the nRF5 SDK.
	
- The final step is to flash the application binary to the chipset. To do this, run the following command:

	```terminal
	$ nrfjprog -f NRF52 --program _build/nrf52840_xxaa.hex --verify
	```
	
That's it! Our application should now be running on the board. To verify that, we will be using a serial terminal program.

In the next section, we'll go through setting up the terminal program and then verify that the application is running correctly.

#### 3. Serial Terminal Program Setup
As we mentioned earlier, we'll be using a program called CoolTerm.

There are three parts to get this working:

- Run the CoolTerm application
- Make sure the serial port settings are correct (listed at [this link](https://infocenter.nordicsemi.com/topic/com.nordic.infocenter.sdk5.v15.3.0/uart_example.html)):
 
	
	
	Now, hit **OK**. 

- Finally, connect to the serial port by clicking the "Connect" button:
	
	
	
	You may not see any output since the program probably started before you connected. To reset the development board, we can simply run the following command from the Terminal:
	
	```terminal
	$ nrfjprog -f NRF52 --reset
	```
	
The first time you run the application you'll most likely get an error that looks something like this:



This is due to the fact that we modified the value of the macro for the number of vendor-specific UUIDs in the SoftDevice. The good part is that the log output tells us exactly which values we need to use for RAM offset and RAM size to fix this problem.

In order to apply the fix, we need to edit the file named `ble_app_template_gcc_nrf52.ld` located at `ble_app_template/pca10056/s140/armgcc/` and modify the values of 
```
RAM (rwx) :  ORIGIN
```
and
```
RAM (rwx) :  LENGTH
```



Now we just need to repeat the steps of cleaning, building, and flashing the SoftDevice, and application to the target.

If all goes well, you should now see the following printed in the Terminal window:
	


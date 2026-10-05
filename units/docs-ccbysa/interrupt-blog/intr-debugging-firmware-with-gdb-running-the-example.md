---
id: "intr-debugging-firmware-with-gdb-running-the-example"
type: "concept"
domain: "debug"
title: "Debugging Firmware with GDB: Running the Example"
summary: "Before we can actually debug the application and use GDB, we need to build the example and flash it to the development kit."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-05-21-gdb-for-firmware-1.md"
doc_source: "https://interrupt.memfault.com/blog/gdb-for-firmware-1#running-the-example"
license: "CC-BY-SA-4.0"
mode: "V"
---

Before we can actually debug the application and use GDB, we need to build the example and flash it to the development kit.

Following are the steps we need to take:
### 1. nRF52 Example Compilation
In our tutorial, we'll be using the UART example included as part of the nRF5 SDK (version 15.3.0). This example is located at:

```
<nRF5_SDK_Folder>/examples/peripheral/uart/
```

You'll notice there are many subfolders in that folder. We are mostly interested in the following highlighted folder in the screenshot:





Before we build the example, let's make sure we have the right compiler flags for debugging. This is necessary to include debugging symbols that help GDB present useful debugging information to the user.

To check the compiler flags, edit the `Makefile` located at `<nRF5_SDK_Folder>/examples/peripheral/uart/pca10056/blank/armgcc`.

In the Makefile, look for the "Optimization flags" section:

```bash
# Optimization flags
OPT = -O3 -g3
# Uncomment the line below to enable link time optimization
#OPT += -flto

# C flags common to all targets
CFLAGS += $(OPT)
```

Let's modify this to reflect the following changes:

```bash
# Optimization flags
OPT = -Og -g3
# Uncomment the line below to enable link time optimization
#OPT += -flto

# C flags common to all targets
CFLAGS += $(OPT)
```

We changed the compiler's optimization level to "-Og", which optimizes the debugging experience. According to GDB's [documentation for Optimization](https://gcc.gnu.org/onlinedocs/gcc-12.2.0/gcc/Optimize-Options.html):

>
Turning on optimization flags makes the compiler attempt to improve the performance and/or code size at the expense of compilation time and possibly the ability to debug the program.
>

and

>
-Og should be the optimization level of choice for the standard edit-compile-debug cycle, offering a reasonable level of optimization while maintaining fast compilation and a good debugging experience. It is a better choice than -O0 for producing debuggable code because some compiler passes that collect debug information are disabled at -O0.
>

Now, we can go ahead and build the project. To do this, run the following command:

```terminal
$ make
```

The output should look something like this:





### 2. Hardware Setup
The second step is to get the hardware set up to run the example.

Here are the steps to accomplish this:

- Connect the development kit to your computer (via the micro-USB to USB-A cable)
- Make sure the development kit jumpers are in the right settings:
	- **SW6** set to "Default" (**not** "nRF ONLY")
	- **SW9** (nRF power source) set to "VDD"
	- **Power** set to "ON"

	

- Erase the development kit by running the following command:

	```terminal
	$ nrfjprog -f NRF52 --eraseall
	```

- The final step is to flash the development kit with the example's binary.

	To do so, run the following command from the folder `<nRF5_SDK_Folder>/examples/peripheral/blinky/pca10056/blank/armgcc`.

	```terminal
	$ nrfjprog -f NRF52 --program _build/nrf52840_xxaa.hex --chiperase
	```

That's it!

Now the nRF52840 development kit should be flashed with the UART example and it should be running properly.

To verify that, we will be using a serial terminal program.

### 3. Serial Terminal Program Setup
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

	If all goes well, you should see the following printed in the Terminal window:


	

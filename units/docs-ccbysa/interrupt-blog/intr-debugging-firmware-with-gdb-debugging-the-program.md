---
id: "intr-debugging-firmware-with-gdb-debugging-the-program"
type: "concept"
domain: "debug"
title: "Debugging Firmware with GDB: Debugging the Program"
summary: "Now that we have the application running properly, let's go ahead and set up the debugger."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-05-21-gdb-for-firmware-1.md"
doc_source: "https://interrupt.memfault.com/blog/gdb-for-firmware-1#debugging-the-program"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that we have the application running properly, let's go ahead and set up the debugger.

### 1. Remote GDB Setup
There are a few steps to get this working.

- **JLinkGDBServer**

	As part of the SEGGER J-Link Software we installed, the program JLinkGDBServer is included. This is the GDB Server application that will interface directly with the development kit and the nRF52840 chipset. It will open up a port (we chose port 2331) over the network to allow connections from a GDB Client.

	To start the J-Link GDB Server, run the following command:

	```terminal
	$ JLinkGDBServerCL -device nrf52840_xxaa -if swd -port 2331
	```

	- "**-device**" specifies the device type ("nrf52840_xxaa" in our case).
	- "**-if**" specifies the debug interface ("swd" refers to Serial Wire Debug which is an alternative to JTAG that is relatively recent and is used for ARM processors. Keep in mind that some chipsets may not support SWD and will require JTAG instead.)
	- "**-port**" specifies the network port where the GDB Server will be accessible by the GDB Client.

	The output should look something like this:

	


- **Running GDB**

	Now that the GDB Server is running, we have to connect to it from a GDB Client. In our case, the client is the `arm-none-eabi-gdb` program included as part of the GNU Arm Embedded Toolchain we downloaded earlier.

	To make things easier, run the following command from the output folder where the binary images for the compiled example are located (`<nRF5_SDK_Folder>/examples/peripheral/uart/pca10056/blank/armgcc/_build/`).

	```terminal
	$ arm-none-eabi-gdb
	```


	


	Next, we want to tell GDB what output file is used for the program running on the development kit. We do so with the following command within the GDB console:

	```bash
	(gdb) file nrf52840_xxaa.out
	```


	


- **Connecting GDB to the Remote Target**

	The last step is to connect to the GDB server:

	```bash
	(gdb) target remote localhost:2331
	```


	


	The GDB Server (which should be left running in another Terminal window) will show something like the following:


	


### 2. GDB Commands
Now that we've been able to connect the debugger to the nRF52 chipset on the development kit, it's time to start having some fun!

**Hint:** In the GDB console, pressing "Enter/Return" on a blank line will repeat the last command called.

Here are some of the most useful GDB commands that you can use for debugging your application:

#### Help
The first command you should be aware of is the **help** command. You can use **help** followed by any other command to learn everything you need to know about the usage of that command. Or you could simply type **help** in the GDB console to see what options are available.

For example, let's run **help** for the "breakpoint" command:



#### Breakpoint
The Breakpoint command is used to set a breakpoint at a location telling the debugger to halt the application when the program reaches that line of code. You can use the shortcut **b** instead of spelling out the full name, too.




#### Continue
The **Continue** command is used to continue execution after a breakpoint was hit. You can simply use the shortcut **c** instead of spelling out the full word.





#### Breakpoints with Condition
Breakpoints are very useful, but sometimes you don't want the application to stop running unless a certain condition has occurred.

This is where the **Breakpoint with condition** command comes in.

In our example program, the code in **main.c** at **line 175** checks the character sent from the UART to see if it matches the `q` or `Q` character:





We can set a breakpoint that only stops the program if we receive a specific character (other than `q` or `Q`), for example: `s`.

```bash
(gdb) b main.c:175 if cr == 's'
```

Now, if we set this breakpoint, we can run the program as normal and then type the character `s` in the CoolTerm program to send this character to the nRF52 chipset.

We'll see that the application halts only if that character is sent across the UART.




#### Backtrace
The Backtrace command is used to show the call stack of the program at the current Program Counter (PC). In simple terms, it shows you a summary of how your program got to where it's currently at.

Here's what the output of **backtrace** looks like when adding the "full" option to show all the local variables as well:



If you want to make it look "pretty" with some basic formatting, you could use the following command:

```bash
(gdb) set print pretty on
```

Here's a screenshot showing the difference between the output with "pretty" being **on** or **off**:



#### Step
The **Step** command is used to *step* through and execute your source code during debugging. It **will** step into any function in its path, however it **will not** step into functions that do not contain debugging information.

For reference, here's our code again from main.c:





Let's take a look at how the Step command behaves after hitting the breakpoint at main.c:175 that we had set.





Notice that GDB stepped into the function **app_uart_get()** after reaching line 172.

#### List
The **List** command shows the source code for the current Program Counter (PC). The default is to show the source code surrounding the location of the PC (with a few code lines before and after).

Here's an example of using **List** after we hit our breakpoint at **main.c:175**.





#### Info
The **Info** command has many uses, but as the name implies, it is used to display more information for a specific element.

Here are some examples for uses of **Info**.

- **Info locals**: shows information about all local variables.

	

- **Info variables**: shows information about all types of variables (local and global).

	

- **Info files**: shows information about all files being debugged.

	

#### Logging
One useful feature within GDB is the ability to log all output to a text file. This makes it much easier to share the output of GDB with others, or to simply save the output for later reference.

It's done as follows:

- `(gdb) set logging on` to start logging
- `(gdb) set logging off` to stop logging
- The default output log filename is `gdb.txt` and it is saved to the same folder where the execution of GDB was initiated from.

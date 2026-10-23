---
id: "zep-debugging-debug-with-eclipse"
type: "concept"
domain: "debug"
title: "Debugging: Debug with Eclipse"
summary: "CMake supports generating a project description file that can be imported into the Eclipse Integrated Development Environment (IDE) and used for graphical debugging."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/debug/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/debug/index.rst"
license: "Apache-2.0"
mode: "V"
---

### Overview


CMake supports generating a project description file that can be imported into
the Eclipse Integrated Development Environment (IDE) and used for graphical
debugging.

The GNU MCU Eclipse plug-ins provide a mechanism to debug ARM projects in
Eclipse with pyOCD, Segger J-Link, and OpenOCD debugging tools.

The following tutorial demonstrates how to debug a Zephyr application in
Eclipse with pyOCD in Windows. It assumes you have already installed the GCC
ARM Embedded toolchain and pyOCD.


### Set Up the Eclipse Development Environment


#. Download and install Eclipse IDE for C/C++ Developers.

#. In Eclipse, install the GNU MCU Eclipse plug-ins by opening the menu
   `Window->Eclipse Marketplace...`, searching for `GNU MCU Eclipse`, and
   clicking `Install` on the matching result.

#. Configure the path to the pyOCD GDB server by opening the menu
   `Window->Preferences`, navigating to `MCU`, and setting the ``Global
   pyOCD Path``.


### Generate and Import an Eclipse Project


#. Set up a GNU Arm Embedded toolchain as described in
   toolchain_gnuarmemb.

#. Navigate to a folder outside of the Zephyr tree to build your application.

```console

# On Windows
cd %userprofile%
```

**Note:** If the build directory is a subdirectory of the source directory, as is usually done in Zephyr, CMake will warn: "The build directory is a subdirectory of the source directory. This is not supported well by Eclipse.  It is strongly recommended to use a build directory which is a sibling of the source directory."

#. Configure your application with CMake and build it with ninja. Note the
   different CMake generator specified by the `-G"Eclipse CDT4 - Ninja"`
   argument. This will generate an Eclipse project description file,
   `.project`, in addition to the usual ninja build files.

#. In Eclipse, import your generated project by opening the menu
   `File->Import...` and selecting the option ``Existing Projects into
   Workspace``. Browse to your application build directory in the choice,
   `Select root directory:`. Check the box for your project in the list of
   projects found and click the `Finish` button.


### Create a Debugger Configuration


#. Open the menu `Run->Debug Configurations...`.

#. Select `GDB PyOCD Debugging`, click the `New` button, and configure the
   following options:

   - In the Main tab:

     - Project: `my_zephyr_app@build`
     - C/C++ Application: `zephyr/zephyr.elf`

   - In the Debugger tab:

     - pyOCD Setup

       - Executable path: `${pyocd_path}\\${pyocd_executable}`
       - Uncheck "Allocate console for semihosting"

     - Board Setup

       - Bus speed: 8000000 Hz
       - Uncheck "Enable semihosting"

     - GDB Client Setup

       - Executable path example (use your `GNUARMEMB_TOOLCHAIN_PATH`):
         `C:\\gcc-arm-none-eabi-6_2017-q2-update\\bin\\arm-none-eabi-gdb.exe`

   - In the SVD Path tab:

     - File path: :file:`<workspace
       top>\\modules\\hal\\nxp\\mcux\\devices\\MK64F12\\MK64F12.xml`


**Note:** This is optional. It provides the SoC's memory-mapped register addresses and bitfields to the debugger.

#. Click the `Debug` button to start debugging.


### RTOS Awareness


Support for Zephyr RTOS awareness is implemented in pyOCD v0.11.0 and later.
It is compatible with GDB PyOCD Debugging in Eclipse, but you must enable
CONFIG_DEBUG_THREAD_INFO=y in your application.

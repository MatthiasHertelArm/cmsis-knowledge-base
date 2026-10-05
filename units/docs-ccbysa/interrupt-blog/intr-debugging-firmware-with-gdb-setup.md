---
id: "intr-debugging-firmware-with-gdb-setup"
type: "concept"
domain: "debug"
title: "Debugging Firmware with GDB: Setup"
summary: "In order to use GDB with any embedded system, we need to set up:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-05-21-gdb-for-firmware-1.md"
doc_source: "https://interrupt.memfault.com/blog/gdb-for-firmware-1#setup"
license: "CC-BY-SA-4.0"
mode: "V"
---

In order to use GDB with any embedded system, we need to set up:

- A GDB Server instance which interfaces directly with the target
- A GDB instance (Client) that connects to the GDB Server
### Software Installation Steps
Let's go through the different steps for downloading the necessary software packages.

For each of these downloads, you can place them anywhere on your machine. I recommend having them all in a single folder, to make it easier to locate later on.
### 1. nRF5 SDK
Installation of the nRF5 SDK is straightforward. All you need to do is download the SDK tarball from Nordic's website and then extract it.

**[Link to download nRF5 SDK](https://www.nordicsemi.com/Software-and-Tools/Software/nRF5-SDK/Download#infotabs)**

Once you extract it, you should see the following directory structure:





### 2. nRF5 Command Line Tools
Next, we need to install the nRF5 Command Line Tools. These include **nrfjprog**, which is a tool for programming your nRF52 development kit via the Segger J-Link debugger and needed in our case for working from the command line.

**[Link to download the nRF5 Command Line Tools](https://www.nordicsemi.com/Software-and-Tools/Development-Tools/nRF5-Command-Line-Tools/Download#infotabs)**

First, make sure you select the appropriate operating system (macOS in our case).






Select the latest version, and then click "Download File".

This is what the contents of the folder should look like:



### 3. SEGGER J-Link
The SEGGER J-Link software is needed for the GDB Server interface to the nRF52 chipset on the development kit.

So let's go ahead and download the software.

[**Link to download SEGGER J-Link Software**](https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack)






This download (for macOS) is a .**pkg** installer file. Once you download it, simply double-click it and go through the installation process.





### 4. GNU Arm Embedded Toolchain
The next software package that we need to install is the GNU Arm Embedded Toolchain which includes the compiler (gcc) and debugger (gdb) for the Arm architecture (which the nRF52840 chipset is based on).

**[Direct link to download the GNU Arm Embedded Toolchain (version 7-2017-q4-major)](https://developer.arm.com/-/media/Files/downloads/gnu-rm/7-2017q4/gcc-arm-none-eabi-7-2017-q4-major-mac.tar.bz2?revision=7f453378-b2c3-4c0d-8eab-e7d5db8ea32e?product=GNU%20Arm%20Embedded%20Toolchain,64-bit,,Mac%20OS%20X,7-2017-q4-major)**






After you download the package, simply extract it to your folder of choice.





### 5. Serial Terminal Program
My choice for a terminal program that I use across projects is a program called **CoolTerm**. What I like about this program is its simplicity and that it supports all the major platforms (Windows, macOS, and Linux).

**[Link to download CoolTerm](https://freeware.the-meiers.org/CoolTermMac.zip)**

For now, all you need to do is download it, open the package and copy the application file to your Mac **Applications** folder so you could launch it in the later steps.

### 6. Adding Necessary Folders to $PATH
In order to access the necessary commands that we'll be calling from anywhere in your system, you need to add their paths to the system **$PATH** environment variable.

To do that, open up a Terminal session and type the following:

```terminal
$ vi ~/.bash_profile
```

Once you've done that, go ahead and add the following lines to the bottom of the file:

```
export PATH = "<Your Folder>/nRF-Command-Line-Tools_9_8_1_OSX/nrfjprog":$PATH
export PATH = "<Your Folder>/gcc-arm-none-eabi-7-2017-q4-major/bin":$PATH
```

Make sure to replace `<Your Folder>` with the appropriate folder name where you placed those packages on your system.

We don't need to add any paths for the SEGGER J-Link software because it ran as an installer and would have already added the necessary binaries to our system.

After you're done editing and saving the `paths` file, close the Terminal and then start a new session to make sure the updated `paths` file gets loaded. Alternatively, you could just execute the following command to reload `.bash_profile`:

```terminal
$ source ~/.bash_profile
```

To verify, you can type the following command:

```terminal
$ echo $PATH
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/mafaneh/Memfault/nRF-Command-Line-Tools_9_8_1_OSX/nrfjprog:/Users/mafaneh/Memfault/gcc-arm-none-eabi-7-2017-q4-major/bin
```

That's it for the setup part, now on to the fun part!

---
id: "intr-securing-firmware-updates-with-aes-example-architecture-code"
type: "concept"
domain: "debug"
title: "Securing Firmware Updates With AES Encryption: Example architecture code"
summary: "It’s time to see everything in action in the example code we have a fairly simple architecture with a boot loader boot.c and an application app.c."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-08-23-firmware-encryption-with-python.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-encryption-with-python#example-architecture-code"
license: "CC-BY-SA-4.0"
mode: "V"
---

It’s time to see everything in action in the example code we have a fairly simple architecture with a boot loader `boot.c` and an application `app.c`.

The bootloader checks if something exists in slot 1 where the encrypted firmware application was installed. If the firmware image exists in Flash, it will proceed to decrypt and install it in slot 2 when finished, it will start the application.



### Toolchain

The full example is available on GitHub at
[interrupt@fwup-encryption](https://github.com/memfault/interrupt/tree/master/example/fwup-encryption).

The following tools to compile and flash the firmware:

* B-L4S5I-IOT01A[^BL4S5I]
* GNU Make 3.81 as the build system
* arm-none-eabi-gcc version 10.3.1 20210824 (release) as compiler
* python 3.9.11
* SEGGER J-Link

### Building & Running the Example

The project will build an application binary `app.bin` where you simply change the state of a GPIO. It will also build a binary file for `boot.bin` which performs firmware decryption and read and write flash memory.

Let’s start by building the project with make:

```shell
$ make
Compiling app.c
Compiling system_app.c
Compiling startup_app.s
Linking library app
Memory region         Used Size  Region Size  %age Used
             RAM:        2640 B       640 KB      0.40%
             ROM:        2176 B         4 KB     53.13%
Generated build/app.elf
Compiling boot.c
Compiling system_boot.c
Compiling Decrypting-EngineAES/aes_ctr.c
Compiling Decrypting-EngineAES/flash.c
Linking library boot
Memory region         Used Size  Region Size  %age Used
             RAM:        2672 B       640 KB      0.41%
             ROM:        2988 B         4 KB     72.95%
Generated build/boot.elf
$
```

In the `Encrypting-PythonAES` directory there is the Python Script to encrypt the firmware, after compiling in the build directory we have the application firmware called `app.bin`, we will start the python script from make so that the encryption of our image is performed:

```shell
$ make encryption
__main__
Bytes to encrypt :{} 2176
[32, 10, 0, 0]
[140, 151, 243, 6]
2172
[8, 0, 35, 217]
[133, 193, 180, 190]
2168
[8, 0, 36, 41]
[200, 82, 215, 95]
2164
[8, 0, 36, 41]
[157, 88, 242, 118]
2160
[8, 0, 36, 41]
[170, 87, 210, 231]
2156
......
16
[0, 0, 0, 0]
[64, 175, 241, 151]
12
[0, 0, 0, 0]
[166, 169, 216, 42]
8
[0, 0, 0, 0]
[178, 91, 28, 154]
4
[32, 0, 4, 72]
[108, 239, 9, 13]
0
$
```

In the build directory, a binary file called `Cipherapp.bin` was generated, which corresponds to our encrypted firmware.
We programmed the `boot.bin` and the `Cipherapp.bin` firmware onto our board using J-Link and initiated the tools through make:

```shell
$ make flash
JLink.exe -device STM32L4S5VI -speed 4000 -si swd -autoconnect 1
SEGGER J-Link Commander V7.80b (Compiled Sep 20 2022 17:11:36)
DLL version V7.80b, compiled Sep 20 2022 17:10:13
Connecting to J-Link via USB...O.K.
Firmware: J-Link STLink V21 compiled Aug 12 2019 10:29:20
Hardware version: V1.00
J-Link uptime (since boot): N/A (Not supported by this model)
S/N: 775917048
VTref=3.300V
Device "STM32L4S5VI" selected.
Connecting to target via SWD
Found SW-DP with ID 0x4BA01477
Found SW-DP with ID 0x4BA01477
DPv0 detected
CoreSight SoC-400 or earlier
Scanning AP map to find all available APs
AP[1]: Stopped AP scan as end of AP map has been reached
AP[0]: AHB-AP (IDR: 0x24770011)
Iterating through AP map to find AHB-AP to use
AP[0]: Core found
AP[0]: AHB-AP ROM base: 0xE00FF000
CPUID register: 0x410FC241. Implementer code: 0x41 (ARM)
Found Cortex-M4 r0p1, Little endian.
FPUnit: 6 code (BP) slots and 2 literal slots
CoreSight components:
ROMTbl[0] @ E00FF000
[0][0]: E000E000 CID B105E00D PID 000BB00C SCS-M7
[0][1]: E0001000 CID B105E00D PID 003BB002 DWT
[0][2]: E0002000 CID B105E00D PID 002BB003 FPB
[0][3]: E0000000 CID B105E00D PID 003BB001 ITM
[0][4]: E0040000 CID B105900D PID 000BB9A1 TPIU
[0][5]: E0041000 CID B105900D PID 000BB925 ETM
Cortex-M4 identified.

J-Link>
```

Now that the J-Link server is running we can flash the firmware:

```shell
J-Link>loadFile C:\fwup-encryption\build\Cipherapp.bin,0x08001000
'loadfile': Performing implicit reset & halt of MCU.
Reset: Halt core after reset via DEMCR.VC_CORERESET.
Reset: Reset device via AIRCR.SYSRESETREQ.
Downloading file [C:\fwup-encryption\build\Cipherapp.bin]...
J-Link: Flash download: Bank 0 @ 0x08000000: Skipped. Contents already match
O.K.

J-Link>
```

We programmed the `boot.bin` and changed the boot address accordingly:

```shell
J-Link>loadFile C:\fwup-encryption\build\boot.bin,0x08000000
'loadfile': Performing implicit reset & halt of MCU.
Reset: Halt core after reset via DEMCR.VC_CORERESET.
Reset: Reset device via AIRCR.SYSRESETREQ.
Downloading file [C:\fwup-encryption\build\boot.bin]...
J-Link: Flash download: Bank 0 @ 0x08000000: Skipped. Contents already match
O.K.

J-Link>
```

Let’s take a look at some of the tasks that the boot performs to decrypt the firmware image:

```c
#define SLOT_ADDRESS_CIPHER_APP  0x08001000
#define SLOT_ADDRESS_PLAIN_APP   0x08002000
#define FLASH_CLEAN_SECTOR_VALUE 0xFFFFFFFF
#define NUMBER_BYTES_TO_PROCESS  16
#define FIRMWARE_PLAIN_APP_SIZE  2176

int main(void) {
    aes_setup();
    if(image_validate()) {
        image_decrypt();
    }
    image_start();
    return 0;
}
```

First, it validates if the encrypted firmware image exists in the CIPHER_APP slot and if the PLAIN_APP slot reserved for the decrypted application is empty. If these conditions are met, it begins the installation of the firmware image:

```c
int image_validate(void) {
    uint32_t slot_app;
    uint32_t slot_chipherApp;
    slot_app = *(uint32_t*)(SLOT_ADDRESS_PLAIN_APP);
    slot_chipherApp = *(uint32_t*)(SLOT_ADDRESS_CIPHER_APP);
    if( slot_app == FLASH_CLEAN_SECTOR_VALUE &&  slot_chipherApp != FLASH_CLEAN_SECTOR_VALUE ) {
        //! Decrypt the app and start the installation
        return 1;
    }

    return 0;
}
```

The decryption process is performed in blocks of 16 bytes. First, a read operation is performed on the flash memory where the encrypted image was programmed, forming an array as a 16-byte block to initiate the decryption process. The decrypted data is then stored in the application slot for further programming:

```c
void image_decrypt(void) {
    uint32_t slot_Cipher_appAddr = SLOT_ADDRESS_CIPHER_APP;
    uint32_t slot_Plain_appAddr = SLOT_ADDRESS_PLAIN_APP;
    int8_t idx = 3;
    uint32_t word;
    int32_t bytes_remaining = FIRMWARE_PLAIN_APP_SIZE;

    word = *(uint32_t*)(slot_Cipher_appAddr);

    flash_unlock();
    //! Erase flash sector slot app
    flash_erase(2, 2);
    while(bytes_remaining) {
        //! Read 16 bytes of encrypted data
        for(size_t i=0; i<NUMBER_BYTES_TO_PROCESS; i++) {
            if(idx < 0) {
                idx = 3;
                slot_Cipher_appAddr += 4;
                word = *(uint32_t*)(slot_Cipher_appAddr);
            }
            CipherFirmware[i] = (word >> (8*idx--)) & 0xff;
        }
        //! Decrypt the 16 bytes of data firmware
        aes_decryption( CipherFirmware, NUMBER_BYTES_TO_PROCESS, PlainFirmware );
        //! Write 16 bytes of data to flash memory
        image_install( PlainFirmware, &slot_Plain_appAddr);
        bytes_remaining -= 16;
        idx = 3;
        slot_Cipher_appAddr += 4;
        word = *(uint32_t*)(slot_Cipher_appAddr);
        if(bytes_remaining <= 0 ) bytes_remaining = 0;
    }
    flash_lock();
}
```

Finally, upon completing the decryption and installation of the firmware image, the boot will launch the application on every restart. This ensures that the decrypted firmware is executed and the device operates using the updated firmware:

```c
void image_start(void) {
    uint32_t jump_address;
    typedef void(*start_app)(void);
    start_app p_jump_app;
    jump_address = *(volatile uint32_t *)(((uint32_t)SLOT_ADDRESS_PLAIN_APP + 4));
    p_jump_app   = (start_app)jump_address;
    //! Initialize the loader's Stack Pointer
    __set_MSP(*(__IO uint32_t *)(SLOT_ADDRESS_PLAIN_APP));
    //! Jump into app
    p_jump_app();
}
```

### Key Storage

The security of a device's firmware encryption process depends on the security of the key storage mechanism. In the case presented in this post, the decryption keys are stored within the bootloader firmware, which poses a potential security risk. To ensure maximum security in a production environment, it's advisable to include a secure element in the hardware design.
A secure element is an isolated execution environment that offers hardware-based security for sensitive code and data.

Hence we need to store and protect the key on the device. Below are some protection mechanisms:

* Encrypt the key using an SoC mechanism
* Store the key in an external crypto or security chip as ATECC608B[^ATECC608B] which provides secure storage
* Use an external Trusted Platform Module (TPM) chip
* Enable flash memory read protection mechanisms on the MCU

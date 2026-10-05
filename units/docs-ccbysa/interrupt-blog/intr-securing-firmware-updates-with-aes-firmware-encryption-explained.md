---
id: "intr-securing-firmware-updates-with-aes-firmware-encryption-explained"
type: "concept"
domain: "debug"
title: "Securing Firmware Updates With AES Encryption: Firmware Encryption Explained"
summary: "Encryption is a process of encoding information, specifically applied to firmware, which involves converting the original firmware image plaintext into an alternative form ciphertext."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-08-23-firmware-encryption-with-python.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-encryption-with-python#firmware-encryption-explained"
license: "CC-BY-SA-4.0"
mode: "V"
---

Encryption is a process of encoding information, specifically applied to firmware, which involves converting the original firmware image **plaintext** into an alternative form **ciphertext**. Authorized parties who possess the encryption key can decrypt the ciphertext back into plaintext and access the original information.

When performing firmware updates with security in mind, it is important to consider the authenticity and confidentiality of our firmware. Encrypting the firmware is a way to enhance the confidentiality of our update system. Let’s see when it is advisable to implement firmware encryption.

### Why encrypt our firmware

When performing updates via OTA, it is crucial to consider that our firmware is exposed to various methods of firmware extraction, such as:

* Sniffing the OTA: An attacker can intercept the binary firmware while the device is undergoing an update.
* Reading the firmware from UART, JTAG, or the device’s flash chip: Attackers may attempt to extract the firmware by accessing these interfaces.
* Intercepting the firmware during the download process: If the firmware is downloaded for device update over unencrypted HTTP traffic, an attacker could intercept it.

Considering these scenarios, it becomes necessary to add security mechanisms to our update system, such as signing or encrypting the firmware image. These measures help ensure the integrity and confidentiality of the firmware during the update process, mitigating the risk of unauthorized access or tampering.

### When to use firmware encryption

Indeed, protecting firmware is important, but it’s essential to analyze certain factors before considering firmware encryption. Firmware encryption may not be necessary for all systems. The primary purpose of employing firmware encryption is to add confidentiality while transporting the firmware to the device or while it resides in an external flash memory.

Firmware encryption is necessary when:

1. The messages sent from the server to the device are not encrypted.
2. The bootloader has secure storage to protect the encryption key.
3. The bootloader installs the new firmware in an external flash memory.
4. The bootloader extracts the firmware from the external flash memory to install it in the internal application flash memory.



Points to consider when firmware encryption is necessary:

| Points | Explanation                                                                                      | Firmware Encryption |
| ------ | ------------------------------------------------------------------------------------------------ | ------------------- |
| 1 3    | The firmware image is exposed from the server to the device and from external flash              | ✅                  |
| 3 4    | The firmware image can be extracted from external flash                                          | ✅                  |
| 2 3    | The firmware can be extracted from external flash we can store decryption keys in secure storage | ✅                  |
| 2 4    | The firmware can be extracted from external flash we can store decryption keys in secure storage | ✅                  |

Firmware encryption is not necessary when:

1. The communication link between the server and the device is already encrypted, for example, using TLS (Transport Layer Security). You can authenticate client and device connections with X.509 certificates.
2. The bootloader performs authenticity and integrity validation on the firmware image using code signing, CRC validation, and a metadata header.
3. The Loader can be used to update and install new firmware images or update the bootloader in case changes to the validation process in firmware images are required.
4. The firmware image boots only if it is validated for authenticity and integrity when installed and at each boot.



Points to consider when firmware encryption is not necessary:

| Points | Explanation                                                                                      | Firmware Encryption |
| ------ | ------------------------------------------------------------------------------------------------ | ------------------- |
| 1 2    | From the server to the device the data is encrypted thanks to the protocol used                  | ❌                  |
| 2 3    | Validation mechanisms can detect changes in firmware integrity                                   | ❌                  |
| 2 4    | Integrity validation mechanisms can detect firmware changes and reject that firmware image       | ❌                  |
| 1 3    | Encrypted data from server to device and also having a code signature is a good combination      | ❌                  |

In this case, if the communication link is already secured, and the bootloader and Loader ensure the integrity of the firmware through code signing, the need for additional firmware encryption may be reduced. However, it’s essential to thoroughly assess the security requirements of your specific system and consider factors such as the sensitivity of the firmware and potential attack vectors to make an informed decision regarding firmware encryption.

Certainly, if you have the option to use a recommended bootloader like MCUBoot[^mcuboot_1] that supports firmware image encryption, it is highly advisable to utilize it. However, if you need to implement a custom bootloader, this publication aims to serve as a starting point for implementing firmware image encryption.

### AES

AES (Advanced Encryption Standard) is a symmetric key cryptographic algorithm, meaning the same key is used for both encryption and decryption of the message. The algorithm offers various modes such as CBC (Cipher Block Chaining), ECB (Electronic Codebook), CTR (Counter), and CCM (Counter with CBC-MAC), each with different characteristics. In this publication, we will focus on the CTR mode for several reasons:

1. Security: CTR mode is considered one of the most secure AES modes[^ctr_mode].
2. Popularity: It is widely used because it allows encrypting/decrypting any block without the need to know any other block. This mode is employed in MCUBoot[^mcuboot_2].
3. Availability: Most AES encryption engines within MCUs can work with this mode.
4. Small footprint: CTR mode does not impose a heavy resource burden on MCUs or cryptographic libraries[^footprint].

While the mathematics behind the AES-CTR algorithm are beyond the scope of this publication, let’s discuss the key points to understand the encryption process.

### CTR Mode

CTR mode, also known as Counter mode, is a stream cipher mode of AES encryption. With stream cipher encryption, it is not necessary to encrypt the **plaintext** in fixed blocks like AES in CBC mode, which encrypts data in 16-byte blocks. If the plaintext to be encrypted is smaller than the block size, padding is required to process a complete 16-byte block.

In contrast, CTR mode performs the encryption of plaintext on a per-byte basis using the corresponding digit of the key stream. Let’s take a moment to define what the key stream is essentially a stream of characters used to obtain the **ciphertext**. In each iteration, a new key stream is generated by encrypting successive values like a counter.

In CTR mode, the encryption process involves:

1. Generating the key stream by encrypting successive counter values.
2. XORing each byte of the plaintext with the corresponding byte of the key stream.
3. Obtaining the ciphertext by repeating this process for each byte of the plaintext.

Since CTR mode operates on a per-byte basis, it offers more flexibility and efficiency when encrypting data of varying sizes, as there is no need for padding. Additionally, it allows for parallelization and random access to encrypted data, making it a popular choice for many applications, including firmware encryption:



Now we know that we need a key stream to begin encrypting the first data, and then a new key stream will be generated in the form of a counter for each subsequent encryption operation until all the plaintext is encrypted.

We can see that we need a couple of inputs:

* (AES_KEYRx (KEY)): For encryption and decryption, we will refer to the value as the `Key` value.
* (AES_IVRx): In CTR mode, the initialization vector is also referred to as the counter, which we will identify as the `Nonce`.

Before moving on to implementation, let’s review some important points:

1. CTR mode requires a `Key` and an initialization vector `Nonce`.
2. We can encrypt plaintext data (AES_DINR (plaintext P1)) in blocks of various sizes, for example, 4 bytes at a time.
3. Each time we encrypt a plaintext block, the counter block increases by one unit.
4. The counter block `Nonce` is the concatenation of a fixed Nonce block, set during initialization, and a 32-bit counter variable.

By understanding these key points, we can proceed with the implementation of CTR mode encryption.

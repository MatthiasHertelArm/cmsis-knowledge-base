---
id: "intr-securing-firmware-updates-with-aes-firmware-decryption-implementation"
type: "concept"
domain: "debug"
title: "Securing Firmware Updates With AES Encryption: Firmware Decryption Implementation"
summary: "We have successfully received the encrypted firmware through our update system. Now, the responsibility lies with our MCU to decrypt the firmware and install it in a flash memory section where the bootloader can execute it."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-08-23-firmware-encryption-with-python.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-encryption-with-python#firmware-decryption-implementation"
license: "CC-BY-SA-4.0"
mode: "V"
---

We have successfully received the encrypted firmware through our update system. Now, the responsibility lies with our MCU to decrypt the firmware and install it in a flash memory section where the bootloader can execute it. In this particular post, we will be utilizing the AES hardware accelerator present in ST Micro's STM32L4S5 MCU to carry out the firmware decryption process. All code mentioned in this post is specifically written for the development kit B-L4S5I-IOT01A[^BL4S5I].

### Define encryption keys

Remember that AES is a symmetric key algorithm so it is no longer necessary to generate new keys to decrypt, we have to use the same keys used to encrypt. Let’s define the initialization vector and the key:

```c
static const uint8_t pKeyAES[16] __attribute__ ((aligned (4))) = {
                            0x58,0x3b,0xf4,0x90,0x1f,0x62,0x35,0x10,0xa1,0x40,
                            0x8e,0x8b,0xe7,0xbd,0x6f,0x5a};
static const uint8_t NonceAES[16] __attribute__ ((aligned (4))) = {
                            0xf8,0x24,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
                            0x00,0x00,0x00,0x00,0x00};
```

### Decryption with AES hardware accelerator

The AES hardware accelerator encrypts and decrypts data and supports CTR mode, for 128-bit or 256-bit key sizes. It is necessary to configure the peripheral according to how we encrypt the firmware to be sure of obtaining the same result when decrypting.

So we need to make a configuration with these points:

1. Decryption with chaining mode Counter (CTR) mode.
2. Key sizes of 128 bits.

Let’s see how the hardware accelerator processes a message when it works in CTR mode presenting a structure similar to the one we defined when encrypting:



The structure of this message is:

1. A 16-byte initial counter block (ICB), composed of two distinct fields:

* Initialization vector (IV): a 96-bit value that must be unique for each encryption
cycle with a given key.
* Counter: a 32-bit big-endian integer that is incremented each time a block
processing is completed. The initial value of the counter must be set to 1.

2. The plaintext P is encrypted as ciphertext C, with a known length. This length can be
non-multiple of 16 bytes, in which case a plaintext padding is required.

### Setup AES hardware accelerator

After obtaining the required parameters, we can proceed to load the configuration into the `CR` register. Additionally, we need to initialize the `key` and initialization vector in their respective `Nonce` registers. The reference manual[^STM32L4S5] provides information about the configuration parameters, which can be accessed in section 34.7.1 of the AES control register (AES_CR).

```c
void aes_setup( void ) {
    uint32_t keyaddr;
    uint32_t Nonce;
    //! Enable source clock for  AES peripheral
    RCC->AHB2ENR |= RCC_AHB2ENR_AESEN;
    //! Disable the AES peripheral
    AES->CR &= ~AES_CR_EN;
    //! Select the mode CTR
    AES->CR |= AES_CR_CHMOD_1;
    //! Select the mode of decryption
    AES->CR |= AES_CR_MODE_1;
    //! Select the Data type 8-bit
    AES->CR |= AES_CR_DATATYPE_1;

    //! Set the key, for default key size it's 128 bits
    keyaddr = (uint32_t)(pKeyAES);
    AES->KEYR3 = __REV(*(uint32_t*)(keyaddr));
    keyaddr += 4;
    AES->KEYR2 = __REV(*(uint32_t*)(keyaddr));
    keyaddr += 4;
    AES->KEYR1 = __REV(*(uint32_t*)(keyaddr));
    keyaddr += 4;
    AES->KEYR0  = __REV(*(uint32_t*)(keyaddr));
    //! Set the Nonce InitVector/InitCounter
    Nonce = (uint32_t)(NonceAES);
    AES->IVR3 = __REV(*(uint32_t*)(Nonce));
    Nonce += 4;
    AES->IVR2 = __REV(*(uint32_t*)(Nonce));
    Nonce += 4;
    AES->IVR1 = __REV(*(uint32_t*)(Nonce));
    Nonce += 4;
    AES->IVR0 = __REV(*(uint32_t*)(Nonce));
    //! Enable the AES peripheral
    AES->CR |=  AES_CR_EN;
}
```

### Decrypt data

Once the configuration is set up properly, we can start decrypting blocks of 16 bytes of data. To achieve this, we input the data into the `DINR` register and obtain the plain text by reading the `DOUTR` register. For more information, please refer to section 34.7.3 (AES data input register - AES_DINR) and section 34.7.4 (AES data output register - AES_DOUTR) of the reference manual[^STM32L4S5].

```c
void aes_decryption( uint8_t *Input_CipherFirmware, uint16_t buf_size, uint8_t *Out_PlainFirmware ) {
    uint32_t inputaddr  = (uint32_t)Input_CipherFirmware;
    uint32_t outputaddr = (uint32_t)Out_PlainFirmware;
    for( uint32_t idx = 0; idx < buf_size; idx += 16 ){
        //! Write the ChipherText in the input register DINR
        AES->DINR = *(uint32_t*)(inputaddr);
        inputaddr += 4;
        AES->DINR = *(uint32_t*)(inputaddr);
        inputaddr += 4;
        AES->DINR = *(uint32_t*)(inputaddr);
        inputaddr += 4;
        AES->DINR = *(uint32_t*)(inputaddr);
        inputaddr += 4;
        //! Computation completed flag
        while( (AES->SR & AES_SR_CCF) == 0);
        //! Clear the completed flag
        AES->CR |= AES_CR_CCFC;
        //! Read the PainText from the output register DOUTR
        *(uint32_t*)(outputaddr) = AES->DOUTR;
        outputaddr+=4U;
        *(uint32_t*)(outputaddr) = AES->DOUTR;
        outputaddr+=4U;
        *(uint32_t*)(outputaddr) = AES->DOUTR;
        outputaddr+=4U;
        *(uint32_t*)(outputaddr) = AES->DOUTR;
        outputaddr+=4U;
    }
}
```

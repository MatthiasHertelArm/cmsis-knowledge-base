---
id: "intr-securing-firmware-updates-with-aes-firmware-encryption-implementation"
type: "concept"
domain: "debug"
title: "Securing Firmware Updates With AES Encryption: Firmware Encryption Implementation"
summary: "To begin with, the implementation, let’s use the PyCryptodome[^pycryptodome] cryptographic library to create a Python script that takes our firmware file and generates a new encrypted output file. First, let’s install the PyCryptodome library in Python."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-08-23-firmware-encryption-with-python.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-encryption-with-python#firmware-encryption-implementation"
license: "CC-BY-SA-4.0"
mode: "V"
---

To begin with, the implementation, let’s use the PyCryptodome[^pycryptodome] cryptographic library to create a Python script that takes our firmware file and generates a new encrypted output file. First, let’s install the PyCryptodome library in Python. You can install it by running the following command:

```
pip install pycryptodome
```

### Define encryption keys

To define the encryption keys, we will generate a key to use in the script using the PyCryptodome library. This same key will also be used for decryption in the MCU. For our configuration, we will use AES-128, which requires a 16-byte key. Additionally, we will use a 2-byte Nonce value as the initialization vector.

```python
from Crypto import Random
myKey = Random.get_random_bytes(16)
myIV  = Random.get_random_bytes(2)
print(myKey.hex())
print(myIV.hex())
```

Here are the generated keys:

```
583bf4901f623510a1408e8be7bd6f5a
f824
```

### Encrypting with PyCryptodome

Let’s use the generated keys to start encrypting data. The first step is to configure our counter block, which is a necessary parameter to create an object that allows us to encrypt using the `.encrypt()` method.

#### Counter Block

According to the PyCryptodome documentation[^pycryptodome], we can create a counter block by concatenating values before (prefix) and after (suffix) the counter variable:



Let’s use our `key` and `Nonce` value to create the counter block using the `Counter.new()` method. The method requires several parameters:

1. The desired counter length in bits.
2. The initial value of the counter.
3. The endianness of the counter data alignment.

> counter length: 112 bit / 8 = 14 bytes
> counter block length: 14 bytes + Nonce 2 bytes = 16 bytes = 128 bit

Since we want a counter length of 112 bits and our Nonce is 2 bytes, the counter block length should be 16 bytes (128 bits) to match the AES-128-bit encryption. We want the counter variable to start at 0, so we’ll set initial_value=0. We’ll also specify `little_endian=False` for big-endian data alignment to align with the counter in the AES processor on the MCU:

```python
import binascii
from Crypto.Cipher import AES
from Crypto.Util import Counter
myKey = "58:3b:f4:90:1f:62:35:10:a1:40:8e:8b:e7:bd:6f:5a"
myIV  = "f8:24"
AES_KEY = binascii.unhexlify(myKey.replace(":", ""))
AES_NONCE = binascii.unhexlify(myIV.replace(":", ""))
blockCounter = Counter.new(112, prefix=AES_NONCE, little_endian=False, initial_value=0)
print( blockCounter )
```

We see the parameters of the counter block:

```
{'counter_len': 14, 'prefix': b'\xf8$', 'suffix': b'', 'initial_value': 0, 'little_endian': False}
```

The result should look something like this:



The size of the `Nonce` (PREFIX) impacts the amount of space available for the counter variable. A larger `Nonce` value means less space is available for the counter. For instance, if a 4-byte Nonce is generated, the remaining 12 bytes will be used for the counter.

It’s important to consider the size of the counter variable because if a significant amount of data is encrypted and the counter variable size is not sufficiently large, it may overflow. The library will raise an `OverflowError` exception as soon as the counter wraps back to its original value.

To address this, one approach is to leave the `Nonce` value empty, allowing the counter variable to have more space. This allows us to encrypt a larger number of data blocks. Since the Nonce value and the counter block share the same space, it needs to be aligned to 16 bytes.

#### Encrypt script

To encrypt a firmware file using the defined `Key` and initialization vector `Nonce`, you can create a script that performs encryption on a firmware file in the .bin format. The manipulation of the firmware binary file can be done using a class that reads the file in blocks of 4 bytes:

```python
class BinaryFile:
    def __init__(self, nameFile, mode):
        self.openFileName = nameFile
        try:
            self.ObjectFile = open(self.openFileName , mode)
        except IOError:
            print("Cannot open binary file \n")
            print("Make sure it is in the same folder as the script\r\n")
            sys.exit(1)
    def CloseFile(self):
        self.ObjectFile.close()
    def ReadFile(self, numberBytes):
        return self.ObjectFile.read(numberBytes)
    def WriteFile(self, dataBytes):
        self.ObjectFile.write(bytes(dataBytes))
    def SizeFile(self):
        return os.path.getsize( self.openFileName )
```

To encrypt, a class is created where the counter is initialized and a SwapLittleEndian method is also added to perform an exchange in the data format since our MCU handles the data in Little Endian format, this is important because if this exchange is not carried out in the format we won’t get the same result when decrypting from MCU:

```python
class  EncryptionCTR:
    def __init__(self, key, iv ):
        self.key = binascii.unhexlify(key.replace(":", ""))
        self.iv  = binascii.unhexlify(iv.replace(":", ""))
        self.count_ctr = Counter.new(112, prefix=self.iv, little_endian=False, initial_value=0)
        self.cipherObject = AES.new(self.key, AES.MODE_CTR, counter=self.count_ctr)
    def EncryptCtr(self, plaintext):
        return self.cipherObject.encrypt(bytes(plaintext))
    def SwapLittleEndian(self,plaintext):
        temp_swap = [bytes]*BYTES_READ
        temp_swap[0] = plaintext[3]
        temp_swap[1] = plaintext[2]
        temp_swap[2] = plaintext[1]
        temp_swap[3] = plaintext[0]
        return temp_swap
```

The script needs the name of the app.bin firmware binary file to be encrypted and a name for a new file that corresponds to the encrypted firmware Cipherapp.bin. A 4-byte read of the original plaintext firmware file is performed, the format exchange is performed, we encrypt the block and finally, the ciphertext block is written to a new binary file:

```python
def main():
    print(__name__)

    PlainFirmware  = BinaryFile(sys.argv[1],'rb')
    CipherFirmware = BinaryFile(sys.argv[2],'wb')
    CryptoFirmware  = EncryptionCTR(mykey,myiv)
    bytes_remaining = 0
    bytes_so_far_cryted = 0
    BinaryFileSize = PlainFirmware.SizeFile()
    bytes_remaining = BinaryFileSize - bytes_so_far_cryted
    print("Bytes to encrypt :{}", bytes_remaining )
    while(bytes_remaining):
        Plainbytes = PlainFirmware.ReadFile(BYTES_READ)
        PlainbytesLittle = CryptoFirmware.SwapLittleEndian(Plainbytes)
        Cipherbytes = CryptoFirmware.EncryptCtr(PlainbytesLittle)
        CipherbytesLittle = CryptoFirmware.SwapLittleEndian(Cipherbytes)
        CipherFirmware.WriteFile(CipherbytesLittle)
        print( PlainbytesLittle )
        print( CipherbytesLittle )

        bytes_so_far_cryted += BYTES_READ
        bytes_remaining = BinaryFileSize - bytes_so_far_cryted
        if( bytes_remaining <= 0 ): bytes_remaining = 0
        print( bytes_remaining )

    PlainFirmware.CloseFile()
    CipherFirmware.CloseFile()
main()
```

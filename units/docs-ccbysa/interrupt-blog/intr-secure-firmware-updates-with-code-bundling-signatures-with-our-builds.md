---
id: "intr-secure-firmware-updates-with-code-bundling-signatures-with-our-builds"
type: "concept"
domain: "debug"
title: "Secure firmware updates with code signing: Firmware Signing Implementation / Bundling signatures with our builds"
summary: "Part of: Firmware Signing Implementation"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-09-08-secure-firmware-updates-with-code-signing.md"
doc_source: "https://interrupt.memfault.com/blog/secure-firmware-updates-with-code-signing#bundling-signatures-with-our-builds"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Firmware Signing Implementation_

Next we must add the signing step to our build and add the signatures to our
image. The latter is easy to do: we already have a metadata for our images saved
into the `image_hdr_t`. We simply add a field for the signature and increment
our metadata version:

```diff
 typedef enum {
     IMAGE_VERSION_1 = 1,
-    IMAGE_VERSION_CURRENT = IMAGE_VERSION_1,
+    IMAGE_VERSION_2 = 2,
+    IMAGE_VERSION_CURRENT = IMAGE_VERSION_2,
 } image_version_t;

 typedef struct __attribute__((packed)) {
@@ -34,10 +35,13 @@
     uint32_t vector_addr;
     uint32_t reserved;
     char git_sha[8];
+    uint8_t ecdsa_sig[64];
 } image_hdr_t;
```

The 64 bytes contain the two integers that make up our signature one after the
other.

We then modify `patch_image_header.py` so that it generates and appends the
signature to our binary. Rather than shell out to `openssl`, we use a native
Python library that implements ECDSA. Simply enough, it is called `ecdsa`.

Generating the signature can be accomplished with a few lines of code:

```python
import hashlib
from ecdsa import SigningKey
from ecdsa.util import sigencode_string
from binascii import hexlify


def gen_binary_signature(data, key_filename):
    with open(key_filename, "r") as f:
        key_pem = f.read()
    key = SigningKey.from_pem(key_pem)
    sig = key.sign_deterministic(data, hashfunc=hashlib.sha256, sigencode=sigencode_string)
    return sig
```

A few things to note:
1. We use SHA-256 as our hashing function, so we must specify it when we
   generate the signature
2. The `sigencode` parameter is used to specify the format of the signature. By
   default, a DER file a generated (this is what openssl uses as well), but by
using `sigencode_string` we tell the library to generate a flat string that
contains the binary representation of both signature integers one after another.
This is a simpler format and will save us from implementing a DER parser in
our firmware.

We then update our `patch_binary_payload` function to invoke
`gen_binary_signature`:

```diff
+def patch_binary_payload(bin_filename, pk_filename):
     """
     Patch crc & data_size fields of image_hdr_t in place in binary

     Raise exception if binary is not a supported type
     """
-    IMAGE_HDR_SIZE_BYTES = 32
+    IMAGE_HDR_SIZE_BYTES = 96
     IMAGE_HDR_MAGIC = 0xCAFE
-    IMAGE_HDR_VERSION = 1
+    IMAGE_HDR_VERSION = 2

     with open(bin_filename, "rb") as f:
         image_hdr = f.read(IMAGE_HDR_SIZE_BYTES)
@@ -35,6 +47,7 @@

     data_size = len(data)
     crc32 = binascii.crc32(data) & 0xffffffff
+    signature = gen_binary_signature(data, 'private.pem')

     image_hdr_crc_data_size = struct.pack("<LL", crc32, data_size)
     print(
@@ -42,11 +55,17 @@
             crc32, data_size, bin_filename
         )
     )
+
     with open(bin_filename, "r+b") as f:
         # Seek to beginning of "uint32_t crc"
         f.seek(4)
         # Write correct values into crc & data_size
         f.write(image_hdr_crc_data_size)
+        # Seek to beginning of signature
+        f.seek(32)
+        # Write the signature in place
+        f.write(signature)


 if __name__ == "__main__":
@@ -54,6 +73,7 @@
         description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
     )
     parser.add_argument("bin", action="store")
+    parser.add_argument("pk", action="store")
     args = parser.parse_args()

-    patch_binary_payload(args.bin)
+    patch_binary_payload(args.bin, args.pk)
```

Since the script now takes an argument, we must modify our Makefile as well

```diff
-$(BUILD_DIR)/$(PROJECT)-%.bin: $(BUILD_DIR)/$(PROJECT)-%.elf
+$(BUILD_DIR)/$(PROJECT)-%.bin: $(BUILD_DIR)/$(PROJECT)-%.elf $(PK_PEM_PATH)
        $(ECHO) "  OBJCOPY      $@"
-       $(Q)$(OCPY) $^ $@ -O binary
+       $(Q)$(OCPY) $< $@ -O binary
        $(ECHO) "  PATCH_IMAGE  $@"
-       $(Q)$(PYTHON) patch_image_header.py $@ > /dev/null
+       $(Q)$(PYTHON) patch_image_header.py $@ $(PK_PEM_PATH) > /dev/null
```

Where `PK_PEM_PATH` is the path to your private key.

We now have a build process that generates signed binaries!

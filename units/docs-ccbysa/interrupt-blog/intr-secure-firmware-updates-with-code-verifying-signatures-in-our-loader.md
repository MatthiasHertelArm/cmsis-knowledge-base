---
id: "intr-secure-firmware-updates-with-code-verifying-signatures-in-our-loader"
type: "concept"
domain: "debug"
title: "Secure firmware updates with code signing: Firmware Signing Implementation / Verifying signatures in our Loader"
summary: "Part of: Firmware Signing Implementation"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-09-08-secure-firmware-updates-with-code-signing.md"
doc_source: "https://interrupt.memfault.com/blog/secure-firmware-updates-with-code-signing#verifying-signatures-in-our-loader"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Firmware Signing Implementation_

Now that our firmware builds are signed, let's verify those signatures in our
Loader!

Remember that the process takes two steps:
1. Compute the SHA-256 hash of our firmware binary
2. Verify the signature with the hash and the public key

First, we'll need an implementation of the ECDSA algorithm. Remember, the first
rule of crypto is "don't roll your own crypto" so you'll want a battle-tested
library implemented by experts. There are a few good options, but we chose
micro-ecc[^micro-ecc] as we are most familiar with it and it is extremely small.

micro-ecc is extremely easy to add to a project: it consists of a single
`.c` (uECC.c) and a single `.h` (uECC.h) file. Add the source file to your list of sources, and
the header file to your include path.

We then add our public key to our firmware. micro-ecc expects our keys to be
"represented in standard format, but without the 0x04
prefix"[^micro-ecc-representation]. We can use `openssl` to get the raw key
data:

```shell
(.venv) $ openssl ec -in private.pem -text -noout
read EC key
Private-Key: (256 bit)
priv:
    4f:93:5d:53:41:82:21:91:11:e9:fe:9f:33:90:09:
    28:da:d0:96:70:f7:5e:26:85:dc:ff:5d:bc:f8:6f:
    5f:15
pub:
    04:d0:e6:a7:a5:4e:33:0e:bb:d9:9e:e6:8f:59:ff:
    b6:c1:19:76:28:60:88:16:6a:17:8b:7b:e0:66:cf:
    7b:71:0d:f5:cc:95:76:22:ae:0e:a4:ef:49:bd:07:
    2a:71:49:84:49:78:eb:34:e5:78:b3:a7:96:48:89:
    7c:4f:d1:7e:a5
ASN1 OID: secp256k1
```

We take the `pub` section, remove the leading `04` bytes, and translate it to a
C array:

```c
static const uint8_t PUBKEY[] = {
  0xd0, 0xe6, 0xa7, 0xa5, 0x4e, 0x33, 0x0e, 0xbb, 0xd9, 0x9e, 0xe6, 0x8f, 0x59,
  0xff, 0xb6, 0xc1, 0x19, 0x76, 0x28, 0x60, 0x88, 0x16, 0x6a, 0x17, 0x8b, 0x7b,
  0xe0, 0x66, 0xcf, 0x7b, 0x71, 0x0d, 0xf5, 0xcc, 0x95, 0x76, 0x22, 0xae, 0x0e,
  0xa4, 0xef, 0x49, 0xbd, 0x07, 0x2a, 0x71, 0x49, 0x84, 0x49, 0x78, 0xeb, 0x34,
  0xe5, 0x78, 0xb3, 0xa7, 0x96, 0x48, 0x89, 0x7c, 0x4f, 0xd1, 0x7e, 0xa5
  // 64 bytes
};
```

We can then verify that uECC is able to read the key correctly by calling
`uECC_valid_public_key`. We add the following code somewhere in our `main`
function at boot:

```c
#include <micro-ecc/uECC.h>

const struct uECC_Curve_t *curve = uECC_secp256k1();
if (!uECC_valid_public_key(PUBKEY, curve)) {
    printf("Public key is NOT valid\n");
} else {
    printf("Public key is valid\n");
}
```

Note that we had to select the same curve we used to generate the key, here
`secp2561k`.

Last but not least, we need to verify the signature itself. This requires
computing the SHA-256, and using `uECC_verify`.

Many MCUs have hardware implementations of SHA-256, but in our case, we used a
software implementation provided by a library called CIFRA[^cifra]. We only need
to add two files from CIFRA to our build: `cifra/src/sha256.c` and `cifra/src/blockwise.c`,
as well as two paths to our include path: `cifra/src` and `cifra/src/ext`.

With that, I implemented a simple sha256 wrapper function which computes the
hash of a given buffer:

```c
static void prv_sha256(const void *buf, uint32_t size, uint8_t *hash_out)
{
  cf_sha256_context ctx;
  cf_sha256_init(&ctx);
  cf_sha256_update(&ctx, buf, size);
  cf_sha256_digest_final(&ctx, hash_out);
}
```

Note that `cf_sha256_update` can be called multiple times, so if you are
validating a binary that isn't memory mapped you can calculate the hash
iteratively rather than all at once. For example, here's an implementation that
reads from a POSIX file:

```c
static void prv_sha256(FILE *fp, uint8_t *hash_out)
{
  #define READ_BUF_SZ 128
  static uint8_t read_buf[READ_BUF_SZ] = {0};

  cf_sha256_context ctx;
  cf_sha256_init(&ctx);

  fseek(fp, sizeof(image_hdr_t), SEEK_SET);
  size_t readsize = 0;
  while ((readsize = fread(read_buf, 1, READ_BUF_SZ, fp)) > 0) {
    cf_sha256_update(&ctx, read_buf, readsize);
  }

  cf_sha256_digest_final(&ctx, hash_out);
}
```

Given a hash and a public key, we can then validate the signature found in our
`imaget_hdr_t`:

```c
if (!uECC_verify(PUBKEY, hash, CF_SHA256_HASHSZ, hdr->ecdsa_sig, curve)) {
    printf("Signature is NOT valid\n");
} else {
    printf("Signature is valid\n");
}
```

Putting it all together, here's our function to verify the signature of a given
image:

```c
int image_check_signature(image_slot_t slot, const image_hdr_t *hdr) {
    void *addr = (slot == IMAGE_SLOT_1 ? &__slot1rom_start__ : &__slot2rom_start__);
    addr += sizeof(image_hdr_t);
    uint32_t len = hdr->data_size;

    uint8_t hash[CF_SHA256_HASHSZ];
    prv_sha256(addr, len, hash);

    const struct uECC_Curve_t *curve = uECC_secp256k1();
    if (!uECC_valid_public_key(PUBKEY, curve)) {
        return -1;
    }

    if (!uECC_verify(PUBKEY, hash, CF_SHA256_HASHSZ, hdr->ecdsa_sig, curve)) {
        return -1;
    }

    return 0;
}
```

We can invoke that function as part of our OTA process in
`loader_shell_commands.c`:

```diff
@@ -32,13 +32,19 @@
         return -1;
     }

     shell_put_line("Validating image");
     // Check & commit image
     if (image_validate(IMAGE_SLOT_2, hdr)) {
         shell_put_line("Validation Failed");
         return -1;
     };

+    shell_put_line("Checking signature");
+    if (image_check_signature(IMAGE_SLOT_2, hdr)) {
+        shell_put_line("Signature does not match");
+        return -1;
+    };
+
     shell_put_line("Committing image");
     if (dfu_commit_image(IMAGE_SLOT_2, hdr)) {
         shell_put_line("Image Commit Failed");
```

Running our firmware, we can watch it all happen over serial:

```shell
$ telnet localhost 4445
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
Bootloader started
Booting slot 1
Shared memory uinitialized, setting magic
Loader STARTED - version 1.0.0 (19dcbe5)
Booting slot 2
App STARTED - version 1.0.1 (19dcbe5) - CRC 0x1b11019d

shell> dfu-mode
Rebooting into DFU mode
Bootloader started
Booting slot 1
Loader STARTED - version 1.0.0 (19dcbe5)
Entering DFU Mode

shell> do-dfu
Starting update
Writing data
Validating image
Checking signature <----- **This is our new log line**
Committing image
Rebooting
Bootloader started
Booting slot 1
Loader STARTED - version 1.0.0 (19dcbe5)
Booting slot 2
App STARTED - version 1.0.1 (19dcbe5) - CRC 0x1b11019d

shell>
```

The full example is available on Github at
[interrupt@fwup-signing](https://github.com/memfault/interrupt/tree/master/example/fwup-signing).

> Note: While researching this post I came across
> [Tinycrypt](https://github.com/intel/tinycrypt), an open source library
> maintained by Intel. Tinycrypt combines micro-ecc with additional primitives
> such as SHA-256. If I were to do it again, I would look into using tinycrypt
> rather than two separate libraries.

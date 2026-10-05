---
id: "intr-secure-firmware-updates-with-code-generating-public-private-key-pairs"
type: "concept"
domain: "debug"
title: "Secure firmware updates with code signing: Firmware Signing Implementation / Generating public/private key pairs"
summary: "Part of: Firmware Signing Implementation"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-09-08-secure-firmware-updates-with-code-signing.md"
doc_source: "https://interrupt.memfault.com/blog/secure-firmware-updates-with-code-signing#generating-public-private-key-pairs"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Firmware Signing Implementation_

Before we can begin, we must generate a pair of keys. Our **private key**, also
known as a **signing key**, is used to create the signatures, and should be kept
private. Anyone with access to the key will be able to sign firmware on your
behalf. Our **public key**, also known as a **validation key**, is used to verify
the signature. It can be freely distributed.

Several tools can be used to generate our key pair but the simplest is
`openssl`, a cross platform cryptography toolset.

First, we generate our private key:
```bash
$ openssl ecparam -name secp256k1 -genkey -noout -out private.pem
```

Then we create a public key to go with this private key:
```bash
$ openssl ec -in private.pem -pubout -out public.pem
```

At this point we should have two files: `public.pem` and `private.pem`.

We can test the sign/verify flow with openssl as well. To sign a file we do:

```bash
$ openssl dgst -sha256 -sign private.pem -out build/fwup-example.bin.sig build/fwup-example.bin
```

Where "fwup-example.bin" is the file we want to sign, and "fwup-example.bin.sig"
is the signature file we want to create.

The signature can then be verified with:

```bash
$ openssl dgst -sha256 -verify public.pem -signature build/fwup-example.bin.sig build/fwup-example.bin
Verified OK
```

That's it! We've got keys we can use to sign and verify firmware builds!

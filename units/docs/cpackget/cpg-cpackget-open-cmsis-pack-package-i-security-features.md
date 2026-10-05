---
id: "cpg-cpackget-open-cmsis-pack-package-i-security-features"
type: "concept"
domain: "pack"
title: "cpackget: Open-CMSIS-Pack Package Installer: Security features"
summary: "The following features are not fully deployed yet and under constant review/discussion. These might suddenly change from release to release, with potential breaking changes. Always check the release/changelog first."
status: "draft"
collection: "cpackget"
source: "Open-CMSIS-Pack/cpackget@d467d31:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/blob/d467d31/README.md#security-features"
license: "Apache-2.0"
mode: "V"
---

The following features are not fully deployed yet and under constant review/discussion. These might suddenly change
from release to release, with potential breaking changes. Always check the release/changelog first.

### Integrity checking

As of release **v0.7.0**, it's possible to create a `.checksum` file of a local `.pack`. This file resembles a common
digest file, used to confirm that an obtained piece of information matches the source's content. \
Instead of just including the digest of the entire .pack as one, it lists the digests of all the files.

The extension includes the pack's name in its canonical form and hash algorithm used, appended by
".checksum": `Pack.Vendor.1.0.0.sha256.checksum`. Currently only works for local packs.

To create it:

```bash
$ cpackget checksum-create Vendor.PackName.1.0.0.pack
```

To verify a `.pack` against it's checksum file:

```bash
$ cpackget checksum-verify Vendor.PackName.1.0.0.pack
```

(the .checksum path is assumed to be the same as the `.pack`, but it can be specified with the `-p` flag)

### Signed Packs

Likewise, this capability can also be extended to check for _authenticity_ and _non-repudiation_. With the usage
of X.509 certificates and/or PGP signatures, it's possible to create a chain of trust where pack vendors can provide
verifiable proof that mitigates malicious attacks (like man-in-the-middle) and assure cpackget users
the legitimacy and authenticity of their published packs.

#### Specification

To achieve this, a protocol was developed which takes advantage of the `.pack` format - packs are always zip files
which by definition contain a general comment field. cpackget generates a _signature_ which gets embed in the pack
through this comment field.

This signature includes a cryptographic signed message of the hashed pack, binding its contents to an entity.

Two different modes are available, which have different requirements to create the signature:

* full: a X.509 public key certificate representing the vendor/publisher and its private key
* pgp: an armored PGP private key

_Note: there's a third, "cert-only" mode, which is recommended only for testing/debugging purposes, as it doesn't
include the signed digest of the pack._

The signature features the following format:
`[cpackget version]:[chosen mode]:[x509 certificate or PGP signed digest]:[signed digest]`. As expected,
the last two elements vary depending on the used mode, and are base64 encoded. Modes are represented with
an `f` or `c` character.

To verify a pack, cpackget does the reverse operation: calculates the signed digest of the pack with the included
X.509 pub key or referenced PGP key and matches it against what's written in the signature.

#### Example usage: X.509

A X.509 public key certificate and its private key is required to use the X.509 signing mode.
[OpenSSL](https://wiki.openssl.org/index.php/Binaries) is the industry standard for this.
If you're running Linux, chances are you already have it installed in your system.

After installation, create both the certificate and private key with:

```bash
$ openssl req -x509 -newkey rsa:3072 -keyout x509_private_rsa.pem -out x509_certificate.pem -nodes
```

The specified key must be RSA, as of current implementation. The most important field is `CN (Common Name)`,
which names the entity signing the pack. Currently, cpackget does not enforce any specific CA to be the `Issuer`,
so if following these steps, this field would represent both the `Issuer` and `Subject` names.
Like the entire feature, this is very much subject to change.

Now, create the signature by providing a pack:

```bash
$ cpackget signature-create Vendor.PackName.1.2.3.pack --private-key x509_private_rsa.pem --certificate x509_certificate.pem
```

Information about the certificate will be displayed, and some basic validations on its integrity will be performed.
Skip these with `--skip-info` and `--skip-validation`, respectively.

A copy of the pack (with a `.signed` extension) should be embed with the X.509 signed digest and the rest of the
signature. Any zip tool like `zipinfo` can be used to view this:

```bash
$ zipinfo -z Vendor.PackName.1.2.3.pack.signed
Archive:  Vendor.PackName.1.2.3.pack.signed
cpackget-v0.8.5:f:LS0tLS1CRUdJTiBQR1AgU0lHTkFUVVJFLS0tLS0KVmVyc2lvbjogR29wZW5QR1AgMi40LjEwCkNvbW1lbnQ6IGh0dHBzOi8vZ29wZW5wZ3Aub3JnCgp3c0R6QkFBQkNnQW5CUUpqWXdYVENaQ1hzckI2R0VKeGJSWWhCTk94N0srOWZ:sCCre...
```

To verify this pack as legitimate and authentic, cpackget needs X.509 public key certificate, and the signed pack:

```bash
$ cpackget signature-verify Vendor.PackName.1.2.3.pack.signed --pub-key x509_certificate.pem
I: Pack signature verification success - pack is authentic
```

#### Example usage: PGP

A PGP key pair is required to use the PGP signing mode. [GnuPG](https://gnupg.org/download/) is the tried & tested
tool for this purpose.

After installation, create one with:

```bash
$ gpg --full-generate-key
```

The specified key must be either RSA or Curve25519. Take note of the `email` field, as it will be used to export it. \
Then, proceed to export both the public and private key locally, so it can be used as input for cpackget:

```bash
$ gpg --output public.pgp --armor --export <your-email>
$ gpg --output private.pgp --armor --export-secret-key <your-email>
```

With both of the keys locally saved, create the signature by providing a pack:

```bash
$ cpackget signature-create Vendor.PackName.1.2.3.pack --pgp --private-key private.pgp
```

A copy of the pack (with a `.signed` extension) should be embed with the PGP signed digest and the rest of
the signature. Any zip tool like `zipinfo` can be used to view this:

```bash
$ zipinfo -z Vendor.PackName.1.2.3.pack.signed
Archive:  Vendor.PackName.1.2.3.pack.signed
cpackget-v0.8.5:p:LS0tLS1CRUdJTiBQR1AgU0lHTkFUVVJFLS0tLS0KVmVyc2lvbjogR29wZW5QR1AgMi40LjEwCkNvbW1lbnQ6IGh0dHBzOi8vZ29wZW5wZ3Aub3JnCgp3c0R6QkFBQkNnQW5CUUpqWXdYVENaQ1hzckI2R0VKeGJSWWhCTk94N0srOWZ...
```

To verify this pack as legitimate and authentic, cpackget needs the public counterpart of the signee's key,
and the signed pack:

```bash
$ cpackget signature-verify Vendor.PackName.1.2.3.pack.signed --pub-key public.pgp
I: Pack signature verification success - pack is authentic
```

For more info on the current implementation: `cpackget help signature-create` and `cpackget help signature-verify`.

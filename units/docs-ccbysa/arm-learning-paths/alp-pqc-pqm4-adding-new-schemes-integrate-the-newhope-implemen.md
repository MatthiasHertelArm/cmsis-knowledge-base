---
id: "alp-pqc-pqm4-adding-new-schemes-integrate-the-newhope-implemen"
type: "concept"
domain: "core"
title: "Implement post-quantum cryptography on Arm Cortex-M4: Add a KEM implementation to pqm4: Integrate the NewHope implementation into pqm4"
summary: "In this section, you'll use NewHope-512-CPA-KEM as a concrete example of a scheme. NewHope is a lattice-based KEM that was a candidate in the NIST PQC standardization process."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/pqc_pqm4/adding-new-schemes.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/pqc_pqm4/adding-new-schemes/#integrate-the-newhope-implementation-into-pqm4"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this section, you'll use NewHope-512-CPA-KEM as a concrete example of a scheme. NewHope is a lattice-based KEM that was a candidate in the NIST PQC standardization process. Although NewHope was not selected for standardization, it remains a useful example because it shares structural similarities with ML-KEM. It also has a clean, well-documented reference implementation. The following steps apply equally to any KEM that follows the NIST/SUPERCOP/PQClean API.

### Download the scheme implementation

Clone the NewHope reference implementation from the pqm4 root directory:

```bash
git clone https://github.com/newhopecrypto/newhope.git
```

The source files you need are in `newhope/ref/`.

### Create the scheme directory

Inside the pqm4 repository, create a directory for the new scheme:

```bash
mkdir -p crypto_kem/newhope512cpa/m4
```

### Copy implementation files

Copy the following files from `newhope/ref/` into `crypto_kem/newhope512cpa/m4/`:

```bash
cp newhope/ref/poly.c    crypto_kem/newhope512cpa/m4/
cp newhope/ref/poly.h    crypto_kem/newhope512cpa/m4/
cp newhope/ref/ntt.c     crypto_kem/newhope512cpa/m4/
cp newhope/ref/ntt.h     crypto_kem/newhope512cpa/m4/
cp newhope/ref/reduce.c  crypto_kem/newhope512cpa/m4/
cp newhope/ref/reduce.h  crypto_kem/newhope512cpa/m4/
cp newhope/ref/cpapke.c  crypto_kem/newhope512cpa/m4/
cp newhope/ref/cpapke.h  crypto_kem/newhope512cpa/m4/
cp newhope/ref/cpakem.c  crypto_kem/newhope512cpa/m4/
cp newhope/ref/cpakem.h  crypto_kem/newhope512cpa/m4/
cp newhope/ref/params.h  crypto_kem/newhope512cpa/m4/
cp newhope/ref/precomp.c crypto_kem/newhope512cpa/m4/
cp newhope/ref/verify.c  crypto_kem/newhope512cpa/m4/
cp newhope/ref/verify.h  crypto_kem/newhope512cpa/m4/
```

Don't copy the following files:

- `randombytes.c` and `randombytes.h`, `rng.c` and `rng.h` — pqm4 provides its own RNG
- `fips202.c` and `fips202.h` — use `mupq/common/fips202.h` instead
- `ccakem.c` and `ccakem.h` — this Learning Path uses the CPA variant only
- `PQCgenKAT_kem.c`
- Standalone test or benchmark files such as `speed.c` and `test_newhope.c`
- Compiled `.o` files

### Create the API header

Create `crypto_kem/newhope512cpa/m4/api.h` and define the required constants and function declarations. Use the values from `params.h` in the NewHope reference implementation for the byte sizes:

```c
#ifndef API_H
#define API_H

#define CRYPTO_SECRETKEYBYTES 3680
#define CRYPTO_PUBLICKEYBYTES 1824
#define CRYPTO_CIPHERTEXTBYTES 2208
#define CRYPTO_BYTES 32

#define CRYPTO_ALGNAME "NewHope512-CPA"

int crypto_kem_keypair(unsigned char *pk, unsigned char *sk);
int crypto_kem_enc(unsigned char *ct, unsigned char *ss, const unsigned char *pk);
int crypto_kem_dec(unsigned char *ss, const unsigned char *ct, const unsigned char *sk);

#endif
```

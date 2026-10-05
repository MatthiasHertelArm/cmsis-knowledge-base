---
id: "tfm-crypto-service-integration-guide-introduction"
type: "concept"
domain: "security"
title: "Crypto Service Integration Guide: Introduction"
summary: "The TF-M Crypto service allows Non Secure world applications and Secure services to use cryptographic functionalities such as symmetric ciphering, message signing and verification, asymmetric encryption and decryption, cryptographic hashes, message authentication codes (MACs), key derivation and agreement, …"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/services/tfm_crypto_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_crypto_integration_guide.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

The TF-M Crypto service allows Non Secure world applications and Secure
services to use cryptographic functionalities such as symmetric ciphering,
message signing and verification, asymmetric encryption and decryption,
cryptographic hashes, message authentication codes (MACs), key derivation and
agreement, authenticated encryption with associated data (AEAD). It exposes the
PSA Crypto APIs [1]_.

The secure service resides in the Crypto partition as a single entry point and
is made of different components:

 - An interface layer that exposes the PSA Crypto API to either NS or S entities
   and is implemented in `interface/src/tfm_crypto_api.c`. The interface is
   based on the Uniform Secure Service Signature and communicates with the
   Secure Partition Manager available in TF-M
 - An init module `secure_fw/partitions/crypto/crypto_init.c` that implements
   functionalities requested by TF-M during the initialisation phase, and an API
   dispatcher that at runtime receives the requests from the interface and
   dispatches them to the component that processes that particular API request
 - A set of components that process cryptographic API requests, each component
   dispatching to a subset of functionalities, i.e. AEAD, Asymmetric, Ciphering,
   Hashing, Key derivation, Key management, MACs, and Random Number Generation
 - An alloc module `secure_fw/partitions/crypto/crypto_alloc.c` that manages
   the partition secure memory, storing multipart application contexts, input /
   outputs of the APIs being requested, inaccessible from NS or other secure
   partitions
 - A library abstraction module `secure_fw/partitions/crypto/crypto_library.c`
   which is used to abstract the details of the cryptographic library used by
   the service *backend* to provide the actual implementation of the crypto
   functionalities. The backend library must expose the PSA Crypto APIs, and
   must provide support to encode *key ownership* into key identifiers. This is
   not standardized by the PSA Crypto APIs so it must be provided as an
   extension to the APIs. The backend library also needs to provide the
   subsystem for key storage and retrieval, and, in case, the interface to the
   cryptographic accelerator of the underlying platform, using the PSA
   cryptoprocessor driver interface specification [2]_. For this reason, it must
   provide a mechanism to access platform *builtin* keys, and permanent key
   slots using the
   TF-M Internal Trusted Storage (ITS) service,
   if available.

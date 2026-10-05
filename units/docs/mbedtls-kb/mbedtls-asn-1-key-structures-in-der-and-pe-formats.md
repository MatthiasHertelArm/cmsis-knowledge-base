---
id: "mbedtls-asn-1-key-structures-in-der-and-pe-formats"
type: "concept"
domain: "security"
title: "ASN.1 key structures in DER and PEM: Formats"
summary: "Below, we discuss the different formats and the structure that you should expect to see in each file."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/cryptography/asn1-key-structures-in-der-and-pem.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/cryptography/asn1-key-structures-in-der-and-pem.md#formats"
license: "Apache-2.0"
mode: "V"
---

Below, we discuss the different formats and the structure that you should expect to see in each file.

### RSA public Key file (PKCS#1)
The RSA Public key PEM file is specific for RSA keys.

It starts and ends with the tags:

```
    -----BEGIN RSA PUBLIC KEY-----
    BASE64 ENCODED DATA
    -----END RSA PUBLIC KEY-----
```

Within the base64 encoded data, the following DER structure is present:

```
    RSAPublicKey ::= SEQUENCE {
      modulus   INTEGER,  -- n
      publicExponent    INTEGER   -- e
    }
```

### Public Key file (PKCS#8)
Because RSA is not used exclusively inside X509, SSL and TLS, a more generic key format, PKCS#8, is available. It identifies the type of public key and contains the relevant data.

It starts and ends with the tags:

```
    -----BEGIN PUBLIC KEY-----
    BASE64 ENCODED DATA
    -----END PUBLIC KEY-----
```

Within the base64 encoded data, the following DER structure is present:

```
    PublicKeyInfo ::= SEQUENCE {
      algorithm   AlgorithmIdentifier,
      PublicKey   BIT STRING
    }
    
    AlgorithmIdentifier ::= SEQUENCE {
      algorithm   OBJECT IDENTIFIER,
      parameters  ANY DEFINED BY algorithm OPTIONAL
    }
```

So, for an RSA public key, the OID is `1.2.840.113549.1.1.1`, and the `RSAPublicKey` is the `PublicKey` key data bitstring.

### RSA private Key file (PKCS#1)
The RSA private key PEM file is specific for RSA keys.

It starts and ends with the tags:

```
    -----BEGIN RSA PRIVATE KEY-----
    BASE64 ENCODED DATA
    -----END RSA PRIVATE KEY-----
```

Within the base64 encoded data, the following DER structure is present:

```
    RSAPrivateKey ::= SEQUENCE {
      version   Version,
      modulus   INTEGER,  -- n
      publicExponent    INTEGER,  -- e
      privateExponent   INTEGER,  -- d
      prime1    INTEGER,  -- p
      prime2    INTEGER,  -- q
      exponent1 INTEGER,  -- d mod (p-1)
      exponent2 INTEGER,  -- d mod (q-1)
      coefficient   INTEGER,  -- (inverse of q) mod p
      otherPrimeInfos   OtherPrimeInfos OPTIONAL
    }
```

### Private Key file (PKCS#8)
Because RSA is not used exclusively inside X509, SSL and TLS, a more generic key format, PKCS#8, is available. It identifies the type of private key and contains the relevant data.

The unencrypted PKCS#8 encoded data starts and ends with the tags:

```
    -----BEGIN PRIVATE KEY-----
    BASE64 ENCODED DATA
    -----END PRIVATE KEY-----
```

Within the base64 encoded data, the following DER structure is present:

```
    PrivateKeyInfo ::= SEQUENCE {
      version Version,
      algorithm   AlgorithmIdentifier,
      PrivateKey  OCTET STRING
    }
    
    AlgorithmIdentifier ::= SEQUENCE {
      algorithm   OBJECT IDENTIFIER,
      parameters  ANY DEFINED BY algorithm OPTIONAL
    }
```

So for an RSA private key, the OID is `1.2.840.113549.1.1.1`, and the `RSAPrivateKey` is the `PrivateKey` key data octet string.

The encrypted PKCS#8 encoded data starts and ends with the tags:

```
    -----BEGIN ENCRYPTED PRIVATE KEY-----
    BASE64 ENCODED DATA
    -----END ENCRYPTED PRIVATE KEY-----
```

Within the base64 encoded data, the following DER structure is present:

```
    EncryptedPrivateKeyInfo ::= SEQUENCE {
      encryptionAlgorithm  EncryptionAlgorithmIdentifier,
      encryptedData    EncryptedData
    }
    
    EncryptionAlgorithmIdentifier ::= AlgorithmIdentifier
    
    EncryptedData ::= OCTET STRING
```

The `EncryptedData OCTET STRING` is a PKCS#8 `PrivateKeyInfo`, as described earlier.

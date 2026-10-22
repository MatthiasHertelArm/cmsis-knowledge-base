---
id: "mbedtls-the-external-dependencies-mbed-tls-file-stream-functions"
type: "concept"
domain: "security"
title: "The external dependencies Mbed TLS relies on: File (stream) functions"
summary: "If MBEDTLS_FS_IO is defined, the file functions are used in several Mbed TLS modules:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/what-external-dependencies-does-mbedtls-rely-on.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/what-external-dependencies-does-mbedtls-rely-on.md#file-stream-functions"
license: "Apache-2.0"
mode: "V"
---

If `MBEDTLS_FS_IO` is defined, the file functions are used in several Mbed TLS modules:

- The MD layer for file hashing (`mbedtls_md_file()`).
- *X509 Parsing* (`x509_crt.c`, `x509_crl.c`, `x509_csr.c`) use the file functions for reading the certificate, CSR and CRL files; it also uses `readdir()` for `mbedtls_x509_crt_parse_path()`.
- The PK layer (`pkparse.c`) uses file functions for reading and parsing keys from files.
- The *MPI* module (`bignum.c`) uses `fwrite` for writing MPIs to files and streams and `fgets` for reading files and streams into MPIs.
- The entropy, *CTR-DRBG* and *HMAC_DRBG* modules use file functions for reading and updating seed files.
- The *DHM* module uses file operations to read DH parameters files (`mbedtls_dhm_parse_dhmfile`).

You can disable all by commenting `MBEDTLS_FS_IO` in `mbedtls_config.h`.

**Functions covered:** 

- `fclose()`
- `ferror()`
- `fgets()`
- `fopen()`
- `fread()`
- `fseek()`
- `ftell()`
- `fwrite()`
- `readdir()`
- `closedir()`

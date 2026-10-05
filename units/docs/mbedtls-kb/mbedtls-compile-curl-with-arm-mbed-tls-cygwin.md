---
id: "mbedtls-compile-curl-with-arm-mbed-tls-cygwin"
type: "concept"
domain: "security"
title: "Compile cURL with Arm Mbed TLS: Cygwin"
summary: "Some additional information for Cygwin users."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/compile-curl-with-mbedtls.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/compile-curl-with-mbedtls.md#cygwin"
license: "Apache-2.0"
mode: "V"
---

Some additional information for Cygwin users.

- First, uninstall the standard cURL package from your Cygwin installation if it is installed. You can use the command `cygcheck -c` to print your installed packages.
- Before you can `wget` the Mbed TLS code, you need a bundle of X.509 certificates inside your Cygwin environment.

   ```
   pushd /usr/ssl/certs
   curl http://curl.haxx.se/ca/cacert.pem | awk 'split_after==1{n++;split_after=0} /-----END CERTIFICATE-----/ {split_after=1} {print >    "cert" n ".pem"}'
   
   c_rehash
   ```
   
- Create an extra symlink for wget

   ```
   ln -sT /usr/ssl /etc/ssl
   ```

- Configure the cURL build system with the following options:

   ```
   ./configure --without-ssl --with-mbedtls=/usr/local --with-ca-bundle=/etc/ssl/certs/ca-bundle.crt
   ```
   
The option `with-mbedtls` points to your Mbed TLS location and `with-ca-bundle` is the location of your certificates bundle you extracted before.

<!---compile-curl-with-mbedtls,
"A short tutorial on how to compile cURL with mbed TLS",
"cURL, compiling cURL, compile cURL, Mbed TLS",
"compiling cURL, cURL, tutorial, cygwin",published,
"2012-10-09 00:00:00",2,9275,
"2015-07-24 11:35:00",
"Paul Bakker"--->

---
id: "mlek-troubleshooting-errors-when-cloning-the-repository"
type: "concept"
domain: "edge-ai"
title: "Troubleshooting: Errors when cloning the repository"
summary: "If you see following errors when cloning the repository:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/troubleshooting.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/troubleshooting.md#errors-when-cloning-the-repository"
license: "Apache-2.0"
mode: "V"
---

If you see following errors when cloning the repository:

- ```log
   fatal: unable to access 'https://git.gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit.git':
   server certificate verification failed. CAfile: /etc/ssl/certs/ca-certificates.crt CRLfile: none
  ```

  We suggest to update to the latest common CA certificates:

  ```commandline
  sudo apt-get update
  sudo apt-get install ca-certificates
  ```

- ```log
  fatal: unable to access 'https://git.gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit.git':
  error:06FFF089:digital envelope routines:CRYPTO_internal:bad key length
  ```

  We suggest to export the `CURL_SSL_BACKEND` variable as `secure-transport`:

  ```commandline
  export CURL_SSL_BACKEND="secure-transport"
  ```

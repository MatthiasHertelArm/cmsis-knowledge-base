---
id: "mbedtls-setting-up-a-python-environment-fo-python-and-package-versions"
type: "concept"
domain: "security"
title: "Setting up a Python environment for Mbed TLS: Python and package versions"
summary: "Each branch of Mbed TLS has different minimum requirements on Python. See README.md in the branch."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/python-environment.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/python-environment.md#python-and-package-versions"
license: "Apache-2.0"
mode: "V"
---

Each branch of Mbed TLS has different minimum requirements on Python. See `README.md` in the branch. Any Python version that's more recent than the minimum should work, however as of November 2022 this is not well tested by the CI so unintended incompatibilities can happen.

Some of the scripts used by Mbed TLS users and developers require third-party packages. Those have version constraints as well. The constraints are documented via `*.requirements.txt` files in the [`scripts` directory](https://github.com/Mbed-TLS/mbedtls/tree/development/scripts).

We run [mypy](http://mypy-lang.org/) and [pylint](https://pylint.pycqa.org/en/latest/) to check Python scripts. It is common that newer versions of Pylint reject our code, because some checks have become stricter or new checks have been added.

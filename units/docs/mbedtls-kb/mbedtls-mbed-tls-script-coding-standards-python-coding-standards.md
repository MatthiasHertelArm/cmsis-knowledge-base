---
id: "mbedtls-mbed-tls-script-coding-standards-python-coding-standards"
type: "concept"
domain: "security"
title: "Mbed TLS script coding standards: Python coding standards"
summary: "As of September 2022, Python scripts must be compatible with Python 3.5, because that's what's on parts of the CI, even though we only promise Python 3.6 in README.md."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/script-coding-standards.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/script-coding-standards.md#python-coding-standards"
license: "Apache-2.0"
mode: "V"
---

### Python version

As of September 2022, Python scripts must be compatible with Python 3.5,
because that's what's on parts of the CI, even though we only promise Python 3.6 in [`README.md`](https://github.com/Mbed-TLS/mbedtls/blob/development/README.md#tool-versions).

Exception: `scripts/config.py` must remain compatible with Python 3.4, which is the earliest version that was officially supported at the time of the 2.28.0 release. (This is only a requirement in 2.28, but it's easiest to keep the development version mostly aligned.) Other scripts in 2.28 are not user-facing and so can require a more recent version.

### Directory structure

Non-executable Python modules are in `scripts/mbedtls_dev`.
Executable Python scripts in `scripts` can use auxiliary modules with `from mbedtls_dev import ...`.

Executable Python scripts in `tests/scripts` cannot refer to modules in `scripts/mbedtls_dev` directly, because we do not assume that `PYTHONPATH` contains the Mbed TLS source tree. To use other Python modules from a script in `tests/scripts`, use the following idiom:

```python
import scripts_path # pylint: disable=unused-import
from mbedtls_dev import ...
```

### Python imports

We follow the usual convention that imports go at the top of a file (after the docstring and the license comment). Imports are typically ordered as follows:

1. Standard library, in lexicographic order.
2. Third-party libraries, if any, in lexicographic order.
3. Modules from `mbedtls_dev`, in lexicographic order.

Avoid importing individual names from modules, as it can be difficult to figure out which module an unqualified name comes from. However, it's ok to import names if they're sufficiently recognizable, for example:

* Importing individual modules from `mbedtls_dev` is fine.
* Importing capitalized type names from `typing` is fine.
* Importing individual submodules from Cryptodome is fine.

### Third-party Python libraries

Avoid bringing in new dependencies, because each dependency adds risk to the project. Only use dependencies if they have a clear advantage.

The minimum supported version of third-party Python libraries is recorded in `*.requirements.txt` files in the [`scripts` directory](https://github.com/Mbed-TLS/mbedtls/tree/development/scripts). As with the [Python version](#language-versions), keep in mind that long-time support branches may need to support older versions.

### Python language features

The maintainers of Mbed TLS are primarily C programmers, not Python programmers. It's ok to use fancy language features if they make the code significantly simpler, but don't necessarily assume that the reader is familiar with them. Make sure that unfamiliar readers can easily look up such fancy features.

* Classes, methods and simple inheritance can be used freely.
* Avoid metaclasses and nontrivial dynamic class creation. If you use these features, write documentation that's accessible to non-experts.
* Do define [special methods](https://docs.python.org/3/reference/datamodel.html#special-method-names) if convenient for comparison, context managers, etc. But avoid customizing attribute access.
* Use [decorators](https://docs.python.org/3/glossary.html#term-decorator) if they have a clear benefit.
* Do use [generators](https://docs.python.org/3/glossary.html#term-generator) and [list comprehension](https://docs.python.org/3/glossary.html#term-list-comprehension) where warranted.

### Python typing

Using type annotations is encouraged. We run [mypy](http://mypy-lang.org/) to verify static typing.

Avoid complex overloading. It's generally easier to understand code if it only expects a specific type of data.

### Python style conventions

We generally follow [PEP 8](https://peps.python.org/pep-0008/). For docstrings, we also follow [PEP 257](https://peps.python.org/pep-0257/).

### Python style enforcement

We run [Pylint](https://pylint.pycqa.org/) for style enforcement. Pylint is quite opinionated sometimes, so if a rule doesn't make sense in a specific context, use a [Pylint pragma comment](https://pylint.pycqa.org/en/latest/user_guide/messages/message_control.html) to disable it.

---
id: "mbedtls-how-to-systematically-generate-tes-creating-a-test-script"
type: "concept"
domain: "security"
title: "How to systematically generate test data: Creating a test script"
summary: "This is only required if an existing script is not being extended. An example is included for each step, showing how to create a test generation script for test_suite_mpi.function, a basic equivalent of generate_bignum_tests.py."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/add-test-generation.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/add-test-generation.md#creating-a-test-script"
license: "Apache-2.0"
mode: "V"
---

This is only required if an existing script is not being extended.
An example is included for each step, showing how to create a test generation script for
`test_suite_mpi.function`, a basic equivalent of
[generate_bignum_tests.py](https://github.com/Mbed-TLS/mbedtls/blob/development/tests/scripts/generate_bignum_tests.py).

### Initial Python script

To create the script, import `test_data_generation` from `mbedtls_dev` and call
`test_data_generation.main()` when the script runs.
The `scripts` directory must be in the system path; for a script in `tests/scripts`, add
it by importing `scripts_path` (see the example below).

For the example, create `generate_bignum_ex_tests.py` in `tests/scripts/`, containing:

```python
#!/usr/bin/env python3
import sys

import scripts_path # pylint: disable=unused-import
from mbedtls_dev import test_data_generation

if __name__ == '__main__':
    # Pass command line arguments and a description for the script
    test_data_generation.main(sys.argv[1:], "Generate bignum tests.")
```

This script can now be run, although it will do nothing at this stage.
Use the `--help` argument for usage details.

```bash
$ tests/scripts/generate_bignum_ex_tests.py
```

### Generating a data file

To generate a data file from the script, you must define a subclass of `BaseTarget`,
setting `target_basename` to the output file basename.
This is a [file target class](#file-target-classes).
Generally `target_basename` is `"test_suite_xyz.generated"` for tests defined
in `test_suite_xyz.function`.
In the example, `metaclass=ABCMeta` is added to the class to explicitly indicate this is
an abstract class.
As Pylint does not recognize this as an abstract class, the `abstract-method` warning is
disabled.

For the example, add the following class:

```python
from abc import ABCMeta
...
class BignumTarget(test_data_generation.BaseTarget, metaclass=ABCMeta):
    #pylint: disable=abstract-method
    """Target for bignum test case generation."""
    # Using .ex in this example to avoid clash with `generate_bignum_tests.py`
    target_basename = "test_suite_mpi.ex.generated"
```

Running the script will now create `test_suite_mpi.ex.generated.data`, and running with
`--list` will list the filename as a valid target.

### Adding the script to the build system

This is not required for the example, but is included here for completeness.
When adding a new script to the build system, the changes required include:
 - Adding the script to
[/tests/scripts/check-generated-files.sh](https://github.com/Mbed-TLS/mbedtls/blob/development/tests/scripts/check-generated-files.sh).
 - Adding the script to
[/scripts/make_generated_files.bat](https://github.com/Mbed-TLS/mbedtls/blob/development/scripts/make_generated_files.bat).
 - Adding calls and targets in CMake and Make for the script and its generated files.
The script will need to be called in the same places where `generate_bignum_tests.py` is
currently called.
 - Ensuring the generated files are covered by the Git ignore list.

Note: for Mbed TLS 2.28 the requirements differ, the changes required are:
 - Adding the script to
[/tests/scripts/check-generated-files.sh](https://github.com/Mbed-TLS/mbedtls/blob/development/tests/scripts/check-generated-files.sh).
 - Committing the generated files.

---
id: "mbedtls-how-to-systematically-generate-tes-complete-example-test-script"
type: "concept"
domain: "security"
title: "How to systematically generate test data: Complete example test script"
summary: "The full test script from the example snippets:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/add-test-generation.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/add-test-generation.md#complete-example-test-script"
license: "Apache-2.0"
mode: "V"
---

The full test script from the example snippets:

```python
import itertools
import sys

from typing import Iterator, List

import scripts_path # pylint: disable=unused-import
from mbedtls_dev import test_case
from mbedtls_dev import test_data_generation


class BignumTarget(test_data_generation.BaseTarget, metaclass=ABCMeta):
    #pylint: disable=abstract-method):
    """Target for bignum test case generation."""
    # Using .ex in this example to avoid clash with `generate_bignum_tests.py`
    target_basename = 'test_suite_mpi.ex.generated'


class BignumAddExample(BignumTarget):
    """Test cases for bignum addition."""
    count = 0
    test_function = "mpi_add_mpi"
    test_name = "MPI add"

    def __init__(self, val_a: int, val_b: int) -> None:
        self.val_a = val_a
        self.val_b = val_b

    def arguments(self) -> List[str]:
        # Format values as quoted hexadecimal strings, without leading 0x
        return [
            "\"{:x}\"".format(self.val_a),
            "\"{:x}\"".format(self.val_b),
            self.result()
        ]

    def description(self) -> str:
        if not self.case_description:
            self.case_description = "{} + {}".format(
                # hex() converts to a hex string with leading 0x
                hex(self.val_a),
                hex(self.val_b)
            )
        # Call description() in the parent class
        return super().description()

    def result(self) -> str:
        # Return as a quoted hexadecimal string, without leading 0x
        return "\"{:x}\"".format(self.val_a + self.val_b)

    @classmethod
    def generate_function_tests(cls) -> Iterator[test_case.TestCase]:
        # Create a list of input values
        input_values = [0, 1, 2, 123]
        # combinations_with_replacement generates a list of all unique
        # combinations, including where inputs are the same i.e. ("0", "0")
        for a_value, b_value in itertools.combinations_with_replacement(
            input_values, 2
        ):
                # Initialize a class instance with these values
                class_instance = cls(a_value, b_value)
                # Yield the TestCase object from this instance
                yield class_instance.create_test_case()


if __name__ == '__main__':
    # Pass command line arguments and a description for the script
    test_data_generation.main(sys.argv[1:], "Generate bignum tests.")
```

Running this script will create 10 test cases in `test_suite_mpi.ex.generated.data`.
The tests can then be generated and ran together with other suites by running `make test`.
To run only these tests:

```sh
$ tests/scripts/generate_bignum_ex_tests.py
$ make tests/test_suite_mpi.ex.generated
$ cd tests
$ ./test_suite_mpi.ex.generated
```

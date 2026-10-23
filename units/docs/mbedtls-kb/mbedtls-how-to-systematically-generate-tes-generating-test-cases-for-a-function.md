---
id: "mbedtls-how-to-systematically-generate-tes-generating-test-cases-for-a-function"
type: "concept"
domain: "security"
title: "How to systematically generate test data: Generating test cases for a function"
summary: "To add test cases for a function, a concrete class derived from BaseTarget must be added to the script. This class must implement all abstract methods and some attributes of BaseTarget."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/add-test-generation.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/add-test-generation.md#generating-test-cases-for-a-function"
license: "Apache-2.0"
mode: "V"
---

To add test cases for a function, a concrete class derived from `BaseTarget` must be
added to the script.
This class must implement all abstract methods and some attributes of `BaseTarget`.
The minimum set of required attributes is listed in
["Creating the function class"](#creating-the-function-class),
and the abstract methods which must be implemented are described in
["Implementing abstract BaseTarget methods](#implementing-abstract-basetarget-methods).
This class will generate test cases.
This is a [test function class](#test-function-classes).

As an example, test case generation is added for the test function `mpi_add_mpi()`.
The added class will be derived from `BignumTarget`, and can be added either to
[tests/scripts/generate_bignum_tests.py](https://github.com/Mbed-TLS/mbedtls/blob/development/tests/scripts/generate_bignum_tests.py)
or the example script described in the previous section.
This example is simplified, and will only handle valid integer inputs.
For a more complete implementation, see the `BignumAdd` class defined in
[tests/scripts/generate_bignum_tests.py](https://github.com/Mbed-TLS/mbedtls/blob/development/tests/scripts/generate_bignum_tests.py).

### Creating the function class

The class must derive from a file target class, and the following class attributes should
be set:
 - `count = 0`: this resets the test case counting mechanism.
Alternatively, to disable test case numbering in descriptions, set
`show_test_count = False`.
 - `test_function`: the test function that the class will generate cases for.
 - `test_name`: a short descriptive name for the test, this can be the same as
`test_function` or a more readable equivalent.
This is used as the start of the description line.

For the example, add the following class:

```python
class BignumAddExample(BignumTarget):
    """Test cases for bignum addition."""
    count = 0
    test_function = "mpi_add_mpi"
    test_name = "MPI add"
```

### Class initialization

Each instance of the class will represent a different test case, each with unique inputs.
To initialize an instance of the class, these inputs must be passed to the `__init__()`
constructor method.

For `mpi_add_mpi()`, two input values are required, `val_a` and `val_b`.
In this example, integers will be used as inputs and stored in the class instance.
As `int` is a multi-precision type in Python, these can be used for bignum
calculations.

For the example, add the following constructor to `BignumAddExample`:

```python
    def __init__(self, val_a: int, val_b: int) -> None:
        self.val_a = val_a
        self.val_b = val_b
```

### Implementing abstract BaseTarget methods

Test function classes must provide an implementation of all the abstract methods declared
in `BaseTarget`.

For the example, the following imports will be required:

```python
import itertools
from typing import Iterator, List
# After import scripts_path
from mbedtls_dev import test_case
```

The method `arguments()` returns the list of arguments passed to the test function.
Arguments must have the syntax expected in `.data` files, with double quotes around
arguments that are strings or hex data.
In the example, we also use an auxillary method `result()` to calculate the expected output.

For the example, add the following methods to `BignumAddExample`:

```python
    def arguments(self) -> List[str]:
        # Format input values as quoted hexadecimal strings, without leading 0x
        return [
            "\"{:x}\"".format(self.val_a),
            "\"{:x}\"".format(self.val_b),
            self.result()
        ]

    def result(self) -> str:
        # Return as a quoted hexadecimal string, without leading 0x
        return "\"{:x}\"".format(self.val_a + self.val_b)
```

The method `generate_function_tests()` handles the construction of class instances for each
unique test case, and yields `test_case.TestCase` objects from each instance.
This is a `classmethod`, which acts on the class, rather than a specific instance.
In the example, a list of strings will be used as inputs, and a test case is generated
for each possible combination.
The standard module `itertools` is used for generation of unique input combinations.

For the example, add the following method to `BignumAddExample`:

```python
    @classmethod
    def generate_function_tests(cls) -> Iterator[test_case.TestCase]:
        # Create a list of input values
        input_values = [0, 1, 2, 123]
        # combinations_with_replacement generates a list of all unique
        # combinations, including where inputs are the same i.e. (0, 0)
        for a_value, b_value in itertools.combinations_with_replacement(
            input_values, 2
        )
            # Initialize a class instance with these values
            class_instance = cls(a_value, b_value)
            # Yield the TestCase object from this instance
            yield class_instance.create_test_case()
```

### Other BaseTarget attributes and methods

The method `description()` returns a description of the test case, in the format
"`test_name` #`count` `case_description`" by default.
`case_description` is an optional description for the specific test case, which may be
explicitly passed when constructing an instance, or generated in the class.
This can be used to add context, and in the example this will be generated by overriding
the `description()` method.

For the example, add the following method to `BignumAddExample`:

```python
    def description(self) -> str:
        if not self.case_description:
            self.case_description = "{} + {}".format(
                # hex() converts to a hex string with leading 0x
                hex(self.val_a),
                hex(self.val_b)
            )
        # Call description() in the parent class
        return super().description()
```

The attribute `dependencies` is a list of build macros, which specifies the required
build config for the test case to run.
This can be set as a class attribute if always required for the test function, or set
conditionally in the constructor if dependent on the test case.

For example, the test function `mbedtls_ecp_curve_info()` takes a curve ID argument,
in the format `MBEDTLS_ECP_XXXX`.
Each test case will depend on the specified curve being enabled, and hence depend on
the macro `MBEDTLS_ECP_XXXX_ENABLED`.
This can be set in the constructor using the the following code:

```python
    def __init__(self, curve_id: str) -> None:
        self.dependencies = ["{}_ENABLED".format(curve_id)]
```

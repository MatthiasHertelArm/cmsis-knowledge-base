---
id: "mbedtls-how-to-systematically-generate-tes-extending-existing-test-classes"
type: "concept"
domain: "security"
title: "How to systematically generate test data: Extending existing test classes"
summary: "When adding test case generation for functions, there may be previously implemented classes which generate tests for similar functions. For example, the test function mpi_add_abs() is very similar to mpi_add_mpi(), but returns an absolute result."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/add-test-generation.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/add-test-generation.md#extending-existing-test-classes"
license: "Apache-2.0"
mode: "V"
---

When adding test case generation for functions, there may be previously implemented
classes which generate tests for similar functions.
For example, the test function `mpi_add_abs()` is very similar to `mpi_add_mpi()`, but
returns an absolute result.
Test structure, input format, and useful test cases may also be common across test
functions.
For example, a variety of test functions for binary operations use two inputs A and B,
and one output, and can be implemented similarly.

### Variants

For variants of a test function, inheritance can be used to reduce repetition of code.
For example, to implement the test function `mpi_add_abs()`, `BignumAddAbs` can inherit
from the `BignumAdd` class.
The necessary changes for implementing `BignumAddAbs` are then reduced:
 - `count` should be reset to 0 for the class.
 - `test_function` should be set to `mpi_add_mpi_abs`.
 - `test_name` should be set to a different name.
 -  We take the same list of inputs as the parent class, but calculate the expected result
differently.

For example, possible implementation of this class:

```python
class BignumAddAbsExample(BignumAddExample):
    """Tests for absolute variant of bignum addition."""
    count = 0
    test_function = "mpi_add_abs"
    test_name = "MPI add (abs)"

    def result(self) -> str:
        return "\"{:x}\"".format(abs(self.int_a) + abs(self.int_b))
```

These tests will then be generated with the same input values as `mpi_add_mpi`, and use
the same methods for generating descriptions and the list of arguments.

### Using abstract classes
  
Abstract classes are used to define common methods and attributes for multiple test
functions.
This can reduce repetition of code, and provide a uniform structure when adding test
generation for similar test functions.
Defined in
[tests/scripts/generate_bignum_tests.py](https://github.com/Mbed-TLS/mbedtls/blob/development/tests/scripts/generate_bignum_tests.py),
`BignumOperation` implements common attributes and methods for testing of binary bignum
operations.
This includes defining the class constructor, `arguments()`, `description()` and test
case generation methods.
By deriving from this class, tests can be added for binary bignum operations with smaller
and simpler classes.
These may only require the class attributes to be set, and the `result()` method to be
defined.

`BignumAdd` and `BignumCmp` are two examples in
[generate_bignum_tests.py](https://github.com/Mbed-TLS/mbedtls/blob/development/tests/scripts/generate_bignum_tests.py)
which derive from `BignumOperation`.

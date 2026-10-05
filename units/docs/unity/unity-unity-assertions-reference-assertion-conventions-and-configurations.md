---
id: "unity-unity-assertions-reference-assertion-conventions-and-configurations"
type: "concept"
domain: "test"
title: "Unity Assertions Reference: Assertion Conventions and Configurations"
summary: "The convention of assertion parameters generally follows this order:"
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@2b80d1a:docs/UnityAssertionsReference.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/2b80d1a/docs/UnityAssertionsReference.md#assertion-conventions-and-configurations"
license: "MIT"
mode: "V"
---

### Naming and Parameter Conventions

The convention of assertion parameters generally follows this order:

```c
TEST_ASSERT_X( {modifiers}, {expected}, actual, {size/count} )
```

The very simplest assertion possible uses only a single `actual` parameter (e.g.
a simple null check).

- `Actual` is the value being tested and unlike the other parameters in an
  assertion construction is the only parameter present in all assertion variants.
- `Modifiers` are masks, ranges, bit flag specifiers, floating point deltas.
- `Expected` is your expected value (duh) to compare to an `actual` value; it’s
  marked as an optional parameter because some assertions only need a single
  `actual` parameter (e.g. null check).
- `Size/count` refers to string lengths, number of array elements, etc.

Many of Unity’s assertions are clear duplications in that the same data type
is handled by several assertions. The differences among these are in how failure
messages are presented. For instance, a `_HEX` variant of an assertion prints
the expected and actual values of that assertion formatted as hexadecimal.

#### TEST_ASSERT_X_MESSAGE Variants

_All_ assertions are complemented with a variant that includes a simple string
message as a final parameter. The string you specify is appended to an assertion
failure message in Unity output.

For brevity, the assertion variants with a message parameter are not listed
below. Just tack on `_MESSAGE` as the final component to any assertion name in
the reference list below and add a string as the final parameter.

_Example:_

```c
TEST_ASSERT_X( {modifiers}, {expected}, actual, {size/count} )
```

becomes messageified like thus…

```c
TEST_ASSERT_X_MESSAGE( {modifiers}, {expected}, actual, {size/count}, message )
```

Notes:

- The `_MESSAGE` variants intentionally do not support `printf` style formatting
  since many embedded projects don’t support or avoid `printf` for various reasons.
  It is possible to use `sprintf` before the assertion to assemble a complex fail
  message, if necessary.
- If you want to output a counter value within an assertion fail message (e.g. from
  a loop) , building up an array of results and then using one of the `_ARRAY`
  assertions (see below) might be a handy alternative to `sprintf`.

#### TEST_ASSERT_X_ARRAY Variants

Unity provides a collection of assertions for arrays containing a variety of
types. These are documented in the Array section below. These are almost on par
with the `_MESSAGE`variants of Unity’s Asserts in that for pretty much any Unity
type assertion you can tack on `_ARRAY` and run assertions on an entire block of
memory.

```c
    TEST_ASSERT_EQUAL_TYPEX_ARRAY( expected, actual, {size/count} )
```

- `Expected` is an array itself.
- `Size/count` is one or two parameters necessary to establish the number of array
  elements and perhaps the length of elements within the array.

Notes:

- The `_MESSAGE` variant convention still applies here to array assertions. The
  `_MESSAGE` variants of the `_ARRAY` assertions have names ending with
  `_ARRAY_MESSAGE`.
- Assertions for handling arrays of floating point values are grouped with float
  and double assertions (see immediately following section).

### TEST_ASSERT_EACH_EQUAL_X Variants

Unity provides a collection of assertions for arrays containing a variety of
types which can be compared to a single value as well. These are documented in
the Each Equal section below. these are almost on par with the `_MESSAGE`
variants of Unity’s Asserts in that for pretty much any Unity type assertion you
can inject `_EACH_EQUAL` and run assertions on an entire block of memory.

```c
TEST_ASSERT_EACH_EQUAL_TYPEX( expected, actual, {size/count} )
```

- `Expected` is a single value to compare to.
- `Actual` is an array where each element will be compared to the expected value.
- `Size/count` is one of two parameters necessary to establish the number of array
  elements and perhaps the length of elements within the array.

Notes:

- The `_MESSAGE` variant convention still applies here to Each Equal assertions.
- Assertions for handling Each Equal of floating point values are grouped with
  float and double assertions (see immediately following section).

### Configuration

#### Floating Point Support Is Optional

Support for floating point types is configurable. That is, by defining the
appropriate preprocessor symbols, floats and doubles can be individually enabled
or disabled in Unity code. This is useful for embedded targets with no floating
point math support (i.e. Unity compiles free of errors for fixed point only
platforms). See Unity documentation for specifics.

#### Maximum Data Type Width Is Configurable

Not all targets support 64 bit wide types or even 32 bit wide types. Define the
appropriate preprocessor symbols and Unity will omit all operations from
compilation that exceed the maximum width of your target. See Unity
documentation for specifics.

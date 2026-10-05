---
id: "unity-unity-configuration-guide-floating-point-types"
type: "concept"
domain: "test"
title: "Unity Configuration Guide: The Options / Floating Point Types"
summary: "In the embedded world, it's not uncommon for targets to have no support for floating point operations at all or to have support that is limited to only single precision."
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@2b80d1a:docs/UnityConfigurationGuide.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/2b80d1a/docs/UnityConfigurationGuide.md#floating-point-types"
license: "MIT"
mode: "V"
---

_Part of: The Options_

In the embedded world, it's not uncommon for targets to have no support for floating point operations at all or to have support that is limited to only single precision.
We are able to guess integer sizes on the fly because integers are always available in at least one size.
Floating point, on the other hand, is sometimes not available at all.
Trying to include `float.h` on these platforms would result in an error. This leaves manual configuration as the only option.

#### `UNITY_INCLUDE_FLOAT`

#### `UNITY_EXCLUDE_FLOAT`

#### `UNITY_INCLUDE_DOUBLE`

#### `UNITY_EXCLUDE_DOUBLE`

By default, Unity guesses that you will want single precision floating point support, but not double precision.
It's easy to change either of these using the include and exclude options here.
You may include neither, either, or both, as suits your needs.
For features that are enabled, the following floating point options also become available.

_Example:_

```C
//what manner of strange processor is this?
#define UNITY_EXCLUDE_FLOAT
#define UNITY_INCLUDE_DOUBLE
```

#### `UNITY_EXCLUDE_FLOAT_PRINT`

Unity aims for as small of a footprint as possible and avoids most standard library calls (some embedded platforms don’t have a standard library!).
Because of this, its routines for printing integer values are minimalist and hand-coded.
Therefore, the display of floating point values during a failure are optional.
By default, Unity will print the actual results of floating point assertion failure (e.g. ”Expected 4.56 Was 4.68”).
To not include this extra support, you can use this define to instead respond to a failed assertion with a message like ”Values Not Within Delta”.
If you would like verbose failure messages for floating point assertions, use these options to give more explicit failure messages.

_Example:_

```C
#define UNITY_EXCLUDE_FLOAT_PRINT
```

#### `UNITY_FLOAT_TYPE`

If enabled, Unity assumes you want your `FLOAT` asserts to compare standard C floats.
If your compiler supports a specialty floating point type, you can always override this behavior by using this definition.

_Example:_

```C
#define UNITY_FLOAT_TYPE float16_t
```

#### `UNITY_DOUBLE_TYPE`

If enabled, Unity assumes you want your `DOUBLE` asserts to compare standard C doubles.
If you would like to change this, you can specify something else by using this option.
For example, defining `UNITY_DOUBLE_TYPE` to `long double` could enable gargantuan floating point types on your 64-bit processor instead of the standard `double`.

_Example:_

```C
#define UNITY_DOUBLE_TYPE long double
```

#### `UNITY_FLOAT_PRECISION`

#### `UNITY_DOUBLE_PRECISION`

If you look up `UNITY_ASSERT_EQUAL_FLOAT` and `UNITY_ASSERT_EQUAL_DOUBLE` as documented in the big daddy Unity Assertion Guide, you will learn that they are not really asserting that two values are equal but rather that two values are "close enough" to equal.
"Close enough" is controlled by these precision configuration options.
If you are working with 32-bit floats and/or 64-bit doubles (the normal on most processors), you should have no need to change these options.
They are both set to give you approximately 1 significant bit in either direction.
The float precision is 0.00001 while the double is 10-12.
For further details on how this works, see the appendix of the Unity Assertion Guide.

_Example:_

```C
#define UNITY_FLOAT_PRECISION 0.001f
```

#### `UNITY_IS_NAN` and `UNITY_IS_INF`

If your toolchain defines `isnan` and `isinf` in `math.h` as macros, nothing needs to be done. If your toolchain doesn't define these, Unity
will create these macros itself. You may override either or both of these defines to specify how you want to evaluate if a number is NaN or Infinity.

_Example:_

```C
#define UNITY_IS_NAN(n) ((n != n) ? 1 : 0)
```

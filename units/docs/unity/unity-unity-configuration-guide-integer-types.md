---
id: "unity-unity-configuration-guide-integer-types"
type: "concept"
domain: "test"
title: "Unity Configuration Guide: The Options / Integer Types"
summary: "If you've been a C developer for long, you probably already know that C's concept of an integer varies from target to target. The C Standard has rules about the int matching the register size of the target microprocessor."
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@2b80d1a:docs/UnityConfigurationGuide.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/2b80d1a/docs/UnityConfigurationGuide.md#integer-types"
license: "MIT"
mode: "V"
---

_Part of: The Options_

If you've been a C developer for long, you probably already know that C's concept of an integer varies from target to target.
The C Standard has rules about the `int` matching the register size of the target microprocessor.
It has rules about the `int` and how its size relates to other integer types.
An `int` on one target might be 16 bits while on another target it might be 64.
There are more specific types in compilers compliant with C99 or later, but that's certainly not every compiler you are likely to encounter.
Therefore, Unity has a number of features for helping to adjust itself to match your required integer sizes.
It starts off by trying to do it automatically.

#### `UNITY_EXCLUDE_STDINT_H`

The first thing that Unity does to guess your types is check `stdint.h`.
This file includes defines like `UINT_MAX` that Unity can use to learn a lot about your system.
It's possible you don't want it to do this (um. why not?) or (more likely) it's possible that your system doesn't support `stdint.h`.
If that's the case, you're going to want to define this.
That way, Unity will know to skip the inclusion of this file and you won't be left with a compiler error.

_Example:_

```C
#define UNITY_EXCLUDE_STDINT_H
```

#### `UNITY_EXCLUDE_LIMITS_H`

The second attempt to guess your types is to check `limits.h`.
Some compilers that don't support `stdint.h` could include `limits.h` instead.
If you don't want Unity to check this file either, define this to make it skip the inclusion.

_Example:_

```C
#define UNITY_EXCLUDE_LIMITS_H
```

If you've disabled both of the automatic options above, you're going to have to do the configuration yourself.
Don't worry.
Even this isn't too bad... there are just a handful of defines that you are going to specify if you don't like the defaults.

#### `UNITY_INT_WIDTH`

Define this to be the number of bits an `int` takes up on your system.
The default, if not autodetected, is 32 bits.

_Example:_

```C
#define UNITY_INT_WIDTH 16
```

#### `UNITY_LONG_WIDTH`

Define this to be the number of bits a `long` takes up on your system.
The default, if not autodetected, is 32 bits.
This is used to figure out what kind of 64-bit support your system can handle.
Does it need to specify a `long` or a `long long` to get a 64-bit value.
On 16-bit systems, this option is going to be ignored.

_Example:_

```C
#define UNITY_LONG_WIDTH 16
```

#### `UNITY_POINTER_WIDTH`

Define this to be the number of bits a pointer takes up on your system.
The default, if not autodetected, is 32-bits.
If you're getting ugly compiler warnings about casting from pointers, this is the one to look at.

_Hint:_ In order to support exotic processors (for example TI C55x with a pointer width of 23-bit), choose the next power of two (in this case 32-bit).

_Supported values:_ 16, 32 and 64

_Example:_

```C
// Choose on of these #defines to set your pointer width (if not autodetected)
//#define UNITY_POINTER_WIDTH 16
//#define UNITY_POINTER_WIDTH 32
#define UNITY_POINTER_WIDTH 64 // Set UNITY_POINTER_WIDTH to 64-bit
```

#### `UNITY_COMPARE_PTRS_ON_ZERO_ARRAY`

Define this to make all array assertions compare pointers instead of contents when a length of zero is specified. When not enabled,
defining a length of zero will always result in a failure and a message warning the user that they have tried to compare empty
arrays.

#### `UNITY_SUPPORT_64`

Unity will automatically include 64-bit support if it auto-detects it, or if your `int`, `long`, or pointer widths are greater than 32-bits.
Define this to enable 64-bit support if none of the other options already did it for you.
There can be a significant size and speed impact to enabling 64-bit support on small targets, so don't define it if you don't need it.

_Example:_

```C
#define UNITY_SUPPORT_64
```

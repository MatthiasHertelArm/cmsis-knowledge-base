---
id: "dsp-vector-q15-example"
type: "concept"
domain: "optimization"
title: "Vector: Q15 example"
summary: "Here, the Q15 value is initialized from the int value i and thus represents \\f$ i/2^{15} \\f$"
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:Documentation/Doxygen/src/vector.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/Documentation/Doxygen/src/vector.md#q15-example"
license: "Apache-2.0"
mode: "V"
---

Example with `Q15` is very similar:

The vectors are defined:

```cpp
Vector<Q15,NB> aQ15;
Vector<Q15,NB> bQ15;
Vector<Q15,NB> cQ15;
```

They are initialized:

```cpp
for(int i = 0;i< NB;i++)
{
   aQ15[i] = bQ15[i] = cQ15[i] = Q15(i);
}
```

Here, the `Q15` value is initialized from the int value `i` and thus represents \f$ i/2^{15} \f$

Some computation is done

```cpp
Vector<Q15,NB> dQ15 = aQ15 + bQ15 * cQ15;
```

The result is displayed:

```cpp
std::cout << "Result = " << dQ15 ;
```

---
id: "stream-cpp-nodes-and-classes-optional-nodes"
type: "concept"
domain: "cmsis-stream"
title: "CPP Nodes and classes: Optional nodes"
summary: "Those nodes are not included by default. They can be found in Include/cg/nodes/cpp"
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/CPPNodes.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/CPPNodes.md#optional-nodes"
license: "Apache-2.0"
mode: "V"
---

Those nodes are not included by default. They can be found in `Include/cg/nodes/cpp`

To use any of them you just need to include the header (for instance in your `AppNodes.h` file):

```C++
#include "CFFT.h"
```

### CFFT / CIFFT

Those nodes are for using the CMSIS-DSP FFT.

Template:

```C++
template<typename IN, int inputSize,
         typename OUT,int outputSize>
class CFFT;
```

Specialization provided only for `float32_t`, `float16_t`,`q15_t`.

The wrapper is copying the input buffer before doing the FFT (since CMSIS-DSP FFT is modifying the input buffer). It is normally possible to modify the input buffer even if it is in the input FIFO.

This implementation has made the choice of not touching the input FIFO with the cost of an additional copy.

Other data types can be easily added based on the current provided example. The user can just implement other specializations.

`CIFFT` is defined with class `CIFFT`.

### InterleavedStereoToMono

Deinterleave a stream of stereo samples to **one** stream of mono samples.

Template:

```C++
template<typename IN, int inputSize,
         typename OUT,int outputSize>
class InterleavedStereoToMono;
```

For specialization `q15_t` and `q31_t`, the inputs are divided by 2 before being added to avoid any overflow.

For specialization `float32_t` : The output is multiplied by `0.5f` for consistency with the fixed point version.

### MFCC

Those nodes are for using the CMSIS-DSP MFCC.

Template:

```C++
template<typename IN, int inputSize,
         typename OUT,int outputSize>
class MFCC;
```

Specializations provided for `float32_t`, `float16_t`, `q31_t` and `q15_t`.

The MFCC is requiring a temporary buffer. The wrappers are thus allocating a memory buffer during initialization of the node.

The buffer is allocated as a C++ vector. See the documentation of the MFCC in CMSIS-DSP to know more about the size of this buffer.

### NullSink

Template:

```C++
template<typename IN, int inputSize>
class NullSink: public GenericSink<IN, inputSize>
```

It is useful for development and debug. This node is doing nothing and just consuming its input.

### OverlapAndAdd

Template:

```c++
template<typename IN,int windowSize, int overlap>
class OverlapAdd: public GenericNode<IN,windowSize,IN,windowSize-overlap>
```

There are two sizes in the template arguments : `windowSize` and `overlap`.

From those size, the template is computing the number of samples consumed and produced by the node.

The implementation is generic but will only build for a type `IN` having an addition operator.

This node is using a little memory (C++ vector) of size `overlap` that is allocated during creation of the node.

This node will overlap input data by `overlap` samples and sum the common overlapping samples.

### SlidingBuffer

Template:

```C++
template<typename IN,int windowSize, int overlap>
class SlidingBuffer: public GenericNode<IN,windowSize-overlap,IN,windowSize>

```

There are two sizes in the template arguments :  `windowSize` and `overlap`.

For those size, the template is computing the number of samples consumed and produced by the node.

The implementation is generic and will work with all types.

This node is using a little memory (C++ vector) of size `overlap` allocated during creation of the node.

This node is moving a window on the input data with an overlap. The output data is the content of the window.

Note that this node is not doing any multiplication with window functions that can be found in signal processing literature. This multiplication has to be implemented in the compute graph in a separate node.

### ToComplex

Template:

```C++
template<typename IN, int inputSize,
         typename OUT,int outputSize>
class ToComplex;
```

Convert a stream of reals a b c d ... to complexes a 0 b 0 c 0 d 0 ...

The implementation is generic and does not enforce the required size constraints.

### ToReal

Template:

```C++
template<typename IN, int inputSize,typename OUT,int outputSize>
class ToReal;
```

Convert a stream of complex a 0 b 0 c 0 ... to reals a b c ...

The implementation is generic and does not enforce the required size constraints.

### Unzip

Template:

```C++
template<typename IN, int inputSize,
         typename OUT1,int output1Size,
         typename OUT2,int output2Size>
class Unzip;
```

Unzip a stream a1 a2 b1 b2 c1 c2 ...

Into 2 streams:
a1 b1 c1 ...
a2 b2 c2 ...

The implementation is generic and does not enforce the required size constraints.

### Zip

Template:

```C++
template<typename IN1, int inputSize1,
         typename IN2,int inputSize2,
         typename OUT,int outputSize>
class Zip;
```

Transform two input streams:

a1 b1 c1 ...

a2 b2 c2 ...

into one output stream:

a1 a2 b1 b2 c1 c2 ...

The implementation is generic and does not enforce the required size constraints

### Host

Those nodes are for host (Windows, Linux, Mac). They can be useful to experiment with a compute graph.

By default there is no nodes to read / write `.wav` files but you can  easily add some if needed (`dr_wav.h` is a simple way to add `.wav` reading / writing and is freely available from the web).

#### FileSink

Template

```C++
template<typename IN, int inputSize>
class FileSink: public GenericSink<IN, inputSize>
```

Write the input samples to a file. The implementation is generic and use iostream for writing the datatype.

The constructor has an additional argument : the name/path of the output file:

```C++
FileSink(FIFOBase<IN> &src, std::string name)
```

#### FileSource

Template:

```C++
template<typename OUT,int outputSize> class FileSource;
```

There is only one specialization for the `float32_t` type.

It is reading text file with one float per line and generating a stream of float.

At the end of file, 0.0f  are generated on the output indefinitely.

The constructor has an additional argument : the name/path of the input file:

```C++
FileSource(FIFOBase<float32_t> &dst,std::string name)
```

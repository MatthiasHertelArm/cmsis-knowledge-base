---
id: "stream-description-of-the-nodes-4-function-and-constant-nodes"
type: "concept"
domain: "cmsis-stream"
title: "Description of the nodes: 4 Function and constant nodes"
summary: "A Compute graph C++ wrapper is useful when the software components you use have a state that needs to be initialized in the C++ constructor, and preserved between successive calls to the run method of the wrapper."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Generic.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Generic.md#4-function-and-constant-nodes"
license: "Apache-2.0"
mode: "V"
---

A Compute graph C++ wrapper is useful when the software components you use have a state that needs to be initialized in the C++ constructor, and preserved between successive calls to the `run` method of the wrapper.

Most CMSIS-DSP functions have no state. The compute graph framework is providing some ways to easily use functions in the graph without having to write a wrapper.

This feature is relying on the nodes:

* `Unary`
  * To use an unary operator like `negate`, `inverse` ...
* `Binary`
  * To use a binary operator like `add`, `mul` ...
* `Constant`
  * Special node to be used **only** with function nodes when some arguments cannot be connected to a FIFO. For instance, with `arm_scale_f32` the scaling factor is a scalar value and a FIFO cannot be connected to this argument. The function is a binary operator but between a stream and a scalar.


All of this is explained in detail in the [simple example with CMSIS-DSP](https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/../Examples/simpledsp/README.md).

The API to create the `Unary`,`Binary` nodes are taking some arguments to customize the name of the inputs and output.

* `input_name` by default it is `"i"`
* `output_name` by default it is `"o"`
* `input_names` (when several inputs) and by default it is `["ia","ib"]`

In case of binary mode, the input names are sorted in alphabetical order. The first argument to the function is the first input in alphabetical order.

### `GenericFunction`

With the `GenericFunction` it is possible to map most pure functions (with no state) to the graph without having to write a wrapper.

Let's see how to use a C function will following prototype:

```C
void myfunc(float *       i0,
            int           nb_samples0,
            custom_type_t testVar,
            float *       i1,
            int           nb_bytes1,
            float *       o,
            int           nb_samples2,
            int           someInt,
            const char*   someStr);
```

This is a complex function with lots of arguments to demonstrate all the features of `GenericFunction`.

The function corresponds to a node with two inputs and one outputs:

* Input buffers `i0` and `i1`
* Output buffer `o`

The  size of each buffer is either given as a number of samples (for `i0` and `o`) or a number of bytes for `i1`.

In addition to those buffers, the function is taking 3 additional arguments:

* An argument `testVar` with a custom type
* An int `someInt`
* A string `someStr`

As with any other nodes, we define the input and outputs and the additional arguments of the node in the graph.

```python
class MyFunction(GenericFunction):
    def __init__(self, length_a
                     , length_b
                     , length_c):
        GenericFunction.__init__(self,"myfunc",
           THIS SECTION IS DESCRIBED BELOW
            )


        self.addInput("ia",CType(F32),length_a)
        self.addInput("ib",CType(F32),length_b)
        self.addOutput("o",CType(Q15),length_c)

        self.addVariableArg("testVar")
        self.addLiteralArg(4,"5")

```

Since IOs are always in alphabetical order, `"ia"` corresponds to `i0`, `ib` to `i1`.

We define 3 additional arguments in the same order:

* A variable `"testVar`"
* An int with value '4' and a string with value "5"

Now we need to define how those node arguments are mapped to the C function.

For this, we pass an array to the `GenericFunction` that describes how the node IO and arguments are mapped to the C arguments.

```C
GenericFunction.__init__(self,"myfunc",
            ["ia"
            ,ArgLength("ia")
            , 0
            ,"ib"
            ,ArgLength("ib",sample_unit=False)
            ,"o"
            ,ArgLength("o")
            ,1,2
            ])
```

The array contains:

* The name of a port (`"ia"`,`"ib"`,`"o"`). It will be mapped to a FIFO. A pointer or a constant when the FIFO argument is connected to a constant node.
* `ArgLength` is the length of the FIFO either in number of samples or number of bytes (`sample_unit=false`)
* An int is the index of an additional argument in the order they have been created with `addVariableArg` and `addLiteralArg`
  * `testVar` is the additional argument created first and has index `0`
  * The int with value `4` is the second argument and has index `1`
  * And finally the string has index `2`
  * The int and the string are mapped at the end of the function since the list is ending with `1,2`

The above definition will generate the following function call:

```C
float* i0;
float* i1;
q15_t* o2;
i0=fifo0.getReadBuffer(7);
i1=fifo1.getReadBuffer(7);
o2=fifo2.getWriteBuffer(5);
myfunc(i0,7,testVar,i1,sizeof(float)*7,o2,5,4,"5");
```

A pure function cannot generate an error. If you need error handling, you need a C++ wrapper.

In this example, the int `someInt` has been introduced as a separate argument. It won't be visible in the graphical representation and cannot be connected to a `Constant` node.

Another way to introduce this argument would be to define a FIFO of type `int` and connect it to a `Constant` node in the graph. 

The generated code would be:

```C
float* i0;
float* i1;
q15_t* o3;
i0=fifo0.getReadBuffer(7);
i1=fifo1.getReadBuffer(7);
o3=fifo2.getWriteBuffer(5);
myfunc(i0,7,testVar,i1,sizeof(float)*7,o3,5,SomeConst,"5");
cgStaticError = 0;
```

The only difference is that the output is now named `o3` instead of `o2` because the virtual FIFO has been counted in the list of FIFO. But since it is connected to a `Constant` node, the FIFO has not been generated in the code. Instead we have the constant `SomeConst` replacing the `4` value at the end.

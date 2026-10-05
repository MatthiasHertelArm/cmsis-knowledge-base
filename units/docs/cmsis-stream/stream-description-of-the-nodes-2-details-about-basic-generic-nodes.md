---
id: "stream-description-of-the-nodes-2-details-about-basic-generic-nodes"
type: "concept"
domain: "cmsis-stream"
title: "Description of the nodes: 2 Details about basic generic nodes"
summary: "When you define a new kind of node, it must inherit from one of those classes. Those classes are providing the methods addInput and/or addOutput to define new inputs / outputs."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Generic.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Generic.md#2-details-about-basic-generic-nodes"
license: "Apache-2.0"
mode: "V"
---

When you define a new kind of node, it must inherit from one of those classes. Those classes are providing the methods `addInput` and/or `addOutput` to define new inputs / outputs.

A new kind of node is generally defined as:

```python
class ProcessingNode(GenericNode):
    def __init__(self,name,theType,inLength,outLength):
        GenericNode.__init__(self,name)
        self.addInput("i",theType,inLength)
        self.addOutput("o",theType,outLength)

    @property
    def typeName(self):
        return "ProcessingNode"
```

The method `typeName` from the parent class must be overridden and provide the name of the `C++` wrapper to be used for this node.

The object constructor is defining the inputs / outputs : number of samples and datatype.

The object constructor is also defining the name used to identity this node in the generated code (so it must be a valid C variable name).

`GenericSink` is only providing the `addInput` function.

`GenericSource` is only providing the `addOutput` function

`GenericNode` is providing both.

You can use each function as much as you want to create several inputs and / or several outputs for a node.

The `Generic` node constructors are accepting another named argument : `identified` and by default it is `True`. This value is used when the code generation is using the `nodeIdentification` mode.

This value can also be changed on the node after creation.

When this value is `True`, the node will be accessible from outside the scheduler using the provided scheduler API in the `C` generated header.

See the [simple](https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/../Examples/simple/README.md) example for more explanation about how to define a new node.

### 2.1 Methods

The constructor of the node is using the `addInput` and/or `addOutput` to define new IOs.

```python
def addInput(self,name,theType,theLength):
```

* `name` is the name of the input. It will becomes a property of the Python object so it must not conflict with existing properties. If `name` is, for instance, `"i"` then it can be accessed with `node.i` in the code
* `theType` is the datatype of the input. It must inherit from `CGStaticType` (see below for more details about defining the types)
* `theLength` is the amount of **samples** consumed by this input at each execution of the node in synchronous mode. In asynchronous mode it would correspond to the average case.

```python
def addOutput(self,name,theType,theLength):
```

* `name` is the name of the output. It will becomes a property of the Python object so it must not conflict with existing properties. If `name` is, for instance, `"o"` then it can be accessed with `node.o` in the code
* `theType` is the datatype of the output. It must inherit from `CGStaticType` (see below for more details about defining the types)
* `theLength` is the amount of **samples** produced by this output at each execution of the node in synchronous mode. In asynchronous mode it would correspond to the average case.

```python
@property
def typeName(self):
    return "ProcessingNode"
```

This method defines the name of the C++ class implementing the wrapper for this node.

A FIFO constraint can come from an IO. Some software components may allocate the memory for the buffers they use for their inputs or outputs. Or they may have to use a specific memory buffer already defined in the system.

It is possible to define those constraint on an input or on an output. The constraint will be inherited by the FIFO connected to this input or output. A buffer constraint can be defined with:

```python
def setBufferConstraint(self,name=None,mustBeArray=True,assignedByNode=True,canBeShared=True)
```

For instance you may define a constraint on an output by writing:

```python
self.o.setBufferConstraint(name="Test",mustBeArray=True,assignedByNode=False)
```

Any FIFO connected to this `o` output will have to use the `Test` buffer and will have to be scheduled in such a way that this buffer is used as an array.

The meaning of the arguments is:

* `name` : C code to access the buffer. It can be the name of a global variable. of a variable passed as argument of the scheduler, a function call returning an address ...
* `mustBeArray` : True if the buffer can only be used as an array (and not as a real FIFO)
* `assignedByNode` :True if buffer is allocated by the node during the node creation (in the node constructors). In that case, the `name` argument is useless. The FIFO will be initialized with a `nullptr` buffer when creating the scheduler. Then the node will set the FIFO buffer during its construction
*  `canBeShared` True if the buffer may be shared with other FIFOs. The logic to decide if the buffer can really be shared is complex. It depends on the scheduling, the compatibility of this buffer with other ones etc ...

### 2.2 Datatypes

Datatypes for the IOs are inheriting from `CGStaticType`.

Currently there are 3 classes defined in the project:

* `CType` for the standard CMSIS-DSP types like `q15_t`, `float32_t` ...
* `CStructType` for a C struct
* `PythonClassType` to create structured datatype for the Python scheduler

#### 2.2.1 CType

You create such a type with `CType(id)` where `id` is one of the constant coming from the Python wrapper:

* F64
* F32
* F16
* Q31
* Q15
* Q7
* UINT32
* UINT16
* UINT8
* SINT32
* SINT16
* SINT8

For instance, to define a `float` type for an IO you can use `CType(F32)`

If you want to use the CMSIS-DSP naming (because you are using CMSIS-DSP), you can pass the option `cmsis_dsp=True`:

```python
CType(F32,cmsis_dsp=True)
```

The datatype will be `float32_t` in the generated code and as consequence you'll need to include the `"arm_math.h"` header.

#### 2.2.2 CStructType

The constructor has the following definition

```python
def __init__(self,name,size_in_bytes): 
```

* `name` is the name of the C struct
* `size_in_bytes` is the size of the C struct. It should take into account padding. It is used when the compute graph memory optimization is used since size of the datatype is needed. 

#### 2.2.3 PythonClassType

```python
def __init__(self,python_name)
```

In Python, there is no `struct`. This datatype is mapped to an object. Object have reference type. Compute graph FIFOs are assuming a value type semantic.

As consequence, in Python side you should never copy those structs since it would copy the reference. You should instead copy the members of the struct and they should be scalar values.

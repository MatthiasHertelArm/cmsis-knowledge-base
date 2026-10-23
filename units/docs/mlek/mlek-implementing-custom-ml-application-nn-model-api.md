---
id: "mlek-implementing-custom-ml-application-nn-model-api"
type: "concept"
domain: "edge-ai"
title: "Implementing custom ML application: NN Model API"
summary: "The Model, which refers to neural network model, is an abstract class wrapping the underlying ML framework API."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/customizing.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/customizing.md#nn-model-api"
license: "Apache-2.0"
mode: "V"
---

The Model, which refers to neural network model, is an abstract class wrapping the underlying ML framework API.

The `Model` class has two subclasses which are themselves abstract: `TflmModel` and `EtModel`.
These subclasses implement the Model API methods for TensorFlow Lite Micro and ExecuTorch frameworks respectively.

The Model API provides methods to perform common operations such as framework initialization, inference
execution, accessing input, and output tensor objects.

To use this abstraction, import the `Model.hpp` header or either `TflmModel.hpp` or `EtModel.hpp` if you prefer.

> **Convention:**  Each ML use-case must have an extension of the `TflmModel` or `EtModel` class depending on the framework that model uses.

### Common API functions

Member functions defined in the `Model` base class:

| Method name              | Visibility | Description                                                                                                                                                            |
|--------------------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `GetInputTensor`         | Public     | Returns the pointer to the model's input tensor.                                                                                                                       |
| `GetOutputTensor`        | Public     | Returns the pointer to the model's output tensor                                                                                                                       |
| `GetType`                | Public     | Returns the model's data type                                                                                                                                          |
| `GetInputShape`          | Public     | Return the pointer to the model's input shape                                                                                                                          |
| `GetOutputShape`         | Public     | Return the pointer to the model's output shape.                                                                                                                        |
| `GetNumInputs`           | Public     | Return the number of input tensors the model has.                                                                                                                      |
| `GetNumOutputs`          | Public     | Return the number of output tensors the model has.                                                                                                                     |
| `LogTensorInfo`          | Public     | Logs the tensor information to `stdout` for the given tensor pointer. Includes: Tensor name, tensor address, tensor type, tensor memory size, and quantization params. |
| `LogInterpreterInfo`     | Public     | Logs the interpreter information to stdout.                                                                                                                            |
| `Init`                   | Public     | Initializes the TensorFlow Lite Micro framework, allocates require memory for the model.                                                                               |
| `IsInited`               | Public     | Checks if this model object has been initialized.                                                                                                                      |
| `IsDataSigned`           | Public     | Checks if the model uses signed data type.                                                                                                                             |
| `ContainsEthosUOperator` | Public     | Checks if the model contains an operator delegated to Ethos-U (TensorFlow Lite Micro only - always returns false for ExecuTorch)                                       |
| `RunInference`           | Public     | Runs the inference, so invokes the interpreter.                                                                                                                        |
| `GetComputeBuffer`       | Public     | Returns pointer to memory region to be used for tensors allocations.                                                                                                   |
| `GetModelBuffer`         | Public     | Returns the pointer to the NN model data array.                                                                                                                        |
| `GetBackendData`         | Public     | Returns backend data specific to the underlying ML Framework.                                                                                                          |

### TensorFlow Lite Micro models

Additional member functions in the `TflmModel` subclass:

| Method name        | Visibility | Description                                   |
|--------------------|------------|-----------------------------------------------|
| `GetOpResolver`    | Protected  | Get the ops resolver.                         |
| `EnlistOperations` | Protected  | Add all the operators required for the model. |

> For models using TensorFlow Lite Micro implementation of the protected virtual
> methods:
>
> ```C++
> virtual const tflite::MicroOpResolver& GetOpResolver() = 0;
> virtual bool EnlistOperations() = 0;
> ```
>
> Network models have different sets of operators.  For TensorFlow Lite models, these operators must be registered
> at runtime with the `tflite::MicroMutableOpResolver` object in the `EnlistOperations` method.
>
> **Note:** Please see the image classification use case for examples of model file implementations:
>   ```commandline
>     source/lib/mlek/fwk/tflm
>       ├── ...
>       ├── MobileNetModel.hpp
>       ├── ...
>       └── MobileNetModel.cc

### ExecuTorch models

Additional member functions in the `EtModel` subclass:

| Method name           | Visibility | Description                                                |
|-----------------------|------------|------------------------------------------------------------|
| `LogMemoryUsage`      | Public     | Print current memory usage to the output.                  |
| `PrepareInputTensors` | Protected  | Prepared model input tensors. Called by the `Init` method. |

> For ExecuTorch models, any operators that fall back to CPU must be included at build time by using the CMake
> `generate_pte_ops_lib` function, and these ops must exist in the ATen Core Operator Set.
>
> Network models can require different size of activation buffer that is returned as
> tensor arena memory by the `GetComputeBuffer` method.
>
> **Note:** Please see the image classification use case for examples of model file implementations:
>
>   ```commandline
>       source/lib/mlek/fwk/executorch
>       ├── ...
>       ├── MobileNetModel.hpp
>       ├── ...
>   ```

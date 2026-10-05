---
id: "mlek-implementing-custom-ml-application-implementing-custom-nn-model"
type: "concept"
domain: "edge-ai"
title: "Implementing custom ML application: Implementing custom NN model"
summary: "The two supported ML frameworks, TensorFlow Lite Micro and ExecuTorch, have different requirements when defining models."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/customizing.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/customizing.md#implementing-custom-nn-model"
license: "Apache-2.0"
mode: "V"
---

The two supported ML frameworks, TensorFlow Lite Micro and ExecuTorch, have different requirements when defining models.

### TensorFlow Lite Micro models

Before inference could be run with a custom NN model, TensorFlow Lite Micro framework must learn about the operators, or
layers, included in the model. You must register operators using the `MicroMutableOpResolver` API.

The *Ethos-U* code samples project has an abstraction around TensorFlow Lite Micro API (see [NN model API](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./customizing.md#nn-model-api)).
Create `HelloWorldTflmModel.hpp` under `source/lib/mlek/fwk/tflm`,
extend Model abstract class, and then declare the required methods.

For example:

```C++
#ifndef HELLOWORLDTFLMMODEL_HPP
#define HELLOWORLDTFLMMODEL_HPP

#include "TflmModel.hpp"

namespace arm::app::fwk::tflm {

class HelloWorldTflmModel: public TflmModel {
  protected:
    /** @brief   Gets the reference to op resolver interface class. */
    const tflite::MicroOpResolver& GetOpResolver() override;

    /** @brief   Adds operations to the op resolver instance. */
    bool EnlistOperations() override;

  private:
    /* Maximum number of individual operations that can be enlisted. */
    static constexpr int ms_maxOpCnt = 5;

    /* A mutable op resolver instance. */
    tflite::MicroMutableOpResolver<ms_maxOpCnt> m_opResolver;
  };

} /* namespace arm::app::fwk::tflm */

#endif /* HELLOWORLDTFLMMODEL_HPP */
```

Place the `HelloWorldTflmModel.cc` file alongside the header and define the methods there. Include
`HelloWorldTflmModel.hpp` created earlier.

> **Note:** The `TflmModel.hpp` included in the header provides access to TensorFlow Lite Micro's operation resolver API.

Please refer to `source/lib/mlek/fwk/tflm` for examples of classes that have been defined for TensorFlow Lite Micro models,
for example `MobileNetModel.hpp` and `MobileNetModel.cc`.

If you are using a TensorFlow Lite model compiled with Vela, it is important to add a custom *Ethos-U* operator to the
operators list.

The following example shows how to add the custom *Ethos-U* operator with the TensorFlow Lite Micro framework.
When defined, `ARM_NPU` excludes the code if the application was built without NPU support.

For example:

```C++
#include "HelloWorldTflmModel.hpp"
#include "mlek/log/log_macros.h"

bool arm::app::HelloWorldTflmModel::EnlistOperations() {

#if defined(ARM_NPU)
    if (kTfLiteOk == this->m_opResolver.AddEthosU()) {
        info("Added %s support to op resolver\n",
            tflite::GetString_ETHOSU());
    } else {
        printf_err("Failed to add Arm NPU support to op resolver.");
        return false;
    }
#endif /* ARM_NPU */

    return true;
}
```

To minimize the memory footprint of the application, we advise you to only register operators that are used by the NN
model.

### ExecuTorch models

Unlike TensorFlowLiteMicro, the ExecuTorch framework does not require runtime registration of operators.

As a result, a class representing an ExecuTorch model can be minimal, or if preferred it is possible to
use an instance of the `EtModel` class in your use case instead:

```C++
#ifndef HELLOWORLDETMODEL_HPP
#define HELLOWORLDETMODEL_HPP

#include "EtModel.hpp"

namespace arm::app::fwk::et {

class HelloWorldEtModel: public EtModel {} /* namespace arm::app::fwk::et */

#endif /* HELLOWORLDETMODEL_HPP */
```

However, it can still be useful to define a class for your model to capture specific metadata,
such as labels for input/output tensor indices.
See `source/lib/mlek/fwk/executorch/MobileNetModel.hpp` for an example of this.

### Using GetModelPointer and GetModelLen methods

These functions are generated in the C++ file containing the neural network model as an array.
This logic for generation of the C++ array from the `.tflite` or `.pte` file needs to be defined
in the `usecase.cmake` file for this `HelloWorld` example.
In the root of `source/app/use_case/hello_world`, create a file called `usecase.cmake` and add the following lines to it:

```cmake
# Generate model file
USER_OPTION(${${use_case}_MODEL_PATH}
            "NN model tflite path"
            "Path-to-your-model"
            FILEPATH)

generate_model_code(
        MODEL_PATH ${${use_case}_MODEL_PATH}
        DESTINATION ${SRC_GEN_DIR}
        EXPRESSIONS ${EXTRA_MODEL_CODE}
        NAMESPACE   "arm" "app" "hello_world")
```

Use the `${use-case}_MODEL_PATH` CMake configuration parameter to include custom model in the generation or
compilation process. Please refer to: [Build options](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./building.md#build-options) for further information.

For more details on `usecase.cmake`, refer to: [Building options](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./building.md#build-options).

For details on code generation flow in general, refer to: [Automatic file generation](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./building.md#automatic-file-generation).

The model data is read during the `Model::Init` method execution.
For implementation details, refer to the framework-specific `Model` subclasses:
 - `source/lib/mlek/fwk/tflm/TflmModel.cc`
 - `source/lib/mlek/fwk/executorch/EtModel.cc`

`Model::Init` requires references to the model and the compute buffer memory regions as well as their sizes.
During the build, a source file will be generated at `<build>/generated/hello_world/src/<model_file_name>.cc`
which contains the model data represented as an array.
It also provides two methods, `arm::app::hello_world::GetModelPointer()` and `arm::app::hello_world::GetModelLen()`
that return a pointer to the model as well as its size in memory.
The file generated is automatically added to the compilation.

We must also define a compute buffer for inference to use.  At the top of `MainLoop.cc`, add:

```c++
namespace arm {
namespace app {
    namespace hello_world {

        extern uint8_t* GetModelPointer();
        extern size_t GetModelLen();
    } /* namespace hello_world */

    static uint8_t activationBuf[ACTIVATION_BUF_SZ] ACTIVATION_BUF_ATTRIBUTE;
} /* namespace app */
} /* namespace arm */
```

These functions and compute buffer can now be used in the `Model.Init` call.

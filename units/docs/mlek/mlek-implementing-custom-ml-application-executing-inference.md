---
id: "mlek-implementing-custom-ml-application-executing-inference"
type: "concept"
domain: "edge-ai"
title: "Implementing custom ML application: Executing inference"
summary: "To run an inference successfully, you must use:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/customizing.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/customizing.md#executing-inference"
license: "Apache-2.0"
mode: "V"
---

To run an inference successfully, you must use:

- A TensorFlow Lite or the PTE (for ExecuTorch) model file,
- An extended Model class,
- A place to add the code to invoke inference,
- A main loop function,
- And some input data.

For the `hello_world` example below the input array is not populated. However, for real-world deployment this data must
either be read from an on-board device or be prepared in the form of C++ sources and baked into the application before
compilation.

For example, the image classification application requires extra build steps to generate C++ sources from the provided
images with `generate_images_code` CMake function.

> **Note:** Check that the input data type for your NN model and input array data type are the same. For example,
> generated C++ sources for images store image data as a `uint8` array. For models that were quantized to an `int8` data
> type, convert the image data to `int8` correctly *before* inference execution. Converting asymmetric data to symmetric
> data involves positioning the zero value. In other words, subtracting an offset for `uint8` values. Please check the
> image classification application source for the code example, such as the `ConvertUint8ToInt8` function.

The following code adds inference invocation to the main loop function:

```c++
#include "hal.h"
#include "mlek/log/log_macros.h"
#include "HelloWorldTflmModel.hpp"
/* Or, if your model is ExecuTorch-based: */
//#include "HelloWorldEtModel.hpp"

namespace arm {
namespace app {
    namespace hello_world {

        extern uint8_t* GetModelPointer();
        extern size_t GetModelLen();
    } /* namespace hello_world */

    static uint8_t activationBuf[ACTIVATION_BUF_SZ] ACTIVATION_BUF_ATTRIBUTE;
} /* namespace app */
} /* namespace arm */

void MainLoop()
{
    printf("Hello world!");

    arm::app::fwk::tflm::HelloWorldTflmModel model;
    /* Or, if your model is ExecuTorch-based: */
    // arm::app::fwk::et::HelloWorldEtModel model;

    /* Define memory regions */
    arm::app::fwk::iface::MemoryRegion modelMem{arm::app::hello_world::GetModelPointer(),
                                                arm::app::hello_world::GetModelLen()};
    arm::app::fwk::iface::MemoryRegion computeMem{arm::app::activationBuf,
                                                  sizeof(arm::app::activationBuf)};

    /* Load the model. */
    if (!model.Init(computeMem, modelMem)) {
        printf_err("Failed to initialise model\n");
        return;
    }

    /* Populate input tensors here */
    // Your-custom-code;

    /* Run inference */
    model.RunInference();

    /* Read or post-process output here */
    const size_t tensorSz = outputTensor->Bytes();
    const uint8_t * outputData = outputTensor->GetData<uint8>();
    // Your-custom-code;
}
```

The code snippet has several important blocks:

- Creating `HelloWorldTflmModel` (or `HelloWorldEtModel`) object and initializing it.

```C++
  arm::app::fwk::tflm::HelloWorldTflmModel model;
  /* Or, if your model is ExecuTorch-based: */
  // arm::app::fwk::et::HelloWorldEtModel model;

  /* Define memory regions */
  arm::app::fwk::iface::MemoryRegion modelMem{arm::app::hello_world::GetModelPointer(),
                                              arm::app::hello_world::GetModelLen()};
  arm::app::fwk::iface::MemoryRegion computeMem{arm::app::activationBuf,
                                                sizeof(arm::app::activationBuf)};

  /* Load the model. */
  if (!model.Init(computeMem, modelMem)) {
      printf_err("Failed to initialise model\n");
      return;
  }
```

- Getting pointers to allocated input and output tensors.

  ```C++
  auto outputTensor = model.GetOutputTensor();
  auto inputTensor = model.GetInputTensor();
  ```
- Running inference

  ```C++
  model.RunInference();
  ```

- Reading inference results: Data and data size from the output tensor.
  We assume that the output layer has a `uint8` data type.

  ```C++
  const size_t tensorSz = outputTensor->Bytes();
  const uint8_t * outputData = outputTensor->GetData<uint8>();
  ```

To add profiling for the *Ethos-U*, include a `Profiler.hpp` header and invoke both `StartProfiling` and
`StopProfiling` around inference execution.

For example:

```C++
Profiler profiler{"Inference"};

profiler.StartProfiling();
model.RunInference();
profiler.StopProfiling();

profiler.PrintProfilingResult();
```

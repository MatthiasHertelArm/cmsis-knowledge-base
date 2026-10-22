---
id: "tflm-offline-memory-plan-via-nonpersist-usage"
type: "concept"
domain: "edge-ai"
title: "Offline Memory Plan Via NonpersistentMemoryPlannerShim: Usage"
summary: "The more efficient memory plan above can be represented by the following C++ struct."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@bd621c2:tensorflow/lite/micro/docs/offline_memory_plan.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/offline_memory_plan.md#usage"
license: "Apache-2.0"
mode: "V"
---

The more efficient memory plan above can be represented by the following C++
struct.

```cc
const struct BufferPlan kOfflineNonPersistentBufferPlan = {
  .buffer_count = 9,
  .buffer_plan_entries = {
    [0] = { .offset = 0 },
    [1] = { .offset = 400 },
    [2] = { .offset = 801 },
    [3] = { .offset = 400 },
    [4] = { .offset = 811 },
    [5] = { .offset = 601 },
    [6] = { .offset = 814 },
    [7] = { .offset = 601 },
    [8] = { .offset = 801 },
   }
};
```

Then you can create a NonPersistentBufferPlannerShim and provide it to the
Interpreter such as below

```cc
// The arena includes both persistent buffers and non-persistent buffers. 
constexpr int kArenaSize = 2*1048;
uint8_t tensor_arena[kArenaSize];

tflite::NonPersistentMemoryPlannerShim planner(&kOfflineNonPersistentBufferPlan);

tflite::MicroAllocator * allocator = tflite::MicroAllocator::Create(
  tensor_arena, arena_size, &planner);

tflite::MicroInterpreter interpreter(model, op_resolver, allocator);
```

---
id: "stream-dynamic-data-flow-prepareforrunning"
type: "concept"
domain: "cmsis-stream"
title: "Dynamic Data Flow: prepareForRunning"
summary: "The method prepareForRunning is needed to check if the node execution is going to be possible."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Async.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Async.md#prepareforrunning"
license: "Apache-2.0"
mode: "V"
---

The method `prepareForRunning` is needed to check if the node execution is going to be possible.

Inside this function, you have access to methods like:

* `willOverflow`
* `willUnderflow`

In case of several IOs, you may also have:

* `willOverflow1`
* `willOverflow2` 

etc ...

The functions have an interface like:

```C++
bool willOverflow(int nb = outputSize)
```

or

```C++
bool willUnderflow(int nb = inputSize)
```

The `inputSize` and `outputSize` are coming from the template arguments. So, by default the node is using the parameters of the static compute graph.

You may want to read or write more or less than what is defined in the static compute graph. But it must be coherent with the `run` function.

If you use `willOverflow(4)` to check if you can write `4` samples in the output in the `prepareForRunning` function, then in the `run` function you must access to the write buffer by requesting `4` samples with `getWriteBuffer(4)`

If you don't want to write or read on an IO, just don't use the function `getWriteBuffer` and `getReadBuffer` in the `run` function.

It is also possible to use the functions `willOverflow`, `willUnderflow` in the `run` function. It can be used to avoid calling the `getReadBuffer` and `getWriteBuffer` when you nevertheless want to run the node although some FIFOs cannot be used.

**WARNING**: You are responsible for checking if a FIFO is going to underflow or overflow **before** using `getReadBuffer` or `getWriteBuffer`.

If the `getReadBuffer` and `getWriteBuffer` are causing an underflow or overflow of the FIFO, you'll have memory corruptions and the compute graph will no more work.

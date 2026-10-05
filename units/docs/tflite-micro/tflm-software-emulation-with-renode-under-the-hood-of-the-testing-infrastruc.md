---
id: "tflm-software-emulation-with-renode-under-the-hood-of-the-testing-infrastruc"
type: "concept"
domain: "edge-ai"
title: "Software Emulation with Renode: Under the hood of the Testing Infrastructure"
summary: "Describe how we wait for a particular string on the UART. Some pointers into the robot files as well as any relevant documentation from Renode."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/renode.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/renode.md#under-the-hood-of-the-testing-infrastructure"
license: "Apache-2.0"
mode: "V"
---

Describe how we wait for a particular string on the UART. Some pointers into the
robot files as well as any relevant documentation from Renode.

A test failure is the absence of a specific string on the UART so the test will
wait for a specific timeout period (configured in the .robot) file before
failing.

 * What this means in practice is that a failing test will take longer to finish
   than a test that passes.

 * If needed, an optimization on this would be to have a specific failure
   message as well so that both success and failure can be detected quickly.

# Running a non-test Binary with Renode

Renode can also be used to run and debug binaries interactively. For example,
to debug `kernel_add_test` on Bluepill platform, run Renode:

```
tensorflow/lite/micro/tools/make/downloads/renode/renode
```
and issue following commands:
```
# Create platform
include @tensorflow/lite/micro/testing/bluepill_nontest.resc
# Load ELF file
sysbus LoadELF @gen/bluepill_x86_64_default/bin/kernel_add_test
# Start simulation
start

# To run again:
Clear
include @tensorflow/lite/micro/testing/bluepill_nontest.resc
sysbus LoadELF @gen/bluepill_cortex-m3_default/bin/keyword_benchmark
start

```

To make repeat runs a bit easier, you can put all the commands into a
single line (up arrow will show the last command in the Renode terminal):
```
Clear; include @tensorflow/lite/micro/testing/bluepill_nontest.resc; sysbus LoadELF @gen/bluepill_x86_64_default/bin/kernel_add_test; start
```

You can also connect GDB to the simulation.
To do that, start the GDB server in Renode before issuing the `start` command:
```
machine StartGdbServer 3333
```
Then you can connect from GDB with:
```
target remote localhost:3333
```

For further reference please see the [Renode documentation](https://renode.readthedocs.io/en/latest/).

# Useful External Links for Renode and Robot Documentation

 * [Testing with Renode](https://renode.readthedocs.io/en/latest/introduction/testing.html?highlight=robot#running-the-robot-test-script)

 * [Robot Testing Framework on Github](https://github.com/robotframework/robotframework). For someone new to
   the Robot Framework, the documentation  can be a bit hard to navigate, so
   here are some links that are relevant to the use of the Robot Framework with
   Renode for TFLM:

   * [Creating Test Data](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#creating-test-data)
     section of the user guide.

   * Renode-specific additions to the Robot test description format are in the
     [RobotFrameworkEngine directory](https://github.com/renode/renode/tree/master/src/Renode/RobotFrameworkEngine). For example,

       * [Start Emulation](https://github.com/renode/renode/blob/master/src/Renode/RobotFrameworkEngine/RenodeKeywords.cs#L41-L42)
       * [Wait For Line On Uart](https://github.com/renode/renode/blob/master/src/Renode/RobotFrameworkEngine/UartKeywords.cs#L62-L63)
     is where `Wait For Line On Uart` is defined.

   * Some documentation for all the [Standard Libraries](http://robotframework.org/robotframework/#standard-libraries)
     that define commands such as:

       * [Remove File](http://robotframework.org/robotframework/latest/libraries/OperatingSystem.html#Remove%20File)
       * [List Files In Directory](https://robotframework.org/robotframework/latest/libraries/OperatingSystem.html#List%20Files%20In%20Directory)

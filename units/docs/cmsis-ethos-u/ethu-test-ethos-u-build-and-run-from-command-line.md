---
id: "ethu-test-ethos-u-build-and-run-from-command-line"
type: "concept"
domain: "edge-ai"
title: "Test-Ethos-U: Build and run from command line"
summary: "By default, the committed Vela models target Ethos-U85 with 256 MACs."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:examples/Test-Ethos-U/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/examples/Test-Ethos-U/README.md#build-and-run-from-command-line"
license: "Apache-2.0"
mode: "V"
---

By default, the committed Vela models target Ethos-U85 with 256 MACs.

To build this configuration execute:

```sh
cbuild Test-Ethos-U85.csolution.yml --active SSE-320-U85 --update-rte --packs
```

Once the application image is available, run it using the following command:

```sh
FVP_Corstone_SSE-320 -f Board/Corstone-320/fvp_config_u85.txt -a out/Test-Ethos-U/SSE-320-U85/Debug/Test-Ethos-U.hex
```

The test reports the detected NPU configuration followed by one result for each model.
A successful run ends with:

```text
[PASS] hello_world (max delta 0 LSB)
[PASS] tiny_cnn (max delta 0 LSB)

2 of 2 checks passed
TEST RESULT: PASS
```

For instructions on using the example with the Keil Studio IDE, see
[Tutorial: Create an Ethos-U application](https://arm-software.github.io/CMSIS_Ethos_U/latest/integration).

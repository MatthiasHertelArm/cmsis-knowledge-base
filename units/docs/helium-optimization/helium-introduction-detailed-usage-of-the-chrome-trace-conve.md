---
id: "helium-introduction-detailed-usage-of-the-chrome-trace-conve"
type: "concept"
domain: "optimization"
title: "Introduction: FVP/AVH/IPX model TARMAC Trace post-processing / Detailed Usage of the Chrome Trace Converter with Audiomark on AVH"
summary: "Part of: FVP/AVH/IPX model TARMAC Trace post-processing"
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:Performance_analysis/ml-dsp-front-end-optimization-with-helium.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/Performance_analysis/ml-dsp-front-end-optimization-with-helium.md#detailed-usage-of-the-chrome-trace-converter-with-audiomark-on-avh"
license: "Apache-2.0"
mode: "V"
---

_Part of: FVP/AVH/IPX model TARMAC Trace post-processing_

In order to demonstrate the complete process of converting tarmac data to Chrome format, we will utilize the Audiomark Beamformer (ABF) analysis as a baseline.

- Corstone-300 ABF Binary generation

The audiomark application and unit tests ARM binaries generation steps are  detailled [here](https://github.com/eembc/audiomark/blob/main/platform/cmsis/README.md)

Under `./platform/cmsis`, issue the **cbuild** command from the CMSIS toolbox to start the compilation stage. Here we are selecting VHT-Corstone-300 target and ARM Compiler 6.22.

```shell
cbuild --context testabf.Release+VHT-Corstone-300 audiomark.csolution.yml --update-rte  --toolchain AC6@6.22
```

This will generate an image in `out/testabf/VHT-Corstone-300/Release/testabf.axf`

- Tarmac log generation:

We're using the standard Corstone-300 VHT command line and use an extra plugin providing TARMAC log capabilities.

```shell
VHT_MPS3_Corstone_SSE-300 -f model_config_sse300.txt  out/testabf/VHT-Corstone-300/Release/testabf.axf --plugin TarmacTrace.so -C TRACE.TarmacTrace.trace-file=testabf_sse300.tarmac
```

 - Tarmac log JSON conversion:

After extracting the symbol file from the application image, we're using the `arm_tarmac_2_chrometracing.py` for converting the TARMAC log into JSON.

 ```shell
 # symbol file extraction
fromelf -s out/testabf/VHT-Corstone-300/Release/testabf.axf > testabf_sse300.sym
# conversion
python arm_tarmac_2_chrometracing.py testabf_sse300.sym testabf_sse300.tarmac testabf_sse300.json
 ```

 - ABF timeline visualization

 Open chrome://tracing URL under Google Chrome and click on the `Load` button for loading the generate JSON


 

Tracing tool commands help will be displayed by clicking on the `?` button.

 

Clicking on the `Self time` arrow allow to sort the top consuming functions.
The duration assume a core running at 1MHz clock, so 100ms represent an equivalent of 100K cycles.

It is important to re-emphasize that AVH/FVP **do not provide cycle accurate measurements**.


Prebuilt Corstone-300 ABF images and tarmac logs are provided as examples in the [tools/examples/](https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/Performance_analysis/tools/examples/) folder.

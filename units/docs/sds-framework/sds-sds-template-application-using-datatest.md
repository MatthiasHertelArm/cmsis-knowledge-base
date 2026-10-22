---
id: "sds-sds-template-application-using-datatest"
type: "concept"
domain: "test"
title: "SDS Template Application: Using DataTest"
summary: "The DataTest project validates the communication channel."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@c18efee:documentation/template.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/template.md#using-datatest"
license: "Apache-2.0"
mode: "V"
---

The **DataTest** project validates the communication channel.

### Recording/playback on Hardware Target

1. Select the `STM32F746G-DISCO` target with Project `DataTest` and Build Type `Debug` to record/playback SDS data files.
2. Configure the file `datatest.sdsio.yml` for your selected [communication interface](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/utilities.md#interface).
3. Start the [SDSIO-Server](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/utilities.md#sdsio-server) with `python sdsio-server.py -c datatest.sdsio.yml`.
4. Build and Run the application.
5. Use [SDS-Check](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/utilities.md#sds-check) to verify correctness of the recording.

**Recording**

Activate recording from the SDSIO-Server by pressing the `R` key. To stop recording, press the `S` key.
Alternatively, recording can be started or stopped by pressing the user button on the board.

This run should generate the files `Test_In.1.sds` and `Test_Out.1.sds` in the folder `datatest/SDS Recordings`. The `DataTest` project is configured to record 1000 data records at an interval of 10 ms.

To verify correctness of the recording using the SDS-Check utility, use the following commands:

```bash
python sds-check.py -i Test_In.1.sds
python sds-check.py -i Test_Out.1.sds
```

When recording is started again, new files with different names are created: `Test_In.2.sds` and `Test_Out.2.sds`.

!!! Note
    - Refer to [Theory of Operation - Filenames](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/theory.md#filenames) for more information.

**Playback**

Activate the playback from the SDSIO-Server by pressing the `P` key.

This run should read the `Test_In.0.sds` file and generate the `Test_Out.0.p.sds` file in the folder `datatest/SDS Recordings`. The `Test_Out.0.sds` file generated during recording is identical to `Test_Out.0.p.sds`, which is generated in playback mode.

To verify correctness of the recording using the SDS-Check utility, use the following command:

```bash
python sds-check.py -i Test_Out.0.p.sds
```

Compare the output files `Test_Out.0.sds` and `Test_Out.0.p.sds` with any program that can compare binary files. If the communication is correct, the files should be identical.

### Configure Bandwidth for DataTest

The **DataTest** project uses a fixed algorithm to verify the communication interface. In `datatest/algorithm_config.h`, you can configure bandwidth and interval to match the requirements of the algorithm under test.

### Playback on Simulation Model

1. Select the target `SSE-300-U55` (or `SSE-320-U85`) with Project `DataTest` and Build Type `Debug` to play back SDS data files.
2. [Build and Run](https://github.com/ARM-software/SDS-Framework/tree/main/template/sdsio/fvp/README.md) the application.
3. Use [SDS-Check](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/utilities.md#sds-check) to verify correctness of the files recorded during playback.

By default, the Template application includes a `datatest.sdsio.yml` configuration file that specifies playback of the `Test_In.0.sds` file,
while new output recordings are stored in the `Test_Out.0.p.sds` file.

Refer to [SDSIO control file: `sdsio.yml`](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/utilities.md#sdsio-control-file-sdsioyml) for more information and configuration of playback files using the [`play:`](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/utilities.md#play) node.

To verify correctness of the recording using the SDS-Check utility, use the following command:

```bash
python sds-check.py -i Test_Out.0.p.sds
```

!!! Tip
    Compare the output files `Test_Out.0.sds` and `Test_Out.0.p.sds` with any program that can compare binary files. If the communication is correct, the files should be identical.

!!! Note
    - Recording mode is not available when using Simulation Model.

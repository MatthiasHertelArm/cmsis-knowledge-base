---
id: "stream-sds-nodes-sds-recorder-2"
type: "concept"
domain: "cmsis-stream"
title: "SDS Nodes: SDS Recorder"
summary: "If the type is defined using argument the_type, the .yml file is not needed anymore."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/PythonSDS.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/PythonSDS.md#sds-recorder"
license: "Apache-2.0"
mode: "V"
---

```Python
accelerometerRec = SDSRecorder("accelerometerRecorder",NB_SAMPLES,
                                sds_yml_file="Accelerometer.sds.yml",
                                sds_connection="recConn_accelerometer"
                              )
```

If the type is defined using argument `the_type`, the `.yml` file is not needed anymore.

`NB_SAMPLES` is the number of samples even when the type is not specified and is implicitely `uint8_t`. In that case, the `.yml` file is used to compute the sample size in bytes.

`sds_yml_file` is the `.yml` file that describes the sensor.
`sds_connection` is the C variable (of type `sds_recorder_cg_connection_t`) used to communicate with the recorder.

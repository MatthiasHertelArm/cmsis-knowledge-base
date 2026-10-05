---
id: "stream-sds-nodes-sds-sensor-2"
type: "concept"
domain: "cmsis-stream"
title: "SDS Nodes: SDS Sensor"
summary: "Example of use with an accelerometer sensor:"
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/PythonSDS.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/PythonSDS.md#sds-sensor"
license: "Apache-2.0"
mode: "V"
---

Example of use with an accelerometer sensor:

```Python
accelerometer = SDSSensor("accelerometerSensor",NB_SAMPLES,
                          sds_yml_file="Accelerometer.sds.yml",
                          sds_connection="sensorConn_accelerometer")
```

The first field is the name of the node like with any other CMSIS-Stream node.

The second field is the number of samples produced by this node. 

Note that this is not sensor related but application related. The user must decides (depending on the use case), how many samples are required from this sensor in the CMSIS-Stream graph.

In synchronous mode, sensor nodes are blocking until the number of samples has been received. It must be taken into account when there are several sensors in a graph.

Note that in general in a CMSIS-Stream node, the number of samples is given in the output type unit. Here the output type is `uint8_t` but the number of samples is not the number of bytes. The sensor `.yml` file is used to compute the size of a sensor sample in bytes and the node will generate the right number of bytes.


`sds_yml_file` is the `.yml` file that describes the sensor.
`sds_connection` is the C variable (of type `sds_sensor_cg_connection_t`) used to communicate with the sensor.


### With drift compensation

With drift compensation, you need to specify the function to use for drift compensation (using `drift_delegate`) and the C variable containing the data required by this function (using `drift_delegate_data`)

```Python
accelerometer = SDSSensor("accelerometerSensor",ACC_BLOCK,
                          sds_yml_file="Accelerometer.sds.yml",
                          sds_connection="sensorConn_accelerometer",
                          drift_delegate=delegate,
                          drift_delegate_data=delegate_data)
```

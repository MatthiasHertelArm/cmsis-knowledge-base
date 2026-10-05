---
id: "stream-sds-nodes-use-from-outside-of-the-scheduler"
type: "concept"
domain: "cmsis-stream"
title: "SDS Nodes: Use from outside of the scheduler"
summary: "To use the SDS nodes, you need to initialize some sds_sensor_cg_connection_t and sds_recorder_cg_connection_t structures and pass them to the scheduler and the nodes."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/CPPSDS.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/CPPSDS.md#use-from-outside-of-the-scheduler"
license: "Apache-2.0"
mode: "V"
---

To use the SDS nodes, you need to initialize some `sds_sensor_cg_connection_t` and `sds_recorder_cg_connection_t` structures and pass them to the scheduler and the nodes.

One possibility is to define a datastructure containing this information and pass this datastructure to the scheduler:

```C
typedef struct {
sds_sensor_cg_connection_t *sensorConn_accelerometer;
sds_recorder_cg_connection_t *recConn_accelerometer;
} demoContext_t;
```

A variable should be defined with this type:

```C
demoContext_t demoContext;
```

Then the scheduler could be called with:

```C
nbIterations = demo_scheduler(&error,&demoContext);
```

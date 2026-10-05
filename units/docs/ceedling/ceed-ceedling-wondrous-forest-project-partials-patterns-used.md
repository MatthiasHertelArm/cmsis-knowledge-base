---
id: "ceed-ceedling-wondrous-forest-project-partials-patterns-used"
type: "concept"
domain: "test"
title: "Ceedling Wondrous Forest Project: Partials Patterns Used"
summary: "Ceedling Wondrous Forest Project: Partials Patterns Used"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/snapshot/examples/wondrous_forest/README.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/snapshot/examples/wondrous_forest/#partials-patterns-used"
license: "MIT"
mode: "V"
---

| Test File               | Pattern                                                       |
|-------------------------|---------------------------------------------------------------|
| TestTemperatureSensor.c | `TEST_PARTIAL_ALL_MODULE` — public + private functions        |
| TestHumiditySensor.c    | `TEST_PARTIAL_ALL_MODULE` + `PARTIAL_LOCAL_VAR()`             |
| TestLightSensor.c       | `TEST_PARTIAL_PUBLIC_MODULE` + `MOCK_PARTIAL_PRIVATE_MODULE`  |
| TestSoilMoisture.c      | `TEST_PARTIAL_ALL_MODULE` + `PARTIAL_LOCAL_VAR()`             |
| TestAlertManager.c      | `TEST_PARTIAL_ALL_MODULE` + traditional mock alongside        |
| TestEventQueue.c        | `TEST_PARTIAL_ALL_MODULE` + file-scope static access          |
| TestForestMonitor.c     | `TEST_PARTIAL_PUBLIC_MODULE` + `MOCK_PARTIAL_PRIVATE_MODULE`  |
| TestSensorHal.c         | Traditional — HAL has no private statics                      |
| TestUartDriver.c        | Traditional — UART driver has no private statics              |

---

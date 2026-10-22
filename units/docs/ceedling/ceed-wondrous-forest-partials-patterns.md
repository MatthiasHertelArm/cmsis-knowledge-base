---
id: "ceed-wondrous-forest-partials-patterns"
type: "concept"
domain: "test"
title: "`wondrous_forest`: Partials patterns"
summary: "Each sensor module uses a different Partials pattern, making the project a comprehensive reference:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/getting-started/example-projects/wondrous-forest.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/getting-started/example-projects/wondrous-forest/#partials-patterns"
license: "MIT"
mode: "V"
---

Each sensor module uses a different Partials pattern, making the project a
comprehensive reference:

| Test file               | Pattern                                                      |
|-------------------------|--------------------------------------------------------------|
| TestTemperatureSensor.c | `TEST_PARTIAL_ALL_MODULE` — public + private functions       |
| TestHumiditySensor.c    | `TEST_PARTIAL_ALL_MODULE` + `PARTIAL_LOCAL_VAR()`            |
| TestLightSensor.c       | `TEST_PARTIAL_PUBLIC_MODULE` + `MOCK_PARTIAL_PRIVATE_MODULE` |
| TestSoilMoisture.c      | `TEST_PARTIAL_ALL_MODULE` + `PARTIAL_LOCAL_VAR()`            |
| TestAlertManager.c      | `TEST_PARTIAL_ALL_MODULE` + traditional mock alongside       |
| TestEventQueue.c        | `TEST_PARTIAL_ALL_MODULE` + file-scope static access         |
| TestForestMonitor.c     | `TEST_PARTIAL_PUBLIC_MODULE` + `MOCK_PARTIAL_PRIVATE_MODULE` |
| TestSensorHal.c         | Traditional — HAL has no private statics                     |
| TestUartDriver.c        | Traditional — UART driver has no private statics             |

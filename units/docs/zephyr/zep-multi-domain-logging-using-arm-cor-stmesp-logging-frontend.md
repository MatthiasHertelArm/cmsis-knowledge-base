---
id: "zep-multi-domain-logging-using-arm-cor-stmesp-logging-frontend"
type: "concept"
domain: "debug"
title: "Multi-domain logging using ARM Coresight STM: STMESP Logging frontend"
summary: "log_frontend API is implemented. Custom frontend assumes that all required operations are executed in the context of the logging macro call. It is also assumed that frontend provides the timestamp."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/logging/cs_stm.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/logging/cs_stm.rst"
license: "Apache-2.0"
mode: "V"
---

log_frontend API is implemented. Custom frontend assumes that all required operations are executed in the context of the logging macro call. It is also assumed that frontend provides the timestamp. Frontend utilizes a fact that there are multiple STMESP register sets and use multiple sets to avoid locking context. The atomically incremented channel counter is used to pick unique STMESP set and
whole message is written to that STMESP. Limited pool of sets is used leaving most of channels for
other purposes.


### Early logging


STMESP cannot be used before STM or ETR/TPIU is setup. In order to support early logging,
before infrastructure is ready a dedicated RAM buffer is used to which data is written. When
STM infrastructure readiness is notified (`log_frontend_stmesp_etr_ready`) then RAM buffer
content is written to STMESP. Early logging is applicable only to the core which owns and configures
Coresight infrastructure (e.g. in case of NRF54H20 it is the Secure core).


### Trace points


There may be cases when logging is too slow (even though it is very fast). For cases like that a dedicated `trace point` API is added. It is extremely fast because it is just a single
write to one STMESP register. There are 2 functions in the API:

* `log_frontend_stmesp_tp` - It accepts single argument - index. Index is between
  0 and 65280.
* `log_frontend_stmesp_tp_d32` - It accepts two arguments - index and user data.
  Index is between 0 and 65280. User data is 32 bit word.

It takes less than 100 ns to log a single trace point on NRF54H20 and it is approx. 7 times faster than the fastest log message.

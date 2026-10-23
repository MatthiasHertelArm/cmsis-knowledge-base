---
id: "ethu-driver-performance-monitoring-unit-pmu"
type: "concept"
domain: "edge-ai"
title: "Driver: Performance Monitoring Unit (PMU)"
summary: "The driver exposes the Ethos-U PMU through pmu_ethosu.h. The API supports a 64-bit cycle counter and programmable event counters. Ethos-U55 and Ethos-U65 builds provide four event counters; Ethos-U85 builds provide eight."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:documentation/doxygen/driver/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/documentation/doxygen/driver/src/main.md#performance-monitoring-unit-pmu"
license: "Apache-2.0"
mode: "V"
---

The driver exposes the Ethos-U PMU through `pmu_ethosu.h`. The API supports a
64-bit cycle counter and programmable event counters. Ethos-U55 and Ethos-U65
builds provide four event counters; Ethos-U85 builds provide eight. Use
ETHOSU_PMU_Get_NumEventCountersForDrv() when code must work with more than
one Ethos-U target or with a multi-variant build.

The target-specific `enum ethosu_pmu_event_type` lists the supported events.
They include NPU and MAC activity or stalls, weight-decoder and activation-output
activity, memory transactions and stalls, latency ranges, and ECC events. The
available event names differ between Ethos-U55/U65 and Ethos-U85. Use the
symbolic enum values with
ETHOSU_PMU_Set_EVTYPER(); do not program hardware
event numbers directly.

### Monitoring AXI transaction latency

On Ethos-U55 and Ethos-U65, `PMCAXI_CHAN.AXI_CNT_SEL` selects one of the
outstanding transaction counters listed under
Ethos-U55 and Ethos-U65, and
`PMCAXI_CHAN.CH_SEL` selects the AXI channel to monitor. The
`ETHOSU_PMU_AXI_LATENCY_*` events count transactions matching both selections.
Other AXI PMU events, such as accepted or completed transactions, data beats,
and stalls, are reported per AXI port rather than per outstanding transaction
counter.

The main API groups are:

| API Function | Description |
|---|---|
| ETHOSU_PMU_Enable(), ETHOSU_PMU_Disable() | Enable or disable the PMU |
| ETHOSU_PMU_Get_NumEventCounters(), ETHOSU_PMU_Get_NumEventCountersForDrv() | Get the number of counters for the compile-time NPU or a specific driver |
| ETHOSU_PMU_Set_EVTYPER(), ETHOSU_PMU_Get_EVTYPER() | Select an event |
| ETHOSU_PMU_CYCCNT_Reset(), ETHOSU_PMU_EVCNTR_ALL_Reset() | Reset counters |
| ETHOSU_PMU_CNTR_Enable(), ETHOSU_PMU_CNTR_Disable() | Enable or disable counters |
| ETHOSU_PMU_Get_CCNTR(), ETHOSU_PMU_Get_EVCNTR() | Read counters |
| ETHOSU_PMU_Get_CNTR_OVS(), ETHOSU_PMU_Set_CNTR_OVS(), ETHOSU_PMU_Set_CNTR_IRQ_Enable(), ETHOSU_PMU_Set_CNTR_IRQ_Disable() | Handle overflow |

Counter masks use `ETHOSU_PMU_CNT1_Msk` and the other event-counter masks, plus
`ETHOSU_PMU_CCNT_Msk` for the cycle counter. Enabling the PMU requests NPU power;
disabling it releases that request, so always pair the two operations.

Override ethosu_inference_begin() to select and
reset events immediately before an inference, and override
ethosu_inference_end() to read the counters and
disable the PMU afterward. These callbacks receive the same `user_arg` that was
passed to ethosu_invoke_v3() or
ethosu_invoke_async(), which can identify where the
results should be stored. PMU measurements are hardware observations; compare
them with Vela compiler estimates, but do not treat the estimates as
cycle-accurate measurements.

### Interpreting PMU events

The Technical Reference Manual for each NPU provides the event encoding and a hardware-level description of what each event counts:

- [Ethos-U55 TRM: `PMU_EVTYPER0..3`](https://support.arm.com/documentation/102420/latest/Programmers-model/Register-page-PMU/PMU-EVTYPER0-----PMU-EVTYPER3) (Table 4-81 in PDF version).
- [Ethos-U65 TRM: `PMU_EVTYPER0..3`](https://support.arm.com/documentation/102023/latest/Programmers-model/Register-page-PMU/PMU-EVTYPER0-----PMU-EVTYPER3) (Table 4-79 in PDF version)
- [Ethos-U85 TRM: PMU_COUNTERS register summary](https://support.arm.com/documentation/102685/latest/Programmers-model/Register-sets-for-NPU-control/PMU-COUNTERS-register-summary) - `PMEVTYPER0..7` and the `EV_TYPE` tables.

Use the event descriptions together with the following guidelines:

- `ETHOSU_PMU_NPU_ACTIVE` counts cycles in which the NPU is running, while
  `ETHOSU_PMU_NPU_IDLE` counts cycles in which it is stopped. Use these events or
  the dedicated cycle counter as the baseline when comparing inferences.
- MAC, activation-output (AO), and weight-decoder (WD) activity events show when
  the corresponding engine is doing useful work. A high stall count relative to
  its activity count points to the resource named by the stall event as a likely
  bottleneck.
- Memory transaction events count accepted or completed requests. Data-beat
  events measure transferred data, and stall events show backpressure from the
  memory system or a configured outstanding-transaction limit.
- Latency events count transactions whose latency reaches the named threshold.
  Compare the threshold counts with the total-transaction event to determine how
  much traffic experiences long latency.
- ECC events indicate corrected or uncorrected memory errors and should normally
  remain zero.

Event counters are 32-bit and can overflow during a long measurement. Check
ETHOSU_PMU_Get_CNTR_OVS() when this is possible.
Because only four or eight events can be measured at once, collect additional
events in repeated runs with identical model, input, memory, and system settings.

### PMU example

The following example counts NPU-active and NPU-idle events and records the NPU
cycle count for one inference. Pass a pointer to `struct pmu_results` as the
`user_arg` to ethosu_invoke_v3() or
ethosu_invoke_async(). The callbacks use
ETHOSU_PMU_Get_NumEventCountersForDrv() so the same pattern can be extended
with additional events on targets that provide more counters.

```c
#include "ethosu_driver.h"
#include "pmu_ethosu.h"

#define PMU_EXAMPLE_EVENT_COUNT 2U

static const enum ethosu_pmu_event_type pmu_events[PMU_EXAMPLE_EVENT_COUNT] = {
    ETHOSU_PMU_NPU_ACTIVE,
    ETHOSU_PMU_NPU_IDLE,
};

struct pmu_results {
    uint64_t cycle_count;
    uint32_t event_count[PMU_EXAMPLE_EVENT_COUNT];
    uint32_t num_events;
};

void ethosu_inference_begin(struct ethosu_driver *drv, void *user_arg)
{
    struct pmu_results *results = (struct pmu_results *)user_arg;
    uint32_t num_events = ETHOSU_PMU_Get_NumEventCountersForDrv(drv);

    if (num_events > PMU_EXAMPLE_EVENT_COUNT) {
        num_events = PMU_EXAMPLE_EVENT_COUNT;
    }
    results->num_events = num_events;

    ETHOSU_PMU_Enable(drv);
    ETHOSU_PMU_CYCCNT_Reset(drv);
    ETHOSU_PMU_EVCNTR_ALL_Reset(drv);

    for (uint32_t i = 0; i < num_events; ++i) {
        ETHOSU_PMU_Set_EVTYPER(drv, i, pmu_events[i]);
        ETHOSU_PMU_CNTR_Enable(drv, 1UL << i);
    }

    ETHOSU_PMU_PMCCNTR_CFG_Set_Start_Event(drv, ETHOSU_PMU_NPU_ACTIVE);
    ETHOSU_PMU_PMCCNTR_CFG_Set_Stop_Event(drv, ETHOSU_PMU_NPU_IDLE);
    ETHOSU_PMU_CNTR_Enable(drv, ETHOSU_PMU_CCNT_Msk);
}

void ethosu_inference_end(struct ethosu_driver *drv, void *user_arg)
{
    struct pmu_results *results = (struct pmu_results *)user_arg;

    results->cycle_count = ETHOSU_PMU_Get_CCNTR(drv);
    for (uint32_t i = 0; i < results->num_events; ++i) {
        results->event_count[i] = ETHOSU_PMU_Get_EVCNTR(drv, i);
    }

    ETHOSU_PMU_Disable(drv);
}
```

---
id: "drv-mci-uhs-i-tuning"
type: "concept"
domain: "drivers"
title: "MCI UHS-I Tuning"
summary: "Host-controller tuning operations and results."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
license: "Apache-2.0"
mode: "V"
---

Host-controller tuning operations and results.


Call ARM_MCI_Control with **control** = ARM_MCI_UHS_TUNING_OPERATION.
Set **arg** to one of the phase codes ARM_MCI_UHS_TUNING_ABORT, ARM_MCI_UHS_TUNING_START,
or ARM_MCI_UHS_RETUNING_START.

These operations return an execution status, call ARM_MCI_Control with
**control** = ARM_MCI_UHS_TUNING_RESULT and check returned value against
ARM_MCI_UHS_TUNING_DONE, ARM_MCI_UHS_TUNING_CONTINUE, or ARM_MCI_UHS_TUNING_ERROR.

UHS-I tuning is performed iteratively until a valid sampling point is found or an error occurs.

Use this order of commands:

1. Start tuning operation using ARM_MCI_UHS_TUNING_OPERATION with ARM_MCI_UHS_TUNING_START
2. Transfer tuning block
3. Inspect the result using ARM_MCI_UHS_TUNING_RESULT

Repeat steps 2 and 3 until the tuning result is ARM_MCI_UHS_TUNING_DONE or an error occurs.

**Note:** A data CRC error may identify an invalid sampling point and shall not be reported through the
      ordinary transfer-error event.

**Example:**
```
volatile uint32_t MCI_Events;

void MCI_SignalEvent_Callback (uint32_t event) {
  // Save current event
  MCI_Events |= event;
}

// Tune Sampling Clock
void mci_tune_sampling_clock(void) {
  int32_t status;
  uint8_t buf[64U];
  uint32_t step = 40U;
  uint32_t r1 = 0U;

  // Start tuning operation
  if (MCIdrv->Control(ARM_MCI_UHS_TUNING_OPERATION, ARM_MCI_UHS_TUNING_START) != ARM_DRIVER_OK) {
    return;
  }

  while(step--) {
    // Setup transfer
    status = MCIdrv->SetupTransfer(buf, 1U, 64U, ARM_MCI_TRANSFER_READ|ARM_MCI_TRANSFER_BLOCK);
    if (status != ARM_DRIVER_OK) {
      break;
    }

    // Clear previous events
    MCI_Events = 0;

    // Transfer tuning block
    status = MCIdrv->SendCommand(19, 0U, ARM_MCI_RESPONSE_SHORT|ARM_MCI_RESPONSE_CRC|ARM_MCI_TRANSFER_DATA, &r1);
    if (status == ARM_DRIVER_OK) {
      // Wait for event
      while ((MCI_Events & ARM_MCI_EVENT_TRANSFER_COMPLETE) == 0U);

      // Check the tuning result
      status = MCIdrv->Control(ARM_MCI_UHS_TUNING_RESULT, 0U);

      if (status == ARM_MCI_UHS_TUNING_DONE) {
        // Tuning completed successfully
        return;
      }
      if (status == ARM_MCI_UHS_TUNING_ERROR) {
        // Tuning error occurred
        break;
      }
    }
  }
  // Tuning failed
  MCIdrv->Control(ARM_MCI_UHS_TUNING_OPERATION, ARM_MCI_UHS_TUNING_ABORT);
}
```

---
id: "threadx-chapter-4-description-of-threadx-s-tx-thread-entry-exit-notify"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Description of ThreadX Services: tx_thread_entry_exit_notify"
summary: "Notify application upon thread entry and exit"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter4.md#tx-thread-entry-exit-notify"
license: "MIT"
mode: "V"
---

Notify application upon thread entry and exit

### Prototype

```c
UINT tx_thread_entry_exit_notify(
    TX_THREAD *thread_ptr,
    VOID (*entry_exit_notify)(TX_THREAD *, UINT));
```

### Description

This service registers a notification callback function that is called whenever the specified thread is entered or exits. The processing of the notification callback is defined by the application.

> **Note:** The application's thread entry/exit notification callback is not allowed to call any ThreadX API with a suspension option.

### Parameters

- *thread_ptr*: Pointer to previously created thread.
- *entry_exit_notify*: Pointer to application's thread entry/exit notification function. The second parameter to the entry/exit notification function designates whether an entry or exit is present. The value **TX_THREAD_ENTRY** (0x00) indicates the thread was entered, while the value **TX_THREAD_EXIT** (0x01) indicates the thread was exited. If this value is **TX_NULL**, notification is disabled.

### Return Values

- **TX_SUCCESS** (0x00) Successful registration of the thread entry/exit notification function.
- **TX_THREAD_ERROR** (0x0E) Invalid thread pointer.
- **TX_FEATURE_NOT_ENABLED** (0xFF) The system was compiled with notification capabilities disabled.

### Allowed From

Initialization, threads, timers, and ISRs

### Preemption Possible

No

### Example

```c
TX_THREAD my_thread;
/* Register the "my_entry_exit_notify" function for monitoring
the entry/exit of the thread "my_thread." */
status = tx_thread_entry_exit_notify(&my_thread,
    my_entry_exit_notify);

/* If status is TX_SUCCESS the entry/exit notification function was
successfully registered. */
void my_entry_exit_notify(TX_THREAD *thread_ptr, UINT condition)
{
    /* Determine if the thread was entered or exited. */
    if (condition == TX_THREAD_ENTRY)
        /* Thread entry! */
    else if (condition == TX_THREAD_EXIT)
        /* Thread exit! */
}
```

### See Also

- [Thread Services](#Thread_Services)

---
id: "threadx-chapter-3-functional-components-of-interrupts-2"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of ThreadX SMP: Interrupts"
summary: "Fast response to asynchronous events is the principal function of real-time, embedded applications. The application knows such an event is present through hardware interrupts."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter3.md#interrupts"
license: "MIT"
mode: "V"
---

Fast response to asynchronous events is the principal function of real-time, embedded applications. The application knows such an event is present through hardware interrupts. 

An interrupt is an asynchronous change in processor execution. Typically, when an interrupt occurs, the processor saves a small portion of the current execution on the stack and transfers control to the appropriate interrupt vector. The interrupt vector is basically just the address of the routine responsible for handling the specific type interrupt. The exact interrupt handling procedure is processor specific. 

### Interrupt Control 
The *tx_interrupt_control* service allows applications to enable and disable interrupts. The previous interrupt enable/disable posture is returned by this service. It is important to mention that interrupt control only affects the currently executing program segment. For example, if a thread disables interrupts, they only remain disabled during execution of that thread. 

> **Warning:** A Non-Maskable Interrupt (NMI) is an interrupt that cannot be disabled by the hardware. Such an interrupt may be used by ThreadX SMP applications. However, the application's NMI handling routine is not allowed to use ThreadX SMP context management or any API services. ThreadX SMP Managed Interrupts

ThreadX SMP provides applications with complete interrupt management. This management includes saving and restoring the context of the interrupted execution. In addition, ThreadX SMP allows certain services to be called from within Interrupt Service Routines (ISRs). The following is a list of ThreadX SMPservices allowed from application ISRs:

- tx_block_allocate 
- tx_block_pool_info_get 
- tx_block_pool_prioritize 
- tx_block_pool_performance_info_get 
- tx_block_pool_performance_system_info_get 
- tx_block_release 
- tx_byte_pool_info_get 
- tx_byte_pool_performance_info_get 
- tx_byte_pool_performance_system_info_get 
- tx_byte_pool_prioritize 
- tx_event_flags_info_get 
- tx_event_flags_get 
- tx_event_flags_set 
- tx_event_flags_performance_info_get 
- tx_event_flags_performance_system_info_get 
- tx_event_flags_set_notify 
- tx_interrupt_control 
- tx_mutex_performance_info_get 
- tx_mutex_performance_system_info_get 
- tx_queue_front_send 
- tx_queue_info_get 
- tx_queue_performance_info_get 
- tx_queue_performance_system_info_get 
- tx_queue_prioritize 
- tx_queue_receive 
- tx_queue_send 
- tx_semaphore_get 
- tx_queue_send_notify 
- tx_semaphore_ceiling_put 
- tx_semaphore_info_get 
- tx_semaphore_performance_info_get 
- tx_semaphore_performance_system_info_get 
- tx_semaphore_prioritize 
- tx_semaphore_put 
- tx_thread_identify 
- tx_semaphore_put_notify 
- tx_thread_entry_exit_notify 
- tx_thread_info_get 
- tx_thread_resume 
- tx_thread_performance_info_get 
- tx_thread_performance_system_info_get 
- tx_thread_stack_error_notify 
- tx_thread_wait_abort 
- tx_time_get 
- tx_time_set 
- tx_timer_activate 
- tx_timer_change 
- tx_timer_deactivate 
- tx_timer_info_get 
- tx_timer_performance_info_get 
- tx_timer_performance_system_info_get

> **Warning:** Suspension is not allowed from ISRs. Therefore, the **wait_option** parameter for all ThreadX SMP service calls made from an ISR must be set to **TX_NO_WAIT**.

### ISR Template 
To manage application interrupts, several ThreadX SMP utilities must be called in the beginning and end of application ISRs. The exact format for interrupt handling varies between ports. Review the ***readme_threadx.txt*** file on the distribution disk for specific instructions on managing ISRs.

The following small code segment is typical of most ThreadX SMP managed ISRs. In most cases, this processing is in assembly language.

**_application_ISR_vector_entry**:  
; Save context and prepare for  
; ThreadX SMP use by calling the ISR  
; entry function.  
CALL **_tx_thread_context_save**  

; The ISR can now call ThreadX SMP  
; services and its own C functions  

; When the ISR is finished, context  
; is restored (or thread preemption)  
; by calling the context restore  
; function. Control does not return!  
JUMP **_tx_thread_context_restore**

### High-frequency Interrupts  
Some interrupts occur at such a high frequency that saving and restoring full context upon each interrupt would consume excessive processing bandwidth. In such cases, it is common for the application to have a small assembly language ISR that does a limited amount of processing for a majority of these high-frequency interrupts. 

After a certain point in time, the small ISR may need to interact with ThreadX SMP. This is accomplished by calling the entry and exit functions described in the above template. 

### Interrupt Latency  
ThreadX SMP locks out interrupts over brief periods of time. The maximum amount of time interrupts are disabled is on the order of the time required to save or restore a thread's context.

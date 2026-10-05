---
id: "threadx-chapter-1-introduction-to-threadx-threadx-smp-benefits"
type: "concept"
domain: "rtos"
title: "Chapter 1: Introduction to ThreadX SMP: ThreadX SMP Benefits"
summary: "Using ThreadX SMP provides many benefits to embedded applications. Of course, the primary benefit rests in how embedded application threads are allocated processing time."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter1.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter1.md#threadx-smp-benefits"
license: "MIT"
mode: "V"
---

Using ThreadX SMP provides many benefits to embedded applications. Of course, the primary benefit rests in how embedded application threads are allocated processing time.

### Automatic Load Balancing

ThreadX SMP provides automatic load balancing (thread execution across available cores), which makes utilizing multicore processors as easy as possible.

### Improved Responsiveness

Prior to real-time kernels like ThreadX SMP, most embedded applications allocated processing time with a simple control loop, usually from within the C _main_ function. This approach is still used in very small or simple applications. However, in large or complex applications, it is not practical because the response time to any event is a function of the worst case processing time of one pass through the control loop.

Making matters worse, the timing characteristics of the application change whenever modifications are made to the control loop. This makes the application inherently unstable and difficult to maintain and improve on.

ThreadX SMP provides fast and deterministic response times to important external events. ThreadX SMP accomplishes this through its preemptive, priority-based scheduling algorithm, which allows a higher-priority thread to preempt an executing lower-priority thread. As a result, the worst-case response time approaches the time required to perform a context switch. This is not only deterministic, but it is also extremely fast.

### Software Maintenance

The ThreadX SMP kernel enables application developers to concentrate on specific requirements of their application threads without having to worry about changing the timing of other areas of the application. This feature also makes it much easier to repair or enhance an application that utilizes ThreadX SMP.

### Increased Throughput

A possible work-around to the control loop response time problem is to add more polling. This improves the responsiveness, but it still doesn't guarantee a constant worst-case response time and does nothing to enhance future modification of the application. Also, the processor is now performing even more unnecessary processing because of the extra polling. All of this unnecessary processing reduces the overall throughput of the system.

An interesting point regarding overhead is that many developers assume that multithreaded environments like ThreadX SMP increase overhead and have a negative impact on total system throughput. But in some cases, multithreading actually reduces overhead by eliminating all of the redundant polling that occurs in control loop environments. The overhead associated with multithreaded kernels is typically a function of the time required for context switching. If the context switch time is less than the polling process, ThreadX SMP provides a solution with the potential of less overhead and more throughput. This makes ThreadX SMP an obvious choice for applications that have any degree of complexity or size.

### Processor Isolation

ThreadX SMP provides a robust processor independent interface between the application and the underlying processor. This allows developers to concentrate on the application rather than spending a significant amount of time learning hardware details.

### Dividing the Application

In control loop-based applications, each developer must have an intimate knowledge of the entire application's run-time behavior and requirements. This is because the processor allocation logic is dispersed throughout the entire application. As an application increases in size or complexity, it becomes impossible for all developers to remember the precise processing requirements of the entire application.

ThreadX SMP frees each developer from the worries associated with processor allocation and allows them to concentrate on their specific piece of the embedded application. In addition, ThreadX SMP forces the application to be divided into clearly defined threads. By itself, this division of the application into threads makes development much simpler.

### Ease of Use

ThreadX SMP is designed with the application developer in mind. The ThreadX SMP architecture and service call interface are designed to be easily understood. As a result, ThreadX SMP developers can quickly use its advanced features.

### Improve Time-to-market

All of the benefits of ThreadX SMP accelerate the software development process. ThreadX SMP takes care of most processor issues and the most common safety certifications, thereby removing this effort from the development schedule. All of this results in a faster time to market!

### Protecting the Software Investment

Because of its architecture, ThreadX SMP is easily ported to new processor and/or development tool environments. This, coupled with the fact that ThreadX SMP insulates applications from details of the underlying processors, makes ThreadX SMP applications highly portable. As a result, the application's migration path is guaranteed, and the original development investment is protected.

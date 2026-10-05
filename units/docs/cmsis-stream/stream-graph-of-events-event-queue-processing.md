---
id: "stream-graph-of-events-event-queue-processing"
type: "concept"
domain: "cmsis-stream"
title: "Graph of events: Event queue processing"
summary: "The events should not disrupt the data flow of CMSIS Stream."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Events.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Events.md#event-queue-processing"
license: "Apache-2.0"
mode: "V"
---

### Event queue

The events should not disrupt the data flow of CMSIS Stream.

So they should be executed asynchronously from the data flow.

Events are put onto a queue and the queue is processed separately from the data flow.

When events are created, you can use a priority. Depending on the queue implementation, those priorities may be used or ignored.

```C
enum cg_event_priority
    {
        kLowPriority = 0,
        kNormalPriority = 1,
        kHighPriority = 2
    };
```

This priority has nothing to do with thread priorities. The queue implementation that you select may use those priorities so that events with highest priorities are handled first. But events of higher priority will not preempt the events of lower priority unless they are executed on threads of different priorities.

With an OS, the queue can be processed with a thread or a thread pool.

The event queue interface is declared in `StreamNode.h`. You should define an implementation.

If you use the python `generateEventSystemExample(".",posix=True)` you will get a default implementation of the queue using C++ standard libraries.
With `posix=False` you'll get an example `CMSIS RTOS2 API` implementation.

```C++
class EventQueue
{
    public:
    using AppHandler = bool (*)(int src_node_id, void *data, Event &&evt);

    bool push(LocalDestination dest, Event &&evt);

    bool push(DistantDestination dest, Event &&evt);

    EventQueue() {};
    virtual ~EventQueue() {};

    virtual bool isEmpty() = 0;
    virtual void clear() = 0;

    // In case of a threaded implementation
    // this should sleep when no more any event are available
    // and wakeup when notified from push or end
    virtual void execute() = 0;

    // True if a request to end the event processing has been made
    bool mustEnd() const noexcept;

    // In case of multi-threaded implementation
    // this should wakeup the thread
    // Request end of event processing for this queue
    virtual void end() noexcept;

    // Async call functions for application handler. Used by EventQueue implementation and EventOutput
    bool callAsyncHandler(int node_id, arm_cmsis_stream::Event &&evt);

    // Sync call functions for application handler. Used by EventQueue implementation and EventOutput
    static bool callSyncHandler(int node_id, arm_cmsis_stream::Event &&evt);

    // Set an application handler.
    static void setHandler(void *data, AppHandler handler);

};
```

The queue implementation should be thread safe.

The `push` may be called from `execute` so the implementation should be careful not to create any deadlock.

The event queue is a static variable of the class `EventQueue` and is the same for all graphs that you may use in the application.

You can also install an event handler in the `EventQueue` for application events.

### Event queue with threads

The queue execution can rely on threads and thread pool.

If you don't use heap allocation for the data flow scheduler, the nodes are destroyed on exit from the scheduler function.

In this case, you should flush the queue before returning from the scheduler function:

```C++
#define CG_AFTER_SCHEDULE       \
  if (::cg_eventQueue) {        \
      ::cg_eventQueue->clear(); \
  }
```

If the events are not flushed, they may act on a node that has been destroyed since they are processed on a different thread from the data flow thread.

**The queue API should be thread safe.**

Using the python `generateExamplePosixMain(".")` you can generate an example implementation.

#### Macros

For portability between different platforms, the thread and mutex implementation is provided with macros that can be defined in your `custom.hpp` file.

With C++ thread and mutexes, you could define:

```C++
#define CG_MUTEX std::shared_mutex
#define CG_INIT_MUTEX(MUTEX)
#define CG_MUTEX_DELETE(MUTEX, ERROR)
#define CG_MUTEX_ERROR_TYPE int
#define CG_MUTEX_HAS_ERROR(ERROR) (ERROR != 0)
#define CG_ENTER_CRITICAL_SECTION(MUTEX, ERROR) \
  {                                             \
    std::unique_lock lock((MUTEX));             \
    ERROR = 0;

#define CG_EXIT_CRITICAL_SECTION(MUTEX, ERROR) \
  ERROR = 0;                                   \
  }

#define CG_ENTER_READ_CRITICAL_SECTION(MUTEX, ERROR) \
  {                                                  \
    std::shared_lock lock((MUTEX));                  \
    ERROR = 0;

#define CG_EXIT_READ_CRITICAL_SECTION(MUTEX, ERROR) \
  ERROR = 0;                                        \
  }
```

The previous implementation assume that an error is fatal : it will throw. So the ERROR variable is just used to have a macro API similar the one for RTOS systems.

With CMSIS RTOS2 you could define:

```C++
class CMSISMutex
{
public:
    CMSISMutex()
    {
        mutex_id = osMutexNew(NULL);
    }

    ~CMSISMutex()
    {
        if (mutex_id != nullptr)
        {
            // Ensure the mutex is deleted only if it was created successfully
            osMutexDelete(mutex_id);
        }
    }

    osMutexId_t id() const
    {
        return mutex_id;
    }

protected:
    osMutexId_t mutex_id;
};

class CMSISLock
{
public:
    CMSISLock(CMSISMutex &mutex) : mutex(mutex)
    {
    }

    osStatus_t acquire()
    {
        error = osMutexAcquire(mutex.id(), 0);
        return error;
    }

    ~CMSISLock()
    {
        if (error == osOK)
        {
            error = osMutexRelease(mutex.id());
        }
    }

    osStatus_t getError() const
    {
        return error;
    }

protected:
    CMSISMutex &mutex;
    osStatus_t error;
};

#define CG_MUTEX CMSISMutex
#define CG_MUTEX_ERROR_TYPE osStatus_t

#define CG_MUTEX_HAS_ERROR(ERROR) (ERROR != osOK)

#define CG_ENTER_CRITICAL_SECTION(MUTEX, ERROR) \
    {                                           \
        CMSISLock lock((MUTEX));                \
        ERROR = lock.acquire();

#define CG_EXIT_CRITICAL_SECTION(MUTEX, ERROR) \
    }

#define CG_ENTER_READ_CRITICAL_SECTION(MUTEX, ERROR) \
    {                                                \
        CMSISLock lock((MUTEX));                     \
        ERROR = lock.acquire();

#define CG_EXIT_READ_CRITICAL_SECTION(MUTEX, ERROR) \
    }

```

The mutex must be a C++ class because it is created and initialized through `std::shared_ptr::allocate_shared`.


### Event queue with bare metal

In case of a bare metal systems, there are other possibilities without threads.

You could use CMSIS Stream macro `CG_BEFORE_NODE_EXECUTION` to interleave event execution with the data flow execution.

```C++
#define CG_BEFORE_NODE_EXECUTION(id) \
  ::cg_eventQueue->execute();
```

But if the event processing takes too long it may disrupt the data flow.

Another possibility would be to use the CMSIS-Stream scheduling in callback mode. The callback could be called from an ISR and the main application would just execute events from the queue or sleep when no events are available.

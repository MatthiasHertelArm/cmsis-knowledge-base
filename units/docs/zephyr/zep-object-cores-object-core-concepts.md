---
id: "zep-object-cores-object-core-concepts"
type: "concept"
domain: "rtos"
title: "Object Cores: Object Core Concepts"
summary: "Each instance of an object embeds an object core field named obj_core. An object core links the object to its object type, and each object type lets debugging tools enumerate the objects of that type."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/object_cores/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/object_cores/index.rst"
license: "Apache-2.0"
mode: "V"
---

Each instance of an object embeds an object core field named `obj_core`. An
object core links the object to its object type, and each object type lets
debugging tools enumerate the objects of that type. Object types are linked
together via a singly linked list. Together, this allows debugging tools to
traverse all the objects in the system.

An object type enumerates its objects from two places:

* Its permanent objects, which are statically defined instances such as those
  created with `K_SEM_DEFINE`. They are walked in place from their
  iterable section and are never registered at run time.
* A bounded registry of the objects initialized at run time, for instance a
  semaphore in a driver's data structure initialized with `k_sem_init`.
  The registry only references the objects; it never stores anything inside
  them.

Because of that, an object may be initialized in any storage, initialized
again in place, or discarded without any object core call: the registry
cannot be corrupted by an object that no longer exists. Some rules follow
from this model:

* An object located in the running thread's stack or in the interrupt stack is
  not registered: its life ends with the stack frame. The object type counts
  such objects in its `skipped` field. Other stacks are not recognized, such
  as the privileged stack a user thread's system calls run on or an exception
  stack specific to an architecture; an object there is registered and stays
  reported until its storage is reused.
* When the registry is full, further objects are not registered and the object
  type counts them in its `dropped` field. The registry size is set with
  `CONFIG_OBJ_CORE_MAX_DYNAMIC_OBJECTS`.
* An object that was discarded without being unregistered stays reported until
  its storage is reused: the walk recognizes the reused storage by the missing
  type tag and drops the entry. The kernel unregisters objects itself when it
  releases them: on thread abort, in `k_object_free`,
  `k_timer_cleanup`, `k_msgq_cleanup` and
  `k_stack_cleanup`, and, with
  `CONFIG_OBJ_CORE_EVICT_ON_FREE`, when memory is returned to a
  heap, a memory slab or a memory blocks allocator. Code that ends an object's
  life in another way may call `k_obj_core_unlink` so that the object
  stops being reported at once; the type tag check is only a backstop, and it
  reads the object's former storage, which must still be mapped.
* Once a type's `dropped` count is not zero, objects exist that no walk
  reports, so an inventory is complete only while it is zero.

Object cores have been integrated into the following kernel objects:

* Condition Variables
* Events
* FIFOs and LIFOs
* Mailboxes
* Memory Slabs
* Message Queues
* Mutexes
* Pipes
* Queues
* Semaphores
* Threads
* Timers
* System Memory Blocks

Developers are free to integrate them if desired into other objects within
their projects. The object_cores sample shows the
facility step by step and the object_monitor sample uses
it to watch the objects of a running application.

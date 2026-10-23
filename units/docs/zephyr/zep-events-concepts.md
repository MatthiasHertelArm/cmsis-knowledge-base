---
id: "zep-events-concepts"
type: "concept"
domain: "rtos"
title: "Events: Concepts"
summary: "Any number of event objects can be defined (limited only by available RAM). Each event object is referenced by its memory address."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/synchronization/events.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/synchronization/events.rst"
license: "Apache-2.0"
mode: "V"
---

Any number of event objects can be defined (limited only by available RAM). Each
event object is referenced by its memory address. One or more threads may wait
on an event object until the desired set of events has been delivered to the
event object. When new events are delivered to the event object, all threads
whose wait conditions have been satisfied become ready simultaneously.

An event object has the following key properties:

* A 32-bit value that tracks which events have been delivered to it.

An event object must be initialized before it can be used.

Events may be **delivered** by a thread or an ISR. When delivering events, the
events may either overwrite the existing set of events or add to them in
a bitwise fashion. When overwriting the existing set of events, this is referred
to as setting. When adding to them in a bitwise fashion, this is referred to as
posting. Both posting and setting events have the potential to fulfill match
conditions of multiple threads waiting on the event object. All threads whose
match conditions have been met are made active at the same time.

Threads may wait on one or more events. They may either wait for all of the
requested events, or for any of them. Furthermore, threads making a wait request
have the option of resetting the current set of events tracked by the event
object prior to waiting. Care must be taken with this option when multiple
threads wait on the same event object.


**Note:** The kernel does allow an ISR to query an event object, however the ISR must not attempt to wait for the events.

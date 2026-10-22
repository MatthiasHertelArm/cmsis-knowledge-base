---
id: "zep-logging-multi-domain-support"
type: "concept"
domain: "debug"
title: "Logging: Architecture / Multi-domain support"
summary: "More complex systems can consist of multiple domains where each domain is an independent binary. Examples of domains are a core in a multicore SoC or one of the binaries (Secure or Nonsecure) on an ARM TrustZone core."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/logging/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/logging/index.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Architecture_

More complex systems can consist of multiple domains where each domain is an
independent binary. Examples of domains are a core in a multicore SoC or one
of the binaries (Secure or Nonsecure) on an ARM TrustZone core.

Tracing and debugging on a multi-domain system is more complex and requires an efficient logging
system. Two approaches can be used to structure this logging system:

* Log inside each domain independently.
  This option is not always possible as it requires that each domain has an available backend
  (for example, UART). This approach can also be troublesome to use and not scalable,
  as logs are presented on independent outputs.
* Use a multi-domain logging system where log messages from each domain end up in one root domain,
  where they are processed exactly as in a single domain case.
  In this approach, log messages are passed between domains using a connection between domains
  created from the backend on one side and linked to the other.

  The Log link is an interface introduced in this multi-domain approach. The Log link is
  responsible for receiving any log message from another domain, creating a copy, and
  putting that local log message copy (including remote data) into the message queue.
  This specific log link implementation matches the complementary backend implementation
  to allow log messages exchange and logger control like configuring filtering, getting log
  source names, and so on.

There are three types of domains in a multi-domain system:

* The *end domain* has the logging core implementation and a cross-domain
  backend. It can also have other backends in parallel.
* The *relay domain* has one or more links to other domains but does not
  have backends that output logs to the user. It has a cross-domain backend either to
  another relay or to the root domain.
* The *root domain* has one or multiple links and a backend that outputs logs
  to the user.

See the following image for an example of a multi-domain setup:

In this architecture, a link can handle multiple domains.
For example, let's consider an SoC with two ARM Cortex-M33 cores with TrustZone: cores A and B (see
the example illustrated above). There are four domains in the system, as
each core has both a Secure and a Nonsecure domain. If *core A nonsecure* (A_NS) is the
root domain, it has two links: one to *core A secure* (A_NS-A_S) and one to
*core B nonsecure* (A_NS-B_NS). *B_NS* domain has one link, to *core B secure*
*B_NS-B_S*), and a backend to *A_NS*.

Since in all instances there is a standard logging subsystem, it is always possible
to have multiple backends and simultaneously output messages to them. An example of this is shown
in the illustration above as a dotted UART backend on the *B_NS* domain.


#### Domain ID


The source of each log message can be identified by the following fields in the header:
`source_id` and `domain_id`.

The value assigned to the `domain_id` is relative. Whenever a domain creates a log message,
it sets its `domain_id` to `0`.
When a message crosses the domain, `domain_id` changes as it is increased by the link offset.
The link offset is assigned during the initialization, where the logger core is iterating
over all the registered links and assigned offsets.

The first link has the offset set to 1.
The following offset equals the previous link offset plus the number of domains in the previous
link.

The following example is shown below, where
the assigned `domain_ids` are shown for each domain:

Let's consider a log message created on the *B_S* domain:

1. Initially, it has its `domain_id` set to `0`.
#. When the *B_NS-B_S* link receives the message, it increases the `domain_id`
   to `1` by adding the *B_NS-B_S* offset.
#. The message is passed to *A_NS*.
#. When the *A_NS-B_NS* link receives the message, it adds the offset (`2`) to the `domain_id`.
   The message ends up with the `domain_id` set to `3`, which uniquely identifies the message
   originator.


#### Cross-domain log message


In most cases, the address space of each domain is unique, and one domain
cannot access directly the data in another domain. For this reason, the backend can
partially process the message before it is passed to another domain. Partial
processing can include converting a string package to a *fully self-contained*
version (copying read-only strings to the package body).

Each domain can have a different timestamp source in terms of frequency and
offset. Logging does not perform any timestamp conversion.


#### Runtime filtering


In the single-domain case, each log source has a dedicated variable with runtime
filtering for each backend in the system. In the multi-domain case, the originator of
the log message is not aware of the number of backends in the root domain.

As such, to filter logs in multiple domains, each source requires a runtime
filtering setting in each domain on the way to the root domain. As the number of
sources in other domains is not known during the compilation, the runtime filtering
of remote sources must use dynamically allocated memory (one word per
source). When a backend in the root domain changes the filtering of the module from a
remote domain, the local filter is updated. After the update, the aggregated
filter (the maximum from all the local backends) is checked and, if changed, the remote domain is
informed about this change. With this approach, the runtime filtering works identically
in both multi-domain and single-domain scenarios.


#### Message ordering


Logging does not provide any mechanism for synchronizing timestamps across multiple
domains:

* If domains have different timestamp sources, messages will be
  processed in the order of arrival to the buffer in the root domain.
* If domains have the same timestamp source or if there is an out-of-bound mechanism that
  recalculates timestamps, there are 2 options:

  * Messages are processed as they arrive in the buffer in the root domain.
    Messages are unordered but they can be sorted by the host as the timestamp
    indicates the time of the message generation.
  * Links have dedicated buffers. During processing, the head of each buffer is checked
    and the oldest message is processed first.

    With this approach, it is possible to maintain the order of the messages at the cost
    of a suboptimal memory utilization (since the buffer is not shared) and increased processing
    latency (see `CONFIG_LOG_PROCESSING_LATENCY_US`).

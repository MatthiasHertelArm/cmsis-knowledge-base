---
id: "txmw-chapter-3-description-of-tracex-event-searching"
type: "concept"
domain: "trace"
title: "Chapter 3 - Description of TraceX: Event Searching"
summary: "TraceX provides an extensive event search capability. The event ID and information fields of each event are the primary search parameters. Not specifying a value for a search parameter indicates that parameter effectively removes that parameter from of the search."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/tracex/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/tracex/chapter3.md#event-searching"
license: "MIT"
mode: "V"
---

TraceX provides an extensive event search capability. The event ID and information fields of each event are the primary search parameters. Not specifying a value for a search parameter indicates that parameter effectively removes that parameter from of the search. In addition, the search can be done such that any parameter found will satisfy the search or all parameters must be found to satisfy the search. The search may also be restricted to a particular context or cover all contexts in the trace. Invoking the event search is done by selecting the ***Search by Value*** button on the toolbar, as shown in **Figure 17**. When selected the search dialog is displayed, which specifies all the parameters for the search. The ***Next*** and ***Previous*** buttons in the search dialog can then be used to find the next and previous events that match the specified search criteria. **Figure 17** shows the search dialog.

(figure: Screenshot of the event search.)

**FIGURE 17**

(figure: Screenshot of the search dialog.)

**FIGURE 18**

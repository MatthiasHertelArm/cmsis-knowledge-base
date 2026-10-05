---
id: "x-cmsis-stream-5"
type: "pattern"
domain: "cmsis-stream"
title: "Test event IDs in a CMSIS Stream processEvent method"
status: "draft"
extracted_from: "proc-cmsis-stream"
source: "cmsis-stream/SKILL.md"
---

Testing for a event defined by the component is done with the `selectors` array.

Example:
```C++
 if (evt.event_id == selectors[selMessage])
```

If the event is a default event as define in `cg_enums.h` CMSIS stream header then the test can use directly the global ID since this ID will not change for different graphs:
Example:
```C++
 if (evt.event_id == kValue)
```

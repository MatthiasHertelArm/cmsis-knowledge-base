---
id: "intr-considerations-when-building-embed-remote-monitoring-of-database-statistics"
type: "concept"
domain: "debug"
title: "Considerations when Building Embedded Databases: Remote Monitoring of Database Statistics"
summary: "Lastly, building and deploying an embedded database requires some way of monitoring performance. Memfault's metrics can be used for this purpose."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-07-24-choosing-or-building-an-embedded-db.md"
doc_source: "https://interrupt.memfault.com/blog/choosing-or-building-an-embedded-db#remote-monitoring-of-database-statistics"
license: "CC-BY-SA-4.0"
mode: "V"
---

Lastly, building and deploying an embedded database requires some way of
monitoring performance. [Memfault's
metrics](https://memfault.com/customers/bond-home-case-study/) can be used for
this purpose.

These are a few things you may want to keep an eye on:

1. Number of operations since boot. Track `gets`, `sets`, `deletes`, and
   `compactions`.

2. How much free space is available? And how much space is occupied by dead
   records?

3. What's the largest headroom available in a page? This is similar to
   `largest_free_block` in heaps.

4. Error due to running out of space in the database due to no page large enough
   to hold the record.

5. Any CRC errors. These happen more often than you may expect, and will surely
   degrade customer experience in some way. So it's a good idea to be able to
   correlate them to specific units and support tickets.

Here's what one heavily-used unit's statistics look like for Bond Bridge Pro. As
you see, our allocation of 4 MB for the database has left us lots of room for
expansion:

```json
{
  "live_records": 235,
  "dead_records": 1516,
  "page_size": 4096,
  "total_dead": 648704,
  "total_free": 4121024,
  "max_free": 4096,
  "total_head": 3472320,
  "max_head": 4096,
  "compactions": 0,
  "empty_pages": 190,
  "size": 4194304,
  "dirty": false,
  "landmines": -3,
  "sets": 4,
  "gets": 2708,
  "deletes": 0
}
```

Happy building! And remember, persistence is not futile. Just never
underestimate the limitations of flash memory.









{:.no_toc}

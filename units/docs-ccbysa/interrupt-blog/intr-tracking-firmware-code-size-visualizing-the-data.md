---
id: "intr-tracking-firmware-code-size-visualizing-the-data"
type: "concept"
domain: "debug"
title: "Tracking Firmware Code Size: How to Track Code Size / Visualizing the Data"
summary: "At this point, we can assume we are storing our code sizes in a database of sorts, and we can now visualize the data. There are many ways to do this, but the ones that come to mind are:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-18-code-size-deltas.md"
doc_source: "https://interrupt.memfault.com/blog/code-size-deltas#visualizing-the-data"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: How to Track Code Size_

At this point, we can assume we are storing our code sizes in a database of
sorts, and we can now visualize the data. There are many ways to do this, but
the ones that come to mind are:

- Export to `.csv` and import to Excel.
- Build a web application using your framework of choice to show the data in
  whatever way you please.
- Spin up a Business Intelligence style tool, such as
  [Redash](https://redash.io/) or [Metabase](https://www.metabase.com/).

In this post, I chose to launch a Redash instance on Heroku
([takes 5 minutes](https://github.com/willnet/redash-on-heroku), it's \~free)
and hooked it up to the PostgreSQL database. This allowed me to create some
pretty quick and useful visualizations!

Here is a chart of the code size of the `.text` region for the last 2,500
commits:



and here is a way to show the extent of each commit's impact on the overall code
size:



If you want to see this data live, check out the
[Redash instance on Heroku](https://zephyr-codesizes.herokuapp.com/public/dashboards/rsertKgwMwqHWzE24G4QUvbZhEe72x4hhsqMSqts?org_slug=default)!

Having these visualizations allow developers to dive into why code space has
disappeared in the past and see where the code size is trending. If you ever
need to find 500 bytes of code space and you have already taken the approaches
listed in the [GCC flags
post](https://interrupt.memfault.com/blog/code-size-optimization-gcc-flags), this is a
good place to start.

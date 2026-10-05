---
id: "intr-the-android-developer-s-journey-in-common-decisions-to-overcome"
type: "concept"
domain: "debug"
title: "The Android Developer's Journey into Hardware Observability: Common decisions to overcome"
summary: "There are many decisions to make at each step of the observability journey that can either lead the developer astray technically or work well for a reasonable amount of time, but fail to scale as the number of …"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-02-28-aosp-observability.md"
doc_source: "https://interrupt.memfault.com/blog/aosp-observability#common-decisions-to-overcome"
license: "CC-BY-SA-4.0"
mode: "V"
---

There are many decisions to make at each step of the observability journey that
can either lead the developer astray technically or work well for a reasonable
amount of time, but fail to scale as the number of devices observed increases.
Each decision can result in a large amount of engineering time designing,
building out, and testing the changes, but also maintaining the system over time
as it gets more complex.

### Push vs pull

While a push notification may trigger the collection of a report, the system as
a whole is still pull-based, because they still require someone to request the
data from the device. A symptom of this is that sometimes, when a bug happens,
the affected user might take several days to reach out to customer support, and
by that time, the data is not in the buffer anymore. Or in another case, there
might be a delay in customer support that causes the data to be lost. Pull-based
systems also make it awkward to pro-actively check how often an issue is
happening across every device, because it means randomly choosing a number of
devices to pull data from, on the off-chance it experienced the issue.

Converting an existing pull-based push system to automatically push data when it
detects an issue can be difficult: the push system took some work and now needs
to be spun down, the backend might not be designed for uploading a higher volume
of data, the device will need to manage its cache of data and dedupe any
uploaded information, and more.

When we initially discussed pulling error reports at a previous company, our
AOSP device didn't have push notifications (since it didn't use Google Mobile
Services), so we spent loads of time investigating and then re-building push
notifications on Android using MQTT, and re-purposing an existing frontend to
allow customer support to send a push trigger for the error report. But there
were so many times where the error report just didn't contain any information
from around the time of the incident because it was requested too late.

### Data analysis fatigue

Inevitably, after tens or hundreds of bugs and customers investigated and fixed
or abandoned, the developer can get tired of manually combing through logs, and
realize they can develop tools to parse the error report automatically. There's
often a lot of noise, and it generally feels possible to filter out what's
important.

Building this tool can feel initially good, but slowly, over time, the
complexity of the data grinds progress to a halt. Sharing the tool within the
company or as an open-source project can keep the momentum going, but unless
there is a dedicated team involved with maintaining it, maintaining the tool can
feel like a chore.

The tool itself is probably not perfect. While programmers can easily think
about text analysis, a visualization is sometimes more effective, and while some
time can be spent building tools like
[Battery Historian](https://github.com/google/battery-historian), it takes a ton
of dedicated engineering effort to really design something that works over time.

At a previous company, it turned out that each of several Android teams had
engineers who each built their own data parsing tool that looked through error
reports and logs for information specific to that team. But as time went on and
the teams changed ownership or the developers moved around, these tools became
more and more unwieldy to use and eventually dropped as a relic of the past.

### Campfire or Wildfire

After a certain number of devices, it becomes impractical to fix every bug on
the device. Instead, teams start introducing a system of prioritization to
determine whether a fire is a small campfire or a widespread wild fire.

If the team has a way to trigger data upload automatically, parse that data into
something actionable automatically, uniquely identify one issue from another,
count the number of times that issue occurs on how many devices, and persist
this information in a queryable format somewhere, then they might be in a
position where they can pro-actively understand what are the most pressing
issues to fix. But it takes a ton of work to develop and maintain all the
systems involved in that pipeline!

In my experience from the device developer side, a lot of progress can be made
on the device-side so that the error reports can be uploaded to the right place.
But when the data operations move from CRUD (create, read, update, delete) to
actual data processing, the amount of cross-functional buy-in and expertise
involved is an order of magnitude more difficult for a company to commit to.

### Building a team with the right expertise

The reality is that all the work in designing, building, and then maintaining
these systems, will require a team of engineers with diverse skillsets across
the entire stack: AOSP developers are needed to collect and upload the data from
the device and provide domain expertise, backend developers are required in
order to maintain and scale pipelines as more and different information is
processed, frontend engineers might be required to create a nicer way to
download the data, data scientists will need to be involved to ingest the
metrics and help set up charts, alerting, and design how to store and query the
data efficiently. Staffing a full team just to maintain a hodgepodge
observability solution is a tall ask, especially for many AOSP engineers who
would rather be solving customer pain points.

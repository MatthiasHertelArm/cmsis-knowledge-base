---
id: "intr-considerations-when-building-embed-considering-your-requirements-for-an-emb"
type: "concept"
domain: "debug"
title: "Considerations when Building Embedded Databases: Considering your Requirements for an Embedded Database"
summary: "Now that it's clear why you need an embedded database, let's consider the different constraints which may lead you in one direction or another when shopping or building a solution:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-07-24-choosing-or-building-an-embedded-db.md"
doc_source: "https://interrupt.memfault.com/blog/choosing-or-building-an-embedded-db#considering-your-requirements-for-an-embedded-database"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that it's clear why you need an embedded database, let's consider the
different constraints which may lead you in one direction or another when
shopping or building a solution:

#### How much data do you have to store? And how much flash is available?

You should start with a back-of-the-envelope calculation of the total amount of
data that your device needs to store. This is harder than it sounds because
you've got to also anticipate space for future features.

My approach is usually to be fairly greedy and allocate a lot of flash to a new
product line, both to the code space and database. This way we can add features
freely without concern for running out of space if the product is successful
enough to experience a decade of feature creep.

#### How important is resilience to power loss during write operations?

Data loss and corruption is incredibly frustrating for customers and expensive
in terms of customer support and reputation. So, your embedded database
should not lose data if power is lost at an inopportune time (such as during a
program or erase operation).

#### Are you storing just one record, or many records?

Some simple applications can get away with a single record structure. However,
if you need arbitrarily-sized enumerations as in a smart home hub that needs to
track schedules for and of several devices, you'll need a database that can
store multiple copies of multiple record types.

#### Do the records form a natural hierarchy?

It can be helpful to take advantage of hierarchical relationships if only for
visualization and detection of orphaned records.

#### How often are records being re-written?

It's important to make a calculation of the number of times any flash page is
expected to be erased in the lifetime of the product and ensure that it is under
the specified endurance in the flash manufacturer's datasheet.

These calculations, although simple, can defy intuition. The highest flash
endurance of 1 million cycles seems like a big number, but if you don't have any
wear leveling and write a record every 10 seconds, you will pass a million
cycles in just 4 months. And the flash built into microcontrollers usually has
much lower endurance, around 10k cycles.

#### How big are your records? Do you tend to write a whole record at once? Or do you often append to a record?

Things get much more complicated when you've got records which need to be able
to be appended to or partially written. If you need these complexities, it's
best to select a filesystem or at least you will want a file-like API.

Keeping things simple means having just a get(), set(), and possibly list() API
where whole records must be read and written at once.

#### When can you tolerate garbage collection delays?

At some point deleted records will need to be cleaned up to make space for more
data. How often this happens depends on the application, but when something like
a device name is included in the device record, any renaming of a device will
result in a dead record.

When those dead records eventually are compacted, a delay for flash page erasure
is incurred. This could be designed to happen on demand (practical and easy), or
to run in the background when the device is idle (sounds better, but hard to
pull off).

#### Do you need a backup and restore function?

Effectively backing up and restoring from backups can be a really powerful user
story. However, doing this well will require some support at the embedded
database level. Simply copying the entire database partition may be excessively
large.

Databases can also be designed to stream records out as part of a backup
mechansism.

#### Is the database read-write or write-only?

In many applications the data you are storing may be logs or sensor data that
never needs to be read by the embedded system, but only recorded for later
analysis by a larger application. Usually this kind of data forms a time-series.
If you know the records to be of fixed size or small maximum size, you could
simply write each record to flash at regular offsets. However, you still should
consider what happens when reaching the end of the allotted flash space. If
continued writes are needed after the partition is full, then a scheme for
handling the erasure of full pages is required which again complicates life for
the implementor.

---
id: "intr-considerations-when-building-embed-a-brief-look-at-a-few-existing-solutions"
type: "concept"
domain: "debug"
title: "Considerations when Building Embedded Databases: A Brief Look at a Few Existing Solutions"
summary: "Now that we've discussed the main challenges of flash memory for data storage, let's take a very brief look at a few specific implementations and their design choices:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-07-24-choosing-or-building-an-embedded-db.md"
doc_source: "https://interrupt.memfault.com/blog/choosing-or-building-an-embedded-db#a-brief-look-at-a-few-existing-solutions"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that we've discussed the main challenges of flash memory for data storage,
let's take a very brief look at a few specific implementations and their design
choices:

### Espressif's NVS Flash

If you are building a product using Espressif SoCs like ESP32, then you have an
full-featured built-in choice called
[nvs_flash](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/storage/nvs_flash.html).
Some salient features are:

- key-value store with string-based keys
- namespace system avoids conflicts between components
- can efficiently enumerate all records in a given namespace
- binary blobs are allowed to exceed page size
- highly efficient for small entries such as integers
- supports resuming of a compaction operation interrupted by power loss
- only officially available for Espressif chips

### Zephyr's NVS

The Zephyr operating system also offers a key-value
[database implementation](https://docs.zephyrproject.org/latest/services/storage/nvs/nvs.html),
which is characteristically lightweight. Two points to note are:

- keys are only 16-bit, so careful planning is required to avoid conflicts
- unlike other solutions, the data CRC is optional, so you can live dangerously
  and save on flash space

### SPIFFS (SPI Flash File System)

[SPIFFS](https://github.com/pellepl/spiffs) is way more ambitious than the
key-value stores discussed above, seeking to provide a POSIX-like filesystem
interface featuring `open`, `write`, `read`, and `seek` functions so that code
written for SPIFFS could potentially execute unmodified on a major OS like
Linux. However, trying to pack full filesystem-like capabilities into the RAM
available in a small embedded system leades to steep tradeoffs in performance
and safety. Reading the [SPIFFS FAQ](https://github.com/pellepl/spiffs/wiki/FAQ)
shines some light on these challenges.

### Bond's _Beau_ Embedded Database

When we were building the Bond Bridge, we looked around for embedded database
solutions but none of the free software solutions available at the time were up
for the task. ESP32 nvs*flash was in early days and the venerable FAT12 format
was too inefficient with small records. So after shipping an MVP with a very
limited database that we affectionately dubbed "UglyDB", we rolled our own
embedded database that we call \_Beau*.

We've used Beau on both smart ceiling fans with 128 kB storing schedules, group,
and scenes and 4 MB for Bond Bridge (basically a smart home hub) which needs to
store similar information about possibly hundreds of devices plus recorded RF
and IR signals.

Our database stores records like this:

```
FFFF BEEF [key] [type] [parent] [data_len] [data_crc] [header_crc]
[data ... ]
```

The idea is that the first word `FFFF BEEF` is a sentinel that signals that a
record follows. The header contains a 64-bit unique record key, 16-bit record
type, the 64-bit key of the parent record (useful for building hierarchical
relationships), the length of the record data, a checksum of the record data,
and finally a checksum of the header.

At boot, the microcontroller can efficiently scan through the database, loading
the key and type metadata, memorizing the physical address (flash offset) of
every record. This scan is efficient because only the headers need be read. The
contents can be skipped over. Things only slow down in the case of corruption,
in which case it is necessary to scan through the database looking for another
valid header.

The `FFFF` at the beginning of the sentinel is important. These `1` bits are
"unprogrammed", so we are able to delete a record by simply programming some of
them so the sentinel reads `DEAD BEEF`. The header is still intact so it's still
possible to efficiently scan through the database.

We always reserve one page (keeping it empty) so that when it is time to compact
a page, all the live records from the old page can be copied to the reserved
page. The old page can then be erased, freeing up the space occupied by dead
(deleted) records.

A killer feature of Beau is backup and restore. To back up, we simply stream the
database records out using HTTP chunked transfer. To restore, we again use
chunked transfer and this time write each record to the database. This technique
has unlocked efficient transfer of smart home devices between hubs, and for an
easy path for upgrades to newer models of hubs, and of course for recovery after
hardware failure or catastrophic firmware issues.

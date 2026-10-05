---
id: "intr-considerations-when-building-embed-why-you-should-care-about-nvs-non-volati"
type: "concept"
domain: "debug"
title: "Considerations when Building Embedded Databases: Why You Should Care About NVS (Non-Volatile Storage)"
summary: "Nearly every embedded system needs to persist data across power cycle."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-07-24-choosing-or-building-an-embedded-db.md"
doc_source: "https://interrupt.memfault.com/blog/choosing-or-building-an-embedded-db#why-you-should-care-about-nvs-non-volatile-storage"
license: "CC-BY-SA-4.0"
mode: "V"
---

Nearly every embedded system needs to persist data across power cycle. A smart
fishtank needs to remember the configured salinity and oxygen setpoints, an
e-bike may store a geofence and riding log, and a smart home hub must store
device, group, and schedule information.

Let's assume for now that we're talking about a small embedded system, like an
STM32 with only the built-in flash available for persistent storage. Is there an
obvious solution? What happens if we just write our data to flash and read it
back on reboot?

For the fishtank example, the data we want to persist could be organized into a
single struct which is read from a specific flash address on boot and written to
that address when the user changes the settings:

```c
typedef struct {
    int salinity;
    int oxygen;
} fishtank_config_t;

fishtank_config_t config;

void load() {
  flash_read(CONFIG_ADDR, &config, sizeof(config));
}

void save() {
  flash_erase_page(CONFIG_ADDR);
  flash_program(CONFIG_ADDR, &config, sizeof(config));
}
```

This solution may "just work" for an MVP fishtank, but as the product evolves we
are going to run into a few issues:

1.  The persisted data is not portable due to endianness and integer size
    differences,
2.  The config will be corrupted if power is lost during the `save()` function,
3.  If a `temperature` field is added to the struct, it will be read as `-1`
    upon firmware upgrade, which may be unexpected.

So we see that even for the simplest products, persisting data to flash presents
some maintainability challenges.

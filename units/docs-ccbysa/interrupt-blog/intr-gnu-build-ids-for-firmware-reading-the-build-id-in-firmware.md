---
id: "intr-gnu-build-ids-for-firmware-reading-the-build-id-in-firmware"
type: "concept"
domain: "debug"
title: "GNU Build IDs for Firmware: Reading the build ID in firmware"
summary: "Once the build ID is in our binary, we need to modify our firmware to read it and, at the very least, print it over serial at boot."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-05-29-gnu-build-id-for-firmware.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-build-id-for-firmware#reading-the-build-id-in-firmware"
license: "CC-BY-SA-4.0"
mode: "V"
---

Once the build ID is in our binary, we need to modify our firmware to read it
and, at the very least, print it over serial at boot.

From the linker script, we know that we will find the build ID section at
`&g_note_build_id`. From the spec, we know the structure of the section and can
write down a typedef:

```c
typedef struct {
    uint32_t namesz;
    uint32_t descsz;
    uint32_t type;
    uint8_t data[];
} ElfNoteSection_t;

extern const ElfNoteSection_t g_note_build_id;
```

We can now simply index into the data field and print the build ID data.

```c
void print_build_id(void) {
    const uint8_t *build_id_data = &g_note_build_id.data[g_note_build_id.namesz];

    printf("Build ID: ");
    for (int i = 0; i < g_note_build_id.descsz; ++i) {
        printf("%02x", build_id_data[i]);
    }
    printf("\n");
}
```

Calling this code on boot, we get:
```
...
Build ID: 8d7aec8b900dce6c14afe557dc8889230518be3e
...
```

> Update: A prior version of the above code was incorrect: `g_note_build_id` was
> declared as a pointer which would lead to random data being read in the best case,
> and a crash in the worst case. Thanks to [Simon
> Doppler](https://github.com/dopsi) for reporting the
> problem.

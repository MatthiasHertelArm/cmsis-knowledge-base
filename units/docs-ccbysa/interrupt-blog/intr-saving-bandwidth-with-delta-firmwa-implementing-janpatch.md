---
id: "intr-saving-bandwidth-with-delta-firmwa-implementing-janpatch"
type: "concept"
domain: "debug"
title: "Saving bandwidth with delta firmware updates: Delta Updates Implementation / Implementing JanPatch"
summary: "Janpatch is distributed as a single header file which makes it easy to integrate into your firmware build. Simply clone the repository, stick it on your include path, and #include <janpatch.h> in your C code."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-08-09-ota-delta-updates.md"
doc_source: "https://interrupt.memfault.com/blog/ota-delta-updates#implementing-janpatch"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Delta Updates Implementation_

Janpatch is distributed as a single header file which makes it easy to integrate
into your firmware build. Simply clone the repository, stick it on your include
path, and `#include <janpatch.h>` in your C code.

Everything the library needs to work is passed via the `janpatch_ctx` struct.
Let's take a look at it:

```c
typedef struct {
    // fread/fwrite buffers
    janpatch_buffer source_buffer;
    janpatch_buffer patch_buffer;
    janpatch_buffer target_buffer;

    // function signatures
    size_t (*fread)(void*, size_t, size_t, JANPATCH_STREAM*);
    size_t (*fwrite)(const void*, size_t, size_t, JANPATCH_STREAM*);
    int    (*fseek)(JANPATCH_STREAM*, long int, int);
    long   (*ftell)(JANPATCH_STREAM*);

    // progress callback
    void   (*progress)(uint8_t);

    // the combination of the size of both the source + patch files (that's the max. the target file can be)
    long   max_file_size;
} janpatch_ctx;
```

First come the source, patch, and target buffers. These are simply RAM buffers
used by Janpatch as working memory. The author recommends matching the size of
your flash sectors for best performance, likely because the whole buffer is
written at once, so you'll save on erase times.

On our STM32, flash sectors are 4kB so we'll simply allocate three static 4kB
buffers:

```c
#include <janpatch.h>

#define SECTOR_SIZE 4096

static unsigned char source_buf[SECTOR_SIZE];
static unsigned char target_buf[SECTOR_SIZE];
static unsigned char patch_buf[SECTOR_SIZE];

int do_janpatch() {
    janpatch_ctx ctx = {
        // fread/fwrite buffers for every file, minimum size is 1 byte
        // when you run on an embedded system with block size flash, set it to the size of a block for best performance
        { source_buf, SECTOR_SIZE },
        { target_buf, SECTOR_SIZE },
        { patch_buf, SECTOR_SIZE },
	...
    };
}
```

The next four fields are function pointers that expect File I/O functions. On
POSIX systems you can simply pass `fread`, `fwrite`, and `fseek`, and define
`JANPATCH_STREAM` as `FILE`. However, we are on a bare metal system and will
need to implement our own. I'll call this module Simple File I/O or `simple_fileio`.

We need our `simple_fileio` module to be able to read data from our
memory-mapped `bin` file, and both read and write data from/to our firmware slot
in flash. We'll also need to keep track of seek offsets as we go to comply with
the POSIX-like API.

First, we'll create a new type to encapsulate all of that state and serve as our
`JANPATCH_STREAM` type. We'll call it `sfio_stream_t`:

```c
typedef enum {
    SFIO_STREAM_SLOT,
    SFIO_STREAM_RAM,
} sfio_stream_type_t;

typedef struct {
    sfio_stream_type_t type;
    size_t offset;
    size_t size;
    union {
	# RAM pointer for SFIO_STREAM_RAM
        uint8_t *ptr;
	# Image slot for SFIO_STREAM_SLOT
	image_slot_t slot;
    };
} sfio_stream_t;
```

We can then implement `sfio_fread` which reads from RAM or image slot at the
stored offset and writes it to an output pointer. Note that while the POSIX API
accepts a `size` and a `count` (for a total number of bytes read of `size *
count`, Janpatch only ever sets a size of `1` so we made the
simplifying assumption that it would always be 1.

```c
size_t sfio_fread(void *ptr, size_t size, size_t count, sfio_stream_t *stream) {
    assert(size == 1);
    if (stream->offset + count > stream->size) {
        count = stream->size - stream->offset;
    }
    if (stream->type == SFIO_STREAM_SLOT) {
        dfu_read(stream->slot, ptr, stream->offset, size * count);
    } else {
        memcpy(ptr, stream->ptr + stream->offset, size * count);
    }

    return count * size;
}
```

Next, our `sfio_fwrite` function needs to write the provided buffer of `count` bytes
to our RAM or image slot, as follows:

```c
size_t sfio_fwrite(const void *ptr, size_t size, size_t count, sfio_stream_t *stream) {
    assert(size == 1);
    if (stream->offset + count > stream->size) {
        count = stream->size - stream->offset;
    }
    if (stream->type == SFIO_STREAM_SLOT) {
        dfu_write(stream->slot, ptr, stream->offset, size * count);
    } else {
        memcpy(stream->ptr + stream->offset, ptr, size * count);
    }

    return count * size;
}
```

Last but not least, `sfio_fseek` simply needs to update the stored `offset`
value. Note that Janpatch only ever uses `SEEK_SET` so we can use that to
simplify our code again:

```c
int sfio_fseek(sfio_stream_t *stream, long int offset, int origin) {
    assert(origin == SEEK_SET);
    if (offset > stream->size) {
        return -1;
    } else {
        stream->offset = offset;
    }
    return 0;
}
```

Astute readers may have noticed that we introduced new functions: `dfu_read` and
`dfu_write`, which we use to write to and read from our image slots. Those
functions convert slot addresses to physical addresses and then use memcpy or flash
APIs to read/write the data. Here's a simple implementation that does no bounds
checking;

```c
int dfu_read(image_slot_t slot, void *ptr, long int offset, size_t count) {
    void *addr = (slot == IMAGE_SLOT_1 ? &__slot1rom_start__ : &__slot2rom_start__);
    addr += offset;
    memcpy(ptr, addr, count);
    return count;
}

int dfu_write(image_slot_t slot, const void *ptr, long int offset, size_t count) {
    uint32_t addr = (uint32_t)(slot == IMAGE_SLOT_1 ? &__slot1rom_start__ : &__slot2rom_start__);
    addr += offset;
    flash_program(addr, ptr, count);
    return count;
}
```

We can now fill in our `janpatch_ctx`:

```c
#define SECTOR_SIZE 4096

janpatch_ctx ctx = {
    // fread/fwrite buffers for every file, minimum size is 1 byte
    // when you run on an embedded system with block size flash, set it to the size of a block for best performance
    { source_buf, SECTOR_SIZE },
    { target_buf, SECTOR_SIZE },
    { patch_buf, SECTOR_SIZE },

    // functions which can perform basic IO
    &sfio_fread,
    &sfio_fwrite,
    &sfio_fseek,

    NULL, // ftell not implemented
    NULL, // progress callback not implemented
};
```

Finally, we need to invoke the `janpatch` method itself. It accepts three
`JANPATCH_STREAM`:

- `source`, here that is our App image in slot 2.
- `patch`, the delta image we hardcoded into our Loader (i.e. memory mapped)
- `target`, also our App image in slot 2, as we are patching in-place.

Here is what the code looks like:

```c
    JANPATCH_STREAM source = {
        .type = SFIO_STREAM_SLOT,
	.offset = 0,
	.size = (size_t)&__slot2rom_size__,
	.slot = IMAGE_SLOT_2,
    };
    JANPATCH_STREAM patch = {
        .type = SFIO_STREAM_RAM,
	.offset = 0,
	.size = (size_t)&_binary_build_patch_bin_size,
	.ptr = data_ptr,
    };
    JANPATCH_STREAM target = {
        .type = SFIO_STREAM_SLOT,
	.offset = 0,
	.size = (size_t)&__slot2rom_size__,
	.slot = IMAGE_SLOT_2,
    };

    shell_put_line("Patching data");
    janpatch(ctx, &source, &patch, &target);
```

That's it! The full example is available on Github in [the Interrupt
repo](https://github.com/memfault/interrupt/tree/master/example/fwup-delta).

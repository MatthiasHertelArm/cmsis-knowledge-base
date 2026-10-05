---
id: "intr-mcuboot-walkthrough-and-porting-gu-creating-an-mcuboot-image"
type: "concept"
domain: "debug"
title: "MCUboot Walkthrough and Porting Guide: Creating an MCUboot Image"
summary: "At this point, we have implemented all the dependencies required to perform an upgrade within MCU boot."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-11-04-mcuboot-overview.md"
doc_source: "https://interrupt.memfault.com/blog/mcuboot-overview#creating-an-mcuboot-image"
license: "CC-BY-SA-4.0"
mode: "V"
---

At this point, we have implemented all the dependencies required to perform an upgrade within MCU boot.

Now that we have ported the bootloader itself, we need to generate an MCUboot compatible binary
image that can be launched. This can easily be done using the `imgtool` utility included in the project. The tool can operate on a binary file.

As we have discussed in [this post](https://interrupt.memfault.com/blog/how-to-write-a-bootloader-from-scratch#putting-it-all-together), an ELF can be converted to a binary using `objcopy`:

```bash
$ arm-none-eabi-objcopy build/nrf52-app.elf nrf52-app-no-header.bin -O binary
```

The `imgtool sign` command can be used to add the MCUboot Image header and trailer to the binary image:

```bash
$ python external/MCUboot/scripts/imgtool.py sign \
    --header-size 0x200 \
    --align 4 \
    --slot-size 0x20000 \
    --version 1.0.0 \
    --pad-header \
    build/nrf52-app-no-header.bin build/nrf52-app.bin
```

where

* `--header-size` Controls the size of the binary header. Usually, the ARM vector table comes immediately after the image header so we need to make sure things are sized appropriately such that the vector table is [aligned appropriately](https://interrupt.memfault.com/blog/how-to-write-a-bootloader-from-scratch#making-our-app-bootloadable)
* `--pad-header` causes the binary passed to be prefixed with the header information. Another
  option is to pre-add a zero-filled region to the binary and then it will be filled with the
  header.
* `--slot-size` matches the size we have provisioned on device for the slot

We can automate the generation of this binary from the ELF by adding it to our Makefile:

```makefile
$(MCUBOOT_IMG0_BIN): $(TARGET_BIN)
    @python $(IMGTOOL_PY) sign --header-size 0x200 --align 8 -S 131072 -v 1.0.0 --pad-header $(TARGET_BIN) $(MCUBOOT_IMG0_BIN)
    @echo "Generated $(patsubst $(ROOT_DIR)/%,%,$@)"

$(TARGET_BIN): $(TARGET_ELF)
    @arm-none-eabi-objcopy $< $@ -O binary
    @echo "Generated $(patsubst $(ROOT_DIR)/%,%,$@)"

$(TARGET_ELF): $(OBJ_FILES) $(LDSCRIPT)
    @echo "Linking library"
    @arm-none-eabi-gcc $(CFLAGS) $(LDFLAGS) $(OBJ_FILES) -o $@ -Wl,-lc -Wl,-lgcc
    @echo "Generated $(patsubst $(ROOT_DIR)/%,%,$@)"
```

The image can also be signed by providing the `--key` argument and encrypted with the `--encrypt`
argument.

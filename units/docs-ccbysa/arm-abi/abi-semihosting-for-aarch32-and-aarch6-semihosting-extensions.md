---
id: "abi-semihosting-for-aarch32-and-aarch6-semihosting-extensions"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting extensions"
summary: "The semihosting API provides an extension mechanism. Semihosting implementations can provide optional functionality and advertise to the semihosting caller that they do so. Semihosting callers must check that the implementation supports the optional functionality before attempting to use it."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

The semihosting API provides an extension mechanism. Semihosting implementations can provide optional functionality and advertise to the semihosting caller that they do so. Semihosting callers must check that the implementation supports the optional functionality before attempting to use it.

Each extension that the specification defines has an associated feature bit. If the implementation provides the extension, then it reports the feature bit as 1. Each extension definition identifies the feature bit by which feature byte it is in, and which bit within that byte. For example, feature byte 0, bit 3. Feature bytes and bits within them are both numbered starting from 0, with feature bit 0 being the least significant bit. Extensions are independent. Unless otherwise stated, support for one feature does not imply support for any other feature. The caller must check the feature bit for every feature it wants to use.


### Semihosting feature bit reporting sequence format


Feature bits are reported using a sequence of bytes, which are accessed by using the SYS_OPEN (0x01) call with the special path name `:semihosting-features`. The byte sequence has the following format:

```

byte 0: SHFB_MAGIC_0 0x53
byte 1: SHFB_MAGIC_1 0x48
byte 2: SHFB_MAGIC_2 0x46
byte 3: SHFB_MAGIC_3 0x42
byte 4: feature byte 0
byte 5: feature byte 1
byte 6: feature byte 2
...
```
There is no limit to the number of bytes that can be returned. As future extensions are defined, new bytes will be added. If the read reaches the end of the file before the byte that contains a particular feature bit, then that feature bit must be taken to be 0.

Since the file is a sequence of bytes, the order remains the same whether the processor is big-endian or little-endian. The contents must be treated as a byte array, not an array of words or any other larger type.



### Requirements for semihosting implementations


An implementation that implements any semihosting extensions must do the following:

* Handle the special path name `:semihosting-features` in SYS_OPEN (0x01) when opened with mode 0 (`r`) or 1 (`rb`). Implement it to return a filehandle that behaves as if it were accessing a file containing a sequence of bytes in the format that is described in feature-bits. Attempts to open this special path name with any other opening mode must fail. The implementation must support opening of this special path name multiple times, both consecutively and simultaneously.

* Support the following operations on the filehandle returned from SYS_OPEN (0x01) of `:semihosting-features` :

    SYS_FLEN (0x0C)
          Returns the length of the byte sequence, including the magic number bytes.
    SYS_ISTTY (0x09)
          Always returns 0.
    SYS_SEEK (0x0A)
          Permits random seeks to anywhere within the byte sequence.
    SYS_READ (0x06)
          Reads bytes from the sequence starting from the current seek position.
    SYS_CLOSE (0x02)
          Closes the filehandle.

The special path name does not correspond to a real file in a filesystem, and so no special case handling of it is expected for SYS_REMOVE (0x0E) or SYS_RENAME (0x0F).



### Requirements for semihosting callers


To read the feature bits, the semihosting caller must:

1. Call SYS_OPEN (0x01) with the special filename `:semihosting-features` and the file opening mode 0 (`r`). If the SYS_OPEN (0x01) fails, then no extensions are supported, so all feature bits should be assumed to be 0.

2. Use the SYS_READ (0x06) call to read bytes from the filehandle returned by step 1. If the read returns fewer than 5 bytes, or the first 4 bytes are not the correct magic numbers, then no extensions are supported.

  The caller must check all the magic bytes, but can optionally use SYS_SEEK (0x0A) to seek forwards in the byte sequence to the subsequent byte, or bytes, of interest. Seeking off the end of the file is undefined, so a caller wanting to use SYS_SEEK (0x0A) must first use SYS_FLEN (0x0C) to determine the size of the byte sequence.

3.    If the SYS_OPEN (0x01) from step 1 did not fail, the caller must now use SYS_CLOSE (0x02) to close the filehandle.

It is important to follow this sequence to ensure correct behavior on legacy semihosting implementations, which do not recognize the special filename `:semihosting-features`.



### Example pseudocode function for querying feature bits


The following C-like pseudocode describes one possible simple implementation of a check for a specific feature bit:

```

#define MAGICLEN 4
bool sh_feature_supported(int bytenum, int bitnum)
{
    unsigned char magic[MAGICLEN];
    unsigned char c;
    int fh;
    int len;

    fh = sys_open(":semihosting-features", 0);
    if (fh == -1) {
        return false;
    }
    len = sys_flen(fh);
    if (len <= bytenum) {
        sys_close(fh);
        return false;
    }
    if (sys_read(fh, &magic, MAGICLEN) != 0) {
        sys_close(fh);
        return false;
    }
    if (magic[0] != SHFB_MAGIC_0 ||
        magic[1] != SHFB_MAGIC_1 ||
        magic[2] != SHFB_MAGIC_2 ||
        magic[3] != SHFB_MAGIC_3) {
        sys_close(fh);
        return false;
    }
    if (sys_seek(fh, bytenum) != 0) {
        sys_close(fh);
        return false;
    }
    if (sys_read(fh, &c, 1) != 0) {
        sys_close(fh);
        return false;
    }
    sys_close(fh);
    return (c & (1 << bitnum)) != 0;
}
```
More sophisticated implementations can choose to cache the contents of the start of the file with the magic bytes and the first few bytes of feature bit data. Conversely if, for instance, the caller knows in advance that it is only interested in feature bits inside the first feature byte, it can simplify this method to perform a single 5 byte read and need not call SYS_FLEN (0x0C) or SYS_SEEK (0x0A).



### Semihosting extensions available


The `Semihosting Extensions Table` lists the semihosting extensions currently available, along with their associated feature byte and bit.


+-----------------------------+--------------+-------------+
| Name                        | Feature byte | Feature bit |
+=============================+==============+=============+
| SH_EXT_EXIT_EXTENDED     |            0 |           0 |
+-----------------------------+--------------+-------------+
| SH_EXT_STDOUT_STDERR     |            0 |           1 |
+-----------------------------+--------------+-------------+

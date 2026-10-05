---
id: "lfs-spec-metadata-types"
type: "concept"
domain: "project"
title: "SPEC: Metadata types"
summary: "What follows is an exhaustive list of metadata in littlefs."
status: "draft"
collection: "littlefs"
source: "littlefs-project/littlefs@6cb4e86:SPEC.md"
doc_source: "https://github.com/littlefs-project/littlefs/blob/6cb4e86/SPEC.md#metadata-types"
license: "BSD-3-Clause"
mode: "V"
---

What follows is an exhaustive list of metadata in littlefs.

---
#### `0x401` LFS_TYPE_CREATE

Creates a new file with this id. Note that files in a metadata block
don't necessarily need a create tag. All a create does is move over any
files using this id. In this sense a create is similar to insertion into
an imaginary array of files.

The create and delete tags allow littlefs to keep files in a directory
ordered alphabetically by filename.

---
#### `0x4ff` LFS_TYPE_DELETE

Deletes the file with this id. An inverse to create, this tag moves over
any files neighboring this id similar to a deletion from an imaginary
array of files.

---
#### `0x0xx` LFS_TYPE_NAME

Associates the id with a file name and file type.

The data contains the file name stored as an ASCII string (may be expanded to
UTF8 in the future).

The chunk field in this tag indicates an 8-bit file type which can be one of
the following.

Currently, the name tag must precede any other tags associated with the id and
can not be reassigned without deleting the file.

Layout of the name tag:

```
        tag                          data
[--      32      --][---        variable length        ---]
[1| 3| 8 | 10 | 10 ][---          (size * 8)           ---]
 ^  ^  ^    ^    ^- size                   ^- file name
 |  |  |    '------ id
 |  |  '----------- file type
 |  '-------------- type1 (0x0)
 '----------------- valid bit
```

Name fields:

1. **file type (8-bits)** - Type of the file.

2. **file name** - File name stored as an ASCII string.

---
#### `0x001` LFS_TYPE_REG

Initializes the id + name as a regular file.

How each file is stored depends on its struct tag, which is described below.

---
#### `0x002` LFS_TYPE_DIR

Initializes the id + name as a directory.

Directories in littlefs are stored on disk as a linked-list of metadata pairs,
each pair containing any number of files in alphabetical order. A pointer to
the directory is stored in the struct tag, which is described below.

---
#### `0x0ff` LFS_TYPE_SUPERBLOCK

Initializes the id as a superblock entry.

The superblock entry is a special entry used to store format-time configuration
and identify the filesystem.

The name is a bit of a misnomer. While the superblock entry serves the same
purpose as a superblock found in other filesystems, in littlefs the superblock
does not get a dedicated block. Instead, the superblock entry is duplicated
across a linked-list of metadata pairs rooted on the blocks 0 and 1. The last
metadata pair doubles as the root directory of the filesystem.

```
 .--------.  .--------.  .--------.  .--------.  .--------.
.| super  |->| super  |->| super  |->| super  |->| file B |
|| block  | || block  | || block  | || block  | || file C |
||        | ||        | ||        | || file A | || file D |
|'--------' |'--------' |'--------' |'--------' |'--------'
'--------'  '--------'  '--------'  '--------'  '--------'

\----------------+----------------/ \----------+----------/
          superblock pairs               root directory
```

The filesystem starts with only the root directory. The superblock metadata
pairs grow every time the root pair is compacted in order to prolong the
life of the device exponentially.

The contents of the superblock entry are stored in a name tag with the
superblock type and an inline-struct tag. The name tag contains the magic
string "littlefs", while the inline-struct tag contains version and
configuration information.

Layout of the superblock name tag and inline-struct tag:

```
        tag                          data
[--      32      --][--      32      --|--      32      --]
[1|- 11 -| 10 | 10 ][---              64               ---]
 ^    ^     ^    ^- size (8)           ^- magic string ("littlefs")
 |    |     '------ id (0)
 |    '------------ type (0x0ff)
 '----------------- valid bit

        tag                          data
[--      32      --][--      32      --|--      32      --|--      32      --]
[1|- 11 -| 10 | 10 ][--      32      --|--      32      --|--      32      --]
 ^    ^     ^    ^            ^- version         ^- block size      ^- block count
 |    |     |    |  [--      32      --|--      32      --|--      32      --]
 |    |     |    |  [--      32      --|--      32      --|--      32      --]
 |    |     |    |            ^- name max        ^- file max        ^- attr max
 |    |     |    '- size (24)
 |    |     '------ id (0)
 |    '------------ type (0x201)
 '----------------- valid bit
```

Superblock fields:

1. **Magic string (8-bytes)** - Magic string indicating the presence of
   littlefs on the device. Must be the string "littlefs".

2. **Version (32-bits)** - The version of littlefs at format time. The version
   is encoded in a 32-bit value with the upper 16-bits containing the major
   version, and the lower 16-bits containing the minor version.

   This specification describes version 2.0 (`0x00020000`).

3. **Block size (32-bits)** - Size of the logical block size used by the
   filesystem in bytes.

4. **Block count (32-bits)** - Number of blocks in the filesystem.

5. **Name max (32-bits)** - Maximum size of file names in bytes.

6. **File max (32-bits)** - Maximum size of files in bytes.

7. **Attr max (32-bits)** - Maximum size of file attributes in bytes.

The superblock must always be the first entry (id 0) in the metadata pair, and
the name tag must always be the first tag in the metadata pair. This makes it
so that the magic string "littlefs" will always reside at offset=8 in a valid
littlefs superblock.

---
#### `0x2xx` LFS_TYPE_STRUCT

Associates the id with an on-disk data structure.

The exact layout of the data depends on the data structure type stored in the
chunk field and can be one of the following.

Any type of struct supersedes all other structs associated with the id. For
example, appending a ctz-struct replaces an inline-struct on the same file.

---
#### `0x200` LFS_TYPE_DIRSTRUCT

Gives the id a directory data structure.

Directories in littlefs are stored on disk as a linked-list of metadata pairs,
each pair containing any number of files in alphabetical order.

```
     |
     v
 .--------.  .--------.  .--------.  .--------.  .--------.  .--------.
.| file A |->| file D |->| file G |->| file I |->| file J |->| file M |
|| file B | || file E | || file H | ||        | || file K | || file N |
|| file C | || file F | ||        | ||        | || file L | ||        |
|'--------' |'--------' |'--------' |'--------' |'--------' |'--------'
'--------'  '--------'  '--------'  '--------'  '--------'  '--------'
```

The dir-struct tag contains only the pointer to the first metadata-pair in the
directory. The directory size is not known without traversing the directory.

The pointer to the next metadata-pair in the directory is stored in a tail tag,
which is described below.

Layout of the dir-struct tag:

```
        tag                          data
[--      32      --][--      32      --|--      32      --]
[1|- 11 -| 10 | 10 ][---              64               ---]
 ^    ^     ^    ^- size (8)           ^- metadata pair
 |    |     '------ id
 |    '------------ type (0x200)
 '----------------- valid bit
```

Dir-struct fields:

1. **Metadata pair (8-bytes)** - Pointer to the first metadata-pair
   in the directory.

---
#### `0x201` LFS_TYPE_INLINESTRUCT

Gives the id an inline data structure.

Inline structs store small files that can fit in the metadata pair. In this
case, the file data is stored directly in the tag's data area.

Layout of the inline-struct tag:

```
        tag                          data
[--      32      --][---        variable length        ---]
[1|- 11 -| 10 | 10 ][---           (size * 8)          ---]
 ^    ^     ^    ^- size                    ^- inline data
 |    |     '------ id
 |    '------------ type (0x201)
 '----------------- valid bit
```

Inline-struct fields:

1. **Inline data** - File data stored directly in the metadata-pair.

---
#### `0x202` LFS_TYPE_CTZSTRUCT

Gives the id a CTZ skip-list data structure.

CTZ skip-lists store files that can not fit in the metadata pair. These files
are stored in a skip-list in reverse, with a pointer to the head of the
skip-list. Note that the head of the skip-list and the file size is enough
information to read the file.

How exactly CTZ skip-lists work is a bit complicated. A full explanation can be
found in the [DESIGN.md](https://github.com/littlefs-project/littlefs/blob/6cb4e86/DESIGN.md#ctz-skip-lists).

A quick summary: For every _n_‍th block where _n_ is divisible by
2‍_ˣ_, that block contains a pointer to block _n_-2‍_ˣ_.
These pointers are stored in increasing order of _x_ in each block of the file
before the actual data.

```
                                                               |
                                                               v
.--------.  .--------.  .--------.  .--------.  .--------.  .--------.
| A      |<-| D      |<-| G      |<-| J      |<-| M      |<-| P      |
| B      |<-| E      |--| H      |<-| K      |--| N      |  | Q      |
| C      |<-| F      |--| I      |--| L      |--| O      |  |        |
'--------'  '--------'  '--------'  '--------'  '--------'  '--------'
  block 0     block 1     block 2     block 3     block 4     block 5
              1 skip      2 skips     1 skip      3 skips     1 skip
```

Note that the maximum number of pointers in a block is bounded by the maximum
file size divided by the block size. With 32 bits for file size, this results
in a minimum block size of 104 bytes.

Layout of the CTZ-struct tag:

```
        tag                          data
[--      32      --][--      32      --|--      32      --]
[1|- 11 -| 10 | 10 ][--      32      --|--      32      --]
 ^    ^     ^    ^            ^                  ^- file size
 |    |     |    |            '-------------------- file head
 |    |     |    '- size (8)
 |    |     '------ id
 |    '------------ type (0x202)
 '----------------- valid bit
```

CTZ-struct fields:

1. **File head (32-bits)** - Pointer to the block that is the head of the
   file's CTZ skip-list.

2. **File size (32-bits)** - Size of the file in bytes.

---
#### `0x3xx` LFS_TYPE_USERATTR

Attaches a user attribute to an id.

littlefs has a concept of "user attributes". These are small user-provided
attributes that can be used to store things like timestamps, hashes,
permissions, etc.

Each user attribute is uniquely identified by an 8-bit type which is stored in
the chunk field, and the user attribute itself can be found in the tag's data.

There are currently no standard user attributes and a portable littlefs
implementation should work with any user attributes missing.

Layout of the user-attr tag:

```
        tag                          data
[--      32      --][---        variable length        ---]
[1| 3| 8 | 10 | 10 ][---           (size * 8)          ---]
 ^  ^  ^    ^    ^- size                    ^- attr data
 |  |  |    '------ id
 |  |  '----------- attr type
 |  '-------------- type1 (0x3)
 '----------------- valid bit
```

User-attr fields:

1. **Attr type (8-bits)** - Type of the user attributes.

2. **Attr data** - The data associated with the user attribute.

---
#### `0x6xx` LFS_TYPE_TAIL

Provides the tail pointer for the metadata pair itself.

The metadata pair's tail pointer is used in littlefs for a linked-list
containing all metadata pairs. The chunk field contains the type of the tail,
which indicates if the following metadata pair is a part of the directory
(hard-tail) or only used to traverse the filesystem (soft-tail).

```
         .--------.
        .| dir A  |-.
        ||softtail| |
.--------|        |-'
|       |'--------'
|       '---|--|-'
|        .-'    '-------------.
|       v                      v
|  .--------.  .--------.  .--------.
'->| dir B  |->| dir B  |->| dir C  |
  ||hardtail| ||softtail| ||        |
  ||        | ||        | ||        |
  |'--------' |'--------' |'--------'
  '--------'  '--------'  '--------'
```

Currently any type supersedes any other preceding tails in the metadata pair,
but this may change if additional metadata pair state is added.

A note about the metadata pair linked-list: Normally, this linked-list contains
every metadata pair in the filesystem. However, there are some operations that
can cause this linked-list to become out of sync if a power-loss were to occur.
When this happens, littlefs sets the "sync" flag in the global state. How
exactly this flag is stored is described below.

When the sync flag is set:

1. The linked-list may contain an orphaned directory that has been removed in
   the filesystem.
2. The linked-list may contain a metadata pair with a bad block that has been
   replaced in the filesystem.

If the sync flag is set, the threaded linked-list must be checked for these
errors before it can be used reliably. Note that the threaded linked-list can
be ignored if littlefs is mounted read-only.

Layout of the tail tag:

```
        tag                          data
[--      32      --][--      32      --|--      32      --]
[1| 3| 8 | 10 | 10 ][---              64               ---]
 ^  ^  ^   ^    ^- size (8)            ^- metadata pair
 |  |  |   '------ id
 |  |  '---------- tail type
 |  '------------- type1 (0x6)
 '---------------- valid bit
```

Tail fields:

1. **Tail type (8-bits)** - Type of the tail pointer.

2. **Metadata pair (8-bytes)** - Pointer to the next metadata-pair.

---
#### `0x600` LFS_TYPE_SOFTTAIL

Provides a tail pointer that points to the next metadata pair in the
filesystem.

In this case, the next metadata pair is not a part of our current directory
and should only be followed when traversing the entire filesystem.

---
#### `0x601` LFS_TYPE_HARDTAIL

Provides a tail pointer that points to the next metadata pair in the
directory.

In this case, the next metadata pair belongs to the current directory. Note
that because directories in littlefs are sorted alphabetically, the next
metadata pair should only contain filenames greater than any filename in the
current pair.

---
#### `0x7xx` LFS_TYPE_GSTATE

Provides delta bits for global state entries.

littlefs has a concept of "global state". This is a small set of state that
can be updated by a commit to _any_ metadata pair in the filesystem.

The way this works is that the global state is stored as a set of deltas
distributed across the filesystem such that the global state can be found by
the xor-sum of these deltas.

```
 .--------.  .--------.  .--------.  .--------.  .--------.
.|        |->| gdelta |->|        |->| gdelta |->| gdelta |
||        | || 0x23   | ||        | || 0xff   | || 0xce   |
||        | ||        | ||        | ||        | ||        |
|'--------' |'--------' |'--------' |'--------' |'--------'
'--------'  '----|---'  '--------'  '----|---'  '----|---'
                 v                       v           v
       0x00 --> xor ------------------> xor ------> xor --> gstate = 0x12
```

Note that storing globals this way is very expensive in terms of storage usage,
so any global state should be kept very small.

The size and format of each piece of global state depends on the type, which
is stored in the chunk field. Currently, the only global state is move state,
which is outlined below.

---
#### `0x7ff` LFS_TYPE_MOVESTATE

Provides delta bits for the global move state.

The move state in littlefs is used to store info about operations that could
cause to filesystem to go out of sync if the power is lost. The operations
where this could occur is moves of files between metadata pairs and any
operation that changes metadata pairs on the threaded linked-list.

In the case of moves, the move state contains a tag + metadata pair describing
the source of the ongoing move. If this tag is non-zero, that means that power
was lost during a move, and the file exists in two different locations. If this
happens, the source of the move should be considered deleted, and the move
should be completed (the source should be deleted) before any other write
operations to the filesystem.

In the case of operations to the threaded linked-list, a single "sync" bit is
used to indicate that a modification is ongoing. If this sync flag is set, the
threaded linked-list will need to be checked for errors before it can be used
reliably. The exact cases to check for are described above in the tail tag.

Layout of the move state:

```
        tag                                    data
[--      32      --][--      32      --|--      32      --|--      32      --]
[1|- 11 -| 10 | 10 ][1|- 11 -| 10 | 10 |---              64               ---]
 ^    ^     ^    ^   ^    ^     ^    ^- padding (0)       ^- metadata pair
 |    |     |    |   |    |     '------ move id
 |    |     |    |   |    '------------ move type
 |    |     |    |   '----------------- sync bit
 |    |     |    |
 |    |     |    '- size (12)
 |    |     '------ id (0x3ff)
 |    '------------ type (0x7ff)
 '----------------- valid bit
```

Move state fields:

1. **Sync bit (1-bit)** - Indicates if the metadata pair threaded linked-list
   is in-sync. If set, the threaded linked-list should be checked for errors.

2. **Move type (11-bits)** - Type of move being performed. Must be either
   `0x000`, indicating no move, or `0x4ff` indicating the source file should
   be deleted.

3. **Move id (10-bits)** - The file id being moved.

4. **Metadata pair (8-bytes)** - Pointer to the metadata-pair containing
   the move.

---
#### `0x5xx` LFS_TYPE_CRC

Last but not least, the CRC tag marks the end of a commit and provides a
checksum for any commits to the metadata block.

The first 32-bits of the data contain a CRC-32 with a polynomial of
`0x04c11db7` initialized with `0xffffffff`. This CRC provides a checksum for
all metadata since the previous CRC tag, including the CRC tag itself. For
the first commit, this includes the revision count for the metadata block.

However, the size of the data is not limited to 32-bits. The data field may
larger to pad the commit to the next program-aligned boundary.

In addition, the CRC tag's chunk field contains a set of flags which can
change the behaviour of commits. Currently the only flag in use is the lowest
bit, which determines the expected state of the valid bit for any following
tags. This is used to guarantee that unwritten storage in a metadata block
will be detected as invalid.

Layout of the CRC tag:

```
        tag                                    data
[--      32      --][--      32      --|---        variable length        ---]
[1| 3| 8 | 10 | 10 ][--      32      --|---        (size * 8 - 32)        ---]
 ^  ^  ^    ^    ^            ^- crc                             ^- padding
 |  |  |    |    '- size
 |  |  |    '------ id (0x3ff)
 |  |  '----------- valid state
 |  '-------------- type1 (0x5)
 '----------------- valid bit
```

CRC fields:

1. **Valid state (1-bit)** - Indicates the expected value of the valid bit for
   any tags in the next commit.

2. **CRC (32-bits)** - CRC-32 with a polynomial of `0x04c11db7` initialized
   with `0xffffffff`.

3. **Padding** - Padding to the next program-aligned boundary. No guarantees
   are made about the contents.

---
#### `0x5ff` LFS_TYPE_FCRC

Added in lfs2.1, the optional FCRC tag contains a checksum of some amount of
bytes in the next commit at the time it was erased. This allows us to ensure
that we only ever program erased bytes, even if a previous commit failed due
to power-loss.

When programming a commit, the FCRC size must be at least as large as the
program block size. However, the program block is not saved on disk, and can
change between mounts, so the FCRC size on disk may be different than the
current program block size.

If the FCRC is missing or the checksum does not match, we must assume a
commit was attempted but failed due to power-loss.

Layout of the FCRC tag:

```
        tag                          data
[--      32      --][--      32      --|--      32      --]
[1|- 11 -| 10 | 10 ][--      32      --|--      32      --]
 ^    ^     ^    ^            ^- fcrc size       ^- fcrc
 |    |     |    '- size (8)
 |    |     '------ id (0x3ff)
 |    '------------ type (0x5ff)
 '----------------- valid bit
```

FCRC fields:

1. **FCRC size (32-bits)** - Number of bytes after this commit's CRC tag's
   padding to include in the FCRC.

2. **FCRC (32-bits)** - CRC of the bytes after this commit's CRC tag's padding
   when erased. Like the CRC tag, this uses a CRC-32 with a polynomial of
   `0x04c11db7` initialized with `0xffffffff`.

---

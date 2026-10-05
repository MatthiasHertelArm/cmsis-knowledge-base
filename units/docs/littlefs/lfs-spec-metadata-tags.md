---
id: "lfs-spec-metadata-tags"
type: "concept"
domain: "project"
title: "SPEC: Metadata tags"
summary: "So in littlefs, 32-bit tags describe every type of metadata. And this means every type of metadata, including file entries, directory fields, and global state. Even the CRCs used to mark the end of commits get their own tag."
status: "draft"
collection: "littlefs"
source: "littlefs-project/littlefs@6cb4e86:SPEC.md"
doc_source: "https://github.com/littlefs-project/littlefs/blob/6cb4e86/SPEC.md#metadata-tags"
license: "BSD-3-Clause"
mode: "V"
---

So in littlefs, 32-bit tags describe every type of metadata. And this means
_every_ type of metadata, including file entries, directory fields, and
global state. Even the CRCs used to mark the end of commits get their own tag.

Because of this, the tag format contains some densely packed information. Note
that there are multiple levels of types which break down into more info:

```
[----            32             ----]
[1|--  11   --|--  10  --|--  10  --]
 ^.     ^     .     ^          ^- length
 |.     |     .     '------------ id
 |.     '-----.------------------ type (type3)
 '.-----------.------------------ valid bit
  [-3-|-- 8 --]
    ^     ^- chunk
    '------- type (type1)
```


Before we go further, there's one important thing to note. These tags are
**not** stored in little-endian. Tags stored in commits are actually stored
in big-endian (and is the only thing in littlefs stored in big-endian). This
little bit of craziness comes from the fact that the valid bit must be the
first bit in a commit, and when converted to little-endian, the valid bit finds
itself in byte 4. We could restructure the tag to store the valid bit lower,
but, because none of the fields are byte-aligned, this would be more
complicated than just storing the tag in big-endian.

Another thing to note is that both the tags `0x00000000` and `0xffffffff` are
invalid and can be used for null values.

Metadata tag fields:

1. **Valid bit (1-bit)** - Indicates if the tag is valid.

2. **Type3 (11-bits)** - Type of the tag. This field is broken down further
   into a 3-bit abstract type and an 8-bit chunk field. Note that the value
   `0x000` is invalid and not assigned a type.

    1. **Type1 (3-bits)** - Abstract type of the tag. Groups the tags into
       8 categories that facilitate bitmasked lookups.

    2. **Chunk (8-bits)** - Chunk field used for various purposes by the different
       abstract types.  type1+chunk+id form a unique identifier for each tag in the
       metadata block.

3. **Id (10-bits)** - File id associated with the tag. Each file in a metadata
   block gets a unique id which is used to associate tags with that file. The
   special value `0x3ff` is used for any tags that are not associated with a
   file, such as directory and global metadata.

4. **Length (10-bits)** - Length of the data in bytes. The special value
   `0x3ff` indicates that this tag has been deleted.

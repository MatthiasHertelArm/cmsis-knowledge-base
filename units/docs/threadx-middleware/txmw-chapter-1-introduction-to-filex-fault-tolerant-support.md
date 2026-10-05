---
id: "txmw-chapter-1-introduction-to-filex-fault-tolerant-support"
type: "concept"
domain: "rtos"
title: "Chapter 1 - Introduction to FileX: Fault Tolerant Support"
summary: "The FileX Fault Tolerant Module is designed to prevent file system corruption caused by interruptions during the file or directory update."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter1.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter1.md#fault-tolerant-support"
license: "MIT"
mode: "V"
---

The FileX Fault Tolerant Module is designed to prevent file system corruption caused by interruptions during the file or directory update. For example, when appending data to a file, FileX needs to update the content of the file, the directory entry, and possibly the FAT entries. If this sequence of update is interrupted (such as power glitch, or the media is ejected in the middle of the update), the file system is in an inconsistent state, which may affect the integrity of the entire file system, leading towards corruption of other files.

The FileX Fault Tolerant Module works by recording all steps required to update a file or a directory along the way. This log entry is stored on the media in dedicated sectors (blocks) that FileX can find and access. The location of the log data can be accessed even without a proper file system. Therefore, in case the file system is corrupted, FileX is still able to find the log entry and restore the file system back into a good state.

As FileX updates file or directory, log entries are created. After the update operation is successfully completed, the log entries are removed. If the log entries were not properly removed after a successful file update, if the recovery process determines that the content in the log entry matches the file system, nothing needs to be done, and the log entries can be cleaned up.

In case the file system update operation was interrupted, next time the media is mounted by FileX, the Fault Tolerant Module analyzes the log entries. The information in the log entries allows FileX to back out partial changes already applied to the file system (in case the failure happens during the early stage of the file update operation), or if the log entries contain re-do information, FileX is able to apply the changes required to finish the prior operation.

This fault tolerant feature is available to all FAT file systems supported by FileX, including FAT12, FAT16, and FAT32. By default fault tolerant is not enabled in FileX. To enable the fault tolerant feature, FileX must be built with the symbol **FX_ENABLE_FAULT_TOLERANT** and **FX_FAULT_TOLERANT** defined. At run time, the application starts fault tolerant service by calling **_fx_fault_tolerant_enable_**.
After the service starts, all file and directory write operations go through the Fault Tolerant Module.

As fault tolerant service starts, it first detects whether or not the media is protected under the Fault Tolerant Module. If it is not, FileX assumes integrity of the file system, and starts protection by allocating free blocks from the file system to be used for logging and caching. If the Fault Tolerant Module logs are found on the file system, it analyzes the log entries. FileX reverts the prior operation or redoes the prior operation, depending on the content of the log entries. The file system becomes available after all the prior log entries are processed. This ensures that FIleX starts from a known good state.

After a media is protected under the FileX Fault Tolerant Module, the media will not be updated with another file system. Doing so would leave the log entries on the file system inconsistent with the contents in the FAT table, the directory entry. If the media is updated by another file system before moving it back to FileX with the Fault Tolerant Module, the result is undefined.

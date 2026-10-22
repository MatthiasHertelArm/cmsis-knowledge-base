---
id: "zep-semihosting-guide-file-operations"
type: "concept"
domain: "rtos"
title: "Semihosting Guide: File Operations"
summary: "Semihosting enables files on the host computer to be opened, read, and modified by an application."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/hardware/arch/semihost.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/hardware/arch/semihost.rst"
license: "Apache-2.0"
mode: "V"
---

Semihosting enables files on the host computer to be opened, read, and modified
by an application. This can be useful when attempting to validate the behaviour
of code across datasets that are larger than what can fit into ROM of an
emulated platform. File paths can be either absolute, or relative to the
directory of the running process.

```c

const char *path = "./data.bin";
long file_len, bytes_read, fd;
uint8_t buffer[16];

/* Open the data file for reading */
fd = semihost_open(path, SEMIHOST_OPEN_RB);
if (fd < 0) {
   return -ENOENT;
}
/* Read all data from the file */
file_len = semihost_flen(fd);
while(file_len > 0) {
   bytes_read = semihost_read(fd, buffer, MIN(file_len, sizeof(buffer)));
   if (bytes_read < 0) {
      break;
   }
   /* Process read data */
   do_data_processing(buffer, bytes_read);
   /* Update remaining length */
   file_len -= bytes_read;
}
/* Close the file */
semihost_close(fd);
```

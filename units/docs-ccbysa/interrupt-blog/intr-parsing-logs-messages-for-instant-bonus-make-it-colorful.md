---
id: "intr-parsing-logs-messages-for-instant-bonus-make-it-colorful"
type: "concept"
domain: "debug"
title: "Parsing Logs Messages for Instant Crash Analysis: 🌈 Bonus: Make it Colorful"
summary: "I have long been using the same Python script to print out the log messages."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-08-04-firmware-logs-stack-trace.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-logs-stack-trace#bonus-make-it-colorful"
license: "CC-BY-SA-4.0"
mode: "V"
---

I have long been using the same Python script to print out the log messages. This one is making things clear by printing the host date, the target date (and the difference between the two), the active tasks count, the filename and line the message is being printed from, all of this using colors!

Here is a snippet of the log after a pin reset. We can see the main product information as an example. I synced the time using an Android application before the reset but we can still see the internal clock being 2 seconds behind the host clock, This is because of the pin reset which takes time for that specific application. Depending on the log level, colors like green, orange, and red are used.


2020-07-26 11:08:13.040 [1595754491 **(-2.041s)**:0:../../main.c:643] ⚡ My awesome product
2020-07-26 11:08:13.042 [1595754491 **(-2.042s)**:0:../../main.c:644] ID: 0x1a9d1d52
2020-07-26 11:08:13.043 [1595754491 **(-2.044s)**:0:../../main.c:647] FW rev: 2.10.4 DEV
2020-07-26 11:08:13.044 [1595754491 **(-2.045s)**:0:../../main.c:654] BL rev: 5
2020-07-26 11:08:13.045 [1595754491 **(-2.046s)**:0:../../main.c:656] HW rev: 1
2020-07-26 11:08:13.047 [1595754491 **(-2.048s)**:0:../../main.c:658] Git branch: master commit:0x70954c0c
2020-07-26 11:08:13.049 [1595754491 **(-2.049s)**:0:../../main.c:659] WDT active: true
2020-07-26 11:08:13.072 [1595754491 **(-2.072s)**:0:../../main.c:330] Reset: Pin reset
2020-07-26 11:08:13.390 [1595754491 **(-2.390s)**:0:../../main.c:285] RAM_START: 0x20002558
2020-07-26 11:08:13.392 [1595754491 **(-2.392s)**:0:../../main.c:702] BT address: e2:f2:78:ad:a1:da
2020-07-26 11:08:13.400 [1595754491 **(-2.400s)**:4:../../device_settings.c:523] Writing device setting (#18, 617)
2020-07-26 11:08:13.800 [1595754491 **(-2.800s)**:3:../../device_settings.c:365] Device setting #18 written
[...]


The Python script is not the only piece needed to print such a beautiful log obviously. On the target side, I have to send the information to print. Macros are used to make it easier to print *upgraded* messages. You will find those two files in my Github repo[^log_files_example] if you want to use them.

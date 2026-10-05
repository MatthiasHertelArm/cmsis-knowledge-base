---
id: "intr-firmware-static-analysis-with-code-running-the-analysis"
type: "concept"
domain: "debug"
title: "Firmware Static Analysis with CodeChecker: Running the analysis"
summary: "CodeChecker uses a very neat technique to instrument your builds: it wraps your existing compiler and keeps track of what files are compiled in what order."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-05-19-static-analysis-with-codechecker.md"
doc_source: "https://interrupt.memfault.com/blog/static-analysis-with-codechecker#running-the-analysis"
license: "CC-BY-SA-4.0"
mode: "V"
---

CodeChecker uses a very neat technique to instrument your builds: it wraps your
existing compiler and keeps track of what files are compiled in what order.
This means that you do not need to setup a separate compiler or build target.

To get started, make sure you’ve sourced the virtual env:

```
$ source ~/codechecker/venv/bin/activate
```

Next set up the `CC_LOGGER_GCC_LIKE` environment variable to let CodeChecker
know that `arm-none-eabi-gcc` is just another GCC build.

```
$ export CC_LOGGER_GCC_LIKE=arm-none-eabi-gcc
```

You can now run the  `CodeChecker log`  command and pass it our standard build
invocation as an argument. Make sure you clean your build first, as any file
skipped in the rebuild will be ignored by CodeChecker:

```
$ make clean
$ CodeChecker log -b "make -f make/stm32f769_discovery.make" -o compilation.json
[INFO 2021-05-18 05:34] - Starting build ...
[... standard build output for your project ...]
[INFO 2021-05-18 05:34] - Build finished successfully.
```

This will produce a `compilation.json` file which contains the list of build
commands you’ve just executed.

Next, we must run the analysis itself. This is done with the `analyze` command,
which can be configured in a number of way. I will cover two of them:
1. `--enable [default | sensitive | extreme]` selects the sensitivity of the
   analysis. What it does under the hood is enable/disable individual checkers
   based on their false-positive rate. I recommend `sensitive`.
2. `--ctu`  enables cross-translation-unit analysis. A translation unit is a
   single C file, so without this flag the analysis only consider files one at
   a time. It is therefore not able to trace bugs that happen when functions
   from different files are used together. Enable CTU solves this issue, at the
   cost of a slower analysis run.

Putting those together, we get:

```
CodeChecker analyze ./compilation.json --output ./reports --enable sensitive --ctu
```

You might want to go grab yourself a coffee while this run, it can be pretty
slow!

This command will create the `reports` folder with the output from your
analysis.

Note that CodeChecker can be run incrementally. For example, if we make a
change in a single file, we can re-run the `log` and `analyze` commands, they
will analyze that file only and update the data in `reports`.

### Inspecting the results

Our reports are not yet human readable. To make sense of them, we finally use
the `parse` command.

```
CodeChecker parse ./reports --print-steps
[...]
----==== Summary ====----
[...]
-----------------------
Severity | Report count
-----------------------
MEDIUM   |           77
LOW      |           44
HIGH     |           24
-----------------------
----=================----
Total number of reports: 145
----=================----
```

As you can see, we’ve found 145 issues in our project, including 24 high
severity issues (mostly uninitialized variables being used and null pointer
dereferences).

With `--print-steps` we told the tool to print-out the execution steps to get
to the error. Inspecting this output, we can immediately see some real issues!

```
[HIGH] /root/ChibiOS/demos/STM32/RT-STM32-LWIP-FATFS-USB/source/web.c:57:15: The left operand of '>=' is a garbage value [core.UndefinedBinaryOperatorResult]
    if (buflen>=5 &&
              ^
  Report hash: 5976a48b4e0090847228a1fce0f5791a
  Steps:
     1, web.c:110:10: Entering loop body
     2, web.c:114:5: Calling 'http_server_serve'
     3, web.c:42:1: Entered call from 'http_server'
     4, web.c:45:3: 'buflen' declared without an initial value
     5, web.c:53:5: Calling 'netbuf_data'
     6, netbuf.c:195:1: Entered call from 'http_server_serve'
     7, netbuf.c:202:7: Assuming field 'ptr' is equal to NULL
     8, netbuf.c:203:5: Returning without writing to '*len'
     9, web.c:53:5: Returning from 'netbuf_data'
    10, web.c:57:15: The left operand of '>=' is a garbage value

Found 1 defect(s) in web.c
```

Let’s take a look at this code in more detail. You can find it on Github at
[ChibiOS/web.c at master · ChibiOS/ChibiOS ·
GitHub](https://github.com/ChibiOS/ChibiOS/blob/master/demos/STM32/RT-STM32-LWIP-FATFS-USB/source/web.c#L57).

```c
static void http_server_serve(struct netconn *conn) {
  struct netbuf *inbuf;
  char *buf;
  u16_t buflen;
  err_t err;

  /* Read the data from the port, blocking if nothing yet there.
   We assume the request (the part we care about) is in one netbuf */
  err = netconn_recv(conn, &inbuf);

  if (err == ERR_OK) {
    netbuf_data(inbuf, (void **)&buf, &buflen);

    /* Is this an HTTP GET command? (only check the first 5 chars, since
    there are other formats for GET, and we're keeping it very simple )*/
    if (buflen>=5 &&
        buf[0]=='G' &&
        buf[1]=='E' &&
        buf[2]=='T' &&
        buf[3]==' ' &&
        buf[4]=='/' ) {
...
```

Indeed we can see that the code does not check the return value of
`netbuf_data`, and in the event that function returns an error, `buflen` ends
up uninitialized. The fix is simple:

```diff
diff --git a/demos/STM32/RT-STM32-LWIP-FATFS-USB/source/web.c b/demos/STM32/RT-STM32-LWIP-FATFS-USB/source/web.c
index d2a8de056..61d8c4d73 100644
--- a/demos/STM32/RT-STM32-LWIP-FATFS-USB/source/web.c
+++ b/demos/STM32/RT-STM32-LWIP-FATFS-USB/source/web.c
@@ -50,16 +50,17 @@ static void http_server_serve(struct netconn *conn) {
   err = netconn_recv(conn, &inbuf);

   if (err == ERR_OK) {
-    netbuf_data(inbuf, (void **)&buf, &buflen);
+    err_t err = netbuf_data(inbuf, (void **)&buf, &buflen);

     /* Is this an HTTP GET command? (only check the first 5 chars, since
     there are other formats for GET, and we're keeping it very simple )*/
-    if (buflen>=5 &&
+    if (!err && (
+        buflen>=5 &&
         buf[0]=='G' &&
         buf[1]=='E' &&
         buf[2]=='T' &&
         buf[3]==' ' &&
-        buf[4]=='/' ) {
+        buf[4]=='/' )) {
```

We can now rerun our analysis:

```bash
(CodeChecker venv) $ CodeChecker log -b "make -f make/stm32f769_discovery.make" -o compilation.json
[INFO 2021-05-18 06:15] - Starting build ...
Compiling web.c
[...]
[INFO 2021-05-18 06:15] - Build finished successfully.

$ CodeChecker analyze ./compilation.json --output ./reports     --enable sensitive --ctu
[...]
[INFO 2021-05-18 06:15] - ----==== Summary ====----
[INFO 2021-05-18 06:15] - Successfully analyzed
[INFO 2021-05-18 06:15] -   clang-tidy: 1
[INFO 2021-05-18 06:15] -   clangsa: 1
[INFO 2021-05-18 06:15] - Reanalyzed compilation commands: 2
[INFO 2021-05-18 06:15] - Total analyzed compilation commands: 1
[INFO 2021-05-18 06:15] - ----=================----
[...]
[INFO 2021-05-18 06:15] - Analysis length: 0.5719277858734131 sec.
```

Thanks to incremental updates, this was very fast (0.5s)! CodeChecker no longer
finds issues in `web.c`:

```
$ CodeChecker parse ./reports-ctu-3 --print-steps | grep web.c
Found no defects in web.c
```

### HTML Export

Wading through reports on the command line is not very ergonomic, so I
recommend you export the reports to HTML. This can be achieved with the
`--export html` flag within the `parse` command:

```
$ CodeChecker parse --export html --output ./reports_html ./reports
```

You can then open the resulting `reports_html/index.html` with your browser of
choice. This will give you a nice HTML UI with a list of all the defects, and
detailed views such as this one:



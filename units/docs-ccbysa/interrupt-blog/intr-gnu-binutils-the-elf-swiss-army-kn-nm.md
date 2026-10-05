---
id: "intr-gnu-binutils-the-elf-swiss-army-kn-nm"
type: "concept"
domain: "debug"
title: "GNU Binutils: the ELF Swiss Army Knife: GNU Binutil Command Examples / nm"
summary: "nm lets you inspect the locations and sizes of symbols within a binary. It can be a quick way to find the address of particular symbols or identify which symbols are taking up the most space in a binary."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-04-08-gnu-binutils.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-binutils#nm"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: GNU Binutil Command Examples_

`nm` lets you inspect the locations and sizes of symbols within a binary. It can be a quick way to
find the address of particular symbols or identify which symbols are taking up the most space in a
binary.

The default output looks like this:

```bash
arm-none-eabi-nm  build/zephyr/zephyr.elf
# symbol address | section type | symbol name |
080107cc T z_unpend_thread_no_timeout
080009e0 T z_vprintk
0800c2b2 T z_work_q_main
```

#### Decoding nm Section Type

The section type is a one character shorthand where:

| Shorthand | Type |
| `t` or `T` | text symbol |
| `r` or `R` | read only data symbol |
| `d` or `D` | read/write data symbol |
| `b` or `B` | BSS / Zero initialized symbol |

Letters are capitalized if the symbol is global and lower case if the symbols are private to
the compilation unit (i.e a static in a C file).

#### Useful arguments

- `-S` - print the size of the symbol
- `-l` - print the line number
- `--size-sort` - sort the symbols by size and display the sizes.
- `-t` - change the radix. For example numbers can be displayed in decimal instead of hex by using
  `-t dec`

#### Finding Largest Symbols

We can use `nm` to quickly identify what the largest objects in the binary are. When doing this, I
like to change the radix to decimal and use the `--size-sort` argument. Let's try it out:

```bash
$ arm-none-eabi-nm --size-sort -t dec -l  build/zephyr/zephyr.elf
[...]
00002048 B rx_stack	subsys/net/ip/net_tc.c:28
00002048 b shell_uart_stack	subsys/shell/shell_uart.c:24
00002048 B tx_stack	subsys/net/ip/net_tc.c:22
00002560 b net_buf_data_rx_bufs	subsys/net/ip/net_pkt.c:117
00002560 b net_buf_data_tx_bufs	subsys/net/ip/net_pkt.c:119
00002564 b eswifi0	drivers/wifi/eswifi/eswifi_core.c:37
```

#### Finding Largest Functions

We can also pipe the result into grep to get largest sizes by section type. For example, to limit
our search to text sections:

```bash
$ arm-none-eabi-nm --size-sort -t dec -l  build/zephyr/zephyr.elf  |
   grep " t " -i
[...]
00000702 T __udivmoddi4
00000796 t eswifi_request_work	zephyr/drivers/wifi/eswifi/eswifi_core.c:322
00000806 T z_vprintk	zephyr/lib/os/printk.c:104
00001898 T shell_process	zephyr/subsys/shell/shell.c:1292
00001978 T z_prf	zephyr/lib/libc/minimal/source/stdout/prf.c:446
```

#### Computing Code Size of a Single C File

We can further pipe our results into a CLI command like `awk` to sum totals and compute the codesize
of a single object file. For example, let's look at `lib/os/printk.c`:

```bash
$ arm-none-eabi-nm  -l --size-sort -t dec build/zephyr/zephyr.elf |
  grep " t .*printk\.c" -i | cut -d ' ' -f 1 |
  awk '{total += $0} END{print "sum="total}'
sum=1180
```

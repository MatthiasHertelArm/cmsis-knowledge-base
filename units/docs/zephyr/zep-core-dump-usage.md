---
id: "zep-core-dump-usage"
type: "concept"
domain: "debug"
title: "Core Dump: Usage"
summary: "When the core dump module is enabled, during a fatal error, CPU registers and memory content are printed or stored according to which backends are enabled."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/debugging/coredump.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/debugging/coredump.rst"
license: "Apache-2.0"
mode: "V"
---

When the core dump module is enabled, during a fatal error, CPU registers
and memory content are printed or stored according to which backends
are enabled. This core dump data can be fed into a custom-made GDB server as
a remote target for GDB (and other GDB compatible debuggers). CPU registers,
memory content and stack can be examined in the debugger.

This usually involves the following steps:

1. Get the core dump log from the device depending on enabled backends.
   For example, if the log module backend is used, get the log output
   from the log module backend.

2. Convert the core dump log into a binary format that can be parsed by
   the GDB server. For example,
   `scripts/coredump/coredump_serial_log_parser.py` can be used
   to convert the serial console log into a binary file.
   If the UDP coredump backend is enabled
   (`DEBUG_COREDUMP_BACKEND_LOGGING_UDP`), run
   `scripts/coredump/coredump_udp_receiver.py` on the collector
   host to reassemble UDP datagrams into the **same** raw binary format.

3. Start the custom GDB server using the script
   `scripts/coredump/coredump_gdbserver.py` with the core dump
   binary log file, and the Zephyr ELF file as parameters. The GDB server
   can also be started from within GDB, see below.

4. Start the debugger corresponding to the target architecture.


**Note:** Developers for Intel ADSP CAVS 15-25 platforms using `ZEPHYR_TOOLCHAIN_VARIANT=zephyr` should use the debugger in the `xtensa-intel_apl_adsp` toolchain of the SDK.

5. When `DEBUG_COREDUMP_BACKEND_FLASH_PARTITION` is enabled the core dump
   data is stored in the flash partition. The flash partition must be defined
   in the device tree:

```devicetree

&flash0 {
   partitions {
      coredump_partition: partition@255000 {
         label = "coredump-partition";
         reg = <0x255000 DT_SIZE_K(4)>;
      };
   };
};
```

### Example


This example uses the log module backend tied to serial console.
This was done on qemu_x86 where a null pointer was dereferenced.

This is the core dump log from the serial console, and is stored
in `coredump.log`:

:
```
Booting from ROM..*** Booting Zephyr OS build zephyr-v2.3.0-1840-g7bba91944a63  ***
Hello World! qemu_x86
E: Page fault at address 0x0 (error code 0x2)
E: Linear address not present in page tables
E:   PDE: 0x0000000000115827 Writable, User, Execute Enabled
E:   PTE: Non-present
E: EAX: 0x00000000, EBX: 0x00000000, ECX: 0x00119d74, EDX: 0x000003f8
E: ESI: 0x00000000, EDI: 0x00101aa7, EBP: 0x00119d10, ESP: 0x00119d00
E: EFLAGS: 0x00000206 CS: 0x0008 CR3: 0x00119000
E: call trace:
E: EIP: 0x00100459
E:      0x00100477 (0x0)
E:      0x00100492 (0x0)
E:      0x001004c8 (0x0)
E:      0x00105465 (0x105465)
E:      0x00101abe (0x0)
E: >>> ZEPHYR FATAL ERROR 0: CPU exception on CPU 0
E: Current thread: 0x00119080 (unknown)
E: #CD:BEGIN#
E: #CD:5a4501000100050000000000
E: #CD:4101003800
E: #CD:0e0000000200000000000000749d1100f803000000000000009d1100109d1100
E: #CD:00000000a71a100059041000060200000800000000901100
E: #CD:4d010080901100e0901100
E: #CD:0100000000000000000000000180000000000000000000000000000000000000
E: #CD:00000000000000000000000000000000e364100000000000000000004c9c1100
E: #CD:000000000000000000000000b49911000004000000000000fc03000000000000
E: #CD:4d0100b4991100b49d1100
E: #CD:f8030000020000000200000002000000f8030000fd03000a02000000dc9e1100
E: #CD:149a1160fd03000002000000dc9e1100249a110087201000049f11000a000000
E: #CD:349a11000a4f1000049f11000a9e1100449a11000a8b10000200000002000000
E: #CD:449a1100388b1000049f11000a000000549a1100ad201000049f11000a000000
E: #CD:749a11000a201000049f11000a000000649a11000a201000049f11000a000000
E: #CD:749a1100e8201000049f11000a000000949a1100890b10000a0000000a000000
E: #CD:a49a1100890b10000a0000000a000000f8030000189b11000200000002000000
E: #CD:f49a1100289b11000a000000189b1100049b11009b0710000a000000289b1100
E: #CD:f49a110087201000049f110045000000f49a1100509011000a00000020901100
E: #CD:f49a110060901100049f1100ffffffff0000000000000000049f1100ffffffff
E: #CD:0000000000000000630b1000189b1100349b1100af0b1000630b1000289b1100
E: #CD:55891000789b11000000000020901100549b1100480000004a891000609b1100
E: #CD:649b1100d00b10004a891000709b110000000000609b11000a00000000000000
E: #CD:849b1100709b11004a89100000000000949b1100794a10000000000058901100
E: #CD:20901100c34a10000a00001734020000d001000000000000d49b110038000000
E: #CD:c49b110078481000b49911000004000000000000000000000c9c11000c9c1100
E: #CD:149c110000000000d49b110038000000f49b1100da481000b499110000040000
E: #CD:0e0000000200000000000000744d0100b4991100b49d1100009d1100109d1100
E: #CD:149c110099471000b4991100000400000800000000901100ad861000409c1100
E: #CD:349c1100e94710008090110000000000349c1100b64710008086100045000000
E: #CD:849c11002d53100000000000d09c11008090110020861000f5ffffff8c9c1100
E: #CD:000000000000000000000000a71a1000a49c1100020200008090110000000000
E: #CD:a49c1100020200000800000000000000a49c11001937100000000000d09c1100
E: #CD:0c9d0000bc9c0000b49d1100b4991100c49c1100ae37100000000000d09c1100
E: #CD:0800000000000000c888100000000000109d11005d031000d09c1100009d1100
E: #CD:109d11000000000000000000a71a1000f803000000000000749d110002000000
E: #CD:5904100008000000060200000e0000000202000002020000000000002c9d1100
E: #CD:7704100000000000d00b1000c9881000549d110000000000489d110092041000
E: #CD:00000000689d1100549d11000000000000000000689d1100c804100000000000
E: #CD:c0881000000000007c9d110000000000749d11007c9d11006554100065541000
E: #CD:00000000000000009c9d1100be1a100000000000000000000000000038041000
E: #CD:08000000020200000000000000000000f4531000000000000000000000000000
E: #CD:END#
E: Halting system
```
1. Run the core dump serial log converter:

```console

./scripts/coredump/coredump_serial_log_parser.py coredump.log coredump.bin
```
2. Start the custom GDB server:

```console

./scripts/coredump/coredump_gdbserver.py build/zephyr/zephyr.elf coredump.bin
```
3. Start GDB:

```console

<path to SDK>/x86_64-zephyr-elf/bin/x86_64-zephyr-elf-gdb build/zephyr/zephyr.elf
```
4. Inside GDB, connect to the GDB server via port 1234:

```console

(gdb) target remote localhost:1234
```
5. Examine the CPU registers:

```console

(gdb) info registers
```
   Output from GDB:

   :
```
eax            0x0                 0
ecx            0x119d74            1154420
edx            0x3f8               1016
ebx            0x0                 0
esp            0x119d00            0x119d00 <z_main_stack+844>
ebp            0x119d10            0x119d10 <z_main_stack+860>
esi            0x0                 0
edi            0x101aa7            1055399
eip            0x100459            0x100459 <func_3+16>
eflags         0x206               [ PF IF ]
cs             0x8                 8
ss             <unavailable>
ds             <unavailable>
es             <unavailable>
fs             <unavailable>
gs             <unavailable>
```
6. Examine the backtrace:

```console

(gdb) bt
```
   Output from GDB:

   :
```
#0  0x00100459 in func_3 (addr=0x0) at zephyr/rtos/zephyr/samples/hello_world/src/main.c:14
#1  0x00100477 in func_2 (addr=0x0) at zephyr/rtos/zephyr/samples/hello_world/src/main.c:21
#2  0x00100492 in func_1 (addr=0x0) at zephyr/rtos/zephyr/samples/hello_world/src/main.c:28
#3  0x001004c8 in main () at zephyr/rtos/zephyr/samples/hello_world/src/main.c:42
```

### Starting the GDB server from within GDB


You can use `target remote |` to start the custom GDB server from inside
GDB, instead of in a separate shell.

1. Start GDB:

```console

<path to SDK>/x86_64-zephyr-elf/bin/x86_64-zephyr-elf-gdb build/zephyr/zephyr.elf
```
2. Inside GDB, start the GDB server using the `--pipe` option:

```console

(gdb) target remote | ./scripts/coredump/coredump_gdbserver.py --pipe build/zephyr/zephyr.elf coredump.bin
```

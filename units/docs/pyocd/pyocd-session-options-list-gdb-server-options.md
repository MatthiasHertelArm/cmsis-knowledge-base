---
id: "pyocd-session-options-list-gdb-server-options"
type: "concept"
domain: "debug"
title: "Session options list: GDB server options"
summary: "These session options are currently only applied when running the GDB server."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/options.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/options.md#gdb-server-options"
license: "Apache-2.0"
mode: "V"
---

These session options are currently only applied when running the GDB server.

<table>

<tr><th>Option Name</th><th>Type</th><th>Default</th><th>Description</th></tr>

<tr><td>enable_semihosting</td>
<td>bool</td>
<td>False</td>
<td>
Set to True to handle semihosting requests. Also see the <tt>semihost_console_type</tt> option.
</td></tr>

<tr><td>enable_swv</td>
<td>bool</td>
<td>False</td>
<td>
Whether to enable SWV printf output over the semihosting console. Requires the <tt>swv_system_clock</tt>
option to be set. The SWO baud rate can be controlled with the <tt>swv_clock</tt> option.
</td></tr>

<tr><td>debug.status_fault_retry_timeout</td>
<td>float</td>
<td>1</td>
<td>
Duration in seconds that a failed target status check will be retried before an error is raised. Only
applies while the target is running after a resume operation in the debugger and pyOCD is waiting for
it to halt again.
</td></tr>

<tr><td>gdbserver_port</td>
<td>int</td>
<td>3333</td>
<td>
Base TCP port for the gdbserver. The core number, which is 0 for the primary core, will be added to
this value.
</td></tr>

<tr><td>persist</td>
<td>bool</td>
<td>False</td>
<td>
If True, the GDB server will not exit after GDB disconnects.
</td></tr>

<tr><td>report_core_number</td>
<td>bool</td>
<td>False</td>
<td>
Whether gdb server should report core number as part of the per-thread information.
</td></tr>

<tr><td>rtos.enable</td>
<td>bool</td>
<td>True</td>
<td>
Overall enable flag for RTOS aware debugging. By default it's enabled but can be switched off
if necessary.
</td></tr>

<tr><td>rtos.name</td>
<td>str</td>
<td><i>No default</i></td>
<td>
Name of the RTOS plugin to use. If not set, all RTOS plugins are given a chance to load.
</td></tr>

<tr><td>semihost_console_type</td>
<td>str</td>
<td>'telnet'</td>
<td>
If set to 'telnet' then the semihosting telnet server will be started. If set to 'console' then
semihosting will print to the console.
</td></tr>

<tr><td>semihost_use_syscalls</td>
<td>bool</td>
<td>False</td>
<td>
Whether to use GDB syscalls for semihosting file access operations, or to have pyOCD perform the
operations. This is most useful if GDB is running on a remote system.
</td></tr>

<tr><td>semihost.commandline</td>
<td>str</td>
<td><i>Empty</i></td>
<td>
Program command line string, used for the SYS_GET_CMDLINE semihosting request.
</td></tr>

<tr><td>step_into_interrupt</td>
<td>bool</td>
<td>False</td>
<td>
Set this option to True to enable interrupts when performing step operations. Otherwise
interrupts will be disabled and step operations cannot be interrupted.
</td></tr>

<tr><td>swv_clock</td>
<td>int</td>
<td>1000000 (1 MHz)</td>
<td>
Frequency in Hertz of the SWO baud rate.
</td></tr>

<tr><td>swv_system_clock</td>
<td>int</td>
<td><i>No default</i></td>
<td>
Frequency in Hertz of the target's system clock. Used to compute the SWO baud rate
divider.
</td></tr>

<tr><td>swv_raw_enable</td>
<td>bool</td>
<td>True</td>
<td>
Enable flag for the raw SWV stream server.
</td></tr>

<tr><td>swv_raw_port</td>
<td>int</td>
<td>3443</td>
<td>
TCP port number for the raw SWV stream server.
</td></tr>

<tr><td>swv_raw_file</td>
<td>str</td>
<td>No default</td>
<td>
File path for the raw SWV stream output.
</td></tr>

<tr><td>telnet_port</td>
<td>int</td>
<td>4444</td>
<td>
Base TCP port number for the semihosting telnet server. The core number, which will be 0 for the
primary core, is added to this value.
</td></tr>

<tr><td>vector_catch</td>
<td>str</td>
<td>'h'</td>
<td>
Enable vector catch sources, one letter per enabled source in any order, or
<tt>all</tt> or <tt>none</tt>.

The source letters are:
- <tt>h</tt>=hard fault
- <tt>b</tt>=bus fault
- <tt>m</tt>=mem fault
- <tt>e</tt>=secure fault
- <tt>i</tt>=irq err
- <tt>s</tt>=state err
- <tt>c</tt>=check err
- <tt>p</tt>=nocp
- <tt>r</tt>=reset
- <tt>a</tt>=all
- <tt>n</tt>=none
</td></tr>

<tr><td>register_fields</td>
<td>bool</td>
<td>True</td>
<td>
When set to True, registers with bitfields will have their respective bitfields defined for
presentation in gdb.
</td></tr>

</table>

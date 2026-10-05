---
id: "pyocd-session-options-list-general-options"
type: "concept"
domain: "debug"
title: "Session options list: General options"
summary: "Note that the projectdir, noconfig, and config options must come from either a keyword argument or the options parameter passed to the Session constructor due to how early they are processed."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/options.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/options.md#general-options"
license: "Apache-2.0"
mode: "V"
---

Note that the `project_dir`, `no_config`, and `config` options must come from either a keyword
argument or the _options_ parameter passed to the `Session` constructor due to how early they are
processed. The consequence of this is that these options cannot be set in a YAML config file.

<table class="docs-table">

<tr><th>Option Name</th><th>Type</th><th>Default</th><th>Description</th></tr>

<tr><td>adi.v5.max_invalid_ap_count</td>
<td>int</td>
<td>3</td>
<td>
If this number of invalid APs is found in a row, then AP scanning will stop. The 'scan_all_aps' option
takes precedence over this option if set.
</td></tr>

<tr><td>allow_no_cores</td>
<td>bool</td>
<td>False</td>
<td>
Prevents raising an error if no cores were found after CoreSight discovery.
</td></tr>

<tr><td>auto_unlock</td>
<td>bool</td>
<td>True</td>
<td>
If the target is locked, it will by default be automatically mass erased in order to gain debug
access. Set this option to False to disable auto unlock.
</td></tr>

<tr><td>cache.enable_memory</td>
<td>bool</td>
<td>True</td>
<td>
Enable the memory read cache. Affects memory accesses made through the target debug context, including the
gdbserver.
</td></tr>

<tr><td>cache.enable_register</td>
<td>bool</td>
<td>True</td>
<td>
Enable the core register cache. Affects core register accesses made through the target debug context,
including the gdbserver.
</td></tr>

<tr><td>cache.read_code_from_elf</td>
<td>bool</td>
<td>True</td>
<td>
Controls whether reads of code sections will be taken from an attached ELF file instead of the target memory.
This can improve performance, especially over slow target connections. Requires an ELF file to be set.
</td></tr>

<tr><td>chip_erase</td>
<td>str</td>
<td>'sector'</td>
<td>
Whether to perform a chip erase or sector erases when programming flash. The value must be one of
'auto', 'sector', or 'chip'.
</td></tr>

<tr><td>cmsis_dap.prefer_v1</td>
<td>bool</td>
<td>False</td>
<td>
If a device provides both CMSIS-DAP v1 and v2 interfaces, use the v1 interface in preference of v2.
Normal behaviour is to prefer the v2 interface. This option is primarily intended for testing.
</td></tr>

<tr><td>commander.history_length</td>
<td>int</td>
<td>1000</td>
<td>
Number of entries in the pyOCD Commander command history. Set to -1 for unlimited.
</td></tr>

<tr><td>config_file</td>
<td>str</td>
<td><i>See description</i></td>
<td>
Relative path to a YAML config file that lets you specify session options either globally or per probe.
The format of the file is documented above. The default is a <tt>pyocd.yaml</tt> or <tt>pyocd.yml</tt> file in the
working directory.
</td></tr>

<tr><td>connect_mode</td>
<td>str</td>
<td>'halt'</td>
<td>
Controls how pyOCD connects to the target. One of 'halt', 'pre-reset', 'under-reset', 'attach'.
<ul>
<li>'halt': immediately halt all accessible cores upon connect.</li>
<li>'pre-reset': perform a hardware reset prior to connect and halt.</li>
<li>'under-reset': assert hardware reset during the connect sequence, then deassert after the cores are halted.
    This connect mode is often necessary to gain control of a target that is in a deep low power mode.</li>
<li>'attach': connect to a running target without halting cores.</li>
</ul>
</td></tr>

<tr><td>cpu.step.instruction.timeout</td>
<td>float</td>
<td>0.0</td>
<td>
<p>Timeout in seconds for instruction step operations. The default of 0 means no timeout.</p>
<p>Note that stepping may take a very long time for to return in cases such as stepping over a branch
into the Secure world where the debugger doesn't have secure debug access, or similar for Privileged
code in the case of UDE.</p>
</td></tr>

<tr><td>dap_protocol</td>
<td>str</td>
<td>'default'</td>
<td>
Wire protocol, either 'swd', 'jtag', or 'default'.
</td></tr>

<tr><td>dap_swj_enable</td>
<td>bool</td>
<td>True</td>
<td>
Send SWJ transition sequence to switch between SWD and JTAG.
</td></tr>

<tr><td>dap_swj_use_dormant</td>
<td>bool</td>
<td>False</td>
<td>
When switching between SWD and JTAG, use the SWJ sequence added in ADIv5.2 that transitions through
a new dormant state. Requires a SWJ-DPv2. Note that if the connection attempt fails using the
deprecated sequence (when this option is disabled), then pyOCD will automatically attempt to use the
new sequence. This option simply skips the deprecated sequence in case it causes problems or it is
known that dormant state is required for the target.
</td></tr>

<tr><td>debug.log_flm_info</td>
<td>bool</td>
<td>False</td>
<td>
Log details of loaded .FLM flash algos.
</td></tr>

<tr><td>debug.traceback</td>
<td>bool</td>
<td>False</td>
<td>
Print tracebacks for exceptions, including errors that are only logged as well as critical errors that cause pyocd to terminate.

Disabled by default, unless the log level is raised to Debug.
</td></tr>

<tr><td>enable_multicore_debug</td>
<td>bool</td>
<td>False</td>
<td>
Whether to put pyOCD into multicore debug mode. The primary effect is to modify the default software
reset type for secondary cores to use VECTRESET, which will fall back to emulated reset for
secondary cores that are not v7-M architecture (VECTRESET is only supported on v7-M). The core that is
considered the primary core is selected by the `primary_core` option.
</td></tr>

<tr><td>fast_program</td>
<td>bool</td>
<td>False</td>
<td>
Setting this option to True will use CRC checks of existing flash sector
contents to determine whether pages need to be programmed.
</td></tr>

<tr><td>flash.timeout.init</td>
<td>float</td>
<td>5.0</td>
<td>
Flash algorithm init and uninit timeout in seconds.
</td></tr>

<tr><td>flash.timeout.analyzer</td>
<td>float</td>
<td>30.0</td>
<td>
Flash CRC analyzer timeout in seconds.
</td></tr>

<tr><td>flash.timeout.erase_all</td>
<td>float</td>
<td>240.0</td>
<td>
Flash algorithm erase all timeout in seconds.
</td></tr>

<tr><td>flash.timeout.erase_sector</td>
<td>float</td>
<td>10.0</td>
<td>
Flash algorithm sector erase timeout in seconds.
</td></tr>

<tr><td>flash.timeout.program</td>
<td>float</td>
<td>10.0</td>
<td>
Flash algorithm programming timeout in seconds.
</td></tr>

<tr><td>frequency</td>
<td>int</td>
<td>1000000 (1 MHz)</td>
<td>
SWD/JTAG frequency in Hertz.
</td></tr>

<tr><td>hide_programming_progress</td>
<td>bool</td>
<td>False</td>
<td>
Disables flash programming progress bar when True.
</td></tr>

<tr><td>keep_unwritten</td>
<td>bool</td>
<td>False</td>
<td>
Whether to preserve existing flash content for ranges of sectors that will be erased but not written
with new data.
</td></tr>

<tr><td>load.pre_reset</td>
<td>str</td>
<td><i>No default</i></td>
<td>
Specify the type of reset to perform before programming. The value must be one of
'off', 'default', 'hardware', 'system', 'core', 'n_srst', 'sysresetreq', 'vectreset' or 'emulated'.
</td></tr>

<tr><td>load.post_reset</td>
<td>str</td>
<td><i>No default</i></td>
<td>
Specify the type of reset to perform after programming. The value must be one of
'off', 'default', 'hardware', 'system', 'core', 'n_srst', 'sysresetreq', 'vectreset' or 'emulated'.
</td></tr>

<tr><td>logging</td>
<td>str, dict</td>
<td><i>No default</i></td>
<td>
Either a dictionary with logging configuration, or a path to a separate yaml logging configuration
file. See the <a href="{% link _docs/configuring_logging.md %}">logging configuration documentation</a> for details of how to
use this option.
</td></tr>

<tr><td>no_config</td>
<td>bool</td>
<td>False</td>
<td>
Do not use default config file.
</td></tr>

<tr><td>pack</td>
<td>str, list of str</td>
<td><i>No default</i></td>
<td>
Path or list of paths to CMSIS Device Family Packs. Devices defined in the pack(s) are added to the
list of available targets.
</td></tr>

<tr><td>pack.debug_sequences.debugvars</td>
<td>str</td>
<td><i>No default</i></td>
<td>
Variable definition statements to change configurable variables defined by and used in the target's debug sequences.
Should be set to a string containing C-style variable assignment statements. C-compatible integer expressions
are allowed, and can refer to previously defined variables. Only those debug variables whose value is being
changed need to be assigned a value; others will retain their default value.
</td></tr>

<tr><td>pack.debug_sequences.disabled_sequences</td>
<td>str, list of str</td>
<td><i>No default</i></td>
<td>
Comma-separated list of names of debug sequences to disable for a CMSIS-Pack based target.
Disabled sequences can be restricted to a given core by appending a colon and processor
name to the sequence's name. If set in a YAML config file, the value must be a list of sequence
names instead of using a single comma-separated value.

Only top-level sequences can be disabled. If a sequence is called from another sequence it will
always be executed even if listed in this option.

Ignored for builtin targets.
</td></tr>

<tr><td>pack.debug_sequences.enable</td>
<td>bool</td>
<td><i>True</i></td>
<td>
Global enable for debug sequences for CMSIS-Pack based targets. Ignored for builtin targets.
</td></tr>

<tr><td>primary_core</td>
<td>int</td>
<td>0</td>
<td>
Core number for the primary/boot core of an asymmetric multicore target. Becomes the default selected
core in the commander and the `SoCTarget` class. Also the core that will control system reset when
`enable_multicore_debug` is set.
</td></tr>

<tr><td>probeserver.port</td>
<td>int</td>
<td>5555</td>
<td>
TCP port for the debug probe server.
</td></tr>

<tr><td>project_dir</td>
<td>str</td>
<td><i>See description</i></td>
<td>
Path to the session's project directory. Defaults to the working directory when the pyocd tool was
executed.
</td></tr>

<tr><td>reset_type</td>
<td>str</td>
<td>'default'</td>
<td>
Which type of reset to use. Must be one of 'default', 'hardware', 'system', 'core', 'n_srst',
'sysresetreq', 'vectreset' or 'emulated'. The 'default' option causes the target type's
default reset type to be used; this is usually `system`. If `enable_multicore_debug` is
set to true, then secondary cores will default to `core`.
</td></tr>

<tr><td>reset.hold_time</td>
<td>float</td>
<td>0.1</td>
<td>
Number of seconds to hold hardware reset asserted.
</td></tr>

<tr><td>reset.post_delay</td>
<td>float</td>
<td>0.1</td>
<td>
Number of seconds to delay after a reset is issued.
</td></tr>

<tr><td>reset.dap_recover.timeout</td>
<td>float</td>
<td>5.0</td>
<td>
Timeout for waiting for the DAP to be accessible after reset, in seconds. If the timeout lapses, an attempt
will be made to reconnect the DP and retry.
</td></tr>

<tr><td>reset.core_recover.timeout</td>
<td>float</td>
<td>2.0</td>
<td>
Timeout in seconds for waiting for a core to be accessible after reset. A warning is printed if the timeout
lapses. Set to 0 to disable the core accessibility test. For halting reset, this is also the timeout for waiting
for the core to halt.
</td></tr>

<tr><td>reset.halt_timeout</td>
<td>float</td>
<td>2.0</td>
<td>
Timeout in seconds for waiting for the core to halt after a reset and halt.
</td></tr>

<tr><td>resume_on_disconnect</td>
<td>bool</td>
<td>True</td>
<td>
Whether to disable debug control and resume the target when disconnecting.

When True, then upon disconnect all CPUs are resumed, and DWT and other trace related blocks are disabled (`DEMCR` system register is cleared).
If False, the target CPU states are left unchanged and any enabled debug hardware (DWT, ITM) remains enabled.
In all cases, breakpoints and watchpoints are removed prior to disconnect.
</td></tr>

<tr><td>scan_all_aps</td>
<td>bool</td>
<td>False</td>
<td>
Controls whether all 256 ADIv5 AP addresses will be probed.
</td></tr>

<tr><td>serve_local_only</td>
<td>bool</td>
<td>True</td>
<td>
When this option is True, the GDB server, probe server, stdio server, rtt server, and raw SWV server are only served
on localhost, making them inaccessible across the network. Set to False to enable connecting to these ports
from any machine on the network.
</td></tr>

<tr><td>smart_flash</td>
<td>bool</td>
<td>True</td>
<td>
If set to True, the flash loader will attempt to not program pages whose contents are not going to
change by scanning target flash memory. A value of False will force all pages to be erased and
programmed.
</td></tr>

<tr><td>target_override</td>
<td>str</td>
<td><i>No default</i></td>
<td>
Target type name to use instead of default board target or default <tt>cortex_m</tt>.
</td></tr>

<tr><td>test_binary</td>
<td>str</td>
<td><i>No default</i></td>
<td>
Specify the test binary file name used by the functional test suite (in the <tt>test/</tt> directory). The
binary must be in the <tt>binaries/</tt> directory. This option is most useful when set in a board config
file for running the functional tests on boards that cannot be automatically detected.
</td></tr>

<tr><td>user_script</td>
<td>str</td>
<td><i>No default</i></td>
<td>
Path of the user script file.
</td></tr>

<tr><td>warning.cortex_m_default</td>
<td>bool</td>
<td><i>True</i></td>
<td>Whether to show the warning when no target type is selected and the default cortex_m target
type is used. The warning is never shown if the cortex_m target type is explicitly specified.
</td></tr>

</table>

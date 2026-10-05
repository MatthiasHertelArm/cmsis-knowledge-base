---
id: "txmw-chapter-5-netx-duo-network-drivers-tsn-driver-support"
type: "concept"
domain: "rtos"
title: "Chapter 5 - NetX Duo Network Drivers: TSN driver support"
summary: "TSN shapers are a series of hardware features that can be added to an Ethernet card equipped with TSN capabilities."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md#tsn-driver-support"
license: "MIT"
mode: "V"
---

TSN shapers are a series of hardware features that can be added to an Ethernet card equipped with TSN capabilities. We will discuss implementation of the PTP driver and the three types of shapers: CBS (Credit-Based Shaper), EST (Enhanced Scheduled Traffic), and FPE (Frame Preemption).

### PTP initialize and callback function
PTP is utilized in various scenarios within the TSN system, particularly when the TAS shaper is enabled. Given the high requirements for the PTP clock, it is recommended to initialize PTP in Fine mode. Additionally, it is necessary to implement the PTP driver callbacks, which are invoked to get, set, and adjust the PTP clock.

the driver interface which is used to sychnorize ptp clock in the network.
```C
UINT nx_driver_ptp_clock_callback(NX_PTP_CLIENT *client_ptr, UINT operation,
                                             NX_PTP_TIME *time_ptr, NX_PACKET *packet_ptr,
                                             VOID *callback_data)
```

| operation                                   |  Description                                                     |
| ------------------------------------------- | -----------------------------------------------------------------|
| ***NX_PTP_CLIENT_CLOCK_INIT***              | A driver PTP pointer is initialized,                             |
| ***NX_PTP_CLIENT_CLOCK_SET***               | Set PTP clock when syncorize PTP in the network                  |
| ***NX_PTP_CLIENT_CLOCK_PACKET_TS_EXTRACT*** | Get timestamp from packet,                                       |
| ***NX_PTP_CLIENT_CLOCK_GET***               | Get timestamp from PTP clock,                                    |
| ***NX_PTP_CLIENT_CLOCK_ADJUST***            | Adjust PTP clock by PTP offset when syncorize PTP in the network,|
| ***NX_PTP_CLIENT_CLOCK_PACKET_TS_PREPARE*** | Add NX_INTERFACE_CAPABILITY_PTP_TIMESTAMP support in interface,  |
| ***NX_PTP_CLIENT_CLOCK_SOFT_TIMER_UPDATE*** | update soft timer, Reserved for hardware driver,                 |



### Credit-based shaper (CBS) - IEEE 802.1Qav Forwarding and Queuing Enhancements for Time-Sensitive Stream
In general, a CBS works by assigning "credits" to each data packet. The number of credits a packet has determines when it can be transmitted. Packets with more credits are transmitted before packets with fewer credits. This allows the CBS to prioritize certain data streams over others, ensuring that high-priority data is transmitted first.
The CBS driver needs to be implemented to support the CBS feature. The driver entry will be invoked from the application, passing application data to configure the CBS driver.

the driver entry:
```C
UINT nx_driver_shaper_cbs_entry(NX_SHAPER_DRIVER_PARAMETER *parameter)

```
Data structure of driver entry parameter:
```C
typedef struct NX_SHAPER_DRIVER_PARAMETER_STRUCT
{
    UINT          nx_shaper_driver_command;
    UCHAR         shaper_type;
    UCHAR         reserved[3];
    void         *shaper_parameter;
    NX_INTERFACE *nx_ip_driver_interface;
} NX_SHAPER_DRIVER_PARAMETER;
```
Data stucture of CBS parameter which define the necessary parameters that CBS driver needs.
```C
typedef struct NX_SHAPER_CBS_PARAMETER_STRUCT
{
    INT   idle_slope;   /* Mbps */
    INT   send_slope;   /* Mbps */
    INT   hi_credit;
    INT   low_credit;
    UCHAR hw_queue_id;
    UCHAR reserved[3];
} NX_SHAPER_CBS_PARAMETER;
```
the driver entry parameter:
| parameter -> nx_shaper_driver_command       |  Description                                                     |
| ------------------------------------------- | -----------------------------------------------------------------|
| ***NX_SHAPER_COMMAND_INIT***                | initialization of enabling CBS,                                  |
| ***NX_SHAPER_COMMAND_CONFIG***              | set hardware queue priority and capability of CBS,                |
| ***NX_SHAPER_COMMAND_PARAMETER_SET***       | set parameter passed from application to driver,                 |



### Time-Aware Shaper (TAS) - IEEE 802.1Qbv Enhancements to Traffic Scheduling
A Time-Aware Shaper (TAS) is a mechanism used in Time-Sensitive Networking (TSN) systems to control the transmission of Ethernet frames based on the time. It's part of the IEEE 802.1Qbv standard.
The TAS works by dividing time into repeating cycles, and each cycle is further divided into time intervals, or "gates". Each gate is either open or closed, and frames can only be transmitted when the gate is open.
The TAS driver needs to be implemented to support the TAS feature. The driver entry will be invoked from the application, passing application data to configure the TAS driver.

the driver entry:
```C
UINT nx_driver_shaper_tas_entry(NX_SHAPER_DRIVER_PARAMETER *parameter)

```

Data stucture of TAS parameter which define the necessary parameters that TAS driver needs.
```C
typedef struct NX_SHAPER_TAS_PARAMETER_STRUCT
{
    ULONG64           base_time;
    UINT              cycle_time;
    UINT              cycle_time_extension;
    UINT              gcl_length;
    NX_SHAPER_TAS_GCL gcl[NX_SHAPER_GCL_LENGTH_MAX];
    void             *fp_parameter; /* Configured by shaper */
} NX_SHAPER_TAS_PARAMETER;
```
the driver entry parameter:

| parameter -> nx_shaper_driver_command       |  Description                                                     |
| ------------------------------------------- | -----------------------------------------------------------------|
| ***NX_SHAPER_COMMAND_INIT***                | initialization of enabling TAS,                                  |
| ***NX_SHAPER_COMMAND_CONFIG***              | set hardware queue priority and capability of TAS,                |
| ***NX_SHAPER_COMMAND_PARAMETER_SET***       | set parameter passed from application to driver,                 |

### Frame preemption (FPE) - 802.1Qbu
In traditional Ethernet networks, once a frame starts transmitting, it must be completely sent before another frame can begin. This can cause delays for time-sensitive data if it has to wait for a large, non-time-sensitive frame to finish transmitting.
Frame Preemption addresses this issue by allowing a high-priority, time-sensitive frame to interrupt the transmission of a low-priority frame. The low-priority frame is then resumed after the high-priority frame has been sent. This ensures that time-sensitive data can be transmitted with minimal delay, even in a busy network
The FPE driver needs to be implemented to support the FPE feature. The driver entry will be invoked from the application, passing application data to configure the FPE driver.
the driver entry:
```C
UINT nx_driver_shaper_fpe_entry(NX_SHAPER_DRIVER_PARAMETER *parameter)

```

Data structure of TAS parameter which define the necessary parameters that TAS driver needs.
```C
typedef struct NX_SHAPER_FP_PARAMETER_STRUCT
{
    UCHAR verification_enable;          /* Enable/Disable fp verification (Application/Driver) */
    UCHAR express_queue_bitmap;         /* Bitmap of express queues */
    UCHAR express_guardband_enable;     /* Enable/Disable guard band on express queue */
    UCHAR reserved;
    UINT  ha;                           /* Hold advance time */
    UINT  ra;                           /* Release advance time */
} NX_SHAPER_FP_PARAMETER;
```
the driver entry parameter:

| parameter -> nx_shaper_driver_command       |  Description                                                     |
| ------------------------------------------- | -----------------------------------------------------------------|
| ***NX_SHAPER_COMMAND_INIT***                | initialization of enabling FPE,                                  |
| ***NX_SHAPER_COMMAND_CONFIG***              | set hardware queue priority and capability of FPE,                |
| ***NX_SHAPER_COMMAND_PARAMETER_SET***       | set parameter passed from application to driver,                 |

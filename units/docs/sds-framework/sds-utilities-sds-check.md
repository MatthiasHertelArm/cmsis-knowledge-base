---
id: "sds-utilities-sds-check"
type: "concept"
domain: "test"
title: "Utilities: SDS-Check"
summary: "The Python utility SDS-Check checks SDS files for correctness and consistency."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@c18efee:documentation/utilities.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/utilities.md#sds-check"
license: "Apache-2.0"
mode: "V"
---

The Python utility [**SDS-Check**](https://github.com/ARM-software/SDS-Framework/tree/main/utilities) checks SDS files for correctness and consistency.

The following checks are performed:

- [Size consistency check](#size-consistency-check): Checks that data size of all records matches the size of the SDS file.
- [Timeslot consistency check](#timeslot-consistency-check): Verifies that the timeslots of the records are in ascending order.
- [Jitter check](#jitter-check): Searches for the record with the largest deviation from the average timeslot interval and prints its record number and deviation.
- [Delta time check](#delta-time-check): Checks for the record with the largest timeslot difference compared to the following record.
- [Duplicate timeslot check](#duplicate-timeslot-check): Checks for records with identical timeslots.

### Usage

- [Setup](#setup) the Python environment.
- Invoke the tool as explained below.

```txt
usage: sds-check.py [-h] -i <sds_file> [-t <tick_rate>]

SDS data validation

options:
  -h, --help      Show this help message and exit

required:
  -i <sds_file>   SDS file

optional:
  -t <tick_rate>  Timeslot tick rate in Hz (default: 1000 for 1 ms tick interval)
```

**Example:**

```txt
python sds-check.py -i Accelerometer.0.sds
File Name         : Accelerometer.0.sds
File Size         : 156.020 bytes
Number of Records : 289
Recording Time    : 14 s
Recording Interval: 50 ms
Data Size         : 153.748 bytes
Block Size        : 532 bytes
Data Rate         : 10.640 byte/s
Jitter            : Not detected
Validation passed
```

!!! Note
    The default tick frequency is 1000 Hz.

### Summary Report

After processing the SDS file, the SDS-Check utility prints a summary report with the following information:

- **File Name**         : Name of the SDS file
- **File Size**         : Size of the file in bytes
- **Number of Records** : Total number of records
- **Recording Time**    : Duration of the recording in seconds or milliseconds
- **Recording Interval**: Time interval between records in milliseconds
- **Data Size**         : Total size of the data without record headers in bytes
- **Block Size**        : Data block size, if all data blocks are of the same size
- **Max Block Size**    : Maximum data block size, if different from the average data block size
- **Min Block Size**    : Minimum data block size, if different from the average data block size
- **Avg Block Size**    : Average data block size
- **Data Rate**         : Recorded data rate in bytes per second
- **Max Jitter**        : Maximum deviation from the expected timeslots, if detected (optional)
- **Max Delta Time**    : Largest difference of the neighboring timeslots, if deviating from the recording interval (optional)
- **Duplicate Tslots**  : Number of duplicated timeslots, if found

### Size consistency check

This check processes the SDS data records and calculates the total size of the SDS data.
It is the sum of all data records (header + data). This data size should match the size of
the SDS file. If the sizes do not match, an error such as the one below is printed:

```txt
Error: File size mismatch. Expected 360 bytes, but file contains 363 bytes.
```

### Timeslot consistency check

This check processes the SDS records and ensures that the timeslots recorded in the records
are arranged in ascending order. If the timeslots are not in the ascending order, an error
such as the one below is printed:

```txt
Error: Timeslot not in ascending order in record 23.
```

### Jitter check

This check processes the SDS data records and searches for the maximum deviation of the recorded
timeslots from the expected ones. If a deviation is found, the maximum deviation is
evaluated as **jitter** and, together with the record number, is printed in the summary report.

```txt
File Name         : Gyroscope.0.sds
  :
Max Jitter        : 59 ms, in record 19
Validation passed
```

### Delta time check

This check processes the SDS records and finds the largest difference in timeslots
between two neighboring records, called **Max Delta Time**.

Normally, in SDS files, the delta time and the recording interval are identical, so no information
about the delta time status is printed. If the delta time and the recording interval are not identical,
that is, a difference is detected, the **Max Delta Time** together with the record number is printed
in the summary report.

```txt
File Name         : Temperature.0.sds
  :
Max Delta Time    : 1.050 ms, in record 2
Validation passed
```

This is not an error, but a report of an anomaly. If the time delta is significantly larger than the
sampling interval, for example many times longer, this may indicate that one or more data records are
missing from the SDS file.

### Duplicate timeslot check

This check processes the SDS records to identify duplicated timeslots. This means that the same timeslot
is used in several consecutive data records.

This may indicate that the recording loop in an embedded application is not set up correctly. It is also
possible that duplicate timeslots are caused by unexpected thread delays in the embedded application.

Duplicate timeslots are unusual in typical recording files. If multiple timeslots with the same value
are found in the SDS file, **Duplicate Tslots** will be added to the summary report.

```txt
File Name         : DataInput.0.sds
  :
Duplicate Tslots  : 4, found at record 1
Validation passed
```

This is not an error, but a report of an anomaly. The report contains the number of records with
the same timeslot and the position in the SDS file where the anomaly was detected (record number).

!!! Note
    Only the first occurrence of a duplicate timeslot is reported.

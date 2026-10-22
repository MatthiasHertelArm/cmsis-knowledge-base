---
id: "sds-utilities-sds-convert"
type: "concept"
domain: "test"
title: "Utilities: SDS-Convert"
summary: "The Python utility SDS-Convert converts SDS files into the selected output format based on the descriptions provided in the metadata (YAML) files."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@c18efee:documentation/utilities.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/utilities.md#sds-convert"
license: "Apache-2.0"
mode: "V"
---

The Python utility [**SDS-Convert**](https://github.com/ARM-software/SDS-Framework/tree/main/utilities) converts SDS files into the
selected output format based on the descriptions provided in the metadata (YAML) files.

### Usage

- [Setup](#setup) the Python environment.
- Depending on the required format, use the tool as shown below.

#### Audio WAV

The `audio_wav` mode converts SDS file (`.sds`) containing raw microphone data into a standard RIFF/WAV file (`.wav`) using linear
PCM encoding. The conversion process involves appending a WAV header, generated from parameters specified in the
associated YAML metadata file (`.yml`), to the raw audio data extracted from the SDS file. The metadata defines
essential audio parameters such as channel configuration (mono or stereo), sample rate (frame rate), and sample
width (bit depth).

```txt
usage: sds-convert.py audio_wav [-h]
                                -i <input_file>
                                -o <output_file>
                                -y <yaml_file>

Convert SDS file to WAV audio files

options:
  -h, --help        show this help message and exit

required:
  -i <input_file>   Input file
  -o <output_file>  Output file
  -y <yaml_file>    YAML metadata file
```

!!! Note
    - The tool expects the SDS file to contain strictly audio data; no header markers or custom formatting.

**Example of metadata yml file for mono microphone:**

```yml
sds:
  name: Mono
  description: Mono 16-bit PCM microphone
  sample-frequency: 16000
  content:
    - audio:
        bit-depth: 16
        channels: 1
        format: pcm
```

**Example of metadata yml file for stereo microphone:**

```yml
sds:
  name: Stereo
  description: Stereo 16-bit PCM microphone
  sample-frequency: 44100
  content:
    - audio:
        bit-depth: 16
        channels: 2
        format: pcm
```

**Example:**

```bash
python sds-convert.py audio_wav -i Microphone.0.sds -o microphone.wav -y Microphone.sds.yml
```

#### CSV

The `csv` mode converts SDS file (`.sds`) containing sensor data into a human-readable CSV file (`.csv`).

Timeslots are represented in floating-point format, in seconds. Using the `--normalize` parameter causes
all timeslots in the input file to be offset so that the first timeslot starts at `0`.

Users may specify a time range selection of the input data to be processed using the following parameters:

- `--start-timeslot <timeslot>`: Starting input data timeslot in floating-point format, in seconds.
- `--stop-timeslot <timeslot>` : Stopping input data timeslot in floating-point format, in seconds.

```txt
usage: sds-convert.py csv [-h]
                          -i <input_file>
                          -o <output_file>
                          -y <yaml_file>
                          [--normalize]
                          [--start-timeslot <timeslot>]
                          [--stop-timeslot <timeslot>]

Convert SDS file to CSV file with timeslots and data columns

options:
  -h, --help                     show this help message and exit

required:
  -i <input_file>                Input file
  -o <output_file>               Output file
  -y <yaml_file>                 YAML metadata file

optional:
  --normalize                    Normalize timeslots so they start with 0
  --start-timeslot <timeslot>    Starting input data timeslot, in seconds (default: None)
  --stop-timeslot <timeslot>     Stopping input data timeslot, in seconds (default: None)
```

!!! Note
    - Current implementation assumes that the tick frequency is `1000 Hz` and does not use the `tick-frequency` value from the metadata file.

**Example of metadata yml file for gyroscope:**

```yml
sds:
  name: Gyroscope
  description: Gyroscope with 1667Hz sample rate
  sample-frequency: 1667
  content:
    - value: x
      type: int16_t
      scale: 0.07
      unit: dps
    - value: y
      type: int16_t
      scale: 0.07
      unit: dps
    - value: z
      type: int16_t
      scale: 0.07
      unit: dps
```

**Example:**

```bash
python sds-convert.py csv -i Gyroscope.0.sds -o Gyroscope.csv -y Gyroscope.sds.yml --normalize --start-timeslot 0.2 --stop-timeslot 0.3
```

#### Qeexo V2 CSV

The `qeexo_v2_csv` mode converts between SDS files (`.sds`) containing sensor data and Qeexo V2 CSV files (`.csv`).

Link to [Qeexo V2 CSV format specification](https://docs.qeexo.com/guides/userguides/data-management#2-1-Data-format-specification).

Timeslots are represented in integer format, in milliseconds. Using the `--normalize` parameter causes
all timeslots in the input file to be offset so that the first timeslot starts at `0`.

Users may specify a time range selection of the input data to be processed using the following parameters:

- `--start-timeslot <timeslot>`: Starting input data timeslot in integer format, in milliseconds.
- `--stop-timeslot <timeslot>` : Stopping input data timeslot in integer format, in milliseconds.

By default, the output file will have raw timeslots in integer format, in milliseconds.
The default output timeslot interval is set to `50 ms`.
To override this setting, use the `--interval <ms>` parameter, where `<ms>` is the desired interval in milliseconds.

An optional label can be added to the output by providing a string argument to the `--label <text>` parameter.
This `<text>` will populate the label column in the output file.

```txt
usage: sds-convert.py qeexo_v2_csv [-h]
                                   -i <input_file> [<input_file> ...]
                                   -o <output_file>
                                   [-y <yaml_file> [<yaml_file> ...]]
                                   [--normalize]
                                   [--start-timeslot <timeslot>]
                                   [--stop-timeslot <timeslot>]
                                   [--label 'label']
                                   [--interval <interval>]
                                   [--sds_index <sds_index>]

Convert between SDS and Qeexo AutoML V2 CSV files (supports multiple sensors)

options:
  -h, --help                          show this help message and exit

required:
  -i <input_file> [<input_file> ...]  Input files
  -o <output_file>                    Output file

optional:
  -y <yaml_file> [<yaml_file> ...]    YAML metadata files
  --normalize                         Normalize timeslots so they start with 0
  --start-timeslot <timeslot>         Starting input data timeslot, in ms (default: None)
  --stop-timeslot <timeslot>          Stopping input data timeslot, in ms (default: None)
  --label 'label'                     Qeexo class label for sensor data (default: None)
  --interval <interval>               Qeexo timeslot interval, in ms (default: 50)
  --sds_index <sds_index>             SDS file index to write (default: <sensor>.0.sds)
```

!!! Note
    - The SDS and metadata file pairs must be passed as arguments in the same order to decode the data correctly.
    - Current implementation assumes that the tick frequency is `1000 Hz` and does not use the `tick-frequency` value from the metadata file.

**Example of metadata yml file for accelerometer:**

```yml
sds:
  name: Accelerometer
  description: Accelerometer with 1667Hz sample rate
  frequency: 1667
  content:
    - value: x
      type: int16_t
      scale: 0.000061
      unit: G
    - value: y
      type: int16_t
      scale: 0.000061
      unit: G
    - value: z
      type: int16_t
      scale: 0.000061
      unit: G
```

**Examples:**

Convert **SDS** files to **Qeexo V2 CSV** files:

```bash
python sds-convert.py qeexo_v2_csv -i Gyroscope.0.sds Accelerometer.0.sds -o SensorFusion.csv -y Gyroscope.sds.yaml Accelerometer.sds.yaml --normalize --start-timeslot 200 --stop-timeslot 300
```

Convert **Qeexo V2 CSV** files to **SDS** files:

```bash
python sds-convert.py qeexo_v2_csv -i Accelerometer.csv -o Accelerometer.sds
```

#### Video

The `video` mode converts an SDS file (`.sds`) containing video frames into a standard MP4 (H.264) file (`.mp4`).
Video frame format must be specified in the YAML metadata file (`.yml`), where pixel format,
resolution and frame stride shall be properly specified.

```txt
usage: sds-convert.py video [-h]
                            -i <input_file>
                            -o <output_file>
                            -y <yaml_file>

Convert SDS file to MP4 video file

options:
  -h, --help        show this help message and exit

required:
  -i <input_file>   Input file
  -o <output_file>  Output file
  -y <yaml_file>    YAML metadata file
```

!!! Note
    - The tool expects the SDS file to contain strictly video frames; no header markers or custom formatting.

**Example of metadata yml file for RGB888 video stream:**

```yml
sds:
  name: Video Stream - RGB888
  description: 192 x 192 RGB888 video frames
  sample-frequency: 24
  content:
    - image:
        pixel_format: RGB888
        width: 192
        height: 192
        stride_bytes: 576   # 3 bytes per pixel
```

**Example:**

```bash
python sds-convert.py video -i Camera.0.sds -o Camera.mp4 -y Camera.sds.yml
```

!!! Note
    - [Theory of Operation - Image Metadata Format](https://github.com/ARM-software/SDS-Framework/blob/c18efee/documentation/theory.md#image-data-stream) contains more information about the supported video formats.

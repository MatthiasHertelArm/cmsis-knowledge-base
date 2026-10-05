---
id: "alp-zephyr-shell-3-mqtt-shell-create-the-mosquitto-docker-co"
type: "concept"
domain: "rtos"
title: "3 mqtt shell: Create the Mosquitto Docker Compose project"
summary: "After building the Zephyr application, you'll run an Eclipse Mosquitto broker in Docker."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_shell/3_mqtt_shell.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_shell/3_mqtt_shell/#create-the-mosquitto-docker-compose-project"
license: "CC-BY-SA-4.0"
mode: "V"
---

After building the Zephyr application, you'll run an Eclipse Mosquitto broker in Docker.

Create a directory named `mosquitto_shell` on your host computer with the following structure:

```output
mosquitto_shell/
|-- docker-compose.yml
`-- mosquitto/
    `-- config/
        `-- mosquitto.conf
```

Edit the `docker-compose.yml` file and add the following text:

```yaml
services:
  mosquitto:
    image: eclipse-mosquitto:latest
    container_name: mosquitto-mqtt
    ports:
      - "1883:1883"
    volumes:
      - ./mosquitto/config:/mosquitto/config:ro
      - ./mosquitto/data:/mosquitto/data
      - ./mosquitto/log:/mosquitto/log
    restart: unless-stopped
```

Edit the `mosquitto.conf` file and add the following text:

```text
listener 1883 0.0.0.0
allow_anonymous true

persistence true
persistence_location /mosquitto/data/

log_dest file /mosquitto/log/mosquitto.log
log_dest stdout
log_type all
```

From the `mosquitto_shell` directory, start the broker:

```bash
docker compose up -d
```

Check that the container is running:

```bash
docker compose ps
```

The output is similar to:

```output
NAME                  IMAGE                        STATUS
mosquitto-mqtt        eclipse-mosquitto:latest     Up
```

The `eclipse-mosquitto` image includes `mosquitto_pub` and `mosquitto_sub`, so you can run both tools from inside the container with `docker exec`.

### (Optional) Install Mosquitto directly on host machine

If you prefer not to use Docker, you can install Mosquitto directly on your host computer. This gives you the `mosquitto` broker, `mosquitto_pub`, and `mosquitto_sub` commands locally.

Install Mosquitto with your operating system package manager.

On Linux (Debian or Ubuntu):

```bash
sudo apt install mosquitto mosquitto-clients
```

On macOS, use Homebrew:

```bash
brew install mosquitto
```

On Windows, use winget:

```bash
winget install EclipseFoundation.Mosquitto
```

After installation on Windows, add the Mosquitto install directory (typically `C:\Program Files\mosquitto`) to your `PATH` environment variable so that `mosquitto_pub` and `mosquitto_sub` are available from the command prompt.

After installing Mosquitto directly, start the broker using your operating system's service manager, or run it manually with a local configuration file.

The remaining commands in this section use `docker exec` to run `mosquitto_sub` and `mosquitto_pub` inside the container. If you installed Mosquitto directly, drop the `docker exec -it mosquitto-mqtt` prefix and run the tools directly instead. 

For example, this container command:

```bash
docker exec -it mosquitto-mqtt mosquitto_sub -h localhost -t "1a2b3c/sh/tx" -v
```

becomes:

```bash
mosquitto_sub -h localhost -t "1a2b3c/sh/tx" -v
```

The same substitution applies to every `mosquitto_pub` command later in this section.

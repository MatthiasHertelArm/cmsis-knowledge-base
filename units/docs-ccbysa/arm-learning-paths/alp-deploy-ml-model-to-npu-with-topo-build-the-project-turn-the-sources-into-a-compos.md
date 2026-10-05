---
id: "alp-deploy-ml-model-to-npu-with-topo-build-the-project-turn-the-sources-into-a-compos"
type: "concept"
domain: "edge-ai"
title: "Deploy a machine learning application to the Arm Ethos-U65 NPU on NXP FRDM i.MX 93 with Topo: Build the Topo Project from scratch: Turn the sources into a Compo"
summary: "Before adding Topo metadata, make the project work as ordinary Compose. Start by containerizing the Cortex-A web application."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/build-the-project.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/build-the-project/#turn-the-sources-into-a-compose-project"
license: "CC-BY-SA-4.0"
mode: "V"
---

Before adding Topo metadata, make the project work as ordinary Compose. Start by containerizing the Cortex-A web application.

Create `webapp/Dockerfile` with the following complete contents:

```Dockerfile
FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

RUN python -m pip install --no-cache-dir flask==3.0.3

COPY src/data/imagenet_classes.txt /opt/mv2-imx93/imagenet_classes.txt
COPY src/app.py .
COPY src/templates/ templates/
COPY src/static/ static/

EXPOSE 3000

CMD ["python", "app.py"]
```

Create `webapp/compose.yaml` with the following complete contents:

```yaml
services:
  webapp:
    platform: linux/arm64
    build:
      context: .
      dockerfile: Dockerfile
    privileged: true
    ports:
      - "${WEBAPP_PORT:-3001}:3000"
    volumes:
      - /sys:/sys
      - /dev:/dev
    restart: unless-stopped
```

Create the root `compose.yaml` with the following complete contents:

```yaml
services:
  webapp:
    platform: linux/arm64
    extends:
      file: webapp/compose.yaml
      service: webapp
```

Check that Compose can read the project:

```bash
docker compose config
```

The output includes the resolved `webapp` service, and is similar to:

```output
services:
  webapp:
    build:
      context: /path/to/new-topo-npu-template/webapp
      dockerfile: Dockerfile
    ports:
      - mode: ingress
        target: 3000
        published: "3001"
```

At this point, Compose can build and run the Cortex-A web application as a normal Linux container. The image runs `webapp/src/app.py`. It packages the Jinja templates from `webapp/src/templates/`, the static assets from `webapp/src/static/`, and the ImageNet labels from `webapp/src/data/imagenet_classes.txt`. The container listens on port `3000`, and Compose publishes it on host port `3001` unless you set `WEBAPP_PORT` to another value.

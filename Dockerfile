FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y cmake gcc g++ make python3 python3-venv python3-dev libasound2-dev

# ffmpeg

RUN python3 -m venv /usr/src/app/.venv
ENV PATH="/usr/src/app/.venv/bin:$PATH"

COPY src/requirements.txt /usr/src/app
RUN pip install -r /usr/src/app/requirements.txt

WORKDIR /usr/src/app
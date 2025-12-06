FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    octave \
    octave-control \
    octave-signal \
    octave-statistics \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

CMD ["octave-cli"]

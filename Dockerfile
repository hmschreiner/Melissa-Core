FROM ubuntu:latest

LABEL maintainer="Henrique Schreiner hms.sud@gmail.com"

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y
RUN apt-get install -y \
    python-pip \
    gcc \
    automake \
    autoconf \
    libtool \
    bison \
    swig \
    python-dev \
    libpulse-dev \
    espeak \
    multimedia-jack \
    git \
    python-pyaudio \
    python-gst-1.0 \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-ugly \
    gstreamer1.0-tools

COPY . /app

WORKDIR /app

COPY t800/data/memory.db.default t800/data/memory.db

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "-m", "t800"]
# CMD ["FLASK_APP=t800/__main__.py", "python", "-m", "flask", "run"]

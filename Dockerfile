FROM ubuntu:latest

MAINTAINER Laukik Panse <lpanse@nyit.edu>
LABEL DESCRIPTION              = "Simple Json hello world " \
      VENDOR                   = "Laukik Panse" \
      VENDOR_URL               = "https://newtonapi.com/"

RUN apt-get update && apt-get -q install -y \
    curl \
    python3-pip \
    dnsutils
EXPOSE 3000
WORKDIR /application
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY app.py .
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]
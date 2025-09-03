FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && pip install scapy
RUN apt-get update 
RUN apt-get install -y --no-install-recommends \
    net-tools \
    install sudo
VOLUME /app
COPY ./src ./src
EXPOSE 8080

CMD ["flask","--app", "./src/hello.py" ,"--debug","run","--host=0.0.0.0", "--port=8080" ]
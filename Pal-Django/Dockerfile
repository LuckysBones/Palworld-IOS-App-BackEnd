FROM python:3.9-slim

WORKDIR /home/PalLens

COPY requirements.txt /home/PalLens

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8211/tcp
EXPOSE 8211/udp
EXPOSE 27015/tcp
EXPOSE 27015/udp
EXPOSE 8212/tcp
EXPOSE 8212/udp

RUN apt-get update && apt-get install -y supervisor

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["tail", "-f", "/dev/null"]
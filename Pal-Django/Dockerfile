FROM python:3.9-slim

WORKDIR /PalLens

COPY requirements.txt /PalLens/
COPY . /PalLens

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8211/tcp
EXPOSE 8211/udp
EXPOSE 27015/tcp
EXPOSE 27015/udp
EXPOSE 8212/tcp
EXPOSE 8212/udp
# Inside Pal-Django/Dockerfile

# Install supervisor
RUN apt-get update && apt-get install -y supervisor

# Add supervisor configuration file
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["tail", "-f", "/dev/null"]
#CMD ["daphne", "-b", "0.0.0.0", "-p", "8001", "PalLensBackEnd.asgi:application"]

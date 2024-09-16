FROM ubuntu:22.04

WORKDIR /Pal

RUN yes | apt update && yes | apt upgrade
RUN yes | apt install neovim
RUN yes | apt install nano

EXPOSE 8222/tcp
EXPOSE 8222/udp
EXPOSE 27015/tcp
EXPOSE 27015/udp
EXPOSE 8212/tcp
EXPOSE 8212/udp

CMD ["tail", "-f", "/dev/null"]
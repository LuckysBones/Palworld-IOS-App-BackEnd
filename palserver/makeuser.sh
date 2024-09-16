#!/bin/bash

#create user steam
useradd -m steam

echo "steam:steam" | chpasswd

#chown -R steam:steam /Pal

chown -R steam PalServer/

su steam -c "bash ./PalServer/PalServer.sh"

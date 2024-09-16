#!/bin/bash

# Add 32-bit architecture supprt and update package lists
dpkg --add-architecture i386 && apt-get update -y

# Install required packages
apt install -y wget curl lib32gcc-s1 lib32stdc++6 libstdc++6:i386 lib32z1

# Create Steam directory and navigate into it
mkdir -p Steam && cd Steam

# Download and extract SteamCMD
curl -sqL "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" | tar zxvf -

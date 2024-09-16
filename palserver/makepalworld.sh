#!/bin/bash

# Define the installation directory (current directory or a subdirectory)
INSTALL_DIR="$(pwd)/PalServer"

# Install the first application (App ID: 2394010)
./Steam/steamcmd.sh +login anonymous +force_install_dir "$INSTALL_DIR" +app_update 2394010 validate +quit

# Create necessary directories (if required)
#mkdir -p "$INSTALL_DIR/Pal/Saved/Config/LinuxServer/"

INSTALL_DIR="$(pwd)/steamapps"
# Install the second application (App ID: 1007)
./Steam/steamcmd.sh +login anonymous +force_install_dir "$INSTALL_DIR" +app_update 1007 +quit

cp PalServer/linux64/steamclient.so PalServer/Pal/Binaries/Linux/

mkdir -p /Pal/PalServer/Pal/Saved/Config/LinuxServer/

cp PalWorldSettings.ini PalServer/Pal/Saved/Config/LinuxServer/

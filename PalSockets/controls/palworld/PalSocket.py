# main.py
# Server side for grabbing Palworld Server stats or commands 
# Program will also send and recive sent, info through a socketio api
import time
import subprocess
import json


# Importing the PalworldRestApi module with the absolute path
from PalSockets.controls.palworld.PalworldApi import PalworldRestApi

class PalConnect:
    # Grab Player Info
    def get_players():
        return PalworldRestApi.findPlayers()

    # Grab Server Metrics
    def get_metrics():
        return PalworldRestApi.findMetrics()

    # Grab Server Info
    def get_info():
        return PalworldRestApi.serverInfo()

    # Send a message to the Server (Pops on the in game screen)
    def push_message(message):
        return PalworldRestApi.sendMessage(message)

    # Server will save the game/world
    def push_save():
        return PalworldRestApi.saveWorld()

    # Sever will Shutdown the server based 
    # on allotted time and a message will be sent
    def push_shutdown(shutdownMessage,shutdownTime):
        return PalworldRestApi.shutWorld(shutdownMessage,shutdownTime)

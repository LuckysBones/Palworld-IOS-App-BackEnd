from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
import json
from PalSockets.controls.palworld.PalSocket import PalConnect

import time

class PlayersConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "Players"
        self.room_group_name = "Group_Players"
        async_to_sync(self.channel_layer.group_send)(
            self.room_name, self.room_group_name
        ) 
        self.accept()
        

    def receive(self, text_data=None):
        self.send(text_data=json.dumps(PalConnect.get_players()))
    
    def disconnect(self, close_code):
        pass
    


class MetricConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "Metric"
        self.room_group_name = "Group_Metric"
        async_to_sync(self.channel_layer.group_send)(
            self.room_name, self.room_group_name
        ) 
        self.accept()

    def receive(self, text_data=None):
        self.send(text_data=json.dumps(PalConnect.get_metrics()))
	
    def pong(self, event):
        print("Pong")
    
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )



class InfoConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "Info"
        self.room_group_name = "Group_Info"
        async_to_sync(self.channel_layer.group_send)(
            self.room_name, self.room_group_name
        ) 
        self.accept()
        

    def receive(self, text_data=None):
        self.send(text_data=json.dumps(PalConnect.get_info()))
    
    def disconnect(self, close_code):
        pass


class MessageConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "Message"
        self.room_group_name = "Group_Message"
        async_to_sync(self.channel_layer.group_send)(
            self.room_name, self.room_group_name
        ) 
        self.accept()

    def receive(self, text_data):
        PalConnect.push_message(text_data)
    
    def disconnect(self, close_code):
        pass



class SaveConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "Save"
        self.room_group_name = "Group_Save"
        async_to_sync(self.channel_layer.group_send)(
            self.room_name, self.room_group_name
        ) 
        self.accept()
        #self.send(text_data=json.dumps())

    def receive(self,text_data):
        PalConnect.push_save()
    
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )



class ShutdownConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "Shutdown"
        self.room_group_name = "Group_Shutdown"
        async_to_sync(self.channel_layer.group_send)(
            self.room_name, self.room_group_name
        ) 
        self.accept()

    def receive(self, text_data):
        PalConnect.push_shutdown(text_data, 30)
    
    def disconnect(self, close_code):
        pass

import requests
import json

class PalworldRestApi:

    def restAPI():
        return "restAPI"

    def findPlayers():
        try:
            url = "http://admin:password@palserver:8212/v1/api/players"
            payload={}
            headers = {'Accept': 'application/json'}
            response = requests.request("GET", url, headers=headers, data=payload)
            return json.loads(response.text)
        except:
            return "error - unable to connect to server"
        

    def findMetrics():
        try:
            url = "http://admin:password@palserver:8212/v1/api/metrics"
            payload={}
            headers = {'Accept': 'application/json'}
            response = requests.request("GET", url, headers=headers, data=payload)
            return json.loads(response.text)
        except:
            return "error - can not grab Metrics"
        
    def sendMessage(message):
        try:
            url = "http://admin:password@palserver:8212/v1/api/announce"
            payload = json.dumps({"message": message})
            headers = {'Content-Type': 'application/json'}
            response = requests.request("POST", url, headers=headers, data=payload)
            return response.text
        except:
            return "error - can not Send Message to the server"

    def serverInfo():
        try:
            url = "http://admin:password@palserver:8212/v1/api/info"
            payload={}
            headers = {'Accept': 'application/json'}
            response = requests.request("GET", url, headers=headers, data=payload)
            return json.loads(response.text)
        except:
            return "error - can not grab Server Info"

    def saveWorld():
        try:
            url = "http://admin:password@palserver:8212/v1/api/save"
            payload={}
            headers = {}
            response = requests.request("POST", url, headers=headers, data=payload)
            return response.text
        except:
            return "error - can not Save the World"
    
    def shutWorld(shutdownMessage,shutdownTime):
        try:
            url = "http://admin:password@palserver:8212/v1/api/shutdown"
            payload = json.dumps({
                "waittime": shutdownTime,
                "message": shutdownMessage
                })
            headers = {
                'Content-Type': 'application/json'
                }
            response = requests.request("POST", url, headers=headers, data=payload)
            return response.text
        except:
            return "error - can not send a ShutDown request"

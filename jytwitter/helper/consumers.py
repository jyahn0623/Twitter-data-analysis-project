from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        print("잘 가시게")
    
    def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        print(message)
        self.send(text_data=json.dumps({
            'messeage' : message,
        }))
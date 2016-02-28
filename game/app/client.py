from socketIO_client import SocketIO, BaseNamespace
import socket
import json

class Connection():
    def __init__(self, stage, ip):
        self.stage = stage
        self.ip = ip
        print(self.ip)

class ClientSession():
    def __init__(self, connection):
        self.connection = connection

    def on_assign_id(self, *args):
        self.connection.id = args[0]
        self.connection.player = args[1]
    
    def on_ball_data(self, *args):
        print(args[0])
        pass 

    def on_opponent_paddle(self, *args):
        print(json.loads(args[0]))
    
    def send_coordinates(self, *args):
        self.mainSocket.emit('UpdatePaddle', json.dumps({"x": self.connection.stage.paddle0.x, "y": self.connection.stage.paddle0.y}))
    
    def start(self):
        self.mainSocket = SocketIO(self.connection.ip, 8888)
        
        # Begin event calls.
        self.mainSocket.wait(seconds=1)
        self.mainSocket.on('AssignId', self.on_assign_id)    
        self.mainSocket.on('BallData', self.on_ball_data)
        self.mainSocket.on('OpponentPaddle', self.on_opponent_paddle)
        self.mainSocket.wait(seconds=1)
        #check_coordinates()

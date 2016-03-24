from socketIO_client import SocketIO, BaseNamespace
import socket
import json
import threading

class Connection():
    def __init__(self, stage, ip):
        self.stage = stage
        self.ip = ip
        print(self.ip)

class ClientSession(threading.Thread):
    def __init__(self, connection):
        threading.Thread.__init__(self)
        self.connection = connection
        self.mainSocket = SocketIO(self.connection.ip, 8888)

    def on_assign_id(self, *args):
        self.connection.id = args[0]
        self.connection.player = args[1]
    
    def on_ball_data(self, *args):
        print(args[0])

    def on_opponent_paddle(self, *args):
        data = json.loads(args[0])
        self.connection.stage.paddle1.x = data["x"]
        self.connection.stage.paddle1.y = data["y"]
    
    def send_coordinates(self, *args):
        self.mainSocket.emit('UpdatePaddle', json.dumps({"x": self.connection.stage.paddle0.x, "y": self.connection.stage.paddle0.y}))
    
    def run(self):
        
        # Begin event calls.
        while(1):
            self.mainSocket.on('AssignId', self.on_assign_id)    
            self.mainSocket.on('BallData', self.on_ball_data)
            self.mainSocket.on('OpponentPaddle', self.on_opponent_paddle)
            self.mainSocket.wait(seconds=.033)
        #check_coordinates()

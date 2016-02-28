from socketIO_client import SocketIO, BaseNamespace
import socket

class Connection():
    def __init__(self, stage):
        self.stage = stage

connection = Connection(None)

def on_assign_id(*args):
    global connection
    connection.id = args[0]
    connection.player = args[1]

def on_ball_data(*args):
    print(args[0])
    pass 

def check_coordinates():
    # Update coordinates of paddles.
    pass

def start():
    global connection
    connection = Connection(None)
    mainSocket = SocketIO('localhost', 8888)
    
    # Begin event calls.

    mainSocket.on('AssignId', on_assign_id)    
    mainSocket.on('BallData', on_ball_data)
    check_coordinates()
    mainSocket.wait()

start()

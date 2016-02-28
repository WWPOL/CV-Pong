from socketIO_client import SocketIO

class Connection:
    def on_connect(self):
        print('Established connection to server.')

io = SocketIO('10.189.41.213', 7777, Connection)
io.wait(seconds=1)

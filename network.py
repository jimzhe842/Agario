import pickle
import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = "192.168.1.181"
        self.port = 5555
        self.addr = (self.server,self.port)
        self.p = self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def getP(self):
        return self.p

    def send(self,data):
        try:
        
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(4096*16))

        except socket.error as e:
            print(e)

            
import pygame
import socket
from _thread import *
import sys
from player import Player
import pickle
import random

width = 1200
height = 800

server = '192.168.1.181'
port = 5555
addr = (server, port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

from game import Game
            



try:
    s.bind(addr)
except socket.error as e:
    print(e)

s.listen()
print("Waiting for a connection, Server started")
##players = [Player(50,50,50,50,(255,0,0)), Player(100,100,50,50,(0,255,0))]
plrs = {}


def threaded_client(conn,player):
    # create a new cell
    conn.send(pickle.dumps(plrs[player]))

    while True:
        try:
            plrUpdate = pickle.loads(conn.recv(4096))
            if player in plrs:
                
                if not plrUpdate:
                    print("Disconnected")
                    break
                else:
                    game.updatePlayer(plrUpdate)
                    print("updated Player")
                    conn.sendall(pickle.dumps(game))
            else:
                break
        except: #Removed socket.error as e
            break

    #try:
    #    print("Closing game: ", gameId)
    #except:
    #    pass


    game.addLoggedPlr(plrs.pop(player))
    #del plrs[player]

    print("Lost connection")
    conn.close()


currentPlayer = 0

game = Game(plrs)

while True:
    conn, addr = s.accept()
    print("Connected to ", addr)
    gameId = currentPlayer // 2
    print(gameId)
    
    
    plrs[currentPlayer] = Player(random.randint(0,width),random.randint(0,height),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),currentPlayer)

    start_new_thread(threaded_client,(conn,currentPlayer))
    currentPlayer += 1

import pygame
import random

width = 1200
height = 800
def magnitude(a,b):
    return ( (( a.x - b.x ) ** 2) + (( a.y - b.y ) ** 2) ) ** ( 1 / 2 )

class Game:

    def __init__(self,plrs):
        self.food = []
        self.plrs = plrs
        self.loggedPlrs = {}

    def updatePlayer(self,player):
        self.plrs[player.id] = player
        for food in self.food:
            if self.isTouching(food,player):
                player.mass += food.mass #int(food.radius / 10)
                self.food.pop(self.food.index(food))
        eatenPlrs = []
        for loggedPlr in self.loggedPlrs.items(): #Player that exited
            loggedPlr = loggedPlr[1]
            if abs(loggedPlr.radius - player.radius) > 3:
                print("isGreater than 3")
                dist = magnitude(player,loggedPlr)
                if loggedPlr.radius > player.radius:
                    if dist + player.radius <= loggedPlr.radius:
                        loggedPlr.mass += player.mass
                        loggedPlr.radius = loggedPlr.get_radius()
                        player.reset()
                else:
                    if dist + loggedPlr.radius <= player.radius:

                        print("okay")
                        player.mass += loggedPlr.mass
                        print("reached 1")
                        eatenPlrs.append(loggedPlr.id)
                        #self.loggedPlrs.pop(loggedPlr.id)
                        #print("existing", self.loggedPlrs[loggedId])
                        print("reached here")
        for id in eatenPlrs:
            self.loggedPlrs.pop(id)
            
        print("hello")
        print("adding")
        if random.randint(0,1) == 0:
            
            #print("Adding")
            self.food.append(Food())
        

    def isTouching(self,food,player):
        if magnitude(food,player) + food.radius <= player.radius:
            return True
        return False

    def addLoggedPlr(self,plr):
        self.loggedPlrs[plr.id] = plr


class Food:
    def __init__(self):
        self.x = random.randint(0,width)
        self.y = random.randint(0,height)
        self.mass = 1
        self.radius = int(( (self.mass * 100) / 3.14 ) ** ( 1/2 ))
        
        self.color = (random.randint(125,255),random.randint(125,255),random.randint(125,255))
        
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

    

        
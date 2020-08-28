import pygame
from network import Network
from player import Player
from game import Game

pygame.init()

width = 1200
height = 800
win = pygame.display.set_mode((width,height))

pygame.display.set_caption("Agario")



font = pygame.font.SysFont('comicsans',30,True)
def redrawWindow(win,game,you):
    win.fill((255,255,255))
    for food in game.food:
        food.draw(win)
    #Need a function that sorts the order of plr radius
    #sortedTable = sorted(game.plrs.items(), key = lambda x: x[1].radius) ; print(sortedTable[0])
    combinedDictionary = {**game.plrs, **game.loggedPlrs}

    print("dictionary")
    for plr in sorted(combinedDictionary.items(), key = lambda x: x[1].mass):
        print("mass", plr[1].mass)
        
        #print(Player)
        plr[1].draw(win)
    #plr2.draw(win)
    
    text = font.render('Mass: ' + str(you.mass),1,(128,128,128))
    win.blit(text,(10, height - text.get_height() - 10 ))
    
    pygame.display.update()

def isEngulfing(them, you, dist):
    if them.radius > you.radius:
        if dist + you.radius <= them.radius:
            you.reset()
    else:
        if dist + them.radius <= you.radius:
            you.mass += them.mass
            # you.radius = int((((you.radius ** 2) * 3.14 + (them.radius ** 2) * 3.14) / 3.14) ** (1/2))

    #if you.x >= them.x and you.x <= them.x + diff:
    #    if you.y >= them.y and you.y <= them.y + diff:
    #        return True
    #return False



def magnitude(a,b):
    return ( (( a.x - b.x ) ** 2) + (( a.y - b.y ) ** 2) ) ** ( 1 / 2 )


def main():
    run = True
    n = Network()
    updatedPlr = n.getP()
    clock = pygame.time.Clock()

    plrId = updatedPlr.id
    while run:
        clock.tick(27)
        game = n.send(updatedPlr)
        updatedPlr = game.plrs[plrId]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        for _,plr in game.plrs.items(): #need items for dictionary
            if plr != updatedPlr:
                if abs(plr.radius - updatedPlr.radius) > 3:
                    dist = magnitude(plr,updatedPlr)
                    isEngulfing(plr,updatedPlr,dist)

        updatedPlr.move()
        #print("Ate")
        redrawWindow(win,game,updatedPlr)
main()
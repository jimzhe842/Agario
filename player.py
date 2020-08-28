import pygame

class Player():
    def __init__(self,x,y,color,id):
        self.x = x
        self.y = y
        
        self.color = color
        self.secondaryColor = ( color[0] / 2, color[1] / 2, color[2] / 2 ) 
        self.vel = 5
        self.id = id
        self.mass = 5
        self.radius = int(( (self.mass * 100) / 3.14 ) ** ( 1/2 ))
        #self.left = False

    def __repr__(self):

        return repr((self.id,self.x,self.y,self.radius,self.color,self.vel))

    def get_radius(self):
        self.radius = int(( (self.mass * 100) / 3.14 ) ** ( 1/2 ))
        return self.radius

    def move(self):
        #print(self.x)
        #keys = pygame.key.get_pressed()

        #if keys[pygame.K_UP]:
        #    self.y -= self.vel
        #if keys[pygame.K_DOWN]:
        #    self.y += self.vel

        #if keys[pygame.K_LEFT]:
        #    self.x -= self.vel

        #if keys[pygame.K_RIGHT]:
        #    self.x += self.vel

        mousePos = pygame.mouse.get_pos()
        mouseX = mousePos[0]
        mouseY = mousePos[1]
        deltaX = mouseX - self.x
        deltaY = mouseY - self.y
        print(int(self.vel * max(15/self.radius, 0.2)))
        #self.vel = int(5 * (max((15/self.radius) ** (1/2),0.2)))
        dist = ( (( deltaX ) ** 2) + (( deltaY ) ** 2) ) ** ( 1 / 2 )
        if dist >= 5:

            self.x += int(deltaX/dist * self.vel * min((dist/100) ** (1/2),1))

            self.y += int(deltaY/dist * self.vel * min((dist/100) ** (1/2),1))

    def reset(self):
        self.x = 100
        self.y = 100
        self.mass = 5
        self.vel = 5
        self.radius = int(((self.mass * 100)/3.14) ** 1/2)

    def draw(self,win):
        pygame.draw.circle(win,self.secondaryColor,(self.x,self.y),self.get_radius()+2)
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

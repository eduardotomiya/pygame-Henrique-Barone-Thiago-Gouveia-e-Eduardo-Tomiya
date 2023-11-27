import pygame,random

class circle(object):
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.xv = random.randint(-6,6 )
        self.yv = 12
        self.xx = self.x + self.w
        self.yy = self.y + self.h

    def draw(self, win):
        pygame.draw.circle(win, self.color, [self.x, self.y],12,6)
        
    def move(self):
        self.x += self.xv
        self.y += self.yv

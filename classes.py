import pygame

class square():
    def __init__(self, x, y, num):
        self.x = x + 10
        self.y = y + 10
        self.num = num
        self.size = 180
        self.clicked = 0

    def click(self, type):
        self.clicked = type

    def draw(self, win):
        self.rect = pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.size, self.size))
        if self.clicked == 1:
            pygame.draw.line(win, (0, 0, 255), (self.x + 8, self.y + self.size), (self.x - 8 + self.size, self.y), 20)
            pygame.draw.line(win, (0, 0, 255), (self.x + 8, self.y), (self.x - 8 + self.size, self.y + self.size), 20)
        elif self.clicked == 2:
            pygame.draw.circle(win, (255, 0, 0), (round(self.x + self.size / 2), round(self.y + self.size / 2)), round(self.size / 2), 10)
# Akif Yahya Dirican's Snake Game

import pygame
from pygame.locals import *
import time
import random

SIZE = 20

class Apple:
    def __init__(self, parent_screen):
        self.apple = pygame.image.load ("apple.png").convert()
        self.apple = pygame.transform.scale(self.apple, (20,20))
        self.parent_screen = parent_screen
        self.x = SIZE * 7
        self.y = SIZE * 7

    def draw(self):
        self.parent_screen.blit(self.apple,(self.x, self.y))
        pygame.display.flip()

    def move (self):
        self.x = random.randint(0, 24) * SIZE
        self.y = random.randint(0, 24) * SIZE

class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load ("green.png").convert()
        self.block = pygame.transform.scale(self.block, (20,20))
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = "down"

    def draw(self):
        self.parent_screen.fill ((255,255,255))
        for i in range (self.length):
            self.parent_screen.blit(self.block,(self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length (self):
        self.length += 1
        self.x.append (SIZE)
        self.y.append (SIZE)
        
    def move_up(self):
        self.direction = "up"
    def move_down(self):
        self.direction = "down"
    def move_right(self):
        self.direction = "right"
    def move_left(self):
        self.direction = "left"

    def walk(self):
        for i in range (self.length -1, 0, -1):
                self.y [i] = self.y [i-1]
                self.x [i] = self.x [i-1]

        if self.direction == "up":
            self.y[0] -= SIZE

        elif self.direction == "down":
            self.y[0] += SIZE

        elif self.direction == "right":
            self.x[0] += SIZE

        elif self.direction == "left":
            self.x[0] -= SIZE

        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500,500))
        self.surface.fill ((255,255,255))
        self.snake = Snake (self.surface, 3)
        self.snake.draw()
        self.apple = Apple (self.surface)
        self.apple.draw()

    def is_collision (self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def score(self):
        font = pygame.font.SysFont("arial", 12)
        score = font.render (f"Score: {self.snake.length}", True, (1,1,1))
        self.surface.blit (score, (450,12))

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.score()
        pygame.display.flip()

        if self.is_collision (self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

        for i in range(3, self.snake.length):
            if self.is_collision (self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                exit()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                
                elif event.type == QUIT:
                    running = False
            
            self.play()
            time.sleep(0.1)
   
if __name__ == "__main__":
    game = Game()
    game.run()
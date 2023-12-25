# Akif Yahya Dirican's Snake Game

import pygame
from pygame.locals import *
import time
import random

SIZE = 20

class PlayingScreen:
    def __init__(self, surface):
        self.surface = surface
        self.border_width = SIZE
        self.width = 500
        self.height = 500

    def draw_screen(self):
        # Clear the screen with a white background
        self.surface.fill((255, 255, 255))

        # Draw horizontal borders
        pygame.draw.rect(self.surface, (0, 0, 0), (0, 0, self.width, self.border_width))  # Top border
        pygame.draw.rect(self.surface, (0, 0, 0), (0, 0, self.border_width, self.height))  # Left border
        pygame.draw.rect(self.surface, (0, 0, 0), (0, self.height - self.border_width, self.width, self.border_width))  # Bottom border
        pygame.draw.rect(self.surface, (0, 0, 0), (self.width - self.border_width, 0, self.border_width, self.height))  # Right border

    def is_collision_with_border(self, x, y):
        return x < self.border_width or x >= self.width - self.border_width or y < self.border_width or y >= self.height - self.border_width

class Apple:
    def __init__(self, parent_screen):
        self.apple = pygame.image.load ("apple.png").convert()
        self.apple = pygame.transform.scale(self.apple, (SIZE, SIZE))
        self.parent_screen = parent_screen
        self.x = random.randint(1, 23) * SIZE
        self.y = random.randint(1, 23) * SIZE

    def draw(self):
        self.parent_screen.blit(self.apple,(self.x, self.y))
        pygame.display.flip()

    def move (self):
        self.x = random.randint(1, 23) * SIZE
        self.y = random.randint(1, 23) * SIZE

class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = "down"

    def draw(self):
        self.head = pygame.image.load ("snake_head.png").convert()
        self.head = pygame.transform.scale(self.head, (SIZE, SIZE))
        self.parent_screen.blit(self.head, (self.x[0], self.y[0]))
        for i in range(1, self.length):
            pygame.draw.rect(self.parent_screen, (0, 255, 0), (self.x[i], self.y[i], SIZE, SIZE))  # Draw green squares for the snake
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
        self.playing_screen = PlayingScreen(self.surface)
        self.snake = Snake (self.surface, 3)
        self.apple = Apple (self.surface)

    def is_collision (self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def score(self):
        font = pygame.font.SysFont("arial", 12)
        score = font.render (f"Score: {self.snake.length}", True, (1,1,1))
        self.surface.blit (score, (10,480))

    def play(self):
        self.playing_screen.draw_screen()
        self.snake.walk()
        self.apple.draw()
        self.snake.draw()
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
            if self.playing_screen.is_collision_with_border(self.snake.x[0], self.snake.y[0]):
                pygame.quit()  # Quit Pygame
                exit()  # Exit the game loop

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
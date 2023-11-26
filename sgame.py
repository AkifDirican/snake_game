# Akif Yahya Dirican's Snake Game

import pygame
from pygame.locals import *

def draw_block():
    surface.fill ((255,255,255))
    surface.blit(block,(block_x,block_y))
    pygame.display.flip()
   
if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((500,500))
    surface.fill ((255,255,255))

    block = pygame.image.load ("Messi_block.png").convert()
    block = pygame.transform.scale(block, (70,70))
    block_x = 250
    block_y = 250
    surface.blit(block,(block_x,block_y))

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if event.key == K_UP:
                    block_y -= 5
                    draw_block ()
                if event.key == K_DOWN:
                    block_y += 5
                    draw_block ()
                if event.key == K_LEFT:
                    block_x -= 5
                    draw_block ()
                if event.key == K_RIGHT:
                    block_x += 5
                    draw_block ()
                
            elif event.type == QUIT:
                running = False

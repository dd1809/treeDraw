import copy
import pygame as pg
from random import randint
from matrix_processing import generate_matrix, change_matrix_BFS, change_matrix_DFS

width_count, height_count = 200, 200
size = 5
resolution = width, height = width_count * size + 1, height_count * size + 1
FPS = 60

screen = pg.display.set_mode(resolution)
clock = pg.time.Clock()

COLORS = {'.': (0, 150, 0),
          'S': (255, 0, 0),
          'U': (0, 0, 200),
          'D': (255, 255, 0),
          'L': (0, 200, 200),
          'R': (200, 0, 200)}
while True:
    blocks = generate_matrix(width_count, height_count)
    for frame in change_matrix_BFS(blocks):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()

        screen.fill(pg.Color(0, 80, 0))

        [pg.draw.line(screen, (78, 78, 78), (x, 0), (x, height)) for x in range(0, width, size)]
        [pg.draw.line(screen, (78, 78, 78), (0, y), (width, y)) for y in range(0, height, size)]

        '''for x_block in range(1, width_count - 1):
            for y_block in range(1, height_count - 1):
                if frame[y_block][x_block] in COLORS:
                    pg.draw.rect(screen, (COLORS[frame[y_block][x_block]]),
                                 (x_block * size + 2, y_block * size + 2, size - 2, size - 2))'''

        [pg.draw.rect(screen, (COLORS[frame[y_block][x_block]]),
                      (x_block * size + 2, y_block * size + 2, size - 2, size - 2))
         for x_block in range(1, width_count - 1)
         for y_block in range(1, height_count - 1)
         if frame[y_block][x_block] in COLORS]

        clock.tick(FPS)
        pg.display.flip()
        print("FPS:", int(clock.get_fps()))

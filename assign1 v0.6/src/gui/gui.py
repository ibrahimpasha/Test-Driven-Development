import pygame
from itertools import product
from src.game.game_of_life import *
import sys

ROWS = COLUMNS = 50
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DELAY = 10
WINDOW_SIDE_LENGTH = 600
SIDE_LENGTH = int((4 * WINDOW_SIDE_LENGTH) / (5 * ROWS + 1))
WINDOW_SIZE = [WINDOW_SIDE_LENGTH, WINDOW_SIDE_LENGTH]
MIN, MAX = 0, ROWS
PADDING = 10
STOP = False

default_living_positions = [(1, 1), (2, 2), (2, 3), (3, 1), (3, 2),
                    (8, 8), (8, 9), (9, 7), (10, 8), (10, 9), (9, 10),
                    (21, 21), (22, 22), (22, 23), (23, 21), (23, 22),
                    (11, 2), (12, 2), (13, 2),
                    (1, 21), (1, 22), (2, 21), (2, 22)]


living_positions = list(eval("".join(sys.argv[1:]).replace(')(', '), (')[1:-1])) if(len(sys.argv)>4) else default_living_positions

pygame.init()
pygame.display.set_caption("Game of Life")
screen = pygame.display.set_mode(WINDOW_SIZE)

clock = pygame.time.Clock()

while not STOP:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      STOP = True
  
  screen.fill(BLACK)
  (min_x, min_y), (max_x, max_y) = get_bounds(living_positions)
  MIN = min(min_x, min_y) if min_x <= MIN or min_y <= MIN else MIN
  MAX = max(max_x, max_y) if max_x >= MAX or max_y >= MAX else MAX
  SIDE_LENGTH = int((4 * WINDOW_SIDE_LENGTH) / (5 * MAX + 1))
  
  for row, column in product(range(MIN, MAX + PADDING), range(MIN, MAX + PADDING)):
    color = BLACK if (row, column) in living_positions else WHITE
    pygame.draw.rect(screen, color,
                     [((SIDE_LENGTH / 4) + SIDE_LENGTH) * column + SIDE_LENGTH / 4,
                      ((SIDE_LENGTH / 4) + SIDE_LENGTH) * row + SIDE_LENGTH / 4,
                      SIDE_LENGTH,
                      SIDE_LENGTH])

  clock.tick(DELAY)
  pygame.display.flip()
  living_positions = next_generation(living_positions)

pygame.quit()

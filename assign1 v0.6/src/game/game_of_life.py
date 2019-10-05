from enum import Enum
from collections import Counter
from functools import reduce

class CellState(Enum):
  DEAD = 0
  ALIVE = 1


def next_cell_state(current_state, number_of_life_neighbors):
  return CellState.ALIVE if number_of_life_neighbors == 3 \
    or current_state == CellState.ALIVE and number_of_life_neighbors == 2 \
    else CellState.DEAD


def generate_signal(position):
  x, y = position
  return [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
            (x, y - 1), (x, y + 1),
            (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]


def generate_signals(positions=[]):
  return reduce(list.__add__, list(map(generate_signal, positions))) if positions else []


def count_signals(signals=[]):
  return dict(Counter(signals))
  

def next_generation(living_positions=[]):
  signal_map_counts = count_signals(generate_signals(living_positions))
  return list(dict(filter(lambda x: next_cell_state(CellState.ALIVE if x[0] in living_positions else CellState.DEAD, x[1]) == CellState.ALIVE, signal_map_counts.items())).keys())


def get_bounds(points=[]):
  x_list, y_list = list(map(lambda x: x[0], points)), list(map(lambda x: x[1], points))
  return 2 * points if not points or len(points)==1 else [(min(x_list), min(y_list)), (max(x_list),  max(y_list))]

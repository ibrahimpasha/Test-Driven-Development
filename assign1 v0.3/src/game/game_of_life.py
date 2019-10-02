from enum import Enum

class CellState(Enum):
  DEAD = 0
  ALIVE = 1

live_cell_tracker = {(2,2): 1, (2, 3):1, (2, 4):1, (1,1):1}
neighbours_tracker = {}
directions = []

def next_cell_state(current_state, number_of_life_neighbors):
  return CellState.ALIVE if number_of_life_neighbors == 3 or number_of_life_neighbors == 2 and current_state == CellState.ALIVE else CellState.DEAD

def get_cell_state(cell):
  return CellState.ALIVE if cell in live_cell_tracker else CellState.DEAD
  
def get_neighbor_count(cell):
  return neighbours_tracker[cell]

def signal_generator(cell_position):
  global directions
  current_cell_neighbor_count = 0
  if cell_position !=  (0, 0):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                   (0, -1)         , (0, 1),
                   (1, -1), (1, 0), (1, 1)]
  else:
    directions = [(0, 1),(1, 0), (1, 1)]
    
  for direction in directions:
    neighbor_cell = tuple(map(sum, zip(cell_position, direction)))
    if neighbor_cell not in neighbours_tracker:
      neighbours_tracker[neighbor_cell] = 1
      
    neighbours_tracker[neighbor_cell] += 1
    
    if get_cell_state(neighbor_cell) == CellState.ALIVE:
      current_cell_neighbor_count += 1
      
  return current_cell_neighbor_count

print(signal_generator((2, 2)))
print(signal_generator((2, 3)))
print(signal_generator((2, 4)))
print(signal_generator((3, 3)))
print(neighbours_tracker)

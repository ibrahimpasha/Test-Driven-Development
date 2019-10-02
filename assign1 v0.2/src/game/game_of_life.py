import numpy as np
from enum import IntEnum


class Cell(IntEnum):
  ALIVE = 1
  DEAD = 0
  

class Neighbors(IntEnum):
  ZERO = 0
  ONE = 1
  TWO = 2
  THREE = 3
  FOUR = 4
  FIVE = 5
  SIX = 6
  SEVEN = 7
  EIGHT = 8


class GameOfLife:

  def __init__(self):
    self.SIZE = 1000
    self.game_matrix = np.zeros((self.SIZE, self.SIZE))
  
  def activate_cell(self, row, col):
    self.game_matrix[row, col] = Cell.ALIVE
    return self.game_matrix[row, col] == Cell.ALIVE
  
  def deactivate_cell(self, row, col):
    self.game_matrix[row, col] = Cell.DEAD
    return self.game_matrix[row, col] == Cell.DEAD
  
  def count_neighbors(self, row, col):
    temp = 0
    if row not in [0, self.SIZE - 1] and col not in [0, self.SIZE - 1]:
      temp += self.game_matrix[row - 1, col - 1]
      temp += self.game_matrix[row - 1, col]
      temp += self.game_matrix[row - 1, col + 1]
      temp += self.game_matrix[row, col - 1]
      temp += self.game_matrix[row, col + 1]
      temp += self.game_matrix[row + 1, col - 1]
      temp += self.game_matrix[row + 1, col]
      temp += self.game_matrix[row + 1, col + 1]
      return temp
    else:
      raise ValueError("Edge or Corner Case")

  def dead_constraints(self, row, col):
    if self.game_matrix[row, col] == Cell.DEAD:
      current_count = self.count_neighbors(row, col)
      if current_count == Neighbors.THREE:
        self.game_matrix[row, col] = Cell.ALIVE
        return Cell.ALIVE
      else:
        self.game_matrix[row, col] = Cell.DEAD
        return Cell.DEAD
    else:
      raise ValueError("Expected a DEAD Cell...")
  
  def alive_constraints(self, row, col):
    if self.game_matrix[row, col] == Cell.ALIVE:
      current_count = self.count_neighbors(row, col)
      if current_count <= Neighbors.ONE or current_count >= Neighbors.FOUR:
        return Cell.DEAD
      else:
        return Cell.ALIVE
    else:
      raise ValueError("Expected Cell to be ALIVE")
